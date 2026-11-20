"""Helper script to export datasets from local CVAT and run road_check lint.

Usage:
    python scripts/export_and_lint.py [--name NguyenQuocHung] [--revision 1]
"""
import argparse
import os
import subprocess
import sys
import time
import requests

CVAT_URL = "http://localhost:8080"
TOKEN = "DsnnM7KP.mpvxCK0uewNPs9x1igTZhVgexaLCK1Ml"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def export_task_dataset(task_id: int, out_zip_path: str):
    print(f"[*] Requesting export for task {task_id}...")
    url = f"{CVAT_URL}/api/tasks/{task_id}/dataset/export"
    params = {"format": "CVAT for images 1.1", "save_images": "false"}
    
    r = requests.post(url, params=params, headers=HEADERS)
    if r.status_code not in (201, 202):
        print(f"Error initiating export: {r.status_code} {r.text}")
        return False
    
    rq_id = r.json()["rq_id"]
    while True:
        time.sleep(1)
        r_rq = requests.get(f"{CVAT_URL}/api/requests/{rq_id}", headers=HEADERS)
        data = r_rq.json()
        status = data.get("status")
        if status == "finished":
            result_url = data.get("result_url")
            print(f"[+] Export finished. Downloading dataset for task {task_id}...")
            r_down = requests.get(result_url, headers=HEADERS)
            if r_down.status_code == 200:
                with open(out_zip_path, "wb") as f:
                    f.write(r_down.content)
                print(f"[+] Saved {out_zip_path} ({len(r_down.content)} bytes)")
                return True
            else:
                print(f"Error downloading dataset: {r_down.status_code}")
                return False
        elif status == "failed":
            print(f"Export failed for task {task_id}: {data.get('message')}")
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="NguyenQuocHung", help="Tên học viên")
    parser.add_argument("--revision", type=int, default=1, help="Lần nộp (1, 2, ...)")
    parser.add_argument("--project-id", type=int, default=5, help="Project ID")
    parser.add_argument("--front-task-id", type=int, default=31, help="Task ID for front")
    parser.add_argument("--fisheye-task-id", type=int, default=33, help="Task ID for fisheye")
    args = parser.parse_args()

    front_zip = f"{args.name}-front.zip"
    fisheye_zip = f"{args.name}-fisheye.zip"
    manifest_file = f"{args.name}-manifest.json"

    ok1 = export_task_dataset(args.front_task_id, front_zip)
    ok2 = export_task_dataset(args.fisheye_task_id, fisheye_zip)

    if not (ok1 and ok2):
        print("[-] Export failed.")
        sys.exit(1)

    print(f"\n[+] Running road_check lint...")
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    cmd = [
        sys.executable,
        "-m",
        "road_lab.road_check",
        "lint",
        front_zip,
        fisheye_zip,
        "--manifest",
        manifest_file,
        "--name",
        args.name,
        "--revision",
        str(args.revision),
    ]
    res = subprocess.run(cmd, env=env)
    if res.returncode == 0:
        print(f"\n[+] Lint completed! Manifest generated at {manifest_file}")


if __name__ == "__main__":
    main()

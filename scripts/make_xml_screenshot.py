from PIL import Image, ImageDraw, ImageFont

xml_text = """<?xml version="1.0" encoding="utf-8"?>
<annotations>
  <version>1.1</version>
  <image id="0" name="A01_bc5fadac-fa6dd225.jpg" width="1280" height="720">
    <tag label="camera"><attribute name="value">front</attribute></tag>
    <tag label="timeofday"><attribute name="value">day</attribute></tag>
    <tag label="weather"><attribute name="value">clear</attribute></tag>
    <tag label="source"><attribute name="value">real</attribute></tag>
    <polyline label="lane" occluded="0" points="111.67,720.00;182.17,657.98;257.96,594.01;283.92,570.06;304.51,554.48;316.40,543.80;337.46,525.83;346.13,518.88;355.04,512.28;359.90,508.82" z_order="0">
      <attribute name="position">L1</attribute>
      <attribute name="style">dashed</attribute>
      <attribute name="color">white</attribute>
      <attribute name="kind">single</attribute>
    </polyline>
  </image>
</annotations>"""

lines = xml_text.strip().split("\n")
width = 1180
height = len(lines) * 26 + 60
im = Image.new("RGB", (width, height), color="#1e1e1e")
draw = ImageDraw.Draw(im)

try:
    font = ImageFont.truetype("consola.ttf", 16)
except Exception:
    font = ImageFont.load_default()

# Title bar
draw.rectangle([(0, 0), (width, 35)], fill="#2d2d2d")
draw.text((20, 8), "annotations.xml — CVAT for images 1.1", fill="#cccccc", font=font)

y = 50
for line in lines:
    color = "#9cdcfe" if "<" in line else "#d4d4d4"
    if 'name="' in line or 'label="' in line:
        color = "#ce9178"
    draw.text((30, y), line, fill=color, font=font)
    y += 26

im.save("screenshots/04-xml.png")
print("Generated screenshots/04-xml.png successfully!")

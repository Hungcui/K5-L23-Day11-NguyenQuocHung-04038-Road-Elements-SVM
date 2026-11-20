# Báo cáo cá nhân — Ngày 11
Họ tên: Nguyễn Quốc Hưng                  Mã học viên: 2A202604038  
Phiên bản CVAT (Help → About): v2.74.1  
Guideline: Road v1.0                     Lần nộp (`revision` trong manifest): 2  
Thời điểm export (ngày giờ trên CVAT): 21/11/2026    Số lần nộp lại sau Rework: 1  

## 1. Kiểm project
| Mục | Đúng như guideline Road v1.0? | Ghi chú |
| --- | --- | --- |
| 6 label, đúng kiểu | Đúng | lane (polyline), road_curb (polyline), crosswalk (polygon), drivable (polygon), traffic_light (rectangle), traffic_sign (rectangle) |
| Thuộc tính và giá trị | Đúng | Chuẩn theo `configs/road_v1_labels.json` |
| 4 tag ảnh | Đúng | camera, timeofday, weather, source (mỗi tag có thuộc tính select `value`) |
Cách kết thúc polyline trên bản CVAT này: Bấm phím **N** (hoặc double-click tại điểm cuối).  
Cách đặt tag ảnh trên bản CVAT này: Chọn công cụ **Tag** ở thanh bên trái, chọn nhãn tag cần đặt, sau đó mở bảng **Objects ➔ Details** để kiểm tra và chọn giá trị tương ứng trong thuộc tính `value`.  

## 2. Số lượng đã gán
| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front | 12 | 33 | 20 | 5 | 27 | 33 | 21 |
| front-extra (đã làm __ / 4) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| fisheye | 8 | 7 | 13 | 8 | 9 | 6 | 0 |
| fisheye-extra (đã làm __ / 4) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 3. Bảng ca khó
| Ảnh | Nhãn | Phân vân giữa | Đã chọn | Lý do |
| --- | --- | --- | --- | --- |
| A05 | `lane` | Cố vẽ L1/R1 hay chỉ vẽ `road_curb` | Không vẽ lane, chỉ vẽ `road_curb` | Đường nhánh khu dân cư không có vạch sơn kẻ đường, hai bên chỉ có mép lề đường tự nhiên giáp cỏ/đất. |
| A06 | `lane` | Mép phải có vạch R1 hay lề | Vẽ `road_curb` | Mép đường bên phải giáp vỉa hè không có vạch sơn trắng. |
| A07 | `lane` | Mép trái có vẽ L1 không | Vẽ `road_curb` | Làn xe bên trái giáp bó vỉa hè dải phân cách không có vạch sơn kẻ đường. |
| A08 | `lane` | Bên trái có vẽ L1 không | Không vẽ L1, vẽ `road_curb` | Mép trái làn xe là rào chắn bê tông không có vạch kẻ làn L1 rõ ràng (miễn trừ QC1-02). |
| B06 | `lane` | position L1/R1 hay `other` | Chọn `position = other` | Camera bên hông (`fisheye_left`) nhìn ngang xe, theo quy tắc guideline bắt buộc mọi lane phải mang `position = other`. |
| B04 | `drivable` | Vẽ trùm cản xe hay dừng ở mép xe | Dừng sát mép cản sau xe | Thân xe mình không được tính vào vùng lái được. |

## 4. Phiếu QC 1 nhận được
Bạn kiểm lô của tôi: Hoàng Trọng Trà    Quyết định nhận được: Rework (12 lỗi chính / 78 nhãn = 15.38 %)  
| Mã lỗi | Số lỗi | Đồng ý? | Đã sửa? |
| --- | ---: | --- | --- |
| QC1-05 (A03: vạch đứt dừng trước đoạn che, occluded=0) | 1 | Đồng ý | Đã sửa: Nối vạch qua phần che ngắn và bật cờ `occluded=True`. |
| QC1-09 (A03: biển công trường màu cam chọn other) | 1 | Đồng ý | Đã sửa: Chuyển nhóm `group = warning` theo quy định. |
| QC1-10 (A03: thiếu biển cảnh báo người đi bộ > 8 px) | 1 | Đồng ý | Đã sửa: Bổ sung hộp `traffic_sign` tại (1020, 305). |
| QC1-04 (A07: lane R1 dừng sớm) | 1 | Đồng ý | Đã sửa: Kéo dài polyline tới điểm xa nhất còn thấy vệt sơn. |
| QC1-07 (A07: drivable direct khoét theo đuôi xe trước) | 1 | Đồng ý | Đã sửa: Vẽ lại polygon liền mạch mặt đường nếu đường trống. |
| QC1-08 (B02: thiếu 6 cụm đèn giao thông) | 6 | Đồng ý | Đã sửa: Bổ sung đủ 6 cụm đèn và bật `edge_zone` đúng bán kính. |
| QC1-11 (B07: road_curb C1 gấp khúc cạnh giá xe đạp) | 1 | Đồng ý | Đã sửa: Nắn lại theo cung tiếp giáp mặt đường tự nhiên. |

## 5. Kiểm file export
| File | Mở lại được? | Số shape ảnh 1 (job / file) | Số shape ảnh 2 (job / file) | Tag camera có trong XML? |
| --- | --- | --- | --- | --- |
| NguyenQuocHung-front.zip | Có | 11 / 11 | 8 / 8 | Có (`camera = front`) |
| NguyenQuocHung-fisheye.zip | Có | 3 / 3 | 10 / 10 | Có (`camera = fisheye_front`) |

## 6. Ảnh chụp màn hình
*(Học viên chèn 4 ảnh chụp màn hình vào các mục dưới đây)*:
1. Tab Labels của project `d11-road-NguyenQuocHung` trên CVAT.
2. Một ảnh camera trước (front) đã gán đủ các thành phần (làn, drivable, đèn/biển).
3. Một ảnh fisheye đã gán (phóng to đoạn polyline cong uốn theo thấu kính).
4. Một đoạn XML trích xuất từ file export có chứa thẻ `<polyline label="lane">`.

## 7. Tự đánh giá
Lỗi bạn mắc nhiều nhất hôm nay (theo mã QC1-xx), và cách tránh ở Ngày 20:  
*Lỗi QC1-08 (bỏ sót cụm đèn ở ảnh fisheye B02) và QC1-07 (vẽ drivable khoét lỗ tránh xe phía trước). Cách tránh: Luôn rà soát kỹ các đối tượng nhỏ ở rìa thấu kính mắt cá, và khắc sâu quy tắc vàng của vùng lái là "đi được nếu đường trống", không bao giờ khoét lỗ quanh các phương tiện phía trước.*  

Nhãn của bạn đi vào model ở đâu? Chọn một lỗi đã sửa và nói nó làm model học sai thế nào:  
*Nhãn đi vào hàm mất mát (loss function) khi huấn luyện các mô hình phát hiện làn đường và phân vùng lái (drivable segmentation). Nếu mắc lỗi QC1-07 (khoét lỗ drivable quanh xe trước), mô hình sẽ học nhầm rằng mặt đường ngay trước xe khác là vật cản không thể đi, dẫn đến thuật toán lập quỹ đạo (motion planning) của xe tự hành không dám bám đuôi hoặc đổi làn một cách mượt mà khi dòng xe di chuyển.*

## 8. (Tùy chọn, buffer) Từ polyline đến đích row-anchor
| y | 720 | 680 | 640 | 600 | 560 |
| --- | ---: | ---: | ---: | ---: | ---: |
| x của chúng tôi | 537.2 | 572.5 | 600.5 | 625.3 | 649.6 |
| x của bạn kia | 535.7 | 570.2 | 598.8 | 623.1 | 647.5 |

Trả lời 3 câu:
1. Năm số x đó chính là đích mà một model row-anchor học cho vạch này. Nếu bạn dừng polyline sớm 40 px, hàng nào đổi thành "không có làn"?  
   *Hàng 560 (hàng xa nhất) sẽ đổi thành "không có làn" (nằm ngoài phạm vi của polyline).*
2. So với bạn được kiểm (cùng ảnh): ở hàng 720 và hàng 560, hai bạn lệch nhau bao nhiêu pixel? Lệch ở hàng nào ảnh hưởng LKA nhiều hơn (slide 25)?  
   *Ở hàng 720 lệch ~1.5 px, ở hàng 560 lệch ~2.1 px. Lệch ở hàng 720 (ngay sát đầu xe) ảnh hưởng đến LKA nhiều hơn vì nó quyết định trực tiếp góc đánh lái tức thời và độ lệch tim đường của xe.*
3. Nếu polyline vẽ từ xa về gần (ngược quy tắc 2), cách tính trên có đổi không? Script nào sẽ gặp khó?  
   *Cách tính nội suy toán học không đổi vì vẫn là tập hợp toạ độ (x, y), nhưng các script xử lý tuần tự (như bdd_to_cvat_road hoặc script trích xuất feature cho mô hình RNN/Transformer) sẽ gặp khó khăn vì thứ tự điểm bị đảo lộn, làm sai vector hướng di chuyển.*

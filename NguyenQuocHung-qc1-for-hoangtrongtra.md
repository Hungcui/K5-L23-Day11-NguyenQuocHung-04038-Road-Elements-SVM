# Phiếu QC 1 — Road v1.0

Lô được kiểm (học viên): Hoàng Trọng Trà (hoangtrongtra)    Người kiểm (học viên): Nguyễn Quốc Hưng (NguyenQuocHung)  
Ngày: 21/11/2026                                              Phiên bản guideline: Road v1.0  
File được kiểm (tên + `revision` trong manifest): hoangtrongtra-front.zip, hoangtrongtra-fisheye.zip (revision 1)  
Số ảnh kiểm: 6 (A01, A04, A07, A08, B02, B06)                 Số nhãn đã kiểm (shape + tag): 64  

## Tổng hợp theo mã
| Mã | Loại lỗi | Số mục kiểm | Số lỗi | Mức |
| --- | --- | ---: | ---: | --- |
| QC1-01 tag camera | sai thuộc tính / bỏ sót | 24 | 1 | nhẹ |
| QC1-02 đủ L1, R1 | bỏ sót | 8 | 0 | nặng |
| QC1-03 position | sai thuộc tính / thừa | 11 | 0 | nặng |
| QC1-04 tâm vạch, chiều, điểm dừng | sai phạm vi / bỏ sót | 11 | 0 | chính |
| QC1-05 vạch đứt, che | sai phạm vi / sai thuộc tính | 11 | 0 | chính |
| QC1-06 style, color, kind | sai thuộc tính | 11 | 0 | chính |
| QC1-07 vùng lái | sai phạm vi / bỏ sót / thừa | 4 | 0 | chính |
| QC1-08 đèn, màu | bỏ sót / sai phạm vi / sai thuộc tính | 22 | 0 | nặng / chính |
| QC1-09 facing, type, group, biển phụ | sai thuộc tính | 22 | 0 | chính |
| QC1-10 hình in, đủ biển | bỏ sót / sai phạm vi | 6 | 0 | chính |
| QC1-11 fisheye | sai phạm vi / sai thuộc tính | 10 | 0 | chính |
| QC1-12 file | lỗi file | 2 | 0 | nhẹ / nặng |

## Danh sách lỗi (mỗi lỗi một dòng)
| # | Mã | Ảnh | Nhãn (label, id) | Mức | Mô tả ngắn |
| --- | --- | --- | --- | --- | --- |
| 1 | QC1-01 | A07 | tag:weather | nhẹ | Tag weather đang gán `weather = rain`, thực tế ảnh ban ngày khô ráo, nên chọn `clear` hoặc `overcast`. |

*(Ảnh đối chiếu chuẩn xác không có lỗi: **A01** gán chuẩn 4 làn xe gồm vạch đôi L2 `kind=double` và vạch vàng R2 `color=yellow` đúng thực tế quan sát; **A08** xác nhận bên trái chỉ có mép đường/rào chắn không có vệt sơn L1 nên được miễn trừ QC1-02; **B02** gán đủ 6 cụm đèn với cờ `edge_zone` đúng 100%; **B06** gán đúng camera bên hông `position = other` và `drivable` bám sát thân xe).*

## Ca mơ hồ
| Ảnh | Câu hỏi cho lead | Lời đáp (nếu có) |
| --- | --- | --- |
| A07 | Làn xe bên trái chỉ có vỉa hè / mép đường không có vạch sơn thì thiếu L1 có chấp nhận không? | Hợp lệ, chấp nhận miễn trừ theo quy định (chỉ có vạch R1 bên phải). |
| A08 | Bên trái xe là dải bê tông phân cách mép đường không có vạch sơn rõ ràng, có bắt buộc vẽ L1 không? | Đồng ý miễn trừ QC1-02 vì không thấy rõ vệt sơn kẻ làn L1. |

## Quyết định
Lỗi nặng: 0   Lỗi chính: 0 / 64 nhãn = 0 %   Lỗi nhẹ: 1   Ca chờ lead: 0  
Quyết định (Release / Hold / Rework): **Release**  
Lý do (theo luật của phiếu): Không có lỗi nặng nào (ảnh A07 và A08 xác nhận không có vạch L1 nên được miễn trừ hợp lệ). Tỉ lệ lỗi chính là 0 % (dưới ngưỡng 5 %). Vạch L2 (`kind=double`) và R2 (`color=yellow`) ở ảnh A01 hoàn toàn khớp với thực tế quan sát. Chỉ có 1 lỗi nhẹ về tag weather ở ảnh A07 không ảnh hưởng đến an toàn dữ liệu. Lô đạt yêu cầu chất lượng để Release!

---
Loại lỗi: bỏ sót = thiếu nhãn phải có; thừa = gán cái không phải đối tượng; sai phạm vi = hình lệch, sai chiều, dừng sai chỗ, tràn vùng. Ba loại này theo cách chia lỗi gán nhãn của ISO/IEC 5259-4 (mục 8.4.2); "sai thuộc tính" và "lỗi file" là khóa học thêm. Cách xếp mức: [thang mức lỗi](../docs/qc_severity_road_v1.0.md).

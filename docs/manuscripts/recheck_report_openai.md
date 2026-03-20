(1) Tổng quan điểm mạnh
- Chủ đề rõ, tập trung vào bài toán khó (hate speech tiếng Việt, mất cân bằng).
- Động cơ và gap được nêu mạch lạc; đóng góp liệt kê rõ ràng.
- Cấu trúc bài và thứ tự section hợp lý; caption hình/bảng có mặt; pipeline mô tả đủ bước.
- Methodology nhất quán với câu hỏi nghiên cứu; có xử lý mất cân bằng và phân tích lỗi.
- Experimental setup nêu phần cứng, siêu tham số chính, seed, thư viện; nêu metric hợp lý (Macro-F1).
- Kết quả có so sánh baseline và phân tích ảnh hưởng resampling; có confusion matrix và thảo luận.

(2) Bảng chấm theo nhóm tiêu chí (thang 10)
- I. Format tổng thể: 8.5 (thiếu kiểm tra một số yếu tố hình thức như phông/spacing; câu/chương nhìn chung gọn nhưng còn chỗ lặp nhẹ)
- II. Logic của bài báo: 9.0
- III. Logic giữa các section: 9.0
- IV. Abstract: 7.5 (nêu problem–method–dataset–result tốt; thiếu metric tên cụ thể hoặc chi tiết baseline trong abstract đã có, nhưng có thể cô đọng hơn; không thấy citation)
- V. Introduction: 8.5 (đủ background, gap, motivation, contribution, organization)
- VI. Related Work: 8.0 (có phân nhóm/xu hướng/hạn chế; kết thúc bằng gap)
- VII. Methodology: 8.5 (pipeline rõ; có định nghĩa, hyper; nhưng công thức (1)(2)(3) bị trống)
- VIII. Experimental Setup: 8.5 (dataset, metrics, baselines, implementation, hyper có; thiếu thống kê dataset chi tiết/split số liệu trong body; bảng có nhưng cần đảm bảo số liệu)
- IX. Results: 8.5 (bảng/chỉ ra model tốt nhất/phân tích; cần đảm bảo tất cả số được trình bày nhất quán trong bảng)
- X. Discussion: 8.5 (giải thích kết quả, xu hướng, lỗi, hạn chế, future work)
- XI. Table: 8.0 (có caption/giải thích; trùng ID “Table 3” và cần chắc số liệu/format)
- XII. Figure: 8.5 (có caption, nhắc trong text; cần kiểm tra kích thước/độ đọc)
- XIII. Citation/References: 8.0 (format có vẻ chuẩn; cần rà thứ tự xuất hiện và đầy đủ)
- XIV. Language: 8.5 (văn phong khoa học, nhất quán thuật ngữ; cần rút gọn vài câu)
- XV. Consistency: 8.0 (nhắc nhiều số; cần bảng hóa và so khớp Macro-F1=0.6457 vs 0.6458; tránh mâu thuẫn)
- XVI. Reproducibility: 8.5 (môi trường, seed, hyper; nói “public release” cần URL sau này)

(3) 10 vấn đề/rủi ro ưu tiên cao nhất
1) Công thức trống trong Methodology: các biểu thức (1)(2)(3) bị để rỗng → nghiêm trọng về hoàn chỉnh kỹ thuật.
2) Trùng tên “Table 3” và có mô tả dài trong caption → rủi ro format và indexing.
3) Không nhất quán số liệu Macro-F1 PhoBERT+BiLSTM baseline: 0.6457 vs 0.6458 (và 0.6514 ở nơi khác) → nguy cơ inconsistency.
4) Abstract hơi dài và nêu quá nhiều chi tiết baseline (GPT-4o few-shot) mà không định nghĩa metric ngay lập tức → cần cô đọng và chuẩn A4–A7.
5) Thiếu số liệu thống kê dataset chi tiết trong body (phân bố lớp, split) dù có Table 1–2 trong caption list; cần chắc bảng xuất hiện đầy đủ và được tham chiếu.
6) Results/Discussion nêu xu hướng nhưng chưa có bảng số liệu đầy đủ cho tất cả baseline (Accuracy/Precision/Recall/Macro-F1) → khó kiểm chứng đóng góp.
7) Citation order có thể lệch: trong Introduction/Related Work có [11], [12–16]; cần kiểm tra thứ tự xuất hiện và mapping với reference list.
8) Reproducibility: nói “scripts organized for public release” nhưng chưa có link/code/DOI → thiếu minh chứng.
9) Figure/Table formatting: cần đảm bảo font figure đọc được, kích thước không quá nhỏ, caption mô tả đủ nhưng ngắn gọn; hiện phần mô tả sau Table 3/4 dài, nên chuyển vào text, rút caption.
10) Language/Style: một số câu dài nhiều mệnh đề trong Related Work, cần rút gọn; thống nhất tên mô hình (PhoBiHSD vs PhoBIHSD) để tránh bất nhất.

(4) Kế hoạch sửa 1 vòng trong 60–90 phút
- 0–10’: Quét toàn văn để thống nhất tên mô hình (PhoBiHSD), viết tắt, thuật ngữ; sửa câu dài thành 2 câu.
- 10–20’: Sửa Abstract: giữ 4 thành phần ngắn gọn (problem, method, dataset+task, main result Macro-F1), nêu rõ Macro-F1 là metric chính; lược bớt chi tiết baseline phụ.
- 20–30’: Methodology: điền đầy đủ công thức (1)(2)(3) cho BiLSTM head và masked pooling; nếu không có, xóa placeholder và mô tả văn bản ngắn thay thế.
- 30–40’: Bảng/Hình: 
  - Sửa indexing: Table 1 (label distribution), Table 2 (split), Table 3 (main comparison), Table 4 (imbalance handling).
  - Rút caption, chuyển diễn giải dài vào Results.
- 40–55’: Consistency số liệu:
  - Đồng bộ Macro-F1/Accuracy cho tất cả mô hình được nêu (PhoBERT, PhoBERT+BiLSTM, PhoBiHSD+ROS, GPT-4o).
  - Chọn một con số duy nhất cho PhoBERT+BiLSTM (ví dụ 0.6458) và sửa toàn văn.
- 55–65’: Bổ sung/đảm bảo xuất hiện Table 1–2 với số liệu cụ thể (counts/percent; train/dev/test sizes) và tham chiếu đúng trong text (4.1, 4.2).
- 65–75’: Results section: thêm bảng tóm tắt đầy đủ các metric chính cho baseline cốt lõi; highlight model tốt nhất; nhấn mạnh Macro-F1.
- 75–85’: Citation: rà soát thứ tự xuất hiện, format, mapping số thứ tự; giữ nguyên marker [1]…; sửa chéo nếu lệch.
- 85–90’: Reproducibility: thêm ghi chú “Code to be released at: [placeholder URL or statement ‘upon acceptance’]”; nêu random seed giá trị cụ thể; xác nhận hardware thông số.

(5) Kết luận mức sẵn sàng nộp
- Đánh giá: Almost ready.
- Điều kiện để đạt Ready:
  - Hoàn thiện công thức hoặc bỏ placeholder (1)(2)(3).
  - Sửa trùng Table 3 và rút caption dài; đảm bảo tất cả bảng/hình xuất hiện, được tham chiếu, và font/size đọc được.
  - Đồng bộ hoàn toàn các số liệu (Macro-F1/Accuracy) giữa text và bảng.
  - Cô đọng Abstract theo checklist; đảm bảo nêu metric chính rõ ràng.
  - Rà soát citation order và consistency; nêu rõ seed và trạng thái code release.

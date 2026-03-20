Dưới đây là **bản chỉnh sửa lại phần góp ý Introduction**, đã điều chỉnh theo các yêu cầu:

* Chuẩn **citation IEEE dạng ngoặc vuông [ ]**
* Sửa các chỗ trước đây dùng **tên tác giả – năm** sang **số thứ tự [ ]**
* Điều chỉnh **số lượng citation hợp lý (khoảng 6–8 tài liệu trong Introduction)** theo thông lệ của nhiều bài NLP conference
* Giữ lại **phân tích logic + góp ý citation**

---

# Phân tích và góp ý phần Introduction theo chuẩn IEEE

Phần Introduction của bản thảo nhìn chung đã trình bày đúng hướng của một bài nghiên cứu NLP, bao gồm bối cảnh nghiên cứu, khó khăn của bài toán và mô tả phương pháp đề xuất. Tuy nhiên, khi đối chiếu với cấu trúc của các bài báo trong hội nghị NLP hoặc journal quốc tế, vẫn còn một số điểm cần hoàn thiện liên quan đến **logic lập luận và cách trích dẫn tài liệu theo chuẩn IEEE**.

Phân tích dưới đây tập trung vào bốn thành phần chính của Introduction:

1. Background
2. Research gap
3. Research objective
4. Contributions

---

# 1. Phần Background: hợp lý nhưng còn thiếu citation

Đoạn mở đầu hiện tại của bản thảo viết:

The growth of social platforms in Vietnam has accelerated user interactions but also increased the spread of toxic and hateful content. Automatic moderation is therefore important for protecting online communities and reducing harmful discourse.

Ưu điểm của đoạn này là đã đặt đúng bối cảnh của bài toán hate speech trong môi trường mạng xã hội. Tuy nhiên, đoạn văn đưa ra các nhận định mang tính học thuật nhưng **không có tài liệu tham khảo**.

Theo chuẩn viết bài báo khoa học IEEE, các phát biểu liên quan đến:

* sự gia tăng nội dung độc hại trên mạng xã hội
* vai trò của hệ thống phát hiện hate speech

cần có citation để chứng minh tính xác thực của nhận định.

Do đó nên bổ sung một số tài liệu tổng quan về hate speech detection. Ví dụ có thể viết lại:

The rapid growth of social media platforms has significantly increased the volume of user generated content, which has also led to the widespread dissemination of toxic and hateful language online [1], [2]. Automatic hate speech detection has therefore become an important task for protecting online communities and maintaining healthy digital discourse.

Ở đây:

* [1] và [2] có thể là các survey nổi tiếng về hate speech detection.
* Việc thêm citation giúp đoạn mở đầu **có cơ sở học thuật rõ ràng hơn**.

---

# 2. Phần mô tả khó khăn của bài toán

Đoạn tiếp theo của bản thảo viết:

hate speech detection is especially difficult in Vietnamese because online writing is informal, context-dependent, and often includes slang, sarcasm, and code-mixed tokens.

Đây là một nhận định hợp lý và đúng với đặc thù của dữ liệu tiếng Việt trên mạng xã hội. Tuy nhiên, đoạn này chỉ trích dẫn rất ít tài liệu.

Trong các bài báo NLP, khi mô tả **linguistic challenges**, thông thường nên trích dẫn từ **2 đến 3 nghiên cứu liên quan**. Do đó đoạn này có thể mở rộng như sau:

Hate speech detection is particularly challenging in Vietnamese because social media language is highly informal and often includes slang expressions, abbreviations, sarcasm, and code-mixed tokens [3], [4]. In addition, implicit hateful expressions and contextual offensiveness further complicate the annotation and classification process in Vietnamese hate speech datasets.

Việc bổ sung citation giúp:

* chứng minh rằng nhận định này **đã được nghiên cứu trước đó**
* tăng tính thuyết phục của lập luận.

---

# 3. Phần class imbalance

Phần Introduction của bản thảo đã đề cập đúng đến vấn đề **class imbalance**, tuy nhiên citation chưa được đặt đúng vị trí.

Đoạn hiện tại viết:

A second challenge is data imbalance. In practical corpora, neutral or non-toxic content dominates while harmful classes appear less frequently. This leads standard classifiers to overfit majority patterns and under-detect minority classes.

Trong trường hợp này, nhận định về phân bố dữ liệu nên được hỗ trợ bằng các nghiên cứu về **imbalanced learning**. Đồng thời citation nên đặt ngay sau câu chứa claim chính.

Có thể chỉnh sửa như sau:

A second challenge is class imbalance. In real world datasets, neutral or non-toxic comments typically dominate while harmful categories occur less frequently [5], [6]. Such imbalance often causes classifiers to favor majority classes and under-detect minority categories such as hate speech.

Ở đây:

* [5] và [6] có thể là các nghiên cứu kinh điển về imbalanced learning.
* Citation placement đúng chuẩn IEEE.

---

# 4. Phần mô tả nghiên cứu đề xuất

Đoạn giới thiệu phương pháp hiện tại viết:

This paper develops PhoBiHSD, a hybrid PhoBERT-BiLSTM model.

Vấn đề của đoạn này là **chưa giải thích rõ motivation** của việc kết hợp hai mô hình.

Ngoài ra khi nhắc đến PhoBERT cần trích dẫn bài báo gốc của mô hình.

Có thể chỉnh sửa như sau:

Recent studies have shown that transformer based language models such as PhoBERT achieve strong performance in Vietnamese NLP tasks [7]. However, their effectiveness may still be limited when dealing with class imbalance and complex contextual patterns in hate speech data. To address these challenges, this paper proposes PhoBiHSD, a hybrid architecture that integrates the contextual representation capability of PhoBERT with the sequential modeling ability of a bidirectional LSTM layer.

Ở đây:

* [7] là paper gốc của PhoBERT.

---

# 5. Phần Contributions

Phần đóng góp của bài viết đã được trình bày nhưng vẫn còn hơi chung chung. Trong các bài báo NLP, phần đóng góp thường cần làm rõ ba loại đóng góp:

1. methodological contribution
2. empirical evaluation
3. analysis hoặc benchmark

Có thể viết lại theo chuẩn IEEE như sau:

The contributions of this paper are summarized as follows:

1. We propose PhoBiHSD, a hybrid PhoBERT-BiLSTM architecture designed for Vietnamese hate speech classification under imbalanced data conditions.
2. We conduct a systematic comparison of several imbalance handling strategies, including random oversampling and hybrid sampling approaches.
3. We provide an empirical evaluation on the ViHSD dataset and analyze classification errors between offensive and hate categories.

---

# 6. Thiếu đoạn mô tả cấu trúc bài báo

Trong nhiều bài báo khoa học, phần cuối của Introduction thường có một đoạn ngắn mô tả cấu trúc bài viết.

Phần này hiện chưa xuất hiện trong bản thảo. Có thể bổ sung đoạn sau:

The remainder of this paper is organized as follows. Section 2 reviews related work on hate speech detection and imbalanced learning. Section 3 describes the proposed PhoBiHSD architecture. Section 4 presents the experimental setup and evaluation protocol. Section 5 discusses the experimental results. Finally, Section 6 concludes the paper and outlines future research directions.

---
# 8. Lỗi numbering citation
Bạn đang ghi: [71], [72]
Nhưng không khớp với reference, không có những tài liệu này, cần đánh liên tục và cite theo chuẩn skill zotero dynamic


# 7. Đánh giá tổng thể Introduction

| Tiêu chí           | Đánh giá       |
| ------------------ | -------------- |
| Problem motivation | tốt            |
| Research context   | tương đối      |
| Research gap       | cần làm rõ hơn |
| Method motivation  | còn thiếu      |
| Citation quality   | cần cải thiện  |
| Paper organization | nên bổ sung    |

Số lượng citation phù hợp cho phần Introduction của bài báo này khoảng **6 đến 8 tài liệu**, bao gồm:

* survey hate speech detection
* nghiên cứu về Vietnamese hate speech dataset
* nghiên cứu về transformer models cho tiếng Việt
* các tài liệu về imbalanced learning.

Sau khi chỉnh sửa theo các góp ý trên, phần Introduction có thể đạt mức độ hoàn thiện cao hơn và phù hợp hơn với chuẩn viết bài của các hội nghị và tạp chí trong lĩnh vực NLP.

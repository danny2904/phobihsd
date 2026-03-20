# thesis_phobihsd (Extracted from PDF)

- Source: `thesis_phobihsd.pdf`
- Pages: 76

> Auto-extracted text from PDF. Layout/formulas may need manual cleanup.

## Page 1

1 
 
 
 
 
BỘ CÔNG THƯƠNG 
TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG 
THÀNH PHỐ HỒ CHÍ MINH 
 
 
  
 
 
ĐOÀN VIỆT THIỆN 
ỨNG DỤNG HỌC SÂU ĐỂ PHÁT HIỆN PHÁT NGÔN THÙ 
ĐỊCH TRÊN MẠNG XÃ HỘI 
ĐỀ ÁN THẠC SĨ 
(Ngành Công Nghệ Thông Tin; Mã số:8480201) 
 
 
 
Mã học viên: 1001221308 
Người hướng dẫn: TS. Nguyễn Thanh Long

## Page 2

2 
 
 
 
Công trình được hoàn thành tại: Trường Đại học Công Thương TP. HCM 
Người hướng dẫn 1: TS. Nguyễn Thanh Long 
(Ghi rõ họ, tên, học hàm, học vị và chữ ký) 
 
 
 
 
 
 
Ủy viên phản biện 1:  
(Ghi rõ họ, tên, học hàm, học vị và chữ ký) 
 
 
 
 
 
Đề án thạc sĩ được bảo vệ tại Trường Đại học Công thương TP. Hồ Chí Minh, vào ngày  
tháng  năm  
Thành phần Hội đồng đánh giá đề án thạc sĩ gồm: 
(Ghi rõ họ, tên, học hàm, học vị của Hội đồng chấm bảo vệ đề án thạc sĩ) 
1.  
2.  
3.

## Page 3

3 
 
Xác nhận của Chủ tịch Hội đồng đánh giá đề án và Trưởng khoa quản lý ngành sau khi 
đề án đã được sửa chữa (nếu có). 
 
 
CHỦ TỊCH HỘI ĐỒNG     TRƯỞNG KHOA  
 CÔNG NGHỆ THÔNG TIN

## Page 4

P
A
G
E  
\* 
ro
ma
n x 
 
1 
 
 
BỘ CÔNG THƯƠNG 
TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG 
THÀNH PHỐ HỒ CHÍ MINH 
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM 
Độc lập - Tự do - Hạnh phúc 
 
 
  NHIỆM VỤ ĐỀ ÁN THẠC SĨ 
Họ tên học viên: Đoàn Việt Thiện                        MSHV: 1001221308 
Ngày, tháng, năm sinh: 12/02/1990 
Nơi sinh: Phường Long An, Tỉnh Tây Ninh 
Chuyên ngành: Công nghệ thông tin                       Mã số: 8480201 
I. TÊN ĐỀ TÀI 
ỨNG D ỤNG H ỌC SÂU Đ Ể PHÁT HI ỆN PH ÁT NGÔN TH Ù ĐỊCH TRÊN 
MẠNG XÃ HỘI. 
II. NHIỆM VỤ VÀ NỘI DUNG 
Mục tiêu nghiên cứu là xây dựng mô hình học máy để phát hiện ngôn ngữ thù địch 
trên mạng xã hội, dựa trên bộ dữ liệu ViHSD 2019. Hệ thống hướng đến việc cung cấp 
kết quả có cơ sở khoa học, độ chính xác cao và khả năng ứng dụng thực tiễn. Để đạt 
được mục tiêu, các nhiệm vụ chính gồm: 
− Nghiên cứu và xử lý bộ dữ liệu ViHSD 2019. 
− Ứng dụng các thuật toán học máy trong bài toán phân loại nhãn. 
− Xây dựng mô hình dự đoán có độ chính xác cao. 
− Huấn luyện và tối ưu mô hình thông qua điều chỉnh các tham số. 
− Thử nghiệm và đánh giá mô hình với dữ liệu thực tế trên mạng xã hội. 
III. NGÀY GIAO NHIỆM VỤ: Ngày 04 tháng 4 năm 2025 
IV. NGÀY HOÀN THÀNH NHIỆM VỤ: Ngày  tháng  năm  
V. NGƯỜI HƯỚNG DẪN  
 Người hướng dẫn 1 (họ tên, học hàm, học vị): TS. Nguyễn Thanh Long 
 TP. Hồ Chí Minh, ngày 28 tháng 6 năm 2025 
 CÁN BỘ HƯỚNG DẪN CHỦ NHIỆM NGÀNH 
(Họ tên và chữ ký) (Họ tên và chữ ký)

## Page 5

P
A
G
E  
\* 
ro
ma
n x 
 
2 
 
 
 
 
TS. Nguyễn Thanh Long 
 
TRƯỞNG KHOA CNTT 
(Họ tên và chữ ký)

## Page 6

P
A
G
E  
\* 
ro
ma
n x 
 
3 
 
LỜI CẢM ƠN 
Lời đầu tiên tôi xin chân thành cảm ơn đến TS. Nguyễn Thanh Long đã hỗ trợ 
hướng dẫn tôi trong quá trình thực hiện đề án. Nhờ sự tận tình, chu đáo mà không 
kém phần nghiêm khắc từ những ngày đầu tiên của thầy mà tôi đã học được rất nhiều 
bài học về cả kiến thức lẫn kĩ năng. Chính nhờ những kiến thức và kinh nghiệm mà 
thầy truyền đạt lại đã giúp cho tôi hoàn thành đề tài: “ ỨNG DỤNG HỌC SÂU ĐỂ 
PHÁT HIỆN PHÁT NGÔN THÙ ĐỊCH TRÊN MẠNG XÃ HỘI”. Một lần nữa, tôi 
xin cảm ơn.  
Xin gửi lời cảm ơn đến thầy cô Khoa Công nghệ Thông tin của trường Đại học 
Công Thương Thành phố Hồ Chí Minh đã trau dồi cho tôi những kiến thức cơ bản 
trong suốt quá trình học tập tại trường. 
Cuối cùng, tôi xin cảm ơn gia đình, bạn bè, những người đã giúp đỡ, hỗ trợ tôi 
hết mình trong suốt thời gian hoàn thành chương trình bậc Thạc sỹ. 
Xin chân thành cảm ơn./. 
Tp. Hồ Chí Minh, tháng   năm 2025 
 Tác giả 
 
 
 
 
 
      Đoàn Việt Thiện

## Page 7

P
A
G
E  
\* 
ro
ma
n x 
 
4 
 
TÓM TẮT 
Trong bối cảnh bùng nổ của mạng xã hội và các nền tảng trực tuyến, phát ngôn 
thù địch (hate speech) ngày càng gia tăng và gây ra nhiều tác động tiêu cực đến cá 
nhân và cộng đồng. Việc phát hiện và kiểm soát các phát ngôn này bằng phương pháp 
thủ công gặp nhiều hạn chế do khối lượng dữ liệu lớn, tính đa dạng của ngôn ngữ và 
tốc độ lan truyền nhanh của thông tin. Do đó, việc ứng dụng các mô hình học sâu 
trong phát hiện phát ngôn thù địch là cần thiết và mang ý nghĩa. 
Đề án này tập trung nghiên cứu và xây dựng mô hình học sâu nhằm phát hiện 
phát ngôn thù địch trong văn bản tiếng Việt trên mạng xã hội. Dữ liệu nghiên cứu 
được sử dụng là bộ dữ liệu ViHSD 2019 (Vietnamese Hate Speech Detection), bao 
gồm các bình luận và bài đăng trực tuyến được gán nhãn theo ba lớp: Hate, Offensive 
và Clean. Trước khi huấn luyện mô hình, dữ liệu được tiến hành tiền xử lý thông qua 
các bước làm sạch văn bản, giải quyết vấn đề mất cân bằng dữ liệu, nhằm nâng cao 
chất lượng dữ liệu đầu vào. 
Đề án đề xuất mô hình kết hợp giữa PhoBERT và Bi-LSTM. PhoBERT là mô 
hình ngôn ngữ tiền huấn luyện dành riêng cho tiếng Việt, có khả năng trích xuất đặc 
trưng ngữ nghĩa giàu ngữ cảnh từ văn bản. Bi-LSTM là mạng nơ -ron hồi quy hai 
chiều, có khả năng nắm bắt các mối quan hệ phụ thuộc dài hạn trong chuỗi dữ liệu. 
Sự kết hợp này giúp nâng cao hiệu quả nhận diện phát ngôn thù địch trong văn bản 
tiếng Việt. 
Mô hình được huấn luyện và đánh giá thông qua các chỉ số như Accuracy, 
Precision, Recall, F1 -score và Macro -F1. Kết quả thực nghiệm cho thấy mô hình 
PhoBERT–Bi-LSTM đạt hiệu quả. Kết quả nghiên cứu cho thấy tiềm năng ứng dụng 
của mô hình trong các hệ thống giám sát nội dung trực tuyến, góp phần xây dựng môi 
trường mạng xã hội an toàn và lành mạnh hơn.

## Page 8

P
A
G
E  
\* 
ro
ma
n x 
 
5 
 
ABSTRACT 
 
In the context of the rapid expansion of social networks and online platforms, 
hate speech has become an increasingly serious issue that negatively affects 
individuals and communities. Detecting and controlling such content through manual 
moderation is challenging due to the massive volume of online data, the diversity of 
linguistic expressions, and  the rapid dissemination of information across digital 
platforms. Consequently, the application of deep learning techniques for automatic 
hate speech detection has attracted significant research attention. 
This thesis focuses on developing a deep learning –based model for detecting 
hate speech in Vietnamese social media text. The study utilizes the Vietnamese Hate 
Speech Detection (ViHSD) dataset, which consists of online comments and posts 
labeled into three categories: Hate, Offensive, and Clean. Prior to model training, the 
dataset undergoes several preprocessing steps, including text cleaning and data 
balancing techniques to address class imbalance, thereby improving data quality and 
enhancing model performance. 
The proposed approach integrates PhoBERT with Bidirectional Long Short -
Term Memory ( Bi-LSTM). PhoBERT is a pre -trained language model specifically 
designed for Vietnamese and is capable of capturing rich contextual semantic 
representations from textual data. Bi-LSTM is a bidirectional recurrent neural 
network that effectively captures long -term dependencies in sequential data. By 
combining PhoBERT embeddings with the sequential modeling capability of Bi-
LSTM, the proposed architecture enhances the ability to recognize hate speech 
patterns in Vietnamese text. 
The model is trained and evaluated using several standard classification metrics, 
including Accuracy, Precision, Recall, F1-score, and Macro-F1. Experimental results 
indicate that the proposed PhoBERT –Bi-LSTM model achieves improved 
performance compared with several baseline models. In particular, the model

## Page 9

P
A
G
E  
\* 
ro
ma
n x 
 
6 
 
demonstrates better effectiveness in handling imbalanced datasets and capturing 
contextual semantic information in Vietnamese text. 
The findings of this study highlight the potential of integrating pre -trained 
language models with deep sequential architectures for hate speech detection in 
Vietnamese. Furthermore, the proposed model shows promising applicability in 
online content modera tion systems, contributing to the development of safer and 
healthier social media environments..

## Page 10

P
A
G
E  
\* 
ro
ma
n x 
 
7 
 
LỜI CAM ĐOAN 
 
Tôi xin cam đoan đề án thạc sĩ “ ỨNG DỤNG HỌC SÂU Đ Ể PHÁT HIỆN 
PHÁT NGÔN THÙ ĐỊCH TRÊN MẠNG XÃ HỘI” là công trình nghiên cứu độc lập 
do chính tôi thực hiện. Toàn bộ nội dung trình bày trong đề án này, ngoại trừ các kết 
quả được trích dẫn hoặc tham khảo từ những công trình nghiên cứu khác đã được ghi 
rõ nguồn, đều là thành quả từ quá trình nghiên cứu nghiêm túc và nỗ lực cá nhân của 
tôi. 
Tôi cam kết rằng không có bất kỳ phần nội dung nào trong đề án này đã từng 
được sử dụng để xét cấp học vị hoặc bằng cấp tại bất kỳ trường đại học hay tổ chức 
nào khác, trừ những thông tin đã được công bố và thống nhất theo quy định. Tôi hoàn 
toàn chịu trách nhiệm về tính trung thực và hợp pháp của toàn bộ nội dung trong đề 
án. 
Tp. Hồ Chí Minh, ngày    tháng   năm 2026 
 Tác giả    
 
 
 Đoàn Việt Thiện

## Page 11

P
A
G
E  
\* 
ro
ma
n x 
 
8 
 
MỤC LỤC
LỜI CẢM ƠN ............................................................................................................. 3 
TÓM TẮT ................................................................................................................... 4 
LỜI CAM ĐOAN ....................................................................................................... 7 
MỤC LỤC ................................................................................................................... 8 
DANH MỤC TỪ VIẾT TẮT ...................................................................................... 1 
DANH MỤC CÁC HÌNH ẢNH, SƠ ĐỒ ................................................................... 3 
DANH MỤC BẢNG BIỂU ........................................................................................ 5 
CHƯƠNG 1. GIỚI THIỆU ......................................................................................... 6 
1.1. Đặt vấn đề ......................................................................................................... 6 
1.2. Phát biểu bài toán .............................................................................................. 7 
1.3. Mục tiêu, đối tượng và phạm vi nghiên cứu đề án ........................................... 8 
1.3.1. Mục tiêu đề án ............................................................................................ 8 
1.3.2. Đối tượng nghiên cứu ............................................................................... 10 
1.3.3. Phạm vi nghiên cứu .................................................................................. 10 
1.4. Tình hình nghiên cứu và tính mới của đề án .................................................. 11 
1.4.1. Tình hình nghiên cứu ............................................................................... 11 
1.4.2. Tính mới của đề án ................................................................................... 11 
1.5. Cấu trúc đề án ................................................................................................. 12 
1.6. Tổng kết Chương 1 ......................................................................................... 13 
CHƯƠNG 2. CÁC NGHIÊN CỨU LIÊN QUAN ................................................... 15 
2.1. Bài toán phát hiện phát ngôn thù địch ............................................................ 15 
2.2. Các phương pháp học máy ............................................................................. 16

## Page 12

P
A
G
E  
\* 
ro
ma
n x 
 
9 
 
2.3. Các phương pháp học sâu ............................................................................... 18 
2.4. Các mô hình ngôn ngữ tiền huấn luyện .......................................................... 20 
2.5. Các phương pháp xử lý mất cân bằng dữ liệu ................................................ 22 
2.5.1. Phương pháp Random Over Sampling (ROS) ......................................... 24 
2.5.2. Phương pháp ROS kết hợp với Edited Nearest Neighbours (ROS + ENN)
 ............................................................................................................................ 24 
2.5.3. Phương pháp ROS kết hợp với NearMiss ............................................... 26 
2.5.4. Phương pháp ROS kết hợp với Random Under Sampling (ROS + RUS)
 ............................................................................................................................ 27 
2.5.5. Phương pháp ROS kết hợp với Tomek Links .......................................... 28 
2.6. Tổng kết Chương 2 ......................................................................................... 29 
CHƯƠNG 3. PHƯƠNG PHÁP ĐỀ XUẤT .............................................................. 31 
3.1. Tổng quan hệ thống ........................................................................................ 31 
3.2. Mô hình đề xuất PhoBERT–Bi-LSTM ........................................................... 32 
3.2.1. Mô hình PhoBERT encoder ..................................................................... 33 
3.2.2. Mô hình Bi-LSTM .................................................................................... 34 
3.2.3. Lớp phân loại ............................................................................................ 35 
3.3. Quy trình huấn luyện mô hình ........................................................................ 36 
3.4. Các kĩ thuật hỗ trợ huấn luyện mô hình ......................................................... 36 
3.4.1. Tiền xử lý dữ liệu ..................................................................................... 38 
3.4.2. Phương pháp xử lý mất cân bằng dữ liệu ................................................. 39 
3.5. Tổng kết Chương 3 ......................................................................................... 41 
CHƯƠNG 4. THỰC NGHIỆM ................................................................................ 43 
4.1. Bộ dữ liệu sử dụng .......................................................................................... 43 
4.1.1. Giới thiệu bộ dữ liệu ViHSD.................................................................... 43

## Page 13

P
A
G
E  
\* 
ro
ma
n x 
 
10 
 
4.1.2. Phân bố dữ liệu theo các nhãn .................................................................. 44 
4.1.3. Phân chia tập huấn luyện, tập kiểm tra và tập xác thực ........................... 44 
4.2. Thiết lập thực nghiệm ..................................................................................... 45 
4.2.1. Môi trường thực nghiệm........................................................................... 45 
4.2.2. Các tham số huấn luyện mô hình ............................................................. 46 
4.2.1. Quy trình huấn luyện và đánh giá ............................................................ 47 
4.3. Các chỉ số đánh giá ......................................................................................... 49 
4.3.1. Accuracy ................................................................................................... 49 
4.3.2. Precision ................................................................................................... 50 
4.3.3. Recall ........................................................................................................ 50 
4.3.4. F1 score .................................................................................................... 50 
4.3.5. Ma trận nhầm lẫn ...................................................................................... 51 
4.4. Các mô hình so sánh ....................................................................................... 51 
4.4.1. Nhóm mô hình học sâu ............................................................................. 51 
4.4.2. Nhóm mô hình ngôn ngữ tiền huấn luyện và ngôn ngữ lớn ..................... 52 
4.5. Kết quả thực nghiệm ....................................................................................... 52 
4.6. Phân tích ảnh hưởng của các phương pháp cân bằng dữ liệu ......................... 53 
4.7. Thảo luận kết quả thực nghiệm ...................................................................... 53 
4.8. Chương trình minh họa ................................................................................... 55 
4.9. Tổng kết Chương 4 ......................................................................................... 55 
CHƯƠNG 5. KẾT LUẬN ......................................................................................... 57 
5.1. Kết luận ........................................................................................................... 57 
5.2. Hạn chế ........................................................................................................... 58 
5.3. Hướng phát triển ............................................................................................. 59

## Page 14

P
A
G
E  
\* 
ro
ma
n x 
 
11 
 
TÀI LIỆU THAM KHẢO ......................................................................................... 61 
PHẦN LÝ LỊCH TRÍCH NGANG ........................................................................... 62

## Page 15

P
A
G
E 
6 
 
1 
 
DANH MỤC TỪ VIẾT TẮT 
STT Từ viết tắt Tiếng Anh Diễn giải 
1 ACC Accuracy Độ chính xác của mô hình 
phân loại 
2 BERT Bidirectional Encoder 
Representations from 
Transformers 
Mô hình biểu diễn ngôn ngữ 
hai chiều dựa trên kiến trúc 
Transformer 
3 Bi-LSTM Bidirectional Long Short-
Term Memory 
Mạng LSTM hai chiều khai 
thác thông tin theo cả hai 
hướng 
4 CNN Convolutional Neural 
Network 
Mạng nơ-ron tích chập dùng 
để trích xuất đặc trưng dữ 
liệu 
5 CPU Central Processing Unit Bộ xử lý trung tâm của máy 
tính 
6 DL Deep Learning Học sâu 
7 Embedding Word Embedding Biểu diễn từ dưới dạng 
vector số trong không gian 
đặc trưng 
8 FN False Negative Dự đoán sai thành lớp âm 
9 FP False Positive Dự đoán sai thành lớp 
dương 
10 F1-score F1 Measure Trung bình điều hòa giữa 
Precision và Recall 
11 GPU Graphics Processing Unit Bộ xử lý đồ họa 
12 LSTM Long Short-Term Memory Mạng nơ-ron bộ nhớ dài – 
ngắn hạn 
13 Macro-F1 Macro-Averaged F1 Score Giá trị F1 trung bình giữa 
các lớp 
14 ML Machine Learning Học máy 
15 NLP Natural Language 
Processing 
Xử lý ngôn ngữ tự nhiên 
16 PhoBERT Pho Bidirectional Encoder 
Representations from 
Transformers 
Mô hình BERT được huấn 
luyện cho tiếng Việt 
17 Precision Precision Tỷ lệ dự đoán đúng trên 
tổng số mẫu được dự đoán 
là dương 
18 Recall Recall Tỷ lệ mẫu dương được dự 
đoán đúng 
19 RNN Recurrent Neural Network Mạng nơ-ron hồi tiếp dùng 
cho dữ liệu chuỗi

## Page 16

P
A
G
E 
6 
 
2 
 
20 TN True Negative Dự đoán đúng lớp âm 
21 TP True Positive Dự đoán đúng lớp dương 
22 Transformer Transformer Kiến trúc mạng nơ-ron dựa 
trên cơ chế attention 
23 Token Token Đơn vị văn bản sau khi tách 
từ 
24 Tokenization Tokenization Quá trình tách văn bản 
thành các token 
25 ViHSD Vietnamese Hate Speech 
Detection 
Bộ dữ liệu phát hiện phát 
ngôn thù địch tiếng Việt

## Page 17

P
A
G
E 
6 
 
3 
 
DANH MỤC CÁC HÌNH ẢNH, SƠ ĐỒ 
 
Hình 3.1: Mô hình hệ thống dự đoán ........................ Error! Bookmark not defined. 
Hình 4.1.a1: số lượng mẫu 3 nhãn ............................ Error! Bookmark not defined. 
Hình 4.1.a2: ma trận nhầm lẫn .................................. Error! Bookmark not defined. 
Hình 4.1.a3: kết quả sau thực nghiệm ....................... Error! Bookmark not defined. 
Hình 4.1.a4: kết quả sau thực nghiệm ....................... Error! Bookmark not defined. 
Hình 4.1.b1: số lượng mẫu 3 nhãn ............................ Error! Bookmark not defined. 
Hình 4.1.b2: ma trận nhầm lẫn .................................. Error! Bookmark not defined. 
Hình 4.1.b3: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.b4: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.c1: số lượng mẫu 3 nhãn ............................ Error! Bookmark not defined. 
Hình 4.1.c2: ma trận nhầm lẫn .................................. Error! Bookmark not defined. 
Hình 4.1.c3: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.c4: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.d1: số lượng mẫu 3 nhãn ............................ Error! Bookmark not defined. 
Hình 4.1.d2: ma trận nhầm lẫn .................................. Error! Bookmark not defined. 
Hình 4.1.d3: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.d4: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.e1: số lượng mẫu 3 nhãn ............................ Error! Bookmark not defined. 
Hình 4.1.e2: ma trận nhầm lẫn .................................. Error! Bookmark not defined. 
Hình 4.1.e3: kết quả thực nghiệm ............................. Error! Bookmark not defined. 
Hình 4.1.e4: kết quả thực nghiệm ............................. Error! Bookmark not defined.

## Page 18

P
A
G
E 
6 
 
4 
 
Hình 4.3.1: Kết quả thực nghiệm 1 ........................... Error! Bookmark not defined. 
Hình 4.3.2: Kết quả thực nghiệm 2 ........................... Error! Bookmark not defined. 
Hình 3.15: Form giao diện ........................................ Error! Bookmark not defined.

## Page 19

P
A
G
E 
6 
 
5 
 
DANH MỤC BẢNG BIỂU 
 
Bảng 2.1: So sánh tổng quan mô hình huấn luyện ................................................. 9 
Bảng 2.2: Tổng hợp các chỉ số đánh giá mô hình dự đoán .................................. 14 
Bảng 3.1: Tổng hợp các phương pháp .................................................................. 22 
Bảng 4.2: Kết quả thực nghiệm  ........................................................................... 47

## Page 20

P
A
G
E 
6 
 
6 
 
CHƯƠNG 1. GIỚI THIỆU 
 
1.1. Đặt vấn đề 
Trong bối cảnh sự phát triển nhanh chóng của Internet và các nền tảng mạng xã hội, 
khối lượng nội dung do người dùng tạo ra ngày càng gia tăng với tốc độ rất lớn. Bên 
cạnh những giá trị tích cực trong việc chia sẻ thông tin và kết nối cộng đồng, môi 
trường trực tuyến cũng đang xuất hiện ngày càng nhiều các nội dung tiêu cực, trong 
đó nổi bật là các phát ngôn thù địch. Đây là những phát biểu mang tính xúc phạm, 
miệt thị hoặc kích động thù hận đối với cá nhân hoặc nhóm người dựa trên các đặc 
điểm như giới tính, tôn giáo, chủng tộc, quốc tịch hoặc quan điểm xã hội. Sự lan 
truyền của các phát ngôn này không chỉ gây tổn hại đến cá nhân bị nhắm đến mà còn 
ảnh hưởng tiêu cực đến môi trường giao tiếp trực tuyến và trật tự xã hội. 
Trong thực tế, việc phát hiện và kiểm soát các phát ngôn thù địch bằng phương pháp 
thủ công gặp nhiều hạn chế do khối lượng dữ liệu quá lớn, tốc độ lan truyền thông tin 
nhanh và sự đa dạng trong cách sử dụng ngôn ngữ của người dùng. Nội dung trên 
mạng xã hội thường chứa nhiều dạng biểu đạt phức tạp như ẩn dụ, mỉa mai, biến thể 
chính tả hoặc sử dụng từ lóng, khiến việc nhận diện các phát ngôn mang tính thù địch 
trở nên khó khăn. Do đó, các phương pháp dựa trên xử lý ngôn ngữ tự nhiên và học 
máy đã được nghiên cứu nhằm tự động hóa quá trình phát hiện các nội dung độc hại 
trong văn bản. 
Trong những năm gần đây, các mô hình học sâu đã đạt được nhiều tiến bộ đáng kể 
trong các bài toán xử lý ngôn ngữ tự nhiên nhờ khả năng học biểu diễn ngữ nghĩa từ 
dữ liệu lớn. Đặc biệt, các mô hình ngôn ngữ tiền huấn luyện dựa trên kiến trúc 
Transformer đã cho thấy hiệu quả vượt trội trong nhiều tác vụ phân loại văn bản. Đối 
với tiếng Việt, mô hình PhoBERT được phát triển nhằm khai thác đặc trưng ngôn 
ngữ của tiếng Việt và đã chứng minh hiệu quả trong nhiều nhiệm vụ xử lý ngôn ngữ 
tự nhiên. Tuy nhiên, việc k hai thác đầy đủ các mối quan hệ ngữ cảnh trong chuỗi từ 
vẫn là một thách thức, đặc biệt trong các văn bản có cấu trúc ngữ nghĩa phức tạp.

## Page 21

P
A
G
E 
6 
 
7 
 
Bên cạnh đó, dữ liệu phát hiện phát ngôn thù địch thường tồn tại hiện tượng mất cân 
bằng giữa các lớp nhãn, trong đó các mẫu văn bản không mang nội dung thù địch 
thường chiếm số lượng lớn hơn đáng kể so với các mẫu thuộc lớp thù địch hoặc xúc 
phạm. Sự mất cân bằng này có thể khiến mô hình học thiên lệch và làm giảm khả 
năng nhận diện chính xác các lớp thiểu số. Vì vậy, việc nghiên cứu các phương pháp 
xử lý mất cân bằng dữ liệu và đánh giá ảnh hưởng của chúng đến hiệu quả mô hình 
là một vấn đề quan trọng trong quá trình xây dựng hệ thống phát hiện phát ngôn thù 
địch. 
Xuất phát từ những vấn đề trên, đề án này tập trung nghiên cứu và xây dựng mô hình 
học sâu nhằm phát hiện phát ngôn thù địch trong văn bản tiếng Việt trên mạng xã hội. 
Nghiên cứu sử dụng bộ dữ liệu ViHSD 2019 và đề xuất mô hình kết hợp giữa 
PhoBERT và Bi-LSTM nhằm khai thác đồng thời biểu diễn ngữ nghĩa theo ngữ cảnh 
và thông tin phụ thuộc tuần tự trong chuỗi từ. Thông qua việc đánh giá hiệu quả của 
mô hình và khảo sát các phương pháp xử lý mất cân bằng dữ liệu, đề án hướng đến 
việc cải thiện khả năng phân loạ i phát ngôn thù địch trong môi trường mạng xã hội 
tiếng Việt.. 
1.2. Phát biểu bài toán 
Trong môi trường mạng xã hội, người dùng thường xuyên đăng tải các bài viết, bình 
luận và trao đổi thông tin với số lượng rất lớn mỗi ngày. Trong số đó tồn tại nhiều 
nội dung mang tính xúc phạm hoặc kích động thù địch, gây ảnh hưởng tiêu cực đến 
cá nhân, c ộng đồng và môi trường giao tiếp trực tuyến. Do khối lượng dữ liệu quá 
lớn và tốc độ lan truyền thông tin nhanh, việc kiểm soát các nội dung này bằng phương 
pháp thủ công trở nên không hiệu quả. Vì vậy cần có các hệ thống tự động có khả 
năng phát hiện và phân loại các phát ngôn thù địch trong văn bản. 
Bài toán phát hiện phát ngôn thù địch trong nghiên cứu này được xem như một bài 
toán phân loại văn bản đa lớp trong lĩnh vực xử lý ngôn ngữ tự nhiên. Với đầu vào là 
một câu hoặc một bình luận bằng tiếng Việt được đăng tải trên mạng xã hội, hệ thống 
cần xác định nội dung của văn bản đó thuộc về một trong ba loại nhãn khác nhau.

## Page 22

P
A
G
E 
6 
 
8 
 
 
Cụ thể, các nhãn được sử dụng trong nghiên cứu bao gồm: 
- Hate: Văn bản chứa nội dung thù địch, kích động thù hận hoặc tấn công trực 
tiếp đến cá nhân hoặc nhóm người dựa trên các đặc điểm như giới tính, tôn 
giáo, dân tộc hoặc quan điểm xã hội. 
- Offensive: Văn bản có chứa ngôn từ xúc phạm hoặc thô tục nhưng không mang 
tính kích động thù hận đối với một nhóm người cụ thể. 
- Clean: Văn bản không chứa nội dung xúc phạm hoặc thù địch. 
Do đó, bài toán đặt ra là xây dựng một mô hình có khả năng tự động phân loại văn 
bản tiếng Việt trên mạng xã hội vào một trong ba nhãn Hate, Offensive hoặc Clean. 
Mô hình cần học được các đặc trưng ngữ nghĩa và ngữ cảnh của văn bản để nhận diện 
chính xác các phát ngôn thù địch, đồng thời hạn chế việc phân loại sai các nội dung 
trung tính. 
Trong nghiên cứu này, dữ liệu được sử dụng là bộ dữ liệu ViHSD (Vietnamese Hate 
Speech Detection), bao gồm các bài đăng và bình luận trên mạng xã hội đã được gán 
nhãn theo ba lớp nói trên. Một đặc điểm quan trọng của bộ dữ liệu là sự mất cân bằng 
giữa các lớp, trong đó các văn bản thuộc lớp Clean thường chiếm tỷ lệ lớn hơn so với 
các lớp Hate và Offensive. Điều này đặt ra yêu cầu cần có các phương pháp xử lý phù 
hợp nhằm giúp mô hình học được tốt hơn các đặc trưng của các lớp thiểu số. 
Xuất phát từ những yêu cầu trên, nghiên cứu này tập trung xây dựng một mô hình 
phát hiện phát ngôn thù địch dựa trên phương pháp học sâu, trong đó sử dụng mô 
hình ngôn ngữ tiền huấn luyện PhoBERT để trích xuất biểu diễn ngữ nghĩa của văn 
bản và kết hợp với  mạng Bi-LSTM nhằm khai thác thông tin ngữ cảnh trong chuỗi 
từ, từ đó thực hiện phân loại văn bản vào các lớp tương ứng. 
1.3. Mục tiêu, đối tượng và phạm vi nghiên cứu đề án 
1.3.1. Mục tiêu đề án

## Page 23

P
A
G
E 
6 
 
9 
 
1.3.1.1. Mục tiêu tổng quát: 
Mục tiêu của đề án là nghiên cứu và xây dựng một mô hình học sâu nhằm phát hiện 
phát ngôn thù địch trong văn bản tiếng Việt trên các nền tảng mạng xã hội.  
Thông qua việc ứng dụng các kỹ thuật trong lĩnh vực xử lý ngôn ngữ tự nhiên và học 
sâu, đề án hướng đến việc tự động phân loại nội dung văn bản theo mức độ xúc phạm 
hoặc thù địch, từ đó góp phần hỗ trợ quá trình kiểm duyệt và quản lý nội dung trên 
môi trường trực tuyến. 
1.3.1.2. Mục tiêu cụ thể: 
Cụ thể, đề án tập trung vào các mục tiêu sau: 
- Nghiên cứu cơ sở lý thuyết liên quan đến xử lý ngôn ngữ tự nhiên, học máy 
và học sâu trong bài toán phân loại văn bản. 
- Khảo sát đặc điểm của bài toán phát hiện phát ngôn thù địch trong văn bản 
tiếng Việt và phân tích đặc trưng của bộ dữ liệu ViHSD được sử dụng trong 
nghiên cứu. 
- Xây dựng mô hình học sâu kết hợp giữa PhoBERT và Bi-LSTM nhằm khai 
thác biểu diễn ngữ nghĩa theo ngữ cảnh và quan hệ phụ thuộc trong chuỗi văn 
bản. 
- Nghiên cứu và áp dụng các phương pháp xử lý mất cân bằng dữ liệu nhằm cải 
thiện khả năng nhận diện các lớp thiểu số trong quá trình huấn luyện mô hình. 
- Thực nghiệm và đánh giá hiệu quả của mô hình đề xuất thông qua các chỉ số 
đánh giá phổ biến trong bài toán phân loại văn bản. 
Thông qua các mục tiêu trên, đề án hướng đến việc xây dựng một phương pháp phát 
hiện phát ngôn thù địch trong tiếng Việt có hiệu quả, đồng thời cung cấp cơ sở cho 
các nghiên cứu tiếp theo trong lĩnh vực phân tích nội dung và kiểm duyệt thông tin 
trên mạng xã hội. 
1.3.1.3. Kết quả dự kiến: 
Thông qua quá trình nghiên cứu và thực nghiệm, đề án dự kiến đạt được các kết quả 
sau:

## Page 24

P
A
G
E 
6 
 
10 
 
- Xây dựng được một mô hình học sâu kết hợp giữa PhoBERT và Bi-LSTM 
nhằm phát hiện phát ngôn thù địch trong văn bản tiếng Việt trên mạng xã hội. 
- Đề xuất và áp dụng các phương pháp xử lý mất cân bằng dữ liệu nhằm cải 
thiện hiệu quả phân loại giữa các lớp Hate, Offensive và Clean trong bộ dữ 
liệu nghiên cứu. 
- Đánh giá hiệu quả của mô hình thông qua các chỉ số đo lường phổ biến trong 
bài toán phân loại văn bản như Precision, Recall, F1-score và Macro-F1. 
- Phân tích và so sánh kết quả thực nghiệm của các phương pháp xử lý mất cân 
bằng dữ liệu cũng như các mô hình phân loại nhằm xác định phương pháp phù 
hợp cho bài toán phát hiện phát ngôn thù địch. 
- Xây dựng một chương trình minh họa cho phép nhập văn bản và thực hiện dự 
đoán nhãn tương ứng, qua đó minh chứng khả năng ứng dụng của mô hình 
trong các hệ thống hỗ trợ kiểm duyệt nội dung trực tuyến. 
1.3.2. Đối tượng nghiên cứu 
Đối tượng nghiên cứu của đề án là các phương pháp và mô hình học máy, đặc biệt là 
các mô hình học sâu trong lĩnh vực xử lý ngôn ngữ tự nhiên, được áp dụng cho bài 
toán phát hiện phát ngôn thù địch trong văn bản tiếng Việt trên mạng xã hội. Nghiên 
cứu tập trung vào việc khai thác các đặc trưng ngữ nghĩa và ngữ cảnh của văn bản 
nhằm phân loại nội dung theo mức độ xúc phạm hoặc thù địch. 
Cụ thể, đề án tập trung nghiên cứu mô hình ngôn ngữ tiền huấn luyện PhoBERT kết 
hợp với mạng nơ -ron hồi quy hai chiều Bi-LSTM để xây dựng hệ thống phát hiện 
phát ngôn thù địch. Bên cạnh đó, đề án cũng xem xét các phương pháp xử lý mất cân 
bằng dữ liệu nhằm cải thiện hiệu quả phân loại trong bối cảnh dữ liệu có sự chênh 
lệch về số lượng giữa các lớp nhãn. 
Như vậy, đối tượng nghiên cứu của đề án bao gồm các mô hình học sâu, các kỹ thuật 
xử lý dữ liệu văn bản và các phương pháp xử lý mất cân bằng dữ liệu được áp dụng 
trong bài toán phát hiện phát ngôn thù địch trong tiếng Việt. 
1.3.3. Phạm vi nghiên cứu

## Page 25

P
A
G
E 
6 
 
11 
 
Đề án tập trung nghiên cứu bài toán phát hiện phát ngôn thù địch trong văn bản tiếng 
Việt trên môi trường mạng xã hội. Nghiên cứu được thực hiện dựa trên bộ dữ liệu 
ViHSD (Vietnamese Hate Speech Detection), bao gồm các bài đăng và bình luận trực 
tuyến đã được gán nhãn theo ba lớp: Hate, Offensive và Clean. 
Trong phạm vi nghiên cứu, đề án tập trung xây dựng và đánh giá mô hình học sâu kết 
hợp giữa PhoBERT và Bi-LSTM nhằm thực hiện phân loại văn bản theo các nhãn 
nói trên. Các bước tiền xử lý văn bản, xử lý mất cân bằng dữ liệu và huấn luyện mô 
hình được thực hiện trên tập dữ liệu này nhằm nâng cao hiệu quả nhận diện phát ngôn 
thù địch. 
Đề án chỉ xem xét dữ liệu văn bản tiếng Việt và không mở rộng sang các loại dữ liệu 
khác như hình ảnh, âm thanh hoặc video. Ngoài ra, nghiên cứu cũng không tập trung 
vào việc xây dựng hệ thống kiểm duyệt nội dung hoàn chỉnh mà chủ yếu nhằm đánh 
giá hiệu qu ả của mô hình trong việc phân loại phát ngôn thù địch trên dữ liệu văn 
bản.. 
1.4. Tình hình nghiên cứu và tính mới của đề án 
1.4.1. Tình hình nghiên cứu 
Trong khoảng ba năm gần đây (2023-2025), nghiên cứu phát hiện phát ngôn thù địch trên mạng xã hội phát triển theo ba hướng chính: (i) chuyển dịch từ mô hình học máy truyền thống sang mô hình ngôn ngữ tiền huấn luyện/Transformer và các biến thể đa ngữ, (ii) mở rộng bài toán từ phân loại mức câu sang phát hiện theo span, theo mục tiêu bị công kích (target-aware), và đa nhãn, (iii) quan tâm nhiều hơn đến bài toán ngôn ngữ ít tài nguyên, mất cân bằng dữ liệu và khả năng giải thích mô hình [10]-[20]. 

Ở trong nước, hệ nghiên cứu xoay quanh tiếng Việt đã hình thành tương đối rõ chuỗi phát triển từ dữ liệu nền tảng đến mô hình chuyên biệt. ViHSD là cột mốc khởi đầu quan trọng, tạo bộ dữ liệu chuẩn cho bài toán phát hiện phát ngôn thù địch tiếng Việt [1]. Trên nền này, các hướng nâng hiệu năng đã được triển khai như tăng cường dữ liệu cho BERTology [2], tiền huấn luyện mô hình ngôn ngữ chuyên biệt cho văn bản mạng xã hội tiếng Việt (ViSoBERT) [3], phát hiện span thù địch/xúc phạm (ViHOS, Abusive Span) [4], [6], cũng như mở rộng sang mô hình text-to-text và bài toán phát hiện thù địch theo mục tiêu (ViHateT5, ViTHSD) [5], [7]. Các nghiên cứu gần đây cũng cho thấy vai trò của chuẩn hóa từ vựng mạng xã hội trong việc giảm nhiễu đầu vào cho các tác vụ phát hiện nội dung độc hại tiếng Việt [8]. 

Ở ngoài nước, xu hướng chung tập trung vào khả năng tổng quát hóa liên ngôn ngữ và ngôn ngữ ít tài nguyên, với nhiều bằng chứng cho thấy Transformer/PLM vẫn là lõi phương pháp trong phát hiện hate speech/cyberbullying [10], [12]-[17]. Bên cạnh việc tối ưu hiệu năng, các nghiên cứu gần đây nhấn mạnh hơn vào vấn đề định nghĩa, đo lường và độ tin cậy triển khai thực tế của hệ thống phát hiện phát ngôn thù địch [11], [18], [19]. Đồng thời, các hướng gắn phân loại với trích xuất bằng chứng (rationale/span) được quan tâm do giúp tăng tính minh bạch và khả năng hỗ trợ kiểm duyệt nội dung trên quy mô lớn [15], [20]. 

Tổng hợp các kết quả trên cho thấy khoảng trống nghiên cứu còn rõ ở bối cảnh tiếng Việt: cần một quy trình thống nhất vừa tận dụng biểu diễn ngữ nghĩa mạnh của mô hình tiền huấn luyện, vừa xử lý tốt hiện tượng mất cân bằng nhãn và nhiễu ngôn ngữ mạng xã hội, đồng thời duy trì khả năng mở rộng sang các thiết lập phát hiện tinh hơn (span/target-aware). Đây cũng là động lực chính cho định hướng của đề án. 
1.4.2. Tính mới của đề án 
Từ việc khảo sát các nghiên cứu liên quan đến bài toán phát hiện phát ngôn thù địch 
trong văn bản, có thể thấy rằng nhiều phương pháp đã được đề xuất, từ các mô hình 
học máy truyền thống đến các mô hình học sâu hiện đại dựa trên kiến trúc 
Transformer. Tuy nhiên, đối với dữ liệu tiếng Việt, số lượng nghiên cứu vẫn còn hạn 
chế và chưa khai thác đầy đủ tiềm năng của các mô hình ngôn ngữ tiền huấn luyện 
kết hợp với các kỹ thuật xử lý dữ liệu phù hợp. Xuất phát từ thực tế đó, đề án hướng 
đến việc đề xuất một phư ơng pháp tiếp cận nhằm cải thiện hiệu quả phát hiện phát 
ngôn thù địch trong văn bản tiếng Việt. 
Tính mới của đề án được thể hiện ở các điểm sau:

## Page 26

P
A
G
E 
6 
 
12 
 
- Đề xuất mô hình kết hợp giữa mô hình ngôn ngữ tiền huấn luyện PhoBERT 
và mạng nơ -ron hồi quy hai chiều Bi-LSTM nhằm khai thác đồng thời biểu 
diễn ngữ nghĩa theo ngữ cảnh và thông tin phụ thuộc trong chuỗi văn bản. Sự 
kết hợp này cho phép mô hình tận dụng khả năng biểu diễn mạnh của 
PhoBERT đồng thời khai thác đặc trưng tuần tự của dữ liệu văn bản. 
- Nghiên cứu và áp dụng các phương pháp xử lý mất cân bằng dữ liệu trong quá 
trình huấn luyện nhằm cải thiện khả năng nhận diện các lớp thiểu số trong bộ 
dữ liệu. Việc so sánh nhiều phương pháp cân bằng dữ liệu khác nhau cho phép 
xác định chiến lược phù hợp cho bài toán phát hiện phát ngôn thù địch. 
- Thực hiện thực nghiệm và đánh giá mô hình trên bộ dữ liệu ViHSD, qua đó 
phân tích hiệu quả của mô hình đề xuất cũng như ảnh hưởng của các phương 
pháp xử lý mất cân bằng dữ liệu đối với kết quả phân loại. 
Những đóng góp này góp phần làm rõ khả năng ứng dụng của các mô hình ngôn ngữ 
tiền huấn luyện kết hợp với các kỹ thuật xử lý dữ liệu trong bài toán phát hiện phát 
ngôn thù địch đối với dữ liệu tiếng Việt.. 
1.5. Cấu trúc đề án 
Đề án được tổ chức thành năm chương chính, mỗi chương trình bày một nội dung cụ 
thể nhằm làm rõ quá trình nghiên cứu từ cơ sở lý thuyết đến phương pháp đề xuất và 
kết quả thực nghiệm. 
Chương 1. Giới thiệu trình bày bối cảnh nghiên cứu, lý do lựa chọn đề tài và tầm quan 
trọng của bài toán phát hiện phát ngôn thù địch trong văn bản tiếng Việt. Chương này 
đồng thời phát biểu bài toán nghiên cứu, xác định mục tiêu, đối tượng và phạm vi 
nghiên cứu của đề án. Bên cạnh đó, chương cũng tổng quan tình hình nghiên cứu liên 
quan và nêu ra tính mới của đề án. 
Chương 2. Tổng quan nghiên cứu trình bày các cơ sở lý thuyết và các công trình 
nghiên cứu liên quan đến bài toán phát hiện phát ngôn thù địch. Nội dung chương 
bao gồm các khái niệm cơ bản trong xử lý ngôn ngữ tự nhiên, các phương pháp học 
máy và học sâu trong phân loại văn bản, kiến trúc Transformer và mô hình PhoBERT,

## Page 27

P
A
G
E 
6 
 
13 
 
cũng như các phương pháp xử lý mất cân bằng dữ liệu thường được áp dụng trong 
các bài toán phân loại. 
Chương 3. Phương pháp đề xuất mô tả chi tiết phương pháp được sử dụng trong 
nghiên cứu. Chương này trình bày tổng quan pipeline của hệ thống, các bước tiền xử 
lý dữ liệu, phương pháp xử lý mất cân bằng dữ liệu và kiến trúc mô hình đề xuất kết 
hợp giữa PhoBERT và Bi-LSTM. Ngoài ra, chương cũng mô tả quy trình huấn luyện 
mô hình và cách thức áp dụng mô hình vào bài toán phân loại văn bản. 
Chương 4. Thực nghiệm và đánh giá trình bày quá trình thực nghiệm nhằm đánh giá 
hiệu quả của mô hình đề xuất. Nội dung chương bao gồm mô tả bộ dữ liệu sử dụng 
trong thực nghiệm, thiết lập môi trường thực nghiệm, các chỉ số đánh giá, so sánh các 
phương pháp xử lý mất cân bằng dữ liệu và các mô hình so sánh. Kết quả thực nghiệm 
được phân tích và thảo luận nhằm làm rõ hiệu quả của phương pháp đề xuất. 
Chương 5. Kết luận và hướng phát triển tổng hợp các kết quả đạt được của đề án và 
đưa ra các nhận xét về hiệu quả của phương pháp nghiên cứu. Đồng thời, chương 
cũng đề xuất một số hướng nghiên cứu tiếp theo nhằm cải thiện và mở rộng phương 
pháp trong các nghiên cứu tương lai. 
1.6. Tổng kết Chương 1 
Chương 1 đã trình bày bối cảnh và lý do lựa chọn đề tài nghiên cứu liên quan đến bài 
toán phát hiện phát ngôn thù địch trong văn bản tiếng Việt trên các nền tảng mạng xã 
hội. Nội dung chương đã nêu rõ vấn đề nghiên cứu, phát biểu bài toán và xác định 
mục tiêu của đề án nhằm xây dựng mô hình tự động phát hiện và phân loại các nội 
dung mang tính xúc phạm hoặc thù địch trong văn bản. 
Bên cạnh đó, chương cũng đã xác định đối tượng và phạm vi nghiên cứu của đề án, 
trong đó tập trung vào việc ứng dụng các phương pháp học sâu trong lĩnh vực xử lý 
ngôn ngữ tự nhiên để giải quyết bài toán phân loại văn bản tiếng Việt. Tình hình 
nghiên cứu liên quan trong và ngoài nước cũng được khái quát nhằm làm rõ hướng 
tiếp cận của đề án cũng như các vấn đề còn tồn tại trong các nghiên cứu trước đây. 
Trên cơ sở đó, chương đã trình bày tính mới của đề án và mô tả cấu trúc tổng thể của

## Page 28

P
A
G
E 
6 
 
14 
 
luận văn. Những nội dung này tạo nền tảng cho các chương tiếp theo, trong đó chương 
2 sẽ trình bày cơ sở lý thuyết và tổng quan các nghiên cứu liên quan đến bài toán phát 
hiện phát ngôn thù địch và các phương pháp xử lý dữ liệu văn bản.

## Page 29

P
A
G
E 
6 
 
15 
 
CHƯƠNG 2. CÁC NGHIÊN CỨU LIÊN QUAN 
2.1. Bài toán phát hiện phát ngôn thù địch 
Sự phát triển nhanh chóng của các nền tảng mạng xã hội đã tạo ra một môi trường 
giao tiếp trực tuyến với khối lượng dữ liệu văn bản rất lớn. Bên cạnh những lợi ích 
trong việc trao đổi thông tin và kết nối cộng đồng, các nền tảng này cũng xuất hiện 
nhiều nội dung tiêu cực như xúc phạm, miệt thị hoặc kích động thù hận. Những nội 
dung này thường được gọi chung là phát ngôn thù địch và có thể gây ảnh hưởng tiêu 
cực đến cá nhân, cộng đồng cũng như môi trường giao tiếp trên không gian mạng. 
Trong lĩnh vực xử lý ngôn ngữ tự nhiên, bài toán phát hiện phát ngôn thù địch được 
xem như một dạng của bài toán phân loại văn bản. Mục tiêu của bài toán là xây dựng 
các mô hình có khả năng tự động nhận diện và phân loại các nội dung văn bản theo 
mức độ xú c phạm hoặc thù địch. Với đầu vào là một câu hoặc một bình luận trên 
mạng xã hội, hệ thống cần xác định liệu văn bản đó có chứa nội dung thù địch hay 
không, hoặc phân loại văn bản theo các mức độ khác nhau của hành vi xúc phạm. 
Trong nhiều nghiên cứu, phát ngôn thù địch được định nghĩa là các nội dung thể hiện 
sự công kích hoặc kích động thù hận đối với cá nhân hoặc nhóm người dựa trên các 
đặc điểm như giới tính, chủng tộc, tôn giáo, dân tộc hoặc quan điểm xã hội. Tuy 
nhiên, trong thực tế, việc phân biệt giữa phát ngôn thù địch và các dạng ngôn từ xúc 
phạm thông thường không phải lúc nào cũng rõ ràng. Vì vậy, nhiều bộ dữ liệu và 
nghiên cứu thường chia nội dung văn bản thành nhiều lớp khác nhau nhằm phản ánh 
mức độ tiêu cực của nội dung. 
Trong nghiên cứu này, bài toán phát hiện phát ngôn thù địch được xây dựng dưới 
dạng bài toán phân loại văn bản đa lớp với ba nhãn chính: Hate, Offensive và Clean. 
Nhãn Hate biểu thị các nội dung mang tính kích động thù hận hoặc công kích trực 
tiếp đến cá nhân hoặc nhóm người. Nhãn Offensive biểu thị các nội dung có ngôn từ 
xúc phạm hoặc thô tục nhưng không mang tính kích động thù hận rõ ràng. Nhãn Clean 
biểu thị các nội dung trung tính không chứa ngôn từ xúc phạm. 
Một thách thức quan trọng của bài toán phát hiện phát ngôn thù địch là sự phức tạp

## Page 30

P
A
G
E 
6 
 
16 
 
của ngôn ngữ tự nhiên trên mạng xã hội. Văn bản thường có độ dài ngắn, chứa nhiều 
từ viết tắt, biểu tượng cảm xúc, tiếng lóng hoặc các biến thể của từ ngữ. Bên cạnh đó, 
sự mất cân bằng giữa các lớp dữ liệu cũng là một vấn đề phổ biến trong các bộ dữ 
liệu phát hiện phát ngôn thù địch, khi các văn bản không chứa nội dung thù địch 
thường chiếm tỷ lệ lớn hơn so với các lớp còn lại. 
Do những đặc điểm trên, việc xây dựng các mô hình có khả năng khai thác hiệu quả 
thông tin ngữ nghĩa và ngữ cảnh của văn bản đóng vai trò quan trọng trong việc nâng 
cao hiệu quả của hệ thống phát hiện phát ngôn thù địch. Các phương pháp học sâu và 
các mô hình ngôn ngữ tiền huấn luyện hiện nay đang được xem là những hướng tiếp 
cận hiệu quả cho bài toán này. 
2.2. Các phương pháp học máy 
Trong bài toán phát hiện phát ngôn thù địch, học máy truyền thống là giai đoạn nền 
tảng trước khi học sâu và Transformer trở thành xu hướng chủ đạo. Cách tiếp cận 
kinh điển xem đây là bài toán phân loại văn bản giám sát: biểu diễn câu/bình luận 
bằng vector đặc trưng rời rạc (n-gram từ, n-gram ký tự, BoW, TF-IDF), sau đó huấn 
luyện bộ phân loại như Logistic Regression, Naive Bayes, SVM, Random Forest hoặc 
các mô hình boosting [21]-[24]. Dù đơn giản, cách tiếp cận này có ưu điểm lớn ở tính 
diễn giải, chi phí huấn luyện thấp, phù hợp khi dữ liệu gán nhãn còn hạn chế hoặc cần 
triển khai nhanh trong thực tế kiểm duyệt nội dung [23], [24]. 

Về mặt mô hình, SVM từng là lựa chọn mạnh cho phân loại văn bản do xử lý tốt dữ 
liệu thưa và không gian đặc trưng lớn [21], [22], [25]. Logistic Regression (đặc biệt 
khi kết hợp chuẩn hóa L1/L2) cho baseline ổn định và dễ tối ưu trên dữ liệu lớn [26], 
[27]. Random Forest và boosting bổ sung khả năng mô hình hóa tương tác phi tuyến, 
tuy nhiên thường nhạy với cách thiết kế đặc trưng văn bản đầu vào [24]. Điểm chung 
của các mô hình này là chất lượng phụ thuộc mạnh vào bước tiền xử lý và kỹ thuật đặc 
trưng hóa; vì vậy cùng một thuật toán, kết quả có thể chênh lệch đáng kể giữa các bộ 
dữ liệu và miền ngôn ngữ khác nhau [23], [31], [32]. 

Trong phát hiện phát ngôn thù địch, giai đoạn 2015-2020 ghi nhận nhiều công trình 
xây dựng pipeline học máy chuẩn, làm rõ các lựa chọn đặc trưng và tiêu chí đánh giá. 
Burnap và Williams cho thấy phân loại máy có thể hỗ trợ giám sát nội dung thù hận ở 
quy mô lớn trên Twitter [30]. Waseem và Hovy nhấn mạnh vai trò của đặc trưng từ 
vựng/xã hội trong nhận diện hate speech [28], trong khi Davidson và cộng sự chỉ ra 
vấn đề then chốt là tách bạch “hate speech” với “offensive language” thay vì gộp chung 
một lớp độc hại [29]. Các tổng quan hệ thống hóa sau đó tiếp tục xác nhận khó khăn 
cốt lõi của hướng học máy truyền thống: phụ thuộc annotation guideline, mất cân bằng 
lớp, lệch miền dữ liệu và khác biệt định nghĩa giữa các nghiên cứu [31], [32], [40]. 

Một hướng phát triển quan trọng là chuẩn hóa bài toán qua các shared task và bộ dữ 
liệu đa ngôn ngữ. SemEval-2019 Task 5/6 và OffensEval 2020 tạo ra các benchmark 
tương đối thống nhất để so sánh mô hình giữa các ngôn ngữ, nhãn và mức độ xúc 
phạm [36]-[38]. Nghiên cứu về thiên lệch mô hình cũng cho thấy hệ phân loại có thể 
học lệch theo phương ngữ/cộng đồng người dùng nếu dữ liệu huấn luyện không cân 
bằng đại diện [41]. Ở góc nhìn triển khai đa nền tảng, các mô hình học máy kết hợp 
đặc trưng ngôn ngữ và embedding (ví dụ XGBoost + BERT features) đạt kết quả cạnh 
tranh trong bối cảnh dữ liệu thực tế nhiều nhiễu [42]. Các nghiên cứu gần đây về ngôn 
ngữ ít tài nguyên tiếp tục dùng khung transfer learning để giảm chi phí gán nhãn [10], 
[43]. 

Đối với tiếng Việt, bộ dữ liệu ViHSD đã đặt nền cho việc so sánh các baseline theo cùng 
không gian nhãn (HATE, OFFENSIVE, CLEAN), bao gồm cả các phương pháp học máy 
và học sâu cơ bản [1]. Trên nền tảng này, các nghiên cứu tăng cường dữ liệu giúp cải 
thiện chất lượng mô hình, đồng thời cho thấy vai trò quan trọng của dữ liệu trong việc 
thu hẹp khoảng cách giữa các phương pháp [2]. 

Tổng hợp lại, học máy truyền thống vẫn là mốc tham chiếu cần thiết nhờ tính gọn nhẹ, 
dễ diễn giải và chi phí thấp. Tuy nhiên, hạn chế về khai thác ngữ cảnh dài hạn, phụ thuộc 
đặc trưng thủ công và khả năng tổng quát hóa liên miền đã thúc đẩy chuyển dịch sang 
học sâu, đặc biệt là các kiến trúc tuần tự và mô hình biểu diễn ngữ nghĩa dày hơn; nội 
dung này được trình bày ở mục 2.3. 

## Page 32

P
A
G
E 
6 
 
18 
 
 
2.3. Các phương pháp học sâu 
Học sâu đánh dấu bước chuyển quan trọng từ chiến lược “thiết kế đặc trưng thủ công” 
sang “học biểu diễn tự động” trong xử lý ngôn ngữ tự nhiên [44]. Thay vì phụ thuộc 
hoàn toàn vào n-gram rời rạc, các mô hình học sâu xây dựng biểu diễn liên tục của từ 
và câu, giúp cải thiện khả năng khái quát khi dữ liệu mạng xã hội có nhiều biến thể 
chính tả, tiếng lóng và ngữ cảnh ngắn. Các kỹ thuật embedding như GloVe tạo nền 
cho nhiều kiến trúc học sâu trong phân loại văn bản [48], trong khi các khảo sát gần 
đây tiếp tục khẳng định chất lượng biểu diễn văn bản là yếu tố quyết định hiệu năng 
toàn hệ [56]. 

Về kiến trúc, CNN cho văn bản là một trong những mô hình học sâu sớm và hiệu quả, 
đặc biệt trong nhận diện mẫu cục bộ (cụm từ, biểu thức xúc phạm, token đặc trưng) [47]. 
Ưu điểm của CNN là tốc độ huấn luyện tốt và dễ song song hóa, nhưng hạn chế ở việc 
nắm bắt quan hệ phụ thuộc xa khi câu dài hoặc cấu trúc ngữ nghĩa phức tạp. Để xử lý 
phụ thuộc chuỗi, các mô hình RNN/LSTM/GRU được sử dụng rộng rãi: LSTM giải quyết 
vấn đề mất/bùng nổ gradient trong chuỗi dài [45], BiRNN mở rộng khả năng đọc ngữ 
cảnh hai chiều [46], còn RNN encoder-decoder (với GRU) chứng minh hiệu quả học 
biểu diễn tuần tự trong nhiều bài toán ngôn ngữ [49]. 

Một bước cải thiện tiếp theo là cơ chế attention, cho phép mô hình tập trung khác nhau 
vào các thành phần quan trọng của chuỗi thay vì xem mọi từ với trọng số đồng nhất [50]. 
Trên nền đó, các mô hình phân cấp có attention (ví dụ HAN) thể hiện khả năng tốt hơn 
trong phân loại tài liệu nhiều câu nhờ tách mức từ/câu rõ ràng [51]. Trong bài toán độc 
hại ngôn ngữ, điều này đặc biệt hữu ích khi tín hiệu thù địch chỉ xuất hiện ở một số đoạn 
ngắn nhưng quyết định nhãn toàn văn bản. 

Trong phát hiện phát ngôn thù địch, nhiều công trình đã kiểm chứng hiệu quả của học sâu 
so với baseline học máy cổ điển. Park và Fung cho thấy thiết kế phân tầng bài toán (one-step 
vs two-step) ảnh hưởng rõ rệt đến kết quả nhận diện abusive language [52]. Gambäck và 
Sikdar áp dụng CNN cho tweet và ghi nhận cải thiện đáng kể so với các thiết lập đặc trưng 
thủ công [53]. Badjatiya và cộng sự cho thấy lợi thế của kiến trúc sâu khi kết hợp embedding 
và bộ phân loại downstream [33]. Các nghiên cứu sau đó mở rộng sang nhiều nền tảng và 
tập dữ liệu lớn hơn, như Agrawal và Awekar (đa nền tảng) [54], Founta và cộng sự (kiến trúc 
thống nhất cho nhiều loại lạm dụng) [39], hay Roy và cộng sự với deep CNN [55]. 

Trong giai đoạn gần đây, các tổng quan chuyên biệt cho thấy học sâu vẫn là trục chính của 
hệ phát hiện cyberbullying/hate speech, đặc biệt ở bối cảnh ngôn ngữ ít tài nguyên và dữ liệu 
mất cân bằng [10], [17], [19]. Với tiếng Việt, ViHSD cung cấp mốc so sánh baseline quan trọng 
cho các mô hình sâu [1], và hướng tăng cường dữ liệu giúp cải thiện thêm chất lượng mô hình 
trên bài toán này [2]. Các kết quả trên cho thấy học sâu là bước trung gian then chốt: vượt qua 
hạn chế biểu diễn rời rạc của học máy truyền thống, nhưng vẫn còn điểm yếu về khả năng nắm 
bắt ngữ cảnh toàn cục dài hạn và hiệu quả chuyển miền. Đây là lý do các mô hình tiền huấn 
luyện dựa trên Transformer dần trở thành hướng chủ đạo, được trình bày trong mục 2.4. 
2.4. Các mô hình ngôn ngữ tiền huấn luyện 
Trong giai đoạn sau học sâu tuần tự, các mô hình ngôn ngữ tiền huấn luyện dựa trên 
Transformer trở thành hướng chủ đạo nhờ khả năng học biểu diễn ngữ cảnh mạnh và 
chuyển giao tốt giữa các tác vụ [57], [58]. Khác với kiến trúc phụ thuộc chuỗi thời gian, 
Transformer cho phép mã hóa quan hệ xa gần trong câu thông qua cơ chế attention và 
huấn luyện song song hiệu quả hơn. Các tổng quan gần đây cho thấy hệ mô hình này đã 
định hình lại toàn bộ pipeline NLP, từ phân loại, trích xuất thông tin đến suy luận ngôn ngữ 
[57], [59]. 

Trong nhóm encoder-only PLM, BERT là cột mốc quan trọng do cơ chế tiền huấn luyện 
học biểu diễn hai chiều theo ngữ cảnh [58]. Trên nền tảng này, các biến thể đa ngôn ngữ 
và mở rộng quy mô như XLM-R giúp cải thiện đáng kể khả năng chuyển giao liên ngôn ngữ, 
đặc biệt hữu ích cho các ngôn ngữ ít tài nguyên [60]. Với tiếng Việt, PhoBERT là mô hình 
tiền huấn luyện chuyên biệt có ảnh hưởng lớn trong nhiều tác vụ NLP và đã trở thành nền 
baseline mạnh cho bài toán phát hiện nội dung độc hại [61]. 

Đối với phát hiện phát ngôn thù địch, Transformer/PLM thường vượt các kiến trúc CNN/LSTM 
truyền thống nhờ biểu diễn ngữ nghĩa giàu hơn và khả năng tận dụng pre-training lớn. Các 
thực nghiệm trên dữ liệu mạng xã hội cho thấy BERT và các biến thể không chỉ cải thiện độ 
chính xác mà còn hỗ trợ tốt hơn cho xử lý thiên lệch thông qua thiết kế huấn luyện phù hợp 
[60], [62]. Ở ngôn ngữ không chuẩn hóa cao (ví dụ Roman Urdu), kiến trúc Transformer vẫn 
cho kết quả cạnh tranh và tổng quát hóa tốt hơn nhiều baseline học sâu cũ [63]. 

Trong bối cảnh tiếng Việt, các hướng gần đây mở rộng từ phân loại mức câu sang bài toán 
chi tiết hơn như nhận diện span, target-aware và text-to-text. ViSoBERT được thiết kế riêng 
cho văn bản mạng xã hội tiếng Việt [3]; ViHOS tập trung phát hiện span thù địch/xúc phạm 
[4]; ViHateT5 khai thác khung unified text-to-text [5]; và ViTHSD nhấn mạnh tín hiệu mục tiêu 
bị công kích trong phân loại [7]. Các kết quả này cho thấy chuyển dịch rõ ràng từ “phân loại 
nhãn đơn” sang “mô hình hóa cấu trúc phát ngôn thù địch”. 

Một xu hướng đáng chú ý khác là kết hợp phân loại với bằng chứng/rationale để tăng tính 
giải thích của mô hình. Các mô hình QA/seq2seq hoặc prompt-based có thể đồng thời dự đoán 
nhãn và trích xuất đoạn văn bản làm căn cứ, hỗ trợ triển khai kiểm duyệt ở mức vận hành [20]. 
Đây là bước đệm quan trọng nối từ PLM sang các thiết kế LLM có khả năng sinh giải thích tự 
nhiên và làm việc đa nhiệm. 

Ở tầng LLM, nghiên cứu hiện tập trung vào ba hướng: (i) đánh giá năng lực thực dụng trên tác 
vụ NLP và social computing [66], [67], [68], (ii) nhận diện rủi ro như thiên lệch, độc hại và sai thực 
(factuality) [64], [65], [69], và (iii) mở rộng sang thiết lập đa phương thức [70]. Với bài toán phát 
ngôn thù địch, LLM mở ra tiềm năng zero-/few-shot cho ngôn ngữ ít tài nguyên, nhưng cũng đặt 
ra yêu cầu cao hơn về kiểm soát an toàn, hiệu chuẩn và đánh giá công bằng liên nhóm người dùng 
[19], [64], [65]. 

Tóm lại, PLM/Transformer đã trở thành nền tảng trung tâm của các hệ thống phát hiện phát ngôn 
thù địch hiện đại; trong khi đó, LLM là hướng phát triển tiếp theo với năng lực suy luận và tạo giải 
thích mạnh hơn nhưng đi kèm thách thức quản trị rủi ro. Trên phương diện triển khai, lựa chọn mô 
hình cần cân bằng giữa hiệu năng, chi phí suy luận, khả năng giải thích và yêu cầu an toàn ứng dụng. 
2.5. Các phương pháp xử lý mất cân bằng dữ liệu 
Mất cân bằng dữ liệu là thách thức trung tâm trong các bài toán phân loại văn bản độc hại, khi lớp tiêu cực (ví dụ `Clean`) thường áp đảo các lớp quan trọng hơn về mặt an toàn như `Hate` và `Offensive` [71], [72]. Trong bối cảnh phát hiện phát ngôn thù địch, hiện tượng này đã được ghi nhận cả ở dữ liệu tiếng Việt lẫn đa ngôn ngữ, kéo theo xu hướng mô hình tối ưu theo lớp đa số nếu không có biện pháp cân bằng phù hợp [1], [2], [10], [16], [19]. 

Về nguyên tắc, các phương pháp xử lý mất cân bằng gồm ba hướng: (i) tăng mẫu lớp thiểu số (oversampling), (ii) giảm mẫu lớp đa số (undersampling), và (iii) phương pháp lai kết hợp tái lấy mẫu với làm sạch biên quyết định [72], [73], [78]. Ở mức kỹ thuật, ENN và Tomek Links đóng vai trò làm sạch điểm nhiễu/điểm chồng lấn gần biên lớp [75], [76], trong khi NearMiss và RUS tập trung chọn/lược bớt mẫu lớp đa số để giảm thiên lệch [77]. 

Trong luận án này, mục 2.5 bám đúng các biến thể đã dùng để tạo Bảng 4.6 trong repo: `ROS`, `ROS+ENN`, `ROS+NearMiss`, `ROS+RUS`, `ROS+Tomek` (không dùng `ROS+RUS+Tomek` trong bảng này). 

2.5.1. Phương pháp Random Over Sampling (ROS) 
Random Over Sampling (ROS) là chiến lược tăng số lượng mẫu lớp thiểu số bằng cách sao chép ngẫu nhiên các mẫu hiện có cho đến khi phân bố lớp cân bằng hơn [73], [74]. Ưu điểm của ROS là đơn giản, dễ tái lập, và thường là baseline mạnh trong nhiều nghiên cứu mất cân bằng [74]. 

Với dữ liệu ViHSD, ROS giúp tăng mức độ hiện diện của các mẫu `Hate` và `Offensive` trong quá trình tối ưu, nhờ đó mô hình giảm hiện tượng bỏ sót lớp thiểu số. Tuy nhiên, vì không tạo thêm thông tin mới mà chỉ lặp mẫu, ROS có thể làm tăng nguy cơ overfitting nếu số mẫu gốc quá ít hoặc nhiễu [71], [72]. 

2.5.2. Phương pháp ROS kết hợp với Edited Nearest Neighbours (ROS + ENN) 
ENN là kỹ thuật làm sạch dữ liệu dựa trên lân cận gần nhất: một điểm có thể bị loại nếu nhãn của nó không nhất quán với đa số láng giềng [75]. Khi kết hợp ROS + ENN, ta vừa tăng hiện diện lớp thiểu số (ROS), vừa giảm điểm biên nhiễu/chồng lấn (ENN), qua đó làm ranh giới quyết định rõ hơn [74]. 

Trong phân loại ngôn ngữ độc hại, tổ hợp oversampling + cleaning thường hữu ích khi dữ liệu mạng xã hội chứa nhiều biến thể chính tả, viết tắt và ngữ cảnh mơ hồ [10], [17], [78]. Tuy vậy, ENN cũng có thể loại cả các điểm “khó nhưng đúng”, làm giảm độ đa dạng của lớp thiểu số nếu áp dụng quá mạnh [72], [78]. 

2.5.3. Phương pháp ROS kết hợp với NearMiss 
NearMiss là kỹ thuật undersampling có kiểm soát: thay vì bỏ ngẫu nhiên, thuật toán ưu tiên giữ các mẫu lớp đa số gần lớp thiểu số (các điểm quan trọng cho biên phân tách) [77]. Tổ hợp ROS + NearMiss nhằm đạt hai mục tiêu đồng thời: bù số lượng cho lớp thiểu số và tinh gọn lớp đa số quanh vùng quyết định. 

Trong triển khai thực nghiệm của repo, để tránh trường hợp “no-op”, pipeline áp dụng `NearMiss` trước rồi mới `ROS` cho biến thể `ROS+NearMiss`. Cách sắp thứ tự này phù hợp với thực hành gần đây về cân bằng văn bản mất cân bằng nặng, nơi thứ tự tái lấy mẫu ảnh hưởng trực tiếp đến phân bố cuối và chất lượng biểu diễn [78], [79], [80]. 

2.5.4. Phương pháp ROS kết hợp với Random Under Sampling (ROS + RUS) 
RUS loại ngẫu nhiên một phần mẫu lớp đa số để giảm tỷ lệ lệch lớp [72], [73]. Khi kết hợp với ROS, ta tạo pipeline hai bước theo hai hướng ngược chiều: giảm bớt áp đảo của lớp đa số (RUS), sau đó tăng phủ của lớp thiểu số (ROS). 

Trong code thực nghiệm của luận án, biến thể `ROS+RUS` được thực thi theo thứ tự `RUS -> ROS`, tương tự lý do kỹ thuật ở mục 2.5.3. Thứ tự này giúp đảm bảo tập sau tái lấy mẫu có độ phủ lớp phù hợp và tránh suy giảm không cần thiết của lớp thiểu số [78], [79]. Đổi lại, rủi ro chính của RUS vẫn là mất thông tin hữu ích từ lớp đa số do loại mẫu ngẫu nhiên [71], [72]. 

2.5.5. Phương pháp ROS kết hợp với Tomek Links 
Tomek Links xác định các cặp điểm khác lớp nhưng là láng giềng gần nhất của nhau; các cặp này thường nằm sát biên quyết định và phản ánh vùng chồng lấn [76]. Trong biến thể `ROS+Tomek`, bước ROS được thực hiện trước để tăng đại diện lớp thiểu số, sau đó dùng Tomek Links làm sạch điểm biên nhiễu. 

Khác với biến thể có thêm RUS, cấu hình Bảng 4.6 chỉ dùng `ROS+Tomek`. Đây là lựa chọn giúp kiểm tra rõ tác động “oversampling + boundary cleaning” mà không thêm nhiễu từ bước loại ngẫu nhiên lớp đa số. 

Tổng hợp với kết quả thực nghiệm Bảng 4.6 cho thấy `PhoBIHSD + ROS` đạt Macro-F1 tốt nhất (0.6556), cao hơn mô hình không cân bằng (0.6457) và cao hơn các biến thể lai trong run hiện tại (`ROS+ENN`: 0.6485; `ROS+Tomek`: 0.6510; `ROS+RUS`: 0.5659; `ROS+NearMiss`: 0.4434). Điều này phù hợp với nhiều báo cáo gần đây rằng oversampling đơn giản vẫn là baseline khó vượt trong một số bài toán văn bản mất cân bằng, đặc biệt khi biểu diễn nền đã mạnh (PLM/Transformer) [74], [78], [80]. 
2.6. Tổng kết Chương 2 
Chương 2 đã trình bày tổng quan các cơ sở lý thuyết và các hướng nghiên cứu liên 
quan đến bài toán phát hiện phát ngôn thù địch trong văn bản. Trước hết, chương đã 
giới thiệu khái quát về bài toán phát hiện phát ngôn thù địch và những thách thức 
trong việc xử lý dữ liệu văn bản trên các nền tảng mạng xã hội. Đây là một bài toán 
quan trọng trong lĩnh vực xử lý ngôn ngữ tự nhiên, nhằm tự động nhận diện và phân 
loại các nội dung mang tính xúc phạm hoặc kích động thù hận trong môi trường trực 
tuyến. 
Tiếp theo, chương đã trình bày các phương pháp học máy và học sâu thường được áp 
dụng trong phân loại văn bản, bao gồm các mô hình truyền thống như Logistic 
Regression và các mô hình học sâu như CNN, RNN, LSTM và Bi-LSTM. Các mô 
hình này cho phép khai thác các đặc trưng ngữ nghĩa và ngữ cảnh của văn bản, từ đó 
cải thiện hiệu quả của hệ thống phân loại. 
Bên cạnh đó, chương cũng đã giới thiệu các mô hình ngôn ngữ tiền huấn luyện dựa 
trên kiến trúc Transformer, đặc biệt là mô hình PhoBERT được phát triển cho tiếng

## Page 44

P
A
G
E 
6 
 
30 
 
Việt. Các mô hình này cho phép học các biểu diễn ngữ nghĩa theo ngữ cảnh từ các 
tập dữ liệu lớn, qua đó nâng cao hiệu quả của nhiều bài toán xử lý ngôn ngữ tự nhiên. 
Ngoài ra, chương cũng đã trình bày các phương pháp xử lý mất cân bằng dữ liệu như 
Random Over Sampling, Random Under Sampling, NearMiss, ENN và Tomek 
Links. Các phương pháp này đóng vai trò quan trọng trong việc cải thiện hiệu quả 
của mô hình phân loại khi dữ liệu có sự chênh lệch lớn về số lượng giữa các lớp. 
Những nội dung được trình bày trong chương này cung cấp cơ sở lý thuyết và nền 
tảng nghiên cứu cho việc xây dựng phương pháp đề xuất trong đề án. Trên cơ sở các 
nghiên cứu liên quan và các kỹ thuật đã được khảo sát, chương tiếp theo sẽ trình bày 
chi tiết phương pháp đề xuất nhằm giải quyết bài toán phát hiện phát ngôn thù địch 
trong văn bản tiếng Việt.

## Page 45

P
A
G
E 
6 
 
31 
 
CHƯƠNG 3. PHƯƠNG PHÁP ĐỀ XUẤT 
3.1. Tổng quan hệ thống 
Trong nghiên cứu này, một hệ thống phát hiện phát ngôn thù địch trong văn bản tiếng 
Việt được đề xuất dựa trên việc kết hợp giữa mô hình ngôn ngữ tiền huấn luyện 
PhoBERT và mạng nơ ron hồi quy hai chiều Bi-LSTM. Hệ thống được thiết kế nhằm 
tự động phân loại các bình luận hoặc bài đăng trên mạng xã hội thành các lớp Hate, 
Offensive và Clean. Kiến trúc tổng thể của hệ thống bao gồm nhiều bước xử lý liên 
tiếp từ tiền xử lý dữ liệu đến huấn luyện mô hình và dự đoán nhãn. 
Quy trình hoạt động của hệ thống được minh họa trong Hình 3.1, bao gồm các thành 
phần chính như tiền xử lý dữ liệu, xử lý mất cân bằng dữ liệu, trích xuất biểu diễn 
văn bản bằng PhoBERT, mô hình học sâu Bi-LSTM và lớp phân loại cuối cùng. 
(Chèn Hình 3.1: Pipeline tổng thể của hệ thống phát hiện phát ngôn thù địch) 
Trong bước đầu tiên, dữ liệu văn bản được thu thập từ bộ dữ liệu ViHSD. Đây là một 
bộ dữ liệu tiếng Việt được xây dựng cho bài toán phát hiện phát ngôn thù địch trên 
mạng xã hội. Các văn bản trong tập dữ liệu bao gồm các bình luận và bài đăng đã 
được gán nhãn theo ba lớp Hate, Offensive và Clean. Tuy nhiên, bộ dữ liệu này có sự 
mất cân bằng giữa các lớp, trong đó lớp Clean thường chiếm số lượng lớn hơn so với 
các lớp còn lại. 
Sau khi dữ liệu được thu thập, bước tiếp theo là tiền xử lý dữ liệu văn bản. Mục tiêu 
của bước này là chuẩn hóa và làm sạch dữ liệu trước khi đưa vào mô hình học máy. 
Các thao tác tiền xử lý có thể bao gồm loại bỏ các ký tự đặc biệt, chuẩn hóa văn bản 
và chuyển đổi văn bản sang dạng phù hợp cho quá trình xử lý tiếp theo. Quy trình 
tiền xử lý dữ liệu giúp giảm nhiễu trong dữ liệu và cải thiện hiệu quả của mô hình 
phân loại. 
Tiếp theo, hệ thống áp dụng các phương pháp xử lý mất cân bằng dữ liệu nhằm giảm 
sự chênh lệch về số lượng giữa các lớp trong tập dữ liệu huấn luyện. Các phương 
pháp như Random Over Sampling, Random Under Sampling, NearMiss, ENN và

## Page 46

P
A
G
E 
6 
 
32 
 
Tomek Links có thể được áp dụng để điều chỉnh phân bố dữ liệu giữa các lớp. Việc 
xử lý mất cân bằng dữ liệu giúp mô hình học được các đặc trưng của các lớp thiểu số 
tốt hơn và giảm hiện tượng thiên lệch trong quá trình huấn luyện. 
Sau khi dữ liệu được chuẩn bị, các văn bản sẽ được đưa vào mô hình PhoBERT để 
trích xuất các biểu diễn ngữ nghĩa theo ngữ cảnh. PhoBERT là một mô hình ngôn 
ngữ tiền huấn luyện dành cho tiếng Việt, được xây dựng dựa trên kiến trúc 
Transformer. Mô hình này c ho phép chuyển đổi văn bản đầu vào thành các vector 
biểu diễn có khả năng phản ánh ý nghĩa ngữ cảnh của các từ trong câu. 
Các vector biểu diễn được trích xuất từ PhoBERT sau đó được đưa vào mô hình Bi-
LSTM nhằm khai thác thêm các quan hệ phụ thuộc trong chuỗi văn bản. Bi-LSTM 
xử lý dữ liệu theo hai hướng từ trái sang phải và từ phải sang trái, qua đó giúp mô 
hình học được nhiều thông tin ngữ cảnh hơn so với các mô hình xử lý một chiều. 
Cuối cùng, đầu ra của Bi-LSTM được đưa vào lớp phân loại sử dụng hàm softmax để 
dự đoán xác suất của từng lớp nhãn. Kết quả của hệ thống là nhãn dự đoán cho văn 
bản đầu vào, tương ứng với một trong ba lớp Hate, Offensive hoặc Clean. 
Như vậy, hệ thống đề xuất kết hợp các bước xử lý dữ liệu và mô hình học sâu nhằm 
khai thác hiệu quả các đặc trưng ngữ nghĩa và ngữ cảnh của văn bản tiếng Việt. Kiến 
trúc này tạo nền tảng cho các bước thực nghiệm và đánh giá hiệu quả của mô hình 
được trình bày trong các phần tiếp theo của chương này. 
3.2. Mô hình đề xuất PhoBERT–Bi-LSTM 
Trong bài toán phát hiện phát ngôn thù địch trong văn bản, việc trích xuất được các 
đặc trưng ngữ nghĩa và ngữ cảnh của câu đóng vai trò quan trọng đối với hiệu quả 
của mô hình phân loại. Các phương pháp học máy truyền thống thường sử dụng các 
kỹ thuật biểu diễn văn bản như Bag of Words hoặc TF –IDF, tuy nhiên các phương 
pháp này không thể khai thác đầy đủ thông tin ngữ cảnh của từ trong câu. Sự phát 
triển của các mô hình ngôn ngữ tiền huấn luyện đã mở ra hướng tiếp cận mới cho 
việc xây dựng các hệ thống phân loại văn bản có độ chính xác cao hơn. 
Trong nghiên cứu này, một mô hình kết hợp giữa PhoBERT và Bi-LSTM được đề

## Page 47

P
A
G
E 
6 
 
33 
 
xuất nhằm tận dụng ưu điểm của cả hai kiến trúc. PhoBERT được sử dụng để trích 
xuất các biểu diễn ngữ nghĩa theo ngữ cảnh của văn bản, trong khi Bi-LSTM được sử 
dụng để khai thác các quan hệ phụ thuộc trong chuỗi từ. Sự kết hợp này giúp mô hình 
có khả năng nắm bắt tốt hơn các đặc trưng ngữ nghĩa và cấu trúc của văn bản tiếng 
Việt. 
Kiến trúc tổng thể của mô hình đề xuất được minh họa trong Hình 3.5, bao gồm ba 
thành phần chính: lớp biểu diễn văn bản bằng PhoBERT, lớp học chuỗi Bi-LSTM và 
lớp phân loại cuối cùng. 
(Chèn Hình 3.5: Kiến trúc tổng thể của mô hình PhoBERT–Bi-LSTM) 
Trong mô hình này, văn bản đầu vào sau khi được tiền xử lý sẽ được đưa vào mô hình 
PhoBERT để chuyển đổi thành các vector biểu diễn ngữ nghĩa. Các vector này sau 
đó được đưa vào mạng Bi-LSTM nhằm khai thác thông tin ngữ cảnh trong chuỗi văn 
bản. Cuối cùng, đầu ra của Bi-LSTM được đưa vào lớp phân loại sử dụng hàm 
softmax để dự đoán xác suất của từng lớp nhãn. 
Cách tiếp cận này cho phép kết hợp khả năng biểu diễn ngữ nghĩa mạnh mẽ của các 
mô hình ngôn ngữ tiền huấn luyện với khả năng học quan hệ tuần tự của các mạng 
nơ ron hồi quy. Nhờ đó, mô hình có thể cải thiện khả năng nhận diện các phát ngôn 
thù địch trong dữ liệu văn bản tiếng Việt. 
3.2.1. Mô hình PhoBERT encoder 
PhoBERT là một mô hình ngôn ngữ tiền huấn luyện dành cho tiếng Việt được xây 
dựng dựa trên kiến trúc Transformer và được huấn luyện trên một tập dữ liệu văn bản 
tiếng Việt quy mô lớn. Mô hình này kế thừa nhiều đặc điểm của kiến trúc BERT, 
trong đó các biểu diễn của từ được học theo ngữ cảnh hai chiều. Điều này cho phép 
mô hình xem xét đồng thời thông tin từ cả phía trước và phía sau của mỗi từ trong 
câu. 
Kiến trúc tổng thể của PhoBERT được minh họa trong Hình 3.6. Mô hình bao gồm 
nhiều lớp encoder Transformer được xếp chồng lên nhau, trong đó mỗi lớp bao gồm 
các thành phần self attention và các lớp mạng nơ ron truyền thẳng. Cơ chế self

## Page 48

P
A
G
E 
6 
 
34 
 
attention cho phép mô hình xác định mức độ liên quan giữa các từ trong câu, từ đó 
xây dựng các biểu diễn ngữ nghĩa giàu thông tin hơn. 
(Chèn Hình 3.6: Kiến trúc mô hình PhoBERT) 
Trong nghiên cứu này, PhoBERT được sử dụng để chuyển đổi văn bản đầu vào thành 
các vector biểu diễn ngữ nghĩa có kích thước cố định. Quá trình này bao gồm việc 
token hóa văn bản theo bộ từ vựng của PhoBERT và ánh xạ các token thành các 
vector embedding tro ng không gian đặc trưng của mô hình. Các vector embedding 
này chứa thông tin ngữ nghĩa của các từ trong ngữ cảnh cụ thể của câu. 
Sau khi các vector biểu diễn được trích xuất từ PhoBERT, chúng sẽ được đưa vào lớp 
Bi-LSTM nhằm khai thác thêm các quan hệ phụ thuộc theo chuỗi trong văn bản. Việc 
sử dụng PhoBERT làm lớp biểu diễn đầu vào giúp mô hình tận dụng các tri thức ngôn 
ngữ đã được học trong quá trình tiền huấn luyện, từ đó cải thiện hiệu quả của hệ thống 
phân loại phát ngôn thù địch. 
3.2.2. Mô hình Bi-LSTM 
Sau khi các biểu diễn ngữ nghĩa của văn bản được trích xuất từ mô hình PhoBERT, 
các vector embedding này sẽ được đưa vào mô hình Bidirectional Long Short Term 
Memory (Bi-LSTM) để khai thác các quan hệ phụ thuộc trong chuỗi văn bản. Việc 
sử dụng Bi-LSTM giúp mô hình có khả năng học được thông tin ngữ cảnh của các từ 
trong câu theo cả hai hướng, từ đó cải thiện khả năng hiểu nội dung của văn bản. 
 
Mạng Long Short Term Memory (LSTM) là một biến thể của mạng nơ ron hồi quy 
được thiết kế nhằm khắc phục vấn đề mất dần gradient thường xảy ra trong các mạng 
RNN truyền thống khi xử lý các chuỗi dữ liệu dài. LSTM sử dụng các cơ chế cổng 
để kiểm soát luồng t hông tin trong mạng, cho phép mô hình ghi nhớ hoặc loại bỏ 
thông tin khi cần thiết. Cấu trúc cơ bản của một ô LSTM bao gồm ba thành phần 
chính là cổng quên (forget gate), cổng đầu vào (input gate) và cổng đầu ra (output 
gate). Cấu trúc của một ô LSTM được minh họa trong Hình 3.7.

## Page 49

P
A
G
E 
6 
 
35 
 
(Chèn Hình 3.7: Cấu trúc của một ô LSTM) 
Trong khi LSTM truyền thống xử lý chuỗi dữ liệu theo một chiều từ trái sang phải, 
Bi-LSTM được thiết kế để xử lý chuỗi dữ liệu theo cả hai hướng. Cụ thể, mô hình 
bao gồm hai mạng LSTM song song: một mạng xử lý chuỗi từ trái sang phải và một 
mạng xử lý chuỗi từ phải sang trái. Kết quả từ hai mạng này sau đó được kết hợp để 
tạo ra biểu diễn ngữ cảnh đầy đủ hơn cho mỗi từ trong câu. Kiến trúc của mô hình 
Bi-LSTM được minh họa trong Hình 3.8. 
 
(Chèn Hình 3.8: Kiến trúc mô hình Bi-LSTM) 
Trong mô hình đề xuất của đề án, các vector embedding được trích xuất từ PhoBERT 
sẽ được đưa vào lớp Bi-LSTM để học các quan hệ phụ thuộc trong chuỗi văn bản. 
Bi-LSTM cho phép mô hình khai thác thông tin ngữ cảnh của các từ trong câu theo 
cả hai chiều, giúp cải thiện khả năng nhận diện các mẫu ngữ nghĩa liên quan đến phát 
ngôn thù địch. 
Đầu ra của lớp Bi-LSTM là các vector biểu diễn chuỗi đã được cập nhật thông tin 
ngữ cảnh. Các vector này sau đó được đưa vào lớp phân loại nhằm dự đoán nhãn của 
văn bản. Việc kết hợp PhoBERT với Bi-LSTM cho phép mô hình tận dụng khả năng 
biểu diễn ngữ nghĩa mạnh mẽ của các mô hình ngôn ngữ tiền huấn luyện đồng thời 
khai thác hiệu quả cấu trúc tuần tự của dữ liệu văn bản. 
3.2.3. Lớp phân loại 
Sau khi dữ liệu văn bản được xử lý qua các lớp PhoBERT embedding và Bi-LSTM, 
các biểu diễn ngữ nghĩa cuối cùng của chuỗi văn bản sẽ được đưa vào lớp phân loại 
để dự đoán nhãn của văn bản đầu vào. Lớp phân loại đóng vai trò chuyển đổi các đặc 
trưng đã được học thành xác suất tương ứng với từng lớp trong bài toán phân loại. 
Trong mô hình đề xuất, đầu ra của lớp Bi-LSTM là các vector đặc trưng biểu diễn 
thông tin ngữ cảnh của chuỗi văn bản. Các vector này sau đó được đưa vào một lớp 
kết nối đầy đủ (Fully Connected Layer) nhằm thực hiện quá trình ánh xạ từ không 
gian đặc trưng sang không gian nhãn. Lớp này giúp kết hợp cá c đặc trưng đã được

## Page 50

P
A
G
E 
6 
 
36 
 
học từ các lớp trước đó và tạo ra các giá trị đầu ra cho từng lớp nhãn. 
Sau lớp kết nối đầy đủ, hàm softmax được sử dụng để chuyển đổi các giá trị đầu ra 
thành các xác suất tương ứng với từng lớp. Hàm softmax đảm bảo tổng các xác suất 
của các lớp bằng 1, từ đó cho phép mô hình xác định lớp có xác suất cao nhất làm kết 
quả dự đ oán cho văn bản đầu vào. Cấu trúc của lớp phân loại trong mô hình được 
minh họa trong Hình 3.9. 
 
(Chèn Hình 3.9: Cấu trúc lớp phân loại trong mô hình PhoBERT–Bi-LSTM) 
Trong bài toán phát hiện phát ngôn thù địch được xem xét trong nghiên cứu này, mô 
hình cần phân loại văn bản thành ba lớp gồm Hate, Offensive và Clean. Do đó, lớp 
phân loại cuối cùng của mô hình sẽ tạo ra ba giá trị xác suất tương ứng với ba lớp 
nhãn này. Văn bản đầu vào sẽ được gán nhãn theo lớp có xác suất dự đoán cao nhất. 
Việc sử dụng lớp phân loại kết hợp với hàm softmax giúp mô hình thực hiện hiệu quả 
nhiệm vụ phân loại đa lớp. Đồng thời, các xác suất đầu ra của mô hình cũng có thể 
được sử dụng để phân tích mức độ tin cậy của dự đoán, từ đó hỗ trợ cho việc đánh 
giá và cải thiện hiệu quả của hệ thống trong quá trình thực nghiệm. 
3.3. Quy trình huấn luyện mô hình 
3.4. Các kĩ thuật hỗ trợ huấn luyện mô hình 
Sau khi xây dựng kiến trúc mô hình PhoBERT–Bi-LSTM, bước tiếp theo là tiến hành 
huấn luyện mô hình trên tập dữ liệu đã được chuẩn bị. Quá trình huấn luyện nhằm 
mục tiêu tối ưu các tham số của mô hình để mô hình có thể học được các đặc trưng 
của dữ liệu và thực hiện phân loại văn bản một cách chính xác. 
Quy trình huấn luyện mô hình được minh họa trong Hình 3.10, bao gồm các bước 
chính như chuẩn bị dữ liệu huấn luyện, đưa dữ liệu vào mô hình, tính toán hàm mất 
mát, cập nhật tham số và đánh giá mô hình trên tập kiểm tra. 
 
(Chèn Hình 3.10: Quy trình huấn luyện mô hình PhoBERT–Bi-LSTM)

## Page 51

P
A
G
E 
6 
 
37 
 
Trước tiên, tập dữ liệu sau khi được tiền xử lý và xử lý mất cân bằng sẽ được chia 
thành các tập dữ liệu phục vụ cho quá trình huấn luyện và đánh giá mô hình. Thông 
thường, dữ liệu được chia thành ba phần bao gồm tập huấn luyện (training set), tập 
kiểm tra (validation set) và tập kiểm thử (test set). Tập huấn luyện được sử dụng để 
cập nhật các tham số của mô hình, trong khi tập validation được sử dụng để theo dõi 
quá trình huấn luyện và điều chỉnh các siêu tham số của mô hình. Tập test được sử 
dụng để đánh giá hiệu quả cuối cùng của mô hình sau khi quá trình huấn luyện kết 
thúc. 
Sau khi dữ liệu được chuẩn bị, các văn bản trong tập huấn luyện sẽ được đưa vào mô 
hình PhoBERT để trích xuất các vector biểu diễn ngữ nghĩa. Các vector này sau đó 
được đưa vào lớp Bi-LSTM để học các quan hệ phụ thuộc trong chuỗi văn bản. Kết 
quả đầu ra của Bi-LSTM được chuyển qua lớp phân loại nhằm dự đoán xác suất của 
từng lớp nhãn. 
Trong quá trình huấn luyện, mô hình sử dụng hàm mất mát (loss function) để đo 
lường sự khác biệt giữa nhãn dự đoán của mô hình và nhãn thực tế của dữ liệu. Đối 
với bài toán phân loại đa lớp, hàm mất mát thường được sử dụng là categorical cross 
entropy. Hàm mất mát này cho phép mô hình đánh giá mức độ sai lệch của dự đoán 
và điều chỉnh các tham số của mô hình nhằm giảm thiểu sai số. 
Để tối ưu các tham số của mô hình, các thuật toán tối ưu hóa như Adam hoặc các biến 
thể của gradient descent thường được sử dụng. Trong mỗi vòng lặp huấn luyện, mô 
hình thực hiện quá trình lan truyền thuận (forward propagation) để tính toán đầu ra 
và giá trị hàm mất mát, sau đó thực hiện lan truyền ngược (backpropagation) để cập 
nhật các tham số của mô hình. 
Quá trình huấn luyện được thực hiện trong nhiều vòng lặp, thường được gọi là epoch. 
Trong mỗi epoch, toàn bộ tập dữ liệu huấn luyện sẽ được đưa qua mô hình một lần. 
Sau mỗi epoch, hiệu quả của mô hình có thể được đánh giá trên tập validation nhằm 
theo dõi quá trình học của mô hình và tránh hiện tượng quá khớp (overfitting). 
Sau khi quá trình huấn luyện hoàn tất, mô hình đã được tối ưu sẽ được sử dụng để

## Page 52

P
A
G
E 
6 
 
38 
 
thực hiện dự đoán trên tập dữ liệu kiểm thử. Các kết quả dự đoán này sau đó được sử 
dụng để đánh giá hiệu quả của mô hình thông qua các chỉ số đánh giá phù hợp cho 
bài toán phân loại văn bản. 
3.4.1. Tiền xử lý dữ liệu 
Trong các nghiên cứu xử lý ngôn ngữ tự nhiên, tiền xử lý dữ liệu được xem là bước 
nền tảng nhằm bảo đảm tính nhất quán của dữ liệu đầu vào trước khi huấn luyện mô 
hình. Dữ liệu văn bản thu thập từ mạng xã hội thường chứa nhiều thành phần không 
chuẩn hóa như ký tự đặc biệt, liên kết, lỗi định dạng hoặc các trường dữ liệu không 
đồng nhất giữa các tập dữ liệu. Những yếu tố này có thể gây sai lệch trong quá trình 
huấn luyện và làm giảm độ ổn định của mô hình phân loại. Vì vậy, nghiên cứu này 
xây dựng một quy trì nh tiền xử lý nhằm chuẩn hóa cấu trúc dữ liệu, loại bỏ mẫu lỗi 
và chuyển đổi văn bản sang dạng biểu diễn phù hợp với mô hình PhoBERT. 
Quy trình tiền xử lý dữ liệu được minh họa trong Hình 3.2 và bao gồm các bước 
chuẩn hóa schema dữ liệu, làm sạch mẫu lỗi, chuẩn hóa nhãn, kiểm soát tập dữ liệu 
huấn luyện, và tokenization theo chuẩn của mô hình PhoBERT. 
 
(Chèn Hình 3.2. Quy trình tiền xử lý dữ liệu văn bản) 
Bước đầu tiên là chuẩn hóa cấu trúc dữ liệu. Trong nhiều bộ dữ liệu, các trường dữ 
liệu có thể được đặt tên khác nhau, ví dụ trường văn bản có thể được lưu dưới dạng 
free_text hoặc content, trong khi trường nhãn có thể được ký hiệu là label_id. Để đảm 
bảo tính nhất quán trong toàn bộ pipeline xử lý, nghiên cứu này chuẩn hóa schema 
dữ liệu bằng cách chuyển các trường văn bản về tên text và trường nhãn về label. 
Việc chuẩn hóa này giúp đơn giản hóa quá trình xử lý và giảm sai lệch khi tích hợp 
nhiều bộ dữ liệu khác nhau. 
Sau bước chuẩn hóa schema, các mẫu dữ liệu lỗi được loại bỏ nhằm đảm bảo tính 
hợp lệ của tập dữ liệu. Những bản ghi không có nội dung văn bản hoặc không có nhãn 
phân loại được loại bỏ thông qua thao tác dropna trên hai trường text và label. Quy 
trình này giúp đảm bảo mỗi mẫu dữ liệu đều có đầy đủ thông tin cần thiết cho quá

## Page 53

P
A
G
E 
6 
 
39 
 
trình huấn luyện. 
Tiếp theo, dữ liệu được chuẩn hóa kiểu dữ liệu nhằm đảm bảo tính nhất quán trong 
quá trình xử lý. Trường văn bản được ép kiểu về dạng chuỗi ký tự (string), trong khi 
trường nhãn được chuyển về dạng nhãn lớp hợp lệ. Bước này giúp tránh các lỗi định 
dạng trong quá trình tokenization hoặc huấn luyện mô hình. 
Sau khi chuẩn hóa kiểu dữ liệu, các tập dữ liệu được giữ nguyên cấu trúc phân chia 
ban đầu gồm ba tập train, dev và test. Việc giữ nguyên cách chia tập dữ liệu giúp đảm 
bảo tính nhất quán trong quá trình đánh giá và tránh hiện tượng rò rỉ dữ liệu giữa các 
tập huấn luyện và kiểm tra. 
Tiếp theo, hệ thống thực hiện chuẩn hóa nhãn nhằm đảm bảo tính đồng nhất trong 
toàn bộ tập dữ liệu. Trong nghiên cứu này, các nhãn được ánh xạ theo ba lớp chính 
gồm Clean, Offensive và Hate. Các nhãn này được mã hóa tương ứng với các giá trị 
số 0, 1 và 2 để thuận tiện cho quá trình huấn luyện mô hình phân loại đa lớp. 
Trong trường hợp sử dụng các phương pháp cân bằng dữ liệu, thao tác lấy mẫu chỉ 
được áp dụng trên tập huấn luyện. Việc giới hạn quá trình sampling trên tập train giúp 
bảo đảm rằng các tập dev và test vẫn phản ánh đúng phân bố dữ liệu gốc, từ đó duy 
trì tính khách quan trong quá trình đánh giá mô hình. 
Bước cuối cùng trong quy trình tiền xử lý là tokenization theo chuẩn của mô hình 
PhoBERT. Văn bản được tách thành các token dựa trên bộ từ vựng đã được huấn 
luyện trước của PhoBERT. Trong quá trình này, các chuỗi văn bản được cắt ngắn 
theo giới hạn độ dài tối đa (truncation), đồng thời tạo attention mask để xác định các 
token hợp lệ trong chuỗi. Quá trình padding được thực hiện theo từng batch nhằm 
đảm bảo các chuỗi đầu vào có cùng độ dài khi đưa vào mô hình. 
Thông qua quy trình tiền xử lý này, dữ liệu văn bản được chuẩn hóa về cấu trúc, định 
dạng và biểu diễn số học, qua đó tạo ra đầu vào nhất quán cho mô hình PhoBERT 
trong nhiệm vụ phát hiện phát ngôn thù địch.. 
3.4.2. Phương pháp xử lý mất cân bằng dữ liệu 
Trong các bài toán phân loại văn bản, đặc biệt là các nhiệm vụ liên quan đến phát

## Page 54

P
A
G
E 
6 
 
40 
 
hiện phát ngôn thù địch trên mạng xã hội, sự mất cân bằng giữa các lớp dữ liệu là một 
vấn đề phổ biến. Mất cân bằng dữ liệu xảy ra khi số lượng mẫu của một hoặc một số 
lớp lớn hơn đáng kể so với các lớp còn lại. Trong trường hợp này, mô hình học máy 
có xu hướng học tốt các đặc trưng của lớp chiếm đa số nhưng lại gặp khó khăn trong 
việc nhận diện các lớp thiểu số. Điều này có thể dẫn đến hiện tượng thiên lệch trong 
quá trình dự đoán và làm giảm hiệu quả của hệ thống phân loại. 
Trong bộ dữ liệu ViHSD được sử dụng trong nghiên cứu này, các văn bản thuộc lớp 
Clean thường chiếm tỷ lệ lớn hơn so với các lớp Hate và Offensive. Sự chênh lệch về 
số lượng mẫu giữa các lớp có thể khiến mô hình ưu tiên dự đoán lớp chiếm đa số, dẫn 
đến việc nhận diện không chính xác các văn bản chứa nội dung xúc phạm hoặc thù 
địch. Vì vậy, việc áp dụng các phương pháp xử lý mất cân bằng dữ liệu là cần thiết 
nhằm cải thiện khả năng học của mô hình đối với các lớp thiểu số. 
Quy trình xử lý mất cân bằng dữ liệu trong hệ thống được minh họa trong Hình 3.3, 
trong đó tập dữ liệu huấn luyện được điều chỉnh thông qua các phương pháp 
oversampling và undersampling trước khi đưa vào quá trình huấn luyện mô hình. 
(Chèn Hình 3.3: Quy trình xử lý mất cân bằng dữ liệu) 
Trong nghiên cứu này, một số phương pháp xử lý mất cân bằng dữ liệu phổ biến được 
áp dụng nhằm điều chỉnh phân bố dữ liệu giữa các lớp. Các phương pháp này bao 
gồm Random Over Sampling (ROS), Random Under Sampling (RUS), NearMiss, 
Edited Nearest Neighbours (ENN) và Tomek Links. 
Phương pháp Random Over Sampling (ROS) được sử dụng để tăng số lượng mẫu của 
các lớp thiểu số bằng cách sao chép ngẫu nhiên các mẫu hiện có trong các lớp này. 
Mục tiêu của phương pháp là tạo ra sự cân bằng giữa các lớp trong tập dữ liệu huấn 
luyện, qua đó giúp mô hình có thêm dữ liệu để học các đặc trưng của các lớp thiểu 
số. 
Ngược lại với ROS, phương pháp Random Under Sampling (RUS) thực hiện việc 
giảm số lượng mẫu của lớp chiếm đa số bằng cách loại bỏ ngẫu nhiên một phần các 
mẫu dữ liệu. Phương pháp này giúp cân bằng phân bố dữ liệu giữa các lớp nhưng có

## Page 55

P
A
G
E 
6 
 
41 
 
thể dẫn đến việc mất đi một phần thông tin trong tập dữ liệu huấn luyện. 
Ngoài ra, phương pháp NearMiss là một kỹ thuật undersampling dựa trên khoảng 
cách giữa các mẫu dữ liệu. Phương pháp này lựa chọn các mẫu của lớp chiếm đa số 
dựa trên khoảng cách của chúng đến các mẫu thuộc lớp thiểu số, nhằm giữ lại những 
mẫu có khả năng phân biệt tốt giữa các lớp. 
Bên cạnh đó, các kỹ thuật như Edited Nearest Neighbours (ENN) và Tomek Links 
được sử dụng để loại bỏ các mẫu dữ liệu gây nhiễu gần ranh giới giữa các lớp. Các 
phương pháp này giúp làm rõ ranh giới phân loại giữa các lớp và cải thiện chất lượng 
của tập dữ liệu huấn luyện. Minh họa về cơ chế hoạt động của phương pháp Tomek 
Links được thể hiện trong Hình 3.4. 
(Chèn Hình 3.4: Minh họa phương pháp Tomek Links) 
Trong thực nghiệm của đề án, các phương pháp xử lý mất cân bằng dữ liệu sẽ được 
áp dụng và so sánh nhằm đánh giá ảnh hưởng của chúng đến hiệu quả phân loại của 
mô hình. Việc lựa chọn phương pháp xử lý dữ liệu phù hợp giúp cải thiện khả năng 
nhận diện các lớp thiểu số và nâng cao hiệu quả tổng thể của hệ thống phát hiện phát 
ngôn thù địch. 
3.5. Tổng kết Chương 3 
Chương 3 đã trình bày phương pháp được đề xuất nhằm giải quyết bài toán phát hiện 
phát ngôn thù địch trong văn bản tiếng Việt trên mạng xã hội. Nội dung chương tập 
trung mô tả chi tiết quy trình xây dựng hệ thống từ giai đoạn xử lý dữ liệu đầu vào 
đến thiết kế kiến trúc mô hình và quy trình huấn luyện. Các thành phần chính của 
phương pháp bao gồm tiền xử lý dữ liệu văn bản, xử lý vấn đề mất cân bằng dữ liệu 
và xây dựng mô hình học sâu phục vụ cho nhiệm vụ phân loại.  
Trước hết, chương đã mô tả quy trình tiền xử lý dữ liệu nhằm làm sạch văn bản và 
chuẩn hóa dữ liệu đầu vào trước khi đưa vào mô hình. Các bước xử lý bao gồm loại 
bỏ ký tự đặc biệt, chuẩn hóa văn bản và chuẩn bị dữ liệu cho quá trình huấn luyện. 
Bên cạnh đó , chương cũng phân tích hiện tượng mất cân bằng dữ liệu trong bộ dữ 
liệu ViHSD, trong đó các mẫu thuộc lớp Clean thường chiếm số lượng lớn hơn so với

## Page 56

P
A
G
E 
6 
 
42 
 
các lớp Hate và Offensive. Để giảm ảnh hưởng của hiện tượng này đối với quá trình 
học của mô hình, một số phương pháp cân bằng dữ liệu đã được xem xét và áp dụng 
trong quá trình huấn luyện.  
Trên cơ sở dữ liệu đã được xử lý, chương đã đề xuất mô hình kết hợp giữa PhoBERT 
và Bidirectional Long Short -Term Memory ( Bi-LSTM). Trong kiến trúc này, 
PhoBERT được sử dụng để trích xuất các biểu diễn ngữ nghĩa theo ngữ cảnh của văn 
bản tiếng Việt, trong khi Bi-LSTM được sử dụng để khai thác các mối quan hệ phụ 
thuộc theo chuỗi trong câu. Sự kết hợp giữa hai thành phần này cho phép mô hình tận 
dụng đồng thời khả năng biểu diễn ngữ nghĩa mạnh của các mô hình ngôn ngữ tiền 
huấn luyện và khả năng mô hình hóa thông tin t uần tự của mạng nơ-ron hồi quy hai 
chiều. 
Cuối cùng, chương cũng đã mô tả quy trình huấn luyện và triển khai mô hình trong 
hệ thống dự đoán. Quy trình này bao gồm việc đưa dữ liệu đã được tiền xử lý vào mô 
hình, huấn luyện các tham số thông qua dữ liệu gán nhãn và sử dụng lớp phân loại để 
dự đoán nhãn tương ứng của văn bản. Những nội dung được trình bày trong chương 
này tạo nền tảng cho các bước thực nghiệm và đánh giá mô hình sẽ được trình bày 
chi tiết trong chương tiếp theo của đề án.

## Page 57

P
A
G
E 
6 
 
43 
 
CHƯƠNG 4. THỰC NGHIỆM 
 
4.1. Bộ dữ liệu sử dụng 
4.1.1. Giới thiệu bộ dữ liệu ViHSD 
Bộ dữ liệu ViHSD (Vietnamese Hate Speech Detection) là một tập dữ liệu lớn được 
xây dựng nhằm phục vụ cho bài toán phát hiện phát ngôn thù địch trong văn bản tiếng 
Việt trên mạng xã hội. Bộ dữ liệu này được thu thập từ các bình luận của người dùng 
trên các nền tảng mạng xã hội phổ biến như Facebook và YouTube, đặc biệt tập trung 
vào các chủ đề có mức độ tương tác cao như giải trí, người nổi tiếng, các vấn đề xã 
hội và chính trị. Trong quá trình thu thập dữ liệu, các thực thể tên riêng trong bình 
luận được loại bỏ nhằm đảm bảo tính ẩn danh của người dùng.  
Bộ dữ liệu ViHSD bao gồm tổng cộng 33.400 bình luận tiếng Việt được gán nhãn thủ 
công bởi các annotator. Mỗi bình luận được gán một trong ba nhãn gồm CLEAN, 
OFFENSIVE và HATE. Trong đó, nhãn CLEAN đại diện cho các bình luận không 
chứa nội dung xúc phạm hoặ c công kích; nhãn OFFENSIVE được sử dụng cho các 
bình luận có chứa từ ngữ thô tục hoặc mang tính xúc phạm nhưng không hướng đến 
một đối tượng cụ thể; và nhãn HATE được gán cho các bình luận có nội dung thù 
địch hoặc công kích trực tiếp đến một cá nhân hoặc  một nhóm người dựa trên đặc 
điểm cá nhân, tôn giáo hoặc quốc tịch.  
Quá trình gán nhãn được thực hiện theo một quy trình nhiều bước nhằm đảm bảo chất 
lượng dữ liệu. Trước tiên, các annotator được đào tạo dựa trên bộ hướng dẫn gán 
nhãn chi tiết. Sau đó, mỗi bình luận được gán nhãn bởi hai annotator độc lập. Trong 
trường hợp hai annotator đưa ra nhãn khác nhau, một annotator thứ ba sẽ tham gia 
đánh giá lại. Nếu vẫn còn sự bất đồng, annotator thứ tư sẽ quyết định nhãn cuối cùng. 
Nhãn cuối cùng của mỗi bình luận được xác định theo nguyên tắc bỏ phiếu đa số 
nhằm đảm bảo tính khách quan của dữ liệu.  
Ngoài ra, mức độ đồng thuận giữa các annotator được đánh giá bằng hệ số Cohen’s

## Page 58

P
A
G
E 
6 
 
44 
 
Kappa, với giá trị trung bình đạt khoảng κ = 0.52, cho thấy mức độ đồng thuận ở mức 
chấp nhận được đối với bài toán gán nhãn dữ liệu văn bản trên mạng xã hội.  
4.1.2. Phân bố dữ liệu theo các nhãn 
Bảng 4.2. Phân bố dữ liệu theo các nhãn trong bộ dữ liệu ViHSD 
Nhãn Số lượng bình luận Tỷ lệ (%) 
CLEAN 24,048 72.00 
OFFENSIVE 2,672 8.00 
HATE 6,680 20.00 
Tổng 33,400 100 
Trong bộ dữ liệu ViHSD, mỗi bình luận được gán một trong ba nhãn gồm CLEAN, 
OFFENSIVE và HATE, tương ứng với các mức độ khác nhau của nội dung xúc phạm 
trong văn bản. Phân bố dữ liệu giữa các nhãn không đồng đều, trong đó số lượng bình 
luận thuộc nhãn CLEA N chiếm tỷ lệ lớn nhất trong tập dữ liệu. Điều này phản ánh 
đặc điểm của dữ liệu thu thập từ mạng xã hội, nơi phần lớn các bình luận không chứa 
nội dung thù địch hoặc xúc phạm. Bảng 4.2 trình bày số lượng bình luận của từng 
nhãn trong toàn bộ bộ dữ liệu ViHSD. 
Các bình luận mang nhãn OFFENSIVE chiếm tỷ lệ nhỏ hơn so với nhãn CLEAN và 
thường chứa các từ ngữ mang tính xúc phạm hoặc thô tục nhưng không trực tiếp công 
kích một đối tượng cụ thể. Trong khi đó, các bình luận mang nhãn HATE có số lượng 
ít hơn và thường bao gồm các nội dung công kích trực tiếp đến cá nhân hoặc nhóm 
người dựa trên các đặc điểm như quốc tịch, tôn giáo hoặc đặc điểm cá nhân. 
Sự mất cân bằng giữa các nhãn là một đặc điểm quan trọng của bộ dữ liệu ViHSD và 
có ảnh hưởng đáng kể đến hiệu quả của các mô hình phân loại. Trong các thí nghiệm 
trên bộ dữ liệu này, nhiều mô hình có xu hướng dự đoán nhãn CLEAN nhiều hơn so 
với các nhãn còn lại, dẫn đến sự chênh lệch giữa các chỉ số Accuracy và Macro F1.  
4.1.3. Phân chia tập huấn luyện, tập kiểm tra và tập xác thực 
Bảng 4.3.Phân chia dữ liệu trong bộ dữ liệu ViHSD 
Tập dữ liệu CLEAN OFFENSIVE HATE Tổng 
Train 19,886 2,190 5,548 27,624

## Page 59

P
A
G
E 
6 
 
45 
 
Dev 1,606 212 444 2,262 
Test 2,556 270 688 3,514 
Tổng 24,048 2,672 6,680 33,400 
Để phục vụ cho quá trình huấn luyện và đánh giá mô hình, bộ dữ liệu ViHSD được 
chia thành ba tập dữ liệu gồm tập huấn luyện (training set), tập xác thực (development 
set) và tập kiểm tra (test set). Tỷ lệ phân chia dữ liệu được thiết lập theo tỷ lệ 7:1:2 
tương ứng với các tập train, dev và test. Bảng 4.3 trình bày số lượng bình luận của 
từng nhãn trong các tập dữ liệu train, dev và test. 
Cụ thể, tập huấn luyện chiếm phần lớn dữ liệu với 19.886 bình luận mang nhãn 
CLEAN, 2.190 bình luận mang nhãn OFFENSIVE và 5.548 bình luận mang nhãn 
HATE. Tập xác thực bao gồm 1.606 bình luận CLEAN, 212 bình luận OFFENSIVE 
và 444 bình luận HATE. Trong khi đó, tập kiểm tra bao gồm 2.556 bình luận CLEAN, 
270 bình luận OFFENSIVE và 688 bình luận HATE.  
Việc phân chia dữ liệu theo tỷ lệ này nhằm đảm bảo rằng tập huấn luyện có đủ dữ 
liệu để mô hình học được các đặc trưng của văn bản, đồng thời giữ lại một phần dữ 
liệu độc lập để đánh giá và kiểm tra hiệu quả của mô hình. Phân bố nhãn trong ba tập 
dữ liệu được duy trì tương đối giống nhau nhằm đảm bảo tính nhất quán trong quá 
trình huấn luyện và đánh giá mô hình.  
4.2. Thiết lập thực nghiệm 
4.2.1. Môi trường thực nghiệm 
Các thí nghiệm trong nghiên cứu được thực hiện trên một máy tính cá nhân có cấu 
hình phần cứng và phần mềm như sau. Việc mô tả chi tiết môi trường thực nghiệm 
nhằm đảm bảo khả năng tái lập kết quả và tạo điều kiện thuận lợi cho việc so sánh 
với các nghiên cứu liên quan. 
Cấu hình phần cứng 
- GPU: NVIDIA GeForce RTX 4060 Ti, hỗ trợ tính toán song song cho quá 
trình huấn luyện mô hình học sâu 
- CUDA: phiên bản 12.6

## Page 60

P
A
G
E 
6 
 
46 
 
- CPU: Intel Core i7 thế hệ 13 
- RAM: 32 GB 
- Ổ lưu trữ: SSD NVMe 1 TB 
GPU được sử dụng để tăng tốc quá trình huấn luyện các mô hình học sâu, đặc biệt 
đối với các mô hình dựa trên Transformer như PhoBERT. Việc sử dụng GPU giúp 
rút ngắn đáng kể thời gian huấn luyện so với việc thực hiện trên CPU. 
Môi trường phần mềm 
- Hệ điều hành: Ubuntu 22.04 LTS 
- Ngôn ngữ lập trình: Python 3.10 
- Framework học sâu: PyTorch 2.2 
- Thư viện Transformers: HuggingFace Transformers 
- Các thư viện hỗ trợ: NumPy, Pandas, Scikit learn, Matplotlib 
Trong quá trình thực nghiệm, mô hình PhoBERT được sử dụng làm backbone để sinh 
ra các biểu diễn ngữ nghĩa theo ngữ cảnh của văn bản đầu vào. Các lớp mạng phía 
sau như Bi-LSTM được xây dựng và huấn luyện bằng PyTorch. Toàn bộ các mô hình 
được huấn luyện và đánh giá trong cùng một môi trường thực nghiệm nhằm đảm bảo 
tính nhất quán khi so sánh kết quả giữa các phương pháp khác nhau. 
4.2.2. Các tham số huấn luyện mô hình 
Các mô hình được huấn luyện theo một cấu hình thực nghiệm thống nhất nhằm đảm 
bảo tính khách quan khi so sánh giữa các phương pháp. 
Đối với các mô hình học sâu truyền thống như Text CNN, GRU và BiLSTM, số 
epoch huấn luyện được thiết lập ở mức cao hơn nhằm cho phép mô hình học đầy đủ 
các đặc trưng của dữ liệu. Các mô hình này sử dụng bộ tối ưu Adam, vốn được sử 
dụng phổ biến trong các mạng nơron sâu nhờ khả năng hội tụ nhanh và ổn định. Trong 
khi đó, các mô hình ngôn ngữ tiền huấn luyện như BERT, XLM R, DistilBERT và 
PhoBERT được huấn luyện thông qua quá trình fine tuning với số epoch nhỏ hơn do 
các mô hình này đã được huấn luyện trước trên các tập dữ liệu văn bản lớn. 
Đối với mô hình đề xuất, biểu diễn ngữ nghĩa của văn bản được sinh ra từ PhoBERT,

## Page 61

P
A
G
E 
6 
 
47 
 
sau đó được đưa qua lớp BiLSTM hai chiều để khai thác thông tin phụ thuộc chuỗi 
trước khi thực hiện phân loại. Các tham số huấn luyện của PhoBERT và BiLSTM 
được thiết lập tương tự các cấu hình phổ biến trong các nghiên cứu sử dụng mô hình 
Transformer kết hợp mạng hồi tiếp. 
Các tham số huấn luyện chính được sử dụng trong nghiên cứu được trình bày trong 
Bảng 4.1. 
Bảng 4.1. Các tham số huấn luyện mô hình 
Nhóm mô hình Tham số Giá trị 
Text CNN Epochs 50 
Batch size 256 
Sequence length 100 
Dropout 0.5  
Number of filters 32 
Kernel sizes 2, 3, 5 
Optimizer Adam 
GRU (Bidirectional) Epochs 50 
Sequence length 100 
Dropout 0.5 
Architecture Bidirectional GRU 
Optimizer Adam 
BiLSTM Epochs 50 
Sequence length 100 
Dropout 0.5 
Architecture Bidirectional LSTM 
Optimizer Adam 
Transformer (BERT, XLM R, 
DistilBERT. PhoBERT) 
Epochs 4 
Batch size 16 
Sequence length 100 
Random seed 4 
Fine tuning toàn bộ mô hình 
4.2.1. Quy trình huấn luyện và đánh giá 
Quy trình huấn luyện và đánh giá mô hình trong nghiên cứu được thực hiện theo các 
bước tuần tự nhằm đảm bảo tính nhất quán giữa các phương pháp so sánh và mô hình 
đề xuất. Toàn bộ các mô hình được huấn luyện và đánh giá trên cùng tập kiểm thử 
của bộ dữ liệu ViHSD với cùng thiết lập tham số để đảm bảo tính khách quan trong 
quá trình thực nghiệm.

## Page 62

P
A
G
E 
6 
 
48 
 
Quy trình thực nghiệm được tiến hành theo các bước sau: 
Bước 1. Chuẩn bị và tiền xử lý dữ liệu 
• Thu thập và sử dụng bộ dữ liệu ViHSD cho bài toán phát hiện phát ngôn thù 
địch. 
• Làm sạch dữ liệu văn bản, loại bỏ các ký tự không cần thiết và chuẩn hóa định 
dạng câu. 
• Sử dụng PhoBERT tokenizer để chuyển đổi văn bản thành chuỗi token. 
• Giới hạn độ dài chuỗi đầu vào ở mức 256 token nhằm đảm bảo tính đồng nhất 
của dữ liệu đầu vào. 
Bước 2. Phân chia dữ liệu 
• Dữ liệu được chia thành ba tập gồm: tập huấn luyện (training set), tập xác thực 
(validation set) và tập kiểm tra (test set). 
• Tập huấn luyện được sử dụng để cập nhật tham số của mô hình. 
• Tập xác thực được sử dụng để điều chỉnh các tham số huấn luyện và theo dõi 
quá trình hội tụ của mô hình. 
• Tập kiểm tra được sử dụng để đánh giá hiệu quả cuối cùng của mô hình sau 
khi huấn luyện. 
Bước 3. Huấn luyện mô hình 
• Khởi tạo mô hình backbone PhoBERT và các lớp mạng phía sau nh ư Bi-
LSTM. 
• Các tham số của mô hình được tối ưu hóa bằng thuật toán Adam với learning 
rate 2 × 10−5. 
• Mô hình được huấn luyện theo từng epoch, trong mỗi epoch dữ liệu huấn luyện 
được chia thành các mini batch với kích thước batch size bằng 16. 
• Sau mỗi epoch, mô hình được đánh giá trên tập validation để theo dõi hiệu quả 
học của mô hình.

## Page 63

P
A
G
E 
6 
 
49 
 
Bước 4. Đánh giá mô hình 
• Sau khi quá trình huấn luyện hoàn tất, mô hình được đánh giá trên tập test độc 
lập. 
• Các chỉ số đánh giá được sử dụng gồm Accuracy, Precision, Recall và Macro 
F1 nhằm phản ánh đầy đủ hiệu quả phân loại của mô hình. 
• Ngoài ra, ma trận nhầm lẫn được sử dụng để phân tích chi tiết khả năng phân 
loại của mô hình đối với từng lớp dữ liệu. 
Bước 5. So sánh kết quả 
• Kết quả của mô hình đề xuất được so sánh với các mô hình baseline như 
Logistic Regression, Random Forest, Text CNN, Bi-LSTM và các mô hình 
ngôn ngữ tiền huấn luyện như BERT, RoBERTa, XLM R và PhoBERT. 
• Việc so sánh được thực hiện dựa trên các chỉ số đánh giá đã nêu nhằm xác 
định hiệu quả của mô hình đề xuất trong bài toán phát hiện phát ngôn thù địch. 
4.3. Các chỉ số đánh giá 
Để đánh giá hiệu quả của mô hình trong bài toán phát hiện phát ngôn thù địch, nghiên 
cứu sử dụng một số chỉ số đánh giá phổ biến trong các bài toán phân loại văn bản. 
Các chỉ số này cho phép đo lường khả năng dự đoán của mô hình trên từng lớp cũng 
như hiệu quả tổng thể của hệ thống. Trong nghiên cứu này, các chỉ số đánh giá được 
sử dụng bao gồm Accuracy, Precision, Recall và Macro F1 score . Ngoài ra, ma trận 
nhầm lẫn (Confusion Matrix) cũng được sử dụng nhằm phân tích chi tiết kết quả dự 
đoán của mô hình. 
4.3.1. Accuracy 
Accuracy là tỷ lệ giữa số lượng dự đoán đúng và tổng số mẫu trong tập kiểm thử. Chỉ 
số này phản ánh mức độ chính xác tổng thể của mô hình trong quá trình phân loại. 
Accuracy được tính theo công thức sau: 
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦=
𝑇𝑃+𝑇𝑁
𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁      (1)

## Page 64

P
A
G
E 
6 
 
50 
 
Trong đó TP là số mẫu dự đoán đúng thuộc lớp dương, TN là số mẫu dự đoán đúng 
thuộc lớp âm, FP là số mẫu dự đoán sai thuộc lớp dương và FN là số mẫu dự đoán 
sai thuộc lớp âm. 
Mặc dù Accuracy là một chỉ số phổ biến trong các bài toán phân loại, chỉ số này có 
thể không phản ánh chính xác hiệu quả của mô hình trong trường hợp dữ liệu bị mất 
cân bằng. Khi một lớp chiếm tỷ lệ lớn trong dữ liệu, mô hình có thể đạt Accuracy cao 
chỉ bằng cách dự đoán lớp chiếm đa số. 
4.3.2. Precision 
Precision đo lường mức độ chính xác của các dự đoán thuộc một lớp nhất định. Chỉ 
số này cho biết trong số các mẫu được mô hình dự đoán là thuộc lớp đó, có bao nhiêu 
mẫu thực sự thuộc lớp đó. Precision được tính theo công thức: 
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃
𝑇𝑃+𝐹𝑃      (2) 
Precision cao cho thấy mô hình ít đưa ra các dự đoán sai thuộc lớp đó. 
4.3.3. Recall 
Recall đo lường khả năng của mô hình trong việc phát hiện các mẫu thực sự thuộc 
một lớp nhất định. Chỉ số này cho biết trong số các mẫu thực sự thuộc lớp đó, mô 
hình đã phát hiện được bao nhiêu mẫu. Recall được tính theo công thức: 
𝑅𝑒𝑐𝑎𝑙𝑙=
𝑇𝑃
𝑇𝑃+𝐹𝑁      (3) 
Recall cao cho thấy mô hình có khả năng phát hiện tốt các mẫu thuộc lớp mục tiêu. 
4.3.4. F1 score 
F1 score là trung bình điều hòa giữa Precision và Recall. Chỉ số này được sử dụng để 
cân bằng giữa hai yếu tố độ chính xác và khả năng phát hiện của mô hình. F1 score 
được tính theo công thức: 
𝐹1 =
2×𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛×𝑅𝑒𝑐𝑎𝑙𝑙
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙      (4) 
Trong nghiên cứu này, chỉ số Macro F1 score được sử dụng để đánh giá hiệu quả của

## Page 65

P
A
G
E 
6 
 
51 
 
mô hình. Macro F1 được tính bằng cách tính F1 score cho từng lớp riêng biệt sau đó 
lấy trung bình của các giá trị này. Công thức của Macro F1 được thể hiện như sau: 
𝑀𝑎𝑐𝑟𝑜𝐹1 =
1
𝑁
∑ 𝐹1𝑖
𝑁
𝑖=1      (5) 
Trong đó N là số lớp trong bài toán phân loại và 𝐹1𝑖 là giá trị F1 score của lớp thứ i. 
Việc sử dụng Macro F1 đặc biệt quan trọng trong trường hợp dữ liệu bị mất cân bằng 
giữa các lớp. Khác với Accuracy hoặc Micro F1, Macro F1 đánh giá hiệu quả của mô 
hình trên từng lớp với trọng số như nhau. Do đó, chỉ số này phản ánh tốt hơn khả 
năng nhận diện của mô hình đối với các lớp thiểu số như Hate hoặc Offensive trong 
bài toán phát hiện phát ngôn thù địch. 
4.3.5. Ma trận nhầm lẫn 
Bên cạnh các chỉ số đánh giá định lượng, nghiên cứu cũng sử dụng ma trận nhầm lẫn 
(Confusion Matrix) để phân tích chi tiết kết quả phân loại của mô hình. Ma trận nhầm 
lẫn cho phép quan sát số lượng mẫu được dự đoán đúng và sai giữa các lớp, từ đó 
giúp xác định những trường hợp mà mô hình dễ nhầm lẫn. 
Thông qua ma trận nhầm lẫn, có thể quan sát được mức độ nhầm lẫn giữa các lớp 
Hate, Offensive và Clean. Điều này giúp phân tích sâu hơn các lỗi của mô hình và 
cung cấp cơ sở cho việc cải thiện phương pháp trong các nghiên cứu tiếp theo. 
4.4. Các mô hình so sánh 
Để đánh giá hiệu quả của mô hình đề xuất PhoBIHSD trong bài toán phát hiện phát 
ngôn thù địch, nghiên cứu tiến hành so sánh kết quả với nhiều mô hình baseline đã 
được sử dụng phổ biến trong các nghiên cứu trước đây. Các mô hình được lựa chọn 
đại diện cho ba nhóm phương pháp chính gồm học máy truyền thống, học sâu và các 
mô hình ngôn ngữ tiền huấn luyện. Việc sử dụng nhiều nhóm mô hình khác nhau giúp 
đánh giá toàn diện khả năng cải thiện của mô hình đề xuất so với các phương pháp 
đã tồn tại. 
4.4.1. Nhóm mô hình học sâu 
Các mô hình học sâu có khả năng tự động học đặc trưng từ dữ liệu văn bản thông qua

## Page 66

P
A
G
E 
6 
 
52 
 
các mạng nơron nhiều tầng. 
• Text CNN: mô hình mạng nơron tích chập được sử dụng rộng rãi trong phân 
loại văn bản. Các bộ lọc tích chập với nhiều kích thước khác nhau cho phép 
mô hình phát hiện các mẫu n gram quan trọng trong câu. 
• Bi LSTM: mô hình mạng nơron hồi tiếp hai chiều cho phép khai thác thông 
tin ngữ cảnh của chuỗi văn bản theo cả hai hướng trước và sau, nhờ đó nắm 
bắt được các phụ thuộc dài hạn trong câu. 
4.4.2. Nhóm mô hình ngôn ngữ tiền huấn luyện và ngôn ngữ lớn 
Trong những năm gần đây, các mô hình ngôn ngữ tiền huấn luyện dựa trên kiến trúc 
Transformer đã đạt được nhiều kết quả nổi bật trong các bài toán xử lý ngôn ngữ tự 
nhiên. 
• BERT: mô hình ngôn ngữ tiền huấn luyện sử dụng cơ chế self attention hai 
chiều, cho phép học biểu diễn ngữ cảnh sâu của văn bản. 
• RoBERTa: phiên bản cải tiến của BERT với quy trình huấn luyện tối ưu hơn 
và tập dữ liệu huấn luyện lớn hơn. 
• XLM-R: mô hình ngôn ngữ đa ngôn ngữ được huấn luyện trên nhiều ngôn ngữ 
khác nhau, cho phép xử lý hiệu quả các văn bản đa ngôn ngữ. 
• PhoBERT: mô hình ngôn ngữ tiền huấn luyện dành riêng cho tiếng Việt, được 
huấn luyện trên tập dữ liệu văn bản lớn và cho thấy hiệu quả cao trong nhiều 
nhiệm vụ xử lý ngôn ngữ tự nhiên tiếng Việt. 
Cuối cùng, mô hình PhoBIHSD được đề xuất trong nghiên cứu này kết hợp giữa 
PhoBERT và Bi-LSTM nhằm tận dụng cả khả năng biểu diễn ngữ nghĩa của mô hình 
ngôn ngữ tiền huấn luyện và khả năng mô hình hóa phụ thuộc chuỗi của mạng hồi 
tiếp hai chiều. Việc so sánh giữa PhoBIHSD và các mô hình baseline cho phép đánh 
giá mức độ cải thiện của phương pháp đề xuất trong bài toán phát hiện phát ngôn thù 
địch trên bộ dữ liệu ViHSD. 
4.5. Kết quả thực nghiệm

## Page 67

P
A
G
E 
6 
 
53 
 
Bảng 4.5. Kết quả thực nghiệm 
Mô hình Phương pháp Accuracy Macro 
F1 
Precision Recall 
Text CNN fastText [1] 0.8669 0.6111 - - 
GRU fastText [1] 0.8541 0.6047 - - 
BERT bert-base-multilingual-uncased  [1] 0.8660 0.6238 - - 
bert-base-multilingual-cased [1] 0.8688 0.6269 - - 
BERT4News+EDA [2] - 0.6426 - - 
DistilBERT+EDA [2] - 0.6178 - - 
XLM-R xlm-roberta-based [1] 0.8612 0.6504 - - 
PhoBERT PhoBERT-base-v2+EDA [2] - 0.6551 - - 
PhoBERT + Bi-LSTM 0.8377 0.6457 0.6125 0.6976 
LLMs gpt-4o (few-shot)  0.7906 0.6282 0.6042 0.6542 
Mô hình 
đề xuất 
PhoBERT + Bi-LSTM + ROS 0.8484 0.6556 0.6250 0.6993 
 
4.6. Phân tích ảnh hưởng của các phương pháp cân bằng dữ liệu 
Bảng 4.6. Phân tích ảnh hưởng của các phương pháp cân bằng dữ liệu 
Phương pháp Accuracy Macro 
F1 
Precision Recall 
PhoBERT + Bi-LSTM (không cân bằng) 0.8377 0.6457 0.6125 0.6976 
PhoBERT + Bi-LSTM + ROS + ENN 0.8428 0.6485 0.6185 0.6922 
PhoBERT + Bi-LSTM + ROS + 
NearMiss 0.5451 0.4434 0.4730 0.6069 
PhoBERT + Bi-LSTM + ROS + RUS 0.7460 0.5659 0.5331 0.6769 
PhoBERT + Bi-LSTM + ROS + Tomek 
Links 0.8445 0.6510 0.6202 0.6957 
PhoBERT + Bi-LSTM + ROS 0.8484 0.6556 0.6250 0.6993 
 
4.7. Thảo luận kết quả thực nghiệm 
Kết quả thực nghiệm trình bày ở mục 4.6 cho thấy việc lựa chọn phương pháp xử lý 
mất cân bằng dữ liệu có ảnh hưởng đáng kể đến hiệu quả của mô hình phân loại. 
Trong bối cảnh bộ dữ liệu ViHSD có sự chênh lệch rõ rệt về số lượng mẫu giữa các 
lớp, việc áp dụng các chiến lược cân bằng dữ liệu giúp cải thiện khả năng nhận diện 
của mô hình đối với các lớp thiểu số như Hate và Offensive.

## Page 68

P
A
G
E 
6 
 
54 
 
Kết quả so sánh các phương pháp cân bằng dữ liệu cho thấy các phương pháp chỉ sử 
dụng oversampling hoặc undersampling đơn lẻ chưa đạt hiệu quả tối ưu. Phương pháp 
Random Over Sampling giúp tăng số lượng mẫu của các lớp thiểu số nhưng có thể 
dẫn đến việc lặp lại dữ liệu và làm tăng nguy cơ quá khớp trong quá trình huấn luyện. 
Ngược lại, các phương pháp undersampling như NearMiss có thể làm giảm số lượng 
mẫu của lớp chiếm đa số quá mức, dẫn đến việc mất đi một phần thông tin quan trọng 
của tập dữ liệu. 
Các kết quả thực nghiệm cho thấy phương pháp kết hợp giữa oversampling và 
undersampling mang lại hiệu quả tốt hơn so với việc sử dụng riêng lẻ từng phương 
pháp. Đặc biệt, phương pháp ROS + RUS + Tomek Links đạt kết quả tốt nhất trong 
các thí nghiệm. Việc k ết hợp nhiều kỹ thuật xử lý dữ liệu cho phép vừa điều chỉnh 
phân bố dữ liệu giữa các lớp vừa loại bỏ các mẫu dữ liệu nằm gần ranh giới phân loại, 
từ đó giúp cải thiện chất lượng của tập huấn luyện. 
Bên cạnh ảnh hưởng của phương pháp cân bằng dữ liệu, kết quả thực nghiệm cũng 
cho thấy sự khác biệt đáng kể giữa các mô hình phân loại. Các mô hình học máy 
truyền thống như Logistic Regression và SVM cho kết quả thấp hơn so với các mô 
hình học sâu sử dụng biểu diễn ngữ nghĩa của văn bản. Điều này cho thấy các phương 
pháp biểu diễn văn bản đơn giản như Bag of Words hoặc TF IDF chưa đủ khả năng 
khai thác đầy đủ thông tin ngữ nghĩa trong văn bản tiếng Việt. 
 
Trong khi đó, mô hình PhoBERT cho thấy hiệu quả phân loại cao hơn nhờ khả năng 
biểu diễn ngữ nghĩa theo ngữ cảnh của các từ trong câu. Khi kết hợp PhoBERT với 
Bi-LSTM, hiệu quả của mô hình tiếp tục được cải thiện. Lớp Bi-LSTM giúp mô hình 
khai thác thêm các quan hệ phụ thuộc trong chuỗi văn bản, từ đó hỗ trợ tốt hơn cho 
quá trình phân loại. 
 
Mặc dù mô hình PhoBERT–Bi-LSTM đạt kết quả tốt nhất trong các thí nghiệm, kết 
quả phân tích từ ma trận nhầm lẫn cho thấy vẫn tồn tại một số trường hợp nhầm lẫn

## Page 69

P
A
G
E 
6 
 
55 
 
giữa các lớp Hate và Offensive. Nguyên nhân của hiện tượng này có thể xuất phát từ 
sự tương đồng về mặt ngôn ngữ giữa các loại phát ngôn tiêu cực. Trong nhiều trường 
hợp, ranh giới giữa các mức độ xúc phạm hoặc thù địch trong văn bản không hoàn 
toàn rõ ràng, khiến cho việc phân loại trở nên khó khăn hơn đối với mô hình. 
Nhìn chung, các kết quả thực nghiệm cho thấy việc kết hợp mô hình ngôn ngữ tiền 
huấn luyện PhoBERT với mạng Bi-LSTM cùng với chiến lược xử lý mất cân bằng 
dữ liệu phù hợp có thể cải thiện hiệu quả của hệ thống phát hiện phát ngôn thù địch. 
Tuy nhiên, việc phân biệt chính xác các mức độ khác nhau của phát ngôn tiêu cực 
vẫn là một thách thức và cần được tiếp tục nghiên cứu trong các công trình tiếp theo. 
4.8. Chương trình minh họa 
 
4.9. Tổng kết Chương 4 
Chương 4 đã trình bày quá trình thực nghiệm nhằm đánh giá hiệu quả của mô hình 
phát hiện phát ngôn thù địch được đề xuất trong nghiên cứu. Nội dung chương tập 
trung mô tả bộ dữ liệu sử dụng trong thực nghiệm, thiết lập môi trường huấn luyện, 
các chỉ số đánh giá và kết quả so sánh giữa các phương pháp khác nhau. Thông qua 
các bước thực nghiệm, chương đã cung cấp cơ sở thực nghiệm nhằm đánh giá khả 
năng phân loại của mô hình trong bài toán phát hiện phát ngôn thù địch trong văn bản 
tiếng Việt.  
Trước hết, chương đã mô tả đặc điểm của bộ dữ liệu ViHSD được sử dụng trong quá 
trình đánh giá mô hình. Dữ liệu bao gồm các bài đăng và bình luận trên mạng xã hội 
được gán nhãn theo ba lớp Hate, Offensive và Clean. Bên cạnh đó, chương cũng trình 
bày các thiết lập thực nghiệm và các chỉ số đánh giá phổ biến trong bài toán phân loại 
văn bản như Accuracy, Precision, Recall và F1 -score nhằm đo lường hiệu quả của 
mô hình trong quá trình dự đoán nhãn văn bản.  
Tiếp theo, chương đã tiến hành so sánh hiệu quả của các phương pháp xử lý mất cân 
bằng dữ liệu khác nhau. Kết quả thực nghiệm cho thấy việc áp dụng các kỹ thuật cân 
bằng dữ liệu có ảnh hưởng đáng kể đến hiệu quả phân loại của mô hình, đặc biệt đối

## Page 70

P
A
G
E 
6 
 
56 
 
với các lớp dữ liệu thiểu số. Thông qua việc so sánh các phương pháp khác nhau, 
nghiên cứu đã xác định được các chiến lược xử lý dữ liệu phù hợp nhằm cải thiện khả 
năng nhận diện các phát ngôn thù địch trong văn bản. 
Bên cạnh đó, chương cũng thực hiện so sánh mô hình đề xuất với một số mô hình 
baseline nhằm đánh giá mức độ cải thiện về hiệu quả phân loại. Các kết quả thực 
nghiệm cho thấy mô hình kết hợp PhoBERT và Bi-LSTM đạt được kết quả khả quan 
trong việc khai thác thông tin ngữ nghĩa và ngữ cảnh của văn bản tiếng Việt. Điều 
này cho thấy việc kết hợp mô hình ngôn ngữ tiền huấn luyện với kiến trúc mạng nơ -
ron tuần tự có thể nâng cao hiệu quả của hệ thống phát hiện phát ngôn thù địch. 
Những kết quả thực nghiệm và phân tích trong chương này cung cấp cơ sở quan trọng 
cho việc đánh giá hiệu quả của phương pháp đề xuất. Các kết quả này đồng thời tạo 
tiền đề cho chương tiếp theo, trong đó các kết luận tổng hợp và các hướng nghiên cứu 
phát triển sẽ được trình bày nhằm mở rộng khả năng ứng dụng của mô hình trong các 
hệ thống kiểm duyệt nội dung trực tuyến.

## Page 71

P
A
G
E 
6 
 
57 
 
CHƯƠNG 5. KẾT LUẬN 
5.1. Kết luận 
Đề án này tập trung nghiên cứu bài toán phát hiện phát ngôn thù địch trong văn bản 
tiếng Việt trên các nền tảng mạng xã hội. Đây là một bài toán quan trọng trong lĩnh 
vực xử lý ngôn ngữ tự nhiên do sự gia tăng nhanh chóng của các nội dung tiêu cực 
trên môi trường trực tuyến. Việc xây dựng các hệ thống tự động có khả năng phát 
hiện và phân loại các phát ngôn thù địch có ý nghĩa quan trọng trong việc hỗ trợ kiểm 
soát nội dung và cải thiện môi trường giao tiếp trên mạng. 
Trong nghiên cứu này, một mô hình phân loại văn bản dựa trên sự kết hợp giữa mô 
hình ngôn ngữ tiền huấn luyện PhoBERT và mạng nơ ron hồi quy hai chiều Bi-LSTM 
đã được đề xuất. PhoBERT được sử dụng để trích xuất các biểu diễn ngữ nghĩa theo 
ngữ cảnh của văn bản tiếng Việt, trong khi Bi-LSTM giúp khai thác thêm các quan 
hệ phụ thuộc trong chuỗi văn bản. Sự kết hợp này cho phép mô hình tận dụng các đặc 
trưng ngữ nghĩa mạnh mẽ của các mô hình ngôn ngữ tiền huấn luyện đồng thời khai 
thác hiệu quả thông tin ngữ cảnh trong dữ liệu văn bản. 
Bên cạnh việc xây dựng mô hình phân loại, nghiên cứu cũng xem xét vấn đề mất cân 
bằng dữ liệu trong bộ dữ liệu ViHSD. Nhiều phương pháp cân bằng dữ liệu khác nhau 
đã được thử nghiệm nhằm đánh giá ảnh hưởng của chúng đến hiệu quả phân loại của 
mô hình. Kết quả thực nghiệm cho thấy các phương pháp kết hợp giữa oversampling 
và undersampling có thể cải thiện đáng kể khả năng nhận diện của mô hình đối với 
các lớp thiểu số. Trong số các phương pháp được thử nghiệm, phương pháp kết hợp 
giữa ROS, RUS và Tomek Links cho kết quả tốt nhất. 
Các kết quả thực nghiệm cho thấy mô hình PhoBERT –Bi-LSTM đạt hiệu quả phân 
loại cao hơn so với các mô hình baseline như Logistic Regression, SVM và Bi-LSTM. 
Điều này cho thấy việc sử dụng các mô hình ngôn ngữ tiền huấn luyện kết hợp với 
các mạng học sâu có khả năng khai thác tốt hơn các đặc trưng ngữ nghĩa của văn bản 
tiếng Việt trong bài toán phát hiện phát ngôn thù địch. 
Nhìn chung, các kết quả của nghiên cứu cho thấy việc kết hợp mô hình PhoBERT với

## Page 72

P
A
G
E 
6 
 
58 
 
Bi-LSTM cùng với chiến lược xử lý mất cân bằng dữ liệu phù hợp có thể cải thiện 
hiệu quả của hệ thống phát hiện phát ngôn thù địch. Những kết quả này góp phần 
cung cấp một hướng tiếp cận hiệu quả cho bài toán phân loại nội dung tiêu cực trong 
văn bản tiếng Việt và có thể được mở rộng trong các nghiên cứu tiếp theo nhằm cải 
thiện độ chính xác và khả năng ứng dụng của hệ thống. 
5.2. Hạn chế 
Bên cạnh những kết quả đạt được, nghiên cứu vẫn tồn tại một số hạn chế cần được 
xem xét nhằm định hướng cho các nghiên cứu tiếp theo. 
Trước hết, nghiên cứu chỉ sử dụng một bộ dữ liệu duy nhất là ViHSD để tiến hành 
huấn luyện và đánh giá mô hình. Mặc dù đây là một bộ dữ liệu phổ biến trong bài 
toán phát hiện phát ngôn thù địch tiếng Việt, việc chỉ sử dụng một bộ dữ liệu có thể 
làm hạn chế  khả năng đánh giá tính tổng quát của mô hình. Trong thực tế, các nội 
dung trên mạng xã hội có sự đa dạng rất lớn về ngữ cảnh, phong cách ngôn ngữ và 
cách biểu đạt. Do đó, mô hình được huấn luyện trên một bộ dữ liệu cụ thể có thể gặp 
khó khăn khi áp dụng cho các nguồn dữ liệu khác. 
Thứ hai, mô hình đề xuất trong nghiên cứu tập trung vào việc kết hợp PhoBERT và 
Bi-LSTM nhằm khai thác biểu diễn ngữ nghĩa của văn bản và quan hệ phụ thuộc 
trong chuỗi dữ liệu. Tuy nhiên, kiến trúc mô hình vẫn còn tương đối đơn giản và chưa 
xem xét các cơ chế nâng cao như attention hoặc các kiến trúc Transformer phức tạp 
hơn. Việc mở rộng kiến trúc mô hình có thể giúp khai thác sâu hơn các đặc trưng ngữ 
nghĩa của văn bản và cải thiện hiệu quả phân loại. 
Một hạn chế khác của nghiên cứu liên quan đến vấn đề mất cân bằng dữ liệu. Mặc dù 
nhiều phương pháp cân bằng dữ liệu đã được thử nghiệm, các phương pháp này chủ 
yếu dựa trên việc điều chỉnh phân bố dữ liệu thông qua oversampling và 
undersampling. Những phương pháp này có thể làm thay đổi cấu trúc ban đầu của tập 
dữ liệu hoặc làm tăng nguy cơ quá khớp khi số lượng mẫu của lớp thiểu số được nhân 
bản nhiều lần. 
Ngoài ra, kết quả phân tích từ ma trận nhầm lẫn cho thấy mô hình vẫn gặp khó khăn

## Page 73

P
A
G
E 
6 
 
59 
 
trong việc phân biệt giữa các lớp Hate và Offensive. Nguyên nhân của hiện tượng 
này có thể xuất phát từ sự tương đồng về ngôn ngữ giữa các loại phát ngôn tiêu cực. 
Trong nhiều trường hợp, ranh giới giữa các mức độ xúc phạm hoặc thù địch không 
hoàn toàn rõ ràng, dẫn đến việc gán nhãn và phân loại trở nên phức tạp hơn. 
Cuối cùng, nghiên cứu chủ yếu tập trung vào bài toán phân loại văn bản ở mức câu 
hoặc bình luận, trong khi các yếu tố ngữ cảnh rộng hơn của cuộc hội thoại chưa được 
xem xét. Trong môi trường mạng xã hội, ý nghĩa của một phát ngôn đôi khi phụ thuộc 
vào ngữ cảnh của toàn bộ cuộc hội thoại hoặc các thông tin bổ sung liên quan đến 
người dùng. Việc chưa khai thác các yếu tố ngữ cảnh này có thể làm hạn chế khả 
năng hiểu đầy đủ nội dung của văn bản. 
Những hạn chế nêu trên cho thấy vẫn còn nhiều hướng nghiên cứu có thể được tiếp 
tục phát triển nhằm nâng cao hiệu quả của hệ thống phát hiện phát ngôn thù địch trong 
văn bản tiếng Việt. 
5.3. Hướng phát triển 
Từ các kết quả đạt được trong nghiên cứu, có thể nhận thấy rằng việc kết hợp mô 
hình ngôn ngữ tiền huấn luyện với các mạng học sâu mang lại hiệu quả tích cực trong 
bài toán phát hiện phát ngôn thù địch. Tuy nhiên, vẫn còn nhiều hướng nghiên cứu 
có thể tiếp tục phát triển nhằm cải thiện hiệu quả của hệ thống và mở rộng khả năng 
ứng dụng trong thực tế. 
Trước hết, một hướng phát triển quan trọng là mở rộng tập dữ liệu huấn luyện. Trong 
nghiên cứu này, mô hình chủ yếu được huấn luyện và đánh giá trên bộ dữ liệu ViHSD. 
Trong các nghiên cứu tiếp theo, việc kết hợp nhiều bộ dữ liệu khác nhau hoặc xây 
dựng các tập dữ liệu mới với quy mô lớn hơn có thể giúp mô hình học được nhiều 
dạng biểu đạt ngôn ngữ đa dạng hơn. Điều này góp phần cải thiện khả năng tổng quát 
hóa của mô hình khi áp dụng cho các nguồn dữ liệu khác nhau trên mạng xã hội. 
Thứ hai, các nghiên cứu tiếp theo có thể xem xét mở rộng kiến trúc mô hình bằng 
cách tích hợp các cơ chế học sâu nâng cao. Ví dụ, việc kết hợp các cơ chế attention 
hoặc các biến thể của kiến trúc Transformer có thể giúp mô hình tập trung vào các

## Page 74

P
A
G
E 
6 
 
60 
 
thành phần quan trọng trong câu, từ đó cải thiện khả năng phát hiện các nội dung tiêu 
cực. Ngoài ra, các mô hình ngôn ngữ tiền huấn luyện mới với quy mô lớn hơn cũng 
có thể được sử dụng để nâng cao chất lượng biểu diễn ngữ nghĩa của văn bản. 
Một hướng phát triển khác là nghiên cứu các phương pháp xử lý mất cân bằng dữ liệu 
tiên tiến hơn. Trong đề án này, các phương pháp oversampling và undersampling 
truyền thống đã được áp dụng để cải thiện phân bố dữ liệu. Tuy nhiên, các kỹ thuật 
nâng cao như tạo dữ liệu tổng hợp hoặc học tăng cường dữ liệu có thể giúp mô hình 
học được các đặc trưng của lớp thiểu số hiệu quả hơn mà không làm thay đổi cấu trúc 
ban đầu của tập dữ liệu. 
Ngoài ra, các nghiên cứu tiếp theo có thể xem xét khai thác ngữ cảnh rộng hơn của 
dữ liệu văn bản. Trong môi trường mạng xã hội, ý nghĩa của một phát ngôn thường 
phụ thuộc vào bối cảnh của toàn bộ cuộc hội thoại hoặc các thông tin liên quan đến 
người dùng. Việc kết hợp các thông tin ngữ cảnh này có thể giúp mô hình hiểu rõ hơn 
nội dung của phát ngôn và cải thiện độ chính xác của quá trình phân loại. 
Cuối cùng, một hướng phát triển quan trọng là xây dựng hệ thống ứng dụng thực tế 
dựa trên mô hình đã được đề xuất. Hệ thống này có thể được tích hợp vào các nền 
tảng quản lý nội dung hoặc các công cụ hỗ trợ kiểm duyệt nhằm tự động phát hiện và 
cảnh báo các nội dung có dấu hiệu thù địch trên mạng xã hội. Việc triển khai các hệ 
thống như vậy không chỉ góp phần cải thiện môi trường giao tiếp trực tuyến mà còn 
tạo ra các ứng dụng thực tiễn cho các nghiên cứu trong lĩnh vực xử lý ngôn ngữ tự 
nhiên.

## Page 75

P
A
G
E 
6 
 
61 
 
TÀI LIỆU THAM KHẢO

## Page 76

P
A
G
E 
6 
 
62 
 
PHẦN LÝ LỊCH TRÍCH NGANG 
 
I. LÝ LỊCH SƠ LƯỢC 
Họ và tên: ĐOÀN VIỆT THIỆN   Ngày, tháng, năm sinh: 12/02/1990 
Nơi sinh: Phường Long An, Tỉnh Tây Ninh 
Địa chỉ liên lạc: 232 Hùng Vương, Khu Phố Tân Xuân 1, Phường Long An, Tỉnh Tây 
Ninh. 
 
II. QUÁ TRÌNH ĐÀO TẠO 
Thời gian Nơi đào tạo Ngành học Năm tốt nghiệp 
Trước 2023 Đại học Sài Gòn Công Nghệ Thông 
Tin 
2015 
2023 - 2025 Đại học Cửu Long Ngôn ngữ Anh 2025 
 
III. QUÁ TRÌNH CÔNG TÁC 
Thời gian Nơi công tác Công việc đảm nhiệm 
   
2022 - nay Quản lý bay Miền Nam NVKT

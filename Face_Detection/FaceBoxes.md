FaceBoxes
===================

# 1. Giới thiệu

* FaceBoxes là thuật toán phát hiện khuôn mặt thời gian thực trên CPU đạt độ chính xác cao
* Paper có 4 sự đóng góp chính
	* Thiết kế Rapidly Digested Convolutional Layers (RDCL) giúp đạt tốc độ thời gian thực trên CPU
	* Thiết kế Multiple Scale Convolutional Layers (MSCL) giúp nhận diện được khuôn mặt có các kích thước khác nhau
	* Đề xuất một chiến lược sinh ra các anchor giúp tăng tỉ lệ recall trên các khuôn mặt nhỏ
	* Thực nghiệm mô hình trên các dataset và phân tích hiệu quả của từng phần trong kiến trúc mô hình FaceBoxes
	

# 2. Rapidly Digested Convolutional Layers (RDCL)
* Phép toán convolution tốn thời gian khi kích thước input, kernel, output lớn. Do đó khối RDCL được thiết kế để giảm nhanh kích thước (chiều dài và rộng) của input image cũng như giảm số channel của output, qua đó giúp FaceBoxes đạt tốc độ nhanh

* Phân tích khối RDCL
	* Sử dụng stride lớn cho conv và pooling layer để giảm kích thước input. Sau khi đi qua khối RDCL thì input giảm kích thước 32 lần
	* Do sử dụng stride lớn nên kernel size cũng phải đủ lớn để tránh mất thông tin, nhưng cũng cần đủ nhỏ để giữ được tốc độ, nên tác giả sử dụng kernel size như trong paper
	* Để giảm chiều sâu (số channel) thì tác giả sử dụng hàm C.Relu. Đây là yếu tố quan trọng giúp tăng tốc độ mà độ chính xác giảm ít


# 3. Multiple Scale Convolutional Layers (MSCL)
* Khối MSCL có chức năng đề xuất các vùng chứa khuôn mặt, được thiết kế dựa trên mạng Region Proposal Network (RPN) và multiple scale trong mạng SSD

* Nhược điểm của RPN là các anchor được đề xuất chỉ dựa trên 1 conv layer thì chưa đủ tốt để nhận diện được các khuôn mặt có scale khác nhau. Để giải quyết vấn đề này thì khối MSCL sử dụng cơ chế multiple scale, các anchor được đề xuất trên 3 layer khác nhau
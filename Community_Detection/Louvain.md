Louvain - Community detection algorithm
==================

# 1. Giới thiệu
* Đây là thuật toán non-overlapping community detection
* Ưu điểm
	* Thời gian thực hiện: nhanh, giới hạn về kích cỡ mạng có thể xử lý chủ yếu bởi giới hạn về bộ nhớ của máy chứ không còn bị giới hạn bởi thời gian thực hiện thuật toán
	* Áp dụng được với mạng có trọng số trên các cạnh
	* Cho phép tìm ra các cộng đồng ở các mức độ *phân giải* khác nhau (nghĩa là có thể phát hiện cộng đồng từ mức vĩ mô, ít cộng đồng nhưng cộng đồng lớn, cho đến mức vi mô có nhiều cộng đồng nhỏ)
	* Chất lượng các cộng đồng phát hiện được là tốt (nếu đánh giá theo tối ưu hóa modularity), nhưng đánh giá theo paper 2018 thì chất lượng chưa tốt !
	* 


# References
* [Fast unfolding of communities in large networks](https://arxiv.org/abs/0803.0476)
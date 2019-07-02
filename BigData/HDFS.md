Hadoop Distributed File System (HDFS)
=========================

## Giới thiệu

* Khái niệm
	* Distributed File System (DFS) là hệ thống quản lý, lưu trữ file phân tán (file được chia thành nhiều phần dữ liệu, lưu trữ trên nhiều máy tính), cho phép nhiều người cùng truy cập dữ liệu.
	* HDFS là hệ thống viết bằng Java dùng để quản lý file phân tán trong cụm Hadoop.
	
* Lý do ra đời bắt nguồn từ thách thức trong việc xử lý, lưu trữ **dữ liệu lớn**
	* Lưu trữ: lưu trữ truyền thống trên 1 máy tính gặp giới hạn kích thước bộ nhớ (không thể lưu toàn bộ lượng dữ liệu lớn). Khi đó cần sử dụng **nhiều máy tính** có tổng lượng bộ nhớ lớn hơn
	* Xử lý: dùng nhiều máy tính sẽ tạo ra năng lực tính toán tốt hơn (dùng cơ chế tính toán song song)
	* Mở rộng: việc mở rộng bằng cách nâng cấp ram/cpu cho 1 máy tính chỉ thực hiện được ở 1 mức độ nhất định và khi đó, hệ thống sẽ phải dừng hoạt động để nâng cấp. Khi nâng cấp trong hệ phân tán thì chỉ cần thêm máy vào cụm mà không phải dừng hệ thống

## Đặc điểm
* Khả năng mở rộng tốt
* Chịu lỗi
* Toàn vẹn dữ liệu
* Lưu trữ lượng lớn và đa dạng dữ liệu
* Giảm thời gian xử lý dữ liệu	

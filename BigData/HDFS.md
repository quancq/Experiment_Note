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


## Kiến trúc
* HDFS sử dụng kiến trúc NameNode - DataNode (Master - Slave). Thường có 1 NameNode và nhiều DataNode. NameNode chạy trên 1 máy, lưu thông tin quản lý các DataNode. Mỗi DataNode thường cài đặt trên 1 máy, chứa dữ liệu thực sự. 

![HDFS_Architecture](Images/HDFS_Architecture.png)

* NameNode: lưu thông tin mô tả dữ liệu của HDFS (meta data), ví dụ như: danh sách các block của các file, ip máy lưu các block, quyền truy cập file,... NameNode sử dụng 2 file để quản lý:
	* FsImage (File System Image): lưu toàn bộ trạng thái của HDFS (nêu trên)
	* EditLog: lưu các sự thay đổi của hệ thống file, ví dụ: khi tạo file mới, thay đổi hệ số bản sao dữ liệu,...
	
NameNode theo định kì sẽ nhận Heartbeat (một loại tin nhắn) từ các DataNode để kiểm tra các DataNode còn sống không. Nếu DataNode nào quá hạn mà không gửi tin nhắn thì NameNode coi nó đã chết và sẽ tạo các bản sao dữ liệu mới để duy trì được hệ số copy. Ngoài ra các DataNode còn gửi BlockReport (danh sách các block mà DataNode đó lưu trữ) cho NameNode.

NameNode thực hiện 1 số chức năng: tạo mới, xóa file,...

* DataNode: lưu trữ dữ liệu, thực hiện thao tác đọc - ghi dữ liệu. Định kì gửi Heartbeat, BlockReport tới NameNode để báo cáo.

* Data blocks: Các file dữ liệu thường được chia nhỏ thành các block có kích thước quy định trước (trừ block cuối có thể có kích thước nhỏ hơn). **Dữ liệu trong HDFS không thể sửa tùy ý** (chỉ được nối thêm hoặc cắt bớt).

* Cơ chế tạo bản copy dữ liệu (Replicate, chọn các máy tính nào để lưu các bản copy)
	* Vấn đề của 2 hướng giải quyết: 
		* Mọi bản copy dữ liệu đều lưu trên các máy cùng 1 rack. Nhược điểm là nếu rack đó bị hỏng thì dữ liệu thực sự bị mất (*bỏ trứng cùng 1 giỏ*) tức là khả năng chịu lỗi kém; mọi thao tác đọc đều phải đi qua rack này, tạo ra nút cổ chai. Ưu điểm là thời gian ghi dữ liệu nhỏ
		* Các bản copy dữ liệu được phân tán ở các rack khác nhau. Nhược điểm là thời gian cho thao tác ghi file lớn bởi vì thời gian truyền dữ liệu giữa 2 máy cùng rack là ít hơn thời gian truyền giữa 2 máy khác rack. Ưu điểm là tận dụng được băng thông của nhiều switch, cân bằng tải sẽ tốt hơn.
	
	![HadoopCluster](Images/HadoopCluster.png)
	
	> **Thách thức**: khả năng chịu lỗi, khả năng sẵn dùng của dữ liệu, tối ưu băng thông mạng, giảm thời gian đọc - ghi dữ liệu
	
	* Cơ chế sử dụng: để cân bằng được các yêu cầu trên, thuật toán sẽ xem xét đến các máy (node) và các rack. Nếu cần lưu 3 bản dữ liệu, bản 1 được lưu tại 1 random DataNode ở rack R1, 2 bản còn lại được lưu tại 2 DataNode khác nhau nhưng cùng thuộc rack R2. Nếu số bản copy > 3 thì các bản copy tiếp sẽ được lưu trên các rack khác, cố gắng đảm bảo số bản copy trên mỗi rack nhỏ hơn 1 ngưỡng quy định. Thuật toán này mang ưu điểm của cả 2 hướng tiếp cận trên.

* Quy trình đọc ghi dữ liệu
	* Thao tác ghi
	Các block được ghi song song với nhau. Mỗi thao tác ghi 1 block dữ liệu gồm 3 giai đoạn là: thiết lập pipeline, truyền dữ liệu, kết thúc pipeline
		* Thiết lập pipeline
		![SetupPipeline](Images/HDFS_SetupPipeline.png) 
		* Truyền và ghi dữ liệu
		![WriteData](Images/HDFS_WriteData.png) 
		* Kết thúc pipeline
		![ShutdownPipeline](Images/HDFS_ShutdownPipeline.png) 
	
	* Thao tác đọc
	NameNode sẽ lựa chọn bản dữ liệu gần nhất đối với client để giảm thời gian truyền dữ liệu
	![ReadData](Images/HDFS_ReadData.png) 

* Sử dụng nhiều NameNode
* Cân bằng tải


## References
* [Edureka - Apache Hadoop HDFS Architecture](https://www.edureka.co/blog/apache-hadoop-hdfs-architecture/)
* [DataFlair - Apache Hadoop HDFS Architecture](https://data-flair.training/blogs/hadoop-hdfs-architecture/)
* [HDFS Document](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
Scrapy
================

# Tổng quan

# Command line tool
* Các câu lệnh thực hiện trên terminal (bắt đầu bằng **scrapy**) để thao tác với project hoặc thao tác không cần gắn liền với 1 project cụ thể
* Một số câu lệnh
	* Không yêu cầu project
		* ``startproject``
		* ``genspider``
		* ``settings``
		* ``runspider``
		* ``shell``
		* ...
	* Yêu cầu project
		* ``crawl``
		* ``check``
		* ``parse``
		* ``list``
		* ...
* Cấu trúc thư mục mặc định của 1 project scrapy
![ ](./Images_Readme/Scrapy_Default_Project_Structure.png "Default structure of Scrapy projects")

* Scrapy tìm kiếm tham số cấu hình trong file scrapy.cfg, vị trí ưu tiên tìm kiếm theo thứ tự là
	* Trong thư mục gốc project
	* Trong thư mục user: ``~/.config/scrapy.cfg`` và ``~/.scrapy.cfg``
	* Trong thư mục hệ thống: ``/etc/scrapy.cfg`` hoặc ``c:\scrapy\scrapy.cfg``
* [Command Line Tool - Scrapy Document](https://doc.scrapy.org/en/latest/topics/commands.html) 

# Spider
* Định nghĩa
* Chu trình cơ bản mà Spider định nghĩa
* Class Spider
	* Mọi spider khác (kể cả user định nghĩa) cần kế thừa spider này
	* Các thuộc tính: name, start_urls, allowed_domains,...
	* Các phương thức:
		* ``start_requests()``
		* ``parse()``
		* ...
* Class CrawlSpider
	* Hỗ trợ crawl mọi link (recursive) của websites
	* Các thuộc tính:
		* rules: là 1 list các đối tượng Rule. Mỗi đối tượng Rule quy định cách thức crawl trên các websites (link như nào thì extract và cách lấy ra thông tin từ các link đó như thê nào,...)
		* Cách định nghĩa 1 đối tượng Rule
			* link_extractor: định nghĩa 1 link ntn thì sẽ được extract
			* callback: hàm quy định cách thức xử lý mỗi link được extract từ link_extractor
			* follow: biến boolean quyết định liệu mỗi link tìm thấy được từ link_extractor có được crawl tiếp trên link đó không
			* process_links: hàm dùng để lọc các link được extract từ link_extractor (tham số của hàm là đối tượng thuộc kiểu Link)
			* process_requests: hàm dùng để lọc các request tạo ra từ link_extractor
			> Luồng thực hiện (không thấy trong doc nói rõ): các link thõa mãn link_extractor được trích ra, sau đó qua hàm process_links để lọc, sau đó tạo các request, với mỗi req sẽ đi qua hàm process_request để lọc tiếp, sau đó engine sẽ gửi req và khi nhận về response thì sẽ gọi callback để xử lý
			* ...
* Class XMLFeedSpider
	* Dùng để trích ra những node có tên xác định từ 1 tài liệu xml và lấy thông tin từ các nodes đó
	* Các thuộc tính
		* iterator: Định nghĩa kiểu iterator dùng để tìm kiếm các node trong tài liệu. Nên dùng 'iternodes' vì hiệu năng tốt
		* itertag: tên node cần tìm
		* namespace:
	* Các phương thức
		* adapt_response():
		* parse_node(res, node): cần phải override hàm này. Hàm này được gọi với mỗi node tìm được, cần trích ra thông tin, return Item hoặc Request
		* process_results():
* Class CSVFeedSpider
* Class SitemapSpider

# Selector
* Dùng để chọn ra những phần nhất định trong tài liệu HTML/XML
* Có thể dùng Selector built-in của Scrapy hoặc dùng thư viện lxml, BeautifullSoup
* Selector theo CSS hoặc Xpath
	* Nên sử dụng Xpath bởi sức mạnh của nó
	* Nên dùng CSS khi cần query theo class


# Items
* Trước đây, sau khi extract data từ response ta thường đóng gói dữ liệu trong dict. Cách này chỉ phù hợp với project nhỏ. Khi project có quy mô lớn hơn, ta cần đóng gói dữ liệu theo hướng OOP, giúp dễ mở rộng, tái sử dụng... Class Item là 1 cái khung giúp ta việc này (ta cần viết class kế thừa class Item)
* Các trường dữ liệu dùng kiểu đối tượng ``Field``. Với cách này, ta có thể quy định bất kì kiểu dữ liệu cho từng field (và có thể quy định hàm serializer để serialize field này)
* Làm việc với Item gần giống như làm việc với dict
* Có thể thiết kế các Item kế thừa nhau, tận dụng ưu điểm của OOP


# Item loader
* *Item* cung cấp khung để chứa data còn *Item loader* cung cấp cơ chế, cách thức, quy trình từ lúc extract data từ response đến khi build thành Item object
* Nếu không có Item loader
	* Trong hàm parse của spider ta cần parse response để return Item
	* Ở đây có thể quy định các hàm để xử lý, biến đổi, làm sạch data trước khi return Item
	* *Vấn đề* là
		* Code trong hàm parse sẽ phức tạp hơn
		* Chưa tối ưu về mặt tái sử dụng (các hàm tiền - hậu xử lý raw data để build thành Item là gắn liền với 1 quy trình nhất định, thường không phụ thuộc vào spider)
			* Ví dụ Item là bài báo tin tức thì các hàm tiền xử lý cho mục title có thể là loại bỏ kí tự HTML, strip space. Sử dụng các hàm này bởi vì đặc tính của field trong Item là như vậy.
			* Nếu có các Item gần giống nhau về tiền xử lý thì cũng không tái sử dụng được
* Scrapy đưa ra khái niệm Item loader giải quyết các vấn đề trên
	* Cung cấp các hàm tiền xử lý (input processor), hậu xử lý (output processor) có sẵn và cho phép user tự định nghĩa
	* Khái niệm Item loader context
	* Nested loader giúp hạn chế viết xpath, css lặp nhiều lần (nhưng tránh lạm dụng, dễ khiến code khó đọc)
	* Cho phép kế thừa Item loader


# Scrapy shell
* Shell tương tác gần giống với python shell
* Mục đích: cung cấp cách thức debug, test spider nhanh chóng
	* Launch shell và gõ các lệnh test thử xpath (css), kiểm tra kết quả trả về, lặp lại cho đến khi tìm được biểu thức phù hợp (không mất công chạy spider nhiều lần)

# Item Pipeline
* Item sau khi được tạo nên từ spider sẽ chuyển qua các thành phần trong item pipeline để xử lý
* Mục đích của item pipeline:
	* Làm sạch dữ liệu
	* Loại bỏ item không thỏa mãn tiêu chí
	* Kiểm tra item trùng lặp
	* Lưu item vào database
* Các class muốn làm 1 thành phần trong item pipeline cần implement hàm process_item()
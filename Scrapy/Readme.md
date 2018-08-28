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
* 
Flask
====================

# 2. Template
* Template định nghĩa khung biểu diễn cho layout của website
* Mục đích
	* Phân tách logic nghiệp vụ và layout của website giúp các bên (thiết kế web và dev backend) phát triển độc lập
	* Hỗ trợ kế thừa layout
* Các file template html đặt trong thư mục ``templates``
* Ví dụ
```python
<html>
	<head>
		<title>{{ title }} - Microblog</title>
	</head>
	<body>
	<h1>Hello, {{ user.username }}!</h1>
	</body>
</html>
```

```python
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
```

* Template quy định khung, giá trị cụ thể các biến được quyết định lúc runtime. Ta cần gọi hàm ``render_template`` và truyền vào các biến để render. Rendering là quá trình biến template thành file HTML hoàn chỉnh

* Lệnh điều kiện if else
```python
    <head>
        {% if title %}
        <title>{{ title }} - Microblog</title>
        {% else %}
        <title>Welcome to Microblog!</title>
        {% endif %}
    </head>
```

* Vòng lặp
```python
    <body>
        <h1>Hi, {{ user.username }}!</h1>
        {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
        {% endfor %}
    </body>
```

* Sự cần thiết của kế thừa: thông thường, nhiều trang web cùng một domain thường giống nhau một số phần như: nav bar, foot,... Khi đó các layout chung này có thể code trong file HTML base, sau đó các file HTML cụ thể (của các trang khác nhau) sẽ kế thừa để tái sử dụng
	* File base.html cần có ``block``
	``{% block content %}{% endblock %}``
	* File derived.html cần có ``extends`` (cho biết để render file derived thì cần render file base nào) và ``block`` (chứa nội dung điền vào phần tương ứng của file base)
	
```python
	{ extends "base.html" %}

	{% block content %}
		<h1>Hi, {{ user.username }}!</h1>
		{% for post in posts %}
		<div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
		{% endfor %}
	{% endblock %}
```

# 3. Web form
* Flask-WTF là một extension tích hợp với Flask, cung cấp tính năng liên quan đến web form, giải quyết các vấn đề mà Flask không tập trung quan tâm
* Đây là python package => Cài đặt bằng pip
* Khi dùng extension thì có nhiều cấu hình cần config
	* Cách đơn giản là ``app.config['SECRET_KEY'] = 'you-will-never-guess'``
	* Cách giúp dễ mở rộng, tái sử dụng là dùng class
	```python
		class Config(object):
			SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	```
	* Sử dụng config từ file
```python
	from flask import Flask
	from config import Config

	app = Flask(__name__)
	app.config.from_object(Config)
```
* Các form được biểu diễn bởi class. Các trường dữ liệu của form được quy định bởi biến của class

* Login form
	* VD
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
```
* ``validator``: quy định cách kiểm tra, xác thực dữ liệu
* Trong route login cần định nghĩa cho phép server chấp nhận method POST hoặc GET và viết logic xử lý form data nhận từ client
* Hiển thị lỗi cụ thể của field không hợp lệ để người dùng biết
* Nên dùng ``url_for`` để sinh ra link chứ không nên dùng trực tiếp string url. ``url_for`` sẽ map giữa view function và url, khi cần thay đổi url thì chỉ cần thay đổi ở chỗ route chứ không cần replace mọi string url

	
# References

* [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
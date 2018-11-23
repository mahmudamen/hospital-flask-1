# Hospital FlaskApp

Simple application with authentication and CRUD functionality using the Python Flask micro-framework

## Installation

To use this template, your computer needs:

- [Python 2 or 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)
Installing Flask-WTF is simple with pip:
$ pip install Flask-WTF
or, with easy_install:
$ easy_install Flask-WTF
-------------------------------------
for database go to link
$ pip install mysqlclient
$ sudo service mysql start # for ubuntu
$ sudo apt-get install python-dev libmysqlclient-dev # for Debian/Ubuntu 
$ sudo dnf install python-devel mysql-devel # for Fedora $ brew install mysql-connector-c # for Mac OS
GRANT ALL ON testflask.* To 'testuser'@'localhost' IDENTIFIED BY 'testpassword'; 
mysql -u testuser -p 
mysql> CREATE DATABASE testflask; 
mysql> USE testflask; 
mysql> CREATE TABLE users( 
-> id INT(11) PRIMARY KEY AUTO_INCREMENT, 
-> username VARCHAR(20) NOT NULL, 
-> firstname VARCHAR(20) NOT NULL, 
-> lastname VARCHAR(20) NOT NULL);
for other tables go to 
dump folder > 

-------------------------------------
But, you really shouldn't do that.
### Running the app

```bash
python app.py
```
username : mmmm
password : m
Dev by
Mahmudamen 


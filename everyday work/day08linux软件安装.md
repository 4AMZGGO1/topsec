\# 去重并统计每个 IP 的攻击次数 

grep "Failed password" ./secure | awk '{print $11}' | sort | uniq -c | sort -nr

![image-20250717165054613](images/image-20250717165054613.png)

在/tmp/中建立nd2025目录，然后在其中建立bigfile文件大小100M

dd if=/dev/zero of=./bigfile bs=1M count=100
100+0 records in

![image-20250717165406373](images/image-20250717165406373.png)

3、要求将/tmp/nd2025目录 打包并压缩到 /opt目录中 压缩工具选择 gzip工具

tar -zcf /opt/1.tar.gz nd2025

![image-20250717165707005](images/image-20250717165707005.png)

4、将压缩后的文件nd2025.tar.gz  解压到 桌面上 /root/Desktop

tar -zxf 1.tar.gz -C /root/Desktop/

![image-20250717165928901](images/image-20250717165928901.png)

5、使用源码包安装httpd服务，并且可以发布网站，以自己的名字作为内容

解压

cd /root/Desktop
tar -zxvf httpd-2.2.15.tar.gz
cd httpd-2.2.15

安装

./configure --prefix=/usr/local/apache2 --enable-so --enable-rewrite --with-included-apr

![image-20250717170459534](images/image-20250717170459534.png)

编译，安装

make

make install

![image-20250717170623745](images/image-20250717170623745.png)

添加可执行文件路径

echo 'export PATH=$PATH:/usr/local/apache2/bin' >> ~/.bashrc
source ~/.bashrc

![image-20250717170735320](images/image-20250717170735320.png)

启动服务并查看是否正常运行

apachectl start

ps aux | grep httpd

![image-20250717170846842](images/image-20250717170846842.png)

成功在http://192.168.126.129/访问到测试界面

![image-20250717171051468](images/image-20250717171051468.png)

修改主页

vim /var/www/html/index.html

![image-20250717171452583](images/image-20250717171452583.png)

成功访问

![image-20250717171726437](images/image-20250717171726437.png)







6、在kali系统中成功安装QQ并登陆，

安装

sudo dpkg -i QQ_3.2.12_240902_amd64_01.deb

sudo apt install -f

![image-20250717172158733](images/image-20250717172158733.png)

输入qq，打开成功

![image-20250717172245410](images/image-20250717172245410.png)
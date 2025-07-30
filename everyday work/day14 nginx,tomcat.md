# 🧩 作业 1：实现 Nginx 解析 PHP

------

## ✅ 一、总体流程

1. 安装 PHP 和 PHP-FPM
2. 配置 Nginx 与 PHP-FPM 通信
3. 设置网站根目录和 `.php` 处理规则
4. 重启服务并测试

------

## 🧱 二、安装 PHP 和 PHP-FPM（以 CentOS 7 为例）

### 1. 安装 EPEL 和 Remi 源

```bash
yum install epel-release -y
yum install https://rpms.remirepo.net/enterprise/remi-release-7.rpm -y
yum install yum-utils -y
yum-config-manager --enable remi-php81  # 启用 PHP 8.1，可根据需求更换版本
```

### 2. 安装 PHP、PHP-FPM 和常用扩展

```bash
yum install php php-fpm php-mysqlnd php-cli php-gd php-mbstring php-xml -y
```

------

## 🔧 三、配置 PHP-FPM

编辑配置文件：

```bash
vi /etc/php-fpm.d/www.conf
```

确认并修改以下内容：

```conf
listen = 127.0.0.1:9000
user = nginx
group = nginx
```

📷 本地截图：
 ![image-20250725171255847](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171255847.png)
 ![image-20250725171401190](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171401190.png)

------

## 🚀 四、启动 PHP-FPM

```bash
systemctl start php-fpm
systemctl enable php-fpm
```

------

## 🛠 五、配置 Nginx 支持 PHP

编辑 Nginx 配置文件 `/etc/nginx/conf.d/default.conf`：

```nginx
server {
    listen       80;
    server_name  localhost;

    root   /usr/share/nginx/html;
    index  index.php index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

📷 配置截图：
 ![image-20250725171222794](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171222794.png)

------

## 🧪 六、测试 PHP 是否正常运行

创建测试文件：

```bash
echo "<?php phpinfo(); ?>" > /usr/share/nginx/html/index.php
```

访问：

```
http://服务器IP/index.php
```

📷 显示效果：
 ![image-20250725171125262](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171125262.png)

------

## 🔁 七、重启服务

```bash
systemctl restart php-fpm
systemctl restart nginx
```

------

# 🧩 作业 2：Tomcat 安装及木马植入指南

------

## ✅ 一、安装前准备

### 1. 安装 Java（Tomcat 依赖）

```bash
yum install java-1.8.0-openjdk -y
```

------

## 📦 二、下载并安装 Tomcat（以 Tomcat 9 为例）

```bash
cd /usr/local
mkdir tomcat && cd tomcat
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.87/bin/apache-tomcat-9.0.87.tar.gz
tar -zxvf apache-tomcat-9.0.87.tar.gz
mv apache-tomcat-9.0.87 tomcat9
cd tomcat9
```

------

## 🚀 三、启动 Tomcat

```bash
./bin/startup.sh
```

📷 启动截图：
 ![image-20250725171643960](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171643960.png)

------

## 🔍 四、访问 Tomcat 页面

```
http://你的服务器IP:8080
```

📷 页面效果：
 ![image-20250725171717646](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171717646.png)

------

## 🛡 五、开放防火墙端口

```bash
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --reload
```

------

## 📁 六、Tomcat 目录结构简述

| 目录     | 功能说明                  |
| -------- | ------------------------- |
| bin/     | 启动脚本                  |
| webapps/ | 默认部署目录              |
| conf/    | 配置文件（如 server.xml） |
| logs/    | 日志目录                  |
| lib/     | 核心依赖                  |
| temp/    | 临时文件                  |

------

## 🌐 七、启用 Tomcat 管理后台远程访问

### 1. 添加管理用户

编辑 `/usr/local/tomcat/tomcat9/conf/tomcat-users.xml`：

```xml
<tomcat-users>
  <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>
  <user username="admin" password="123.com" roles="manager-gui,admin-gui"/>
</tomcat-users>
```

📷 配置截图：
 ![image-20250725171843870](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171843870.png)

------

### 2. 放开访问限制（根据 IP）

编辑 `/usr/local/tomcat/tomcat9/webapps/manager/META-INF/context.xml`：

```xml
<Context antiResourceLocking="false" privileged="true" >
  <CookieProcessor className="org.apache.tomcat.util.http.Rfc6265CookieProcessor"
                   sameSiteCookies="strict" />
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|192\.168\.126\.\d+" />
</Context>
```

📷 IP 限制配置：
 ![image-20250725171922260](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725171922260.png)

------

### 3. 重启 Tomcat

```bash
cd /usr/local/tomcat/tomcat9
./bin/shutdown.sh
./bin/startup.sh
```

------

### 4. 登录后台

```
http://服务器IP:8080/manager/html
```

输入刚刚配置的用户名密码即可。

------

## 🚨 八、部署恶意 WAR 文件（安全研究用途）

1. 上传 `.war` 大马包至 webapps
2. 浏览器访问：

```
http://192.168.126.138:8080/jshell/jshell.jsp
密码：1q1q1q
```

📷 成功获取 shell：
 ![image-20250725190128382](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725190128382.png)

------

## 🔄 九、修改 Tomcat 启动账户

### 1. 创建新用户

```bash
useradd -r -s /bin/bash tomcat
passwd tomcat
```

### 2. 修改权限

```bash
chown -R tomcat:tomcat /usr/local/tomcat/tomcat9
```

### 3. 用 tomcat 用户启动服务

```bash
cd /usr/local/tomcat/tomcat9/bin     
./shutdown.sh
su - tomcat
cd /usr/local/tomcat/tomcat9
./bin/startup.sh
```

📷 运行截图：
 ![image-20250725191200982](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725191200982.png)

------

# 🧩 作业 3：搭建 CMS 平台（基于 Nginx）

------

## ✅ 一、环境准备

### 1. 安装服务组件

```bash
yum install nginx php-mysql php-gd php-mbstring php-xml mariadb-server -y
```

如有旧 PHP：

```bash
yum remove php* -y
```

### 2. 切换 PHP 版本至 5.6

```bash
yum-config-manager --disable remi-php81
yum-config-manager --enable remi-php56
```

### 3. 安装 PHP 5.6

```bash
yum install php php-fpm php-mysql php-gd php-mbstring php-pdo -y
```

------

## ✅ 二、启动服务

```bash
systemctl enable --now nginx
systemctl enable --now php-fpm
systemctl enable --now mariadb
```

------

## ✅ 三、数据库初始化

```bash
mysql -uroot
CREATE DATABASE cms CHARACTER SET utf8;
USE cms;
SOURCE /usr/share/nginx/html/install.sql;
```

📷 数据导入截图：
 ![image-20250725193003896](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725193003896.png)

------

## ✅ 四、部署 CMS 系统

复制项目：

```bash
cp -r cms /usr/share/nginx/html/
```

访问地址：

```
http://你的服务器IP/cms/index.php
```

------

## ✅ 五、配置数据库连接

编辑配置文件：

```bash
vi /usr/share/nginx/html/cms/include/database.inc.php
```

修改内容如下：

```php
$dbhost = 'localhost';
$dbuser = 'root';
$dbpw   = '123456';
$dbname = 'cms';
```

📷 配置截图：
 ![image-20250725193730692](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725193730692.png)

------

## ✅ 六、设置权限

```bash
cd /usr/share/nginx/html/cms
chmod -R 777 attachment
```

------

## ✅ 七、访问测试

```
http://你的服务器IP/cms/
```

📷 页面效果：
 ![image-20250725193926854](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250725193926854.png)


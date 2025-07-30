# ✅ 1. Crontab 每 3 小时备份日志（12 月，每天 06:00、09:00、12:00）

## 🔍 需求解析

- **执行月份**：仅在 12 月
- **执行时间**：每天的 06:00、09:00 和 12:00
- **执行用户**：`toor`
- **操作内容**：将 `/var/log/secure` 复制到 `/tmp/class` 目录，带时间戳命名，防止覆盖

------

## ⚙️ 权限配置

让 `toor` 拥有对 `/var/log/secure` 的读取权限：

```bash
sudo chmod 644 /var/log/secure
```

------

## 📅 Crontab 配置

编辑系统级 crontab 文件：

```bash
sudo vim /etc/crontab
```

添加以下内容：

```cron
0 6,9,12 * 12 * toor sh -c 'mkdir -p /tmp/class && cp /var/log/secure /tmp/class/secure_$(date +\%Y\%m\%d_\%H\%M).log'
```

### 参数说明：

| 字段 | 取值     | 含义                   |
| ---- | -------- | ---------------------- |
| 分钟 | `0`      | 整点执行               |
| 小时 | `6,9,12` | 每天 6 点、9 点、12 点 |
| 日   | `*`      | 每天                   |
| 月   | `12`     | 仅在 12 月             |
| 星期 | `*`      | 每周的任意一天         |
| 用户 | `toor`   | 以 `toor` 用户执行     |

> ✅ `sh -c '...'` 是为了让 `$(date ...)` 被正确解析
>  ✅ `%` 在 crontab 中需写为 `\%`
>  ✅ `mkdir -p` 确保目录存在

------

# ✅ 2. 日志服务器实时转发网络拓扑及连通性配置

## 🌐 网络拓扑说明

| 设备       | 接口  | IP 地址       | 网关          |
| ---------- | ----- | ------------- | ------------- |
| `kali`     | ens33 | 192.168.1.50  | 192.168.1.254 |
| `centos7`  | ens33 | 192.168.1.254 | 无需配置      |
| `centos7`  | ens34 | 172.16.1.254  | 无需配置      |
| 日志服务器 | ens33 | 172.16.1.50   | 172.16.1.254  |

📷 ![image-20250723192259836](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723192259836.png)

------

## 🛠️ 第一步：实现网络连通性

### ① 启用路由转发功能（在 centos7）

编辑内核配置：

```bash
sudo vi /etc/sysctl.conf
```

取消注释或添加：

```bash
net.ipv4.ip_forward = 1
```

立即生效：

```bash
sudo sysctl -p
```

验证：

```bash
cat /proc/sys/net/ipv4/ip_forward
# 应该输出 1
```

📷 ![image-20250723192618789](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723192618789.png)

------

### ② 配置 NAT 转发（centos7）

```bash
sudo iptables -t nat -A POSTROUTING -o ens34 -j MASQUERADE
```

保存规则：

```bash
sudo yum install iptables-services -y
sudo service iptables save
```

------

### ③ 配置日志服务器默认网关（先前已配置的忽略）

```bash
sudo ip route add default via 172.16.1.254
```

------

### ✅ 测试连通性（从 kali ping）

```bash
ping 172.16.1.50
```

📷 ![image-20250723192938893](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723192938893.png)

------

## ✅ 第二步：日志实时转发配置

### 📤 步骤一：CentOS7 （.254）配置 rsyslog 发送端

编辑 `/etc/rsyslog.conf`，添加：

```bash
*.* @@172.16.1.50:514
```

> `@` 表示 UDP
>  `@@` 表示 TCP（推荐）
>  `514` 是默认端口

重启服务：

```bash
systemctl restart rsyslog
```

📷 ![image-20250723202555319](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250723202555319.png)

------

### 📥 步骤二：日志服务器（172.16.1.50）设置为 rsyslog 接收端

编辑 日志服务器的`/etc/rsyslog.conf`，取消注释

```bash
# UDP
$ModLoad imudp
$UDPServerRun 514

# TCP
$ModLoad imtcp
$InputTCPServerRun 514
```

📷 ![image-20250723194616177](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723194616177.png)

------

## 📦 第三步：分类型日志备份

### ① 修改 rsyslog 配置规则

继续编辑 日志服务器的`/etc/rsyslog.conf`，追加：

```bash
# SSH 登录失败日志
:msg, contains, "Failed password" /var/log/class1/class2.txt
& stop

# SSH 登录成功日志
:msg, contains, "Accepted password" /var/log/class1/class3.txt
& stop
```

------

### ② 创建日志目录与文件

```bash
sudo mkdir -p /var/log/class1
sudo touch /var/log/class1/class2.txt
sudo touch /var/log/class1/class3.txt
sudo chmod 644 /var/log/class1/class*.txt
```

------

### ③ 重启 rsyslog 服务

```bash
sudo systemctl restart rsyslog
```

------

### 🔍 ④ 测试日志是否正确分类记录

#### 🚫 测试 SSH 登录失败（class2.txt）

```bash
ssh wronguser@192.168.1.254
```

查看记录：

```bash
tail -f /var/log/class1/class2.txt
```

📷 ![image-20250723195217082](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723195217082.png)

------

#### ✅ 测试 SSH 登录成功（class3.txt）

```bash
ssh root@192.168.1.254
```

查看记录：

```bash
tail -f /var/log/class1/class3.txt
```

📷 ![image-20250723195313208](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250723195313208.png)

------

 

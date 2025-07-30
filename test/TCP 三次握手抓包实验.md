## TCP 三次握手抓包实验

------

### 🔧 一、实验拓扑图

> 网络拓扑结构如下图所示：

![image-20250730114500846](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250730114500846.png)

- **Client（客户端）**：192.168.123.2
- **Server（服务器）**：192.168.123.1
- **LSW（2层交换机）**：中间连接设备
- 实验软件：**eNSP + Wireshark**

------

### 🎯 二、实验目的

抓取并分析 **TCP 三次握手** 过程中的报文，理解连接建立的工作机制。

------

### 🧪 三、抓包过滤器

在 Wireshark 中使用以下过滤器提取三次握手相关的数据包：

```wireshark
tcp.flags.syn == 1 or (tcp.flags.ack == 1 and tcp.seq == 1 and tcp.ack == 1)
```

说明：

- `tcp.flags.syn == 1`：匹配第一次和第二次握手
- `(tcp.flags.ack == 1 and tcp.seq == 1 and tcp.ack == 1)`：精准匹配第三次握手（客户端确认）

------

### 📦 四、抓包数据分析

> 三个关键数据包如下：

![image-20250730114427068](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250730114427068.png)

```
51	113.657000	192.168.123.2	192.168.123.1	TCP	58	2058 → 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460
→ 第一次握手：客户端向服务端发送 SYN 请求，开始建立连接。

52	113.657000	192.168.123.1	192.168.123.2	TCP	58	80 → 2058 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460
→ 第二次握手：服务器回复 SYN + ACK，表示收到连接请求并同意。

53	113.657000	192.168.123.2	192.168.123.1	TCP	54	2058 → 80 [ACK] Seq=1 Ack=1 Win=8192 Len=0
→ 第三次握手：客户端发送 ACK 确认，连接正式建立。
```

------

### ✅ 五、实验结论

通过抓包可以清晰观察到 TCP 的三次握手过程，验证了 TCP 建立连接的机制。每个握手包都包含特定的标志位和序列号信息，用于可靠的连接确认。

------

如果你还想继续补充“四次挥手”、“抓 HTTPS TLS 握手”、“ACK 延迟问题”等内容，也可以继续拓展这份实验文档。需要我帮你出一整套抓包实验题目也没问题。
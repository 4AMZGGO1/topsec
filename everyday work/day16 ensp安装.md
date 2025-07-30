## **1、抓取 ARP 协议包，查看帧头的目标 MAC 地址的不同**

### **实验目的**

通过抓取 ARP 协议包，了解 ARP 请求和应答报文中以太网帧头的目标 MAC 地址的差异。

------

### **实验环境与工具**

- **工具**：Wireshark 抓包工具
- **拓扑**：ENSP 模拟环境（PC1 + PC2 + 交换机）

------

### **实验拓扑截图**

![image-20250729112440631](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250729112440631.png)

------

### **实验步骤**

1. 在 ENSP 中构建如上拓扑，两台 PC 分别配置 IP 地址。
2. 使用 Wireshark 抓包，选择 PC1 抓取网卡流量。
3. 在 PC1 上使用 `ping` 命令访问 PC2，触发 ARP 过程。
4. 查看 ARP 请求和应答帧的目标 MAC 地址差异。

------

### **ARP 请求包分析**

- **帧头目标 MAC 地址**：`ff:ff:ff:ff:ff:ff`（广播地址）
- **说明**：ARP 请求用于询问“某个 IP 地址对应的 MAC 地址是谁？”

#### ARP 请求帧截图：

![image-20250729112814103](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250729112814103.png)

#### **完整帧信息解读**：

```
Frame 28: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: HuaweiTe_96:6d:06 (54:89:98:96:6d:06), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)
```

#### **字段说明**：

- **帧编号**：第 28 帧，是抓包中最早出现的 ARP 请求。
- **帧长度**：60 字节，是以太网规定的最小帧长（自动补全填充）。
- **协议类型**：Ethernet II 帧，封装的是 ARP 协议。
- **源 MAC**：`54:89:98:96:6d:06`（请求发起方）。
- **目标 MAC**：`ff:ff:ff:ff:ff:ff`（广播地址，发给全网所有主机）。

------

### **ARP 应答包分析**

- **帧头目标 MAC 地址**：`54:89:98:96:6d:06`（单播）
- **说明**：ARP 应答是被询问主机直接把 MAC 地址回复给请求主机。

#### ARP 应答帧截图：

![image-20250729113006251](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20250729113006251.png)

#### **ARP 响应帧 Frame 29 分析**：

```
Frame 29: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: HuaweiTe_24:05:72 (54:89:98:24:05:72), Dst: HuaweiTe_96:6d:06 (54:89:98:96:6d:06)
    Destination: HuaweiTe_96:6d:06 (54:89:98:96:6d:06)
    Source: HuaweiTe_24:05:72 (54:89:98:24:05:72)
    Type: ARP (0x0806)
    Padding: 000000000000000000000000000000000000
Address Resolution Protocol (reply)
```

#### **字段说明**：

| 字段          | 值                            | 含义                            |
| ------------- | ----------------------------- | ------------------------------- |
| 帧编号        | Frame 29                      | 第 29 个抓到的帧，ARP 响应帧    |
| 源 MAC 地址   | `54:89:98:24:05:72`（Huawei） | 被请求主机的 MAC 地址（响应者） |
| 目标 MAC 地址 | `54:89:98:96:6d:06`（Huawei） | 请求主机的 MAC 地址（单播响应） |
| 帧类型        | `0x0806`                      | 表示为 ARP 协议帧               |
| ARP 类型      | reply                         | 表明是一个 ARP 响应包           |
| Padding       | 全部为 0                      | 补足帧长度至 60 字节的填充数据  |

------

### ✅ **ARP 请求与响应帧对比总结**

| 项目                  | ARP 请求帧（Frame 28）      | ARP 响应帧（Frame 29）      |
| --------------------- | --------------------------- | --------------------------- |
| 目标 MAC 地址（帧头） | `ff:ff:ff:ff:ff:ff`（广播） | 请求主机的 MAC 地址（单播） |
| 源 MAC 地址（帧头）   | 请求主机的 MAC 地址         | 响应主机的 MAC 地址         |
| ARP 类型              | request                     | reply                       |
| 帧头通信方式          | 广播                        | 单播                        |

------

### 🧠 **结论：帧头目标 MAC 地址的差异**

| ARP 类型 | 帧头目标 MAC 地址           | 原因说明                                 |
| -------- | --------------------------- | ---------------------------------------- |
| ARP 请求 | `ff:ff:ff:ff:ff:ff`（广播） | 因不知道目标 MAC，需要广播查找           |
| ARP 响应 | 请求主机的 MAC 地址（单播） | 直接回复给请求方，帧目标地址为请求者 MAC |



------

## **2、ENSP 测试两台主机通过交换机通信**

### **实验拓扑**：

```
PC1 ----- SW ----- PC2
```

### **配置步骤**：

1. 将两台主机分别连接到交换机的两个端口。

2. 给 PC1 和 PC2 分别配置 IP 地址：

   - PC1：192.168.100.1/24
   - PC2：192.168.100.2/24

3. 在 PC1 上 ping PC2：

   ```bash
   ping 192.168.100.2
   ```

4. 观察是否通信成功。

### ![image-20250729113406121](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729113406121.png)



------

## ✅ **3、预习用户模式、特权模式、修改设备名称命令（华为设备）**

### **一、实验目的**

熟悉华为交换机的基本命令行操作流程，掌握用户视图、系统视图的切换方法，以及如何修改设备名称。

------

### **二、实验环境**

- ENSP 模拟器
- 一台华为交换机设备（S5700）

------

### **三、基本概念**

| 模式/视图 | 提示符     | 说明                                  |
| --------- | ---------- | ------------------------------------- |
| 用户视图  | `<Huawei>` | 登录后默认进入，可查看基本信息        |
| 系统视图  | `[Huawei]` | 输入 `system-view` 进入，配置各种参数 |

------

### **四、常用命令**

#### 1. **进入系统视图（配置模式）**

```bash
<Huawei> system-view
Enter system view, return user view with Ctrl+Z.
[Huawei]
```

> ![image-20250729114309609](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729114309609.png)

------

#### 2. **修改设备名称**

```bash
[Huawei] sysname SW1
[SW1]
```

> 此命令将设备名称从默认的 `Huawei` 修
>
> 改为 `SW1`，方便识别设备角色。
>
> ![image-20250729114325665](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729114325665.png)

------

#### 3. **退出到用户视图**

```bash
[SW1] quit
<SW1>
```

![image-20250729114402842](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729114402842.png)

#### 4. **从系统视图返回终端直接命令行**

```bash
[SW1] Ctrl+Z
<SW1>
```

------



# 4、预习交换机设置 Telnet 远程控制

------

### ![image-20250729144026135](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729144026135.png)

```bash
<Huawei> system-view

[sw1] sysname SW1

[SW1] interface Vlanif1
[SW1-Vlanif1] ip address 192.168.100.254 255.255.255.0
[SW1-Vlanif1] quit

[SW1] interface GigabitEthernet 0/0/1
[SW1-GigabitEthernet0/0/1] port link-type access
[SW1-GigabitEthernet0/0/1] port default vlan 1
[SW1-GigabitEthernet0/0/1] undo shutdown
[SW1-GigabitEthernet0/0/1] quit


[SW1] user-interface vty 0 4
[SW1-ui-vty0-4] set authentication password simple YourPassword123
[SW1-ui-vty0-4] protocol inbound telnet
[SW1-ui-vty0-4] quit

```

![image-20250729115408944](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729115408944.png)

------

### PC端Telnet登录测试

### 使用 **ENSP 中支持 telnet 的设备**（推荐用 Router 模拟 PC）

1. 在 ENSP 中用一台 **AR 路由器** 代替 PC。

2. 给 AR 分配 IP 地址：

   ```bash
   [AR1] interface GigabitEthernet 0/0/0
   [AR1-GigabitEthernet0/0/0] ip address 192.168.100.1 255.255.255.0
   [AR1-GigabitEthernet0/0/0] undo shutdown
   ```

3. 然后在 AR 的用户视图中执行：

   ```bash
   <AR1> telnet 192.168.100.254
   ```

![image-20250729143951910](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250729143951910.png)


------

## 🧪实验名称：DHCP 地址分配

### 一、实验目的

1. 掌握在华为交换机/路由器上创建 VLAN 接口并进行 IP 配置的方法。
2. 学会通过 DHCP 地址池为特定 VLAN 动态分配 IPv4 地址。
3. 验证终端设备能否正确获取 IP 地址、网关和 DNS 配置。

------

### 二、实验拓扑

- 一台华为三层交换设备（支持 DHCP 和 VLAN 接口）
- 两台连接到交换机的终端设备（如 PC 或虚拟机）
- 接口 G0/0/1、G0/0/2 接入终端，划入 VLAN 10

------

### 三、实验步骤

#### 1️⃣ 启用系统视图与 DHCP 功能

```bash
<Huawei> system-view
[Huawei] sysname dhcp       # 设置设备名称为 dhcp
[dhcp] dhcp enable           # 全局启用 DHCP 功能
```

#### 2️⃣ 配置 VLAN 10 及 Access 端口

```bash
[dhcp] vlan 10
[dhcp] interface GigabitEthernet 0/0/1
[dhcp-GigabitEthernet0/0/1] port link-type access
[dhcp-GigabitEthernet0/0/1] port default vlan 10
[dhcp-GigabitEthernet0/0/1] quit

[dhcp] interface GigabitEthernet 0/0/2
[dhcp-GigabitEthernet0/0/2] port link-type access
[dhcp-GigabitEthernet0/0/2] port default vlan 10
[dhcp-GigabitEthernet0/0/2] quit
```

#### 3️⃣ 配置三层 VLAN 接口

```bash
[dhcp] interface Vlanif 10
[dhcp-Vlanif10] ip address 192.168.1.254 255.255.255.0
[dhcp-Vlanif10] dhcp select global       # 选择使用全局地址池
[dhcp-Vlanif10] quit
```

#### 4️⃣ 配置全局 DHCP 地址池

```bash
[dhcp] ip pool vlan10
[dhcp-ip-pool-vlan10] network 192.168.1.0 mask 24
[dhcp-ip-pool-vlan10] gateway-list 192.168.1.254
[dhcp-ip-pool-vlan10] domain-name topsec-edu.com
[dhcp-ip-pool-vlan10] excluded-ip-address 192.168.1.1
[dhcp-ip-pool-vlan10] dns-list 114.114.114.114
[dhcp-ip-pool-vlan10] quit
```

------

### 四、验证结果

在 PC 上执行 `ipconfig`，显示如下：

```plaintext
IPv4 地址:             192.168.1.253
子网掩码:             255.255.255.0
默认网关:             192.168.1.254
DNS 服务器:           114.114.114.114
```

> ✅ 表明 PC 已从 DHCP 服务器成功获取了 IP 地址及相关网络参数，配置生效。

------

### 五、实验结论

本次实验成功完成以下目标：

- 正确配置了 VLAN 接口 IP；
- 正确设置了 Access 接口与 VLAN 绑定；
- 建立了全局 DHCP 地址池；
- PC 终端通过交换机成功动态获取网络配置。

这为后续大规模网络管理提供了基础，有利于简化 IP 分配和维护。

------

如需附加拓扑图、抓包截图或 `.cfg` 配置文件，可以继续补充，我也可以帮你生成。是否需要加入这些内容？
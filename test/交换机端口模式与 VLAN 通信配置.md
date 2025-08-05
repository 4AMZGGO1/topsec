你这个实验是基于 **华为交换机的三种端口模式（access、trunk、hybrid）配置和 VLAN 通信测试**，现在我们来整理一篇**完整的实验报告**，适合提交作业或实验文档。

------

## 🌐 网络实验报告：交换机端口模式与 VLAN 通信配置

------

### 一、实验目的

1. 掌握华为交换机端口的三种工作模式：**access**、**trunk**、**hybrid**
2. 学会 VLAN 的创建、接口加入 VLAN 的方法
3. 通过实际配置，验证不同端口类型与 VLAN 配置对网络通信的影响

------

### 二、实验拓扑简述

设备包括：

- 三台华为交换机（sw1、sw2、sw3）
- 多台 PC（模拟主机）

连接：

- 三台交换机之间互联，并配置 trunk 或 hybrid 链路
- PC 分别连接到交换机的不同端口，配置在 VLAN 10/20/30 中

------

### 三、实验步骤

#### 1. 交换机 sw1 配置

```bash
<Huawei> sys
[Huawei] sysname lsw1
[lsw1] undo info-center enable     # 关闭日志信息提示
[lsw1] vlan batch 10 20 30         # 创建 VLAN

# 配置 e0/0/1 为 trunk，允许 VLAN 10/20/30
[lsw1] int e0/0/1
[lsw1-Ethernet0/0/1] port link-type trunk
[lsw1-Ethernet0/0/1] port trunk allow-pass vlan 10 20 30

# 配置 e0/0/2 为 access，加入 VLAN 20
[lsw1] int e0/0/2
[lsw1-Ethernet0/0/2] port link-type access
[lsw1-Ethernet0/0/2] port default vlan 20

# 配置 e0/0/3 为 hybrid，pvid 30，untagged 10 30
[lsw1] int e0/0/3
[lsw1-Ethernet0/0/3] port link-type hybrid
[lsw1-Ethernet0/0/3] port hybrid pvid vlan 30
[lsw1-Ethernet0/0/3] port hybrid untagged vlan 10 30
```

------

#### 2. 交换机 sw2 配置

```bash
<Huawei> sys
[Huawei] sysname sw2
[sw2] undo info-center enable
[sw2] vlan batch 10 20 30

# trunk 口
[sw2] int e0/0/1
[sw2-Ethernet0/0/1] port link-type trunk
[sw2-Ethernet0/0/1] port trunk allow-pass vlan 10 20 30

# access 口
[sw2] int e0/0/2
[sw2-Ethernet0/0/2] port link-type access
[sw2-Ethernet0/0/2] port default vlan 20

# hybrid 口
[sw2] int e0/0/3
[sw2-Ethernet0/0/3] port link-type hybrid
[sw2-Ethernet0/0/3] port hybrid pvid vlan 30
[sw2-Ethernet0/0/3] port hybrid untagged vlan 10 30
```

------

#### 3. 交换机 sw3 配置

```bash
<Huawei> sys
[Huawei] sysname sw3
[sw3] undo info-center enable
[sw3] vlan batch 10 20 30

# hybrid 配置
[sw3] int e0/0/1
[sw3-Ethernet0/0/1] port link-type hybrid
[sw3-Ethernet0/0/1] port hybrid pvid vlan 10
[sw3-Ethernet0/0/1] port hybrid untagged vlan 10 20 30

# trunk 端口配置
[sw3] int e0/0/2
[sw3-Ethernet0/0/2] port link-type trunk
[sw3-Ethernet0/0/2] port trunk allow-pass vlan 10 20 30

[sw3] int e0/0/3
[sw3-Ethernet0/0/3] port link-type trunk
[sw3-Ethernet0/0/3] port trunk allow-pass vlan 10 20 30
```

------

### 四、测试与验证

通过 PC 模拟主机分别连接到 VLAN 不同端口，设置 IP 地址在相同网段后进行互 ping 测试：

```bash
PC> ping 192.168.1.4

Reply from 192.168.1.4: bytes=32 time=110ms TTL=128
Reply from 192.168.1.4: bytes=32 time=93ms TTL=128
Reply from 192.168.1.4: bytes=32 time=78ms TTL=128
Reply from 192.168.1.4: bytes=32 time=78ms TTL=128
Reply from 192.168.1.4: bytes=32 time=31ms TTL=128
```

说明设备间 VLAN 通信成功，端口配置生效，VLAN 隔离和打标签机制均正常工作。

------

### 五、实验总结

- **Access端口**：只能属于一个 VLAN，常用于终端连接
- **Trunk端口**：支持多个 VLAN，打标签传输，适用于交换机互连
- **Hybrid端口**：灵活，可配置打/不打标签，适用于接无线AP、摄像头等设备

通过本次实验，深入理解了不同端口模式的使用场景及配置方法，掌握了 VLAN 的划分与通信配置，为日后实际网络部署打下了坚实基础。

------

如需生成 Word/PDF 版实验报告，也可以告诉我，我可以帮你排版。是否继续？
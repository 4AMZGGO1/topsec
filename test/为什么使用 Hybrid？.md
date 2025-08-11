

------

## 🧠 为什么使用 Hybrid？

在华为交换机中：

| 模式       | 功能                                                         |
| ---------- | ------------------------------------------------------------ |
| **Access** | 只能属于一个 VLAN，用于接入主机                              |
| **Trunk**  | 可属于多个 VLAN，主要用于交换机之间传递多个 VLAN 的数据      |
| **Hybrid** | 可属于多个 VLAN，**既可接主机，也可接交换机，支持灵活的 tag/untag 配置**，适合特殊场景 |

你当前的拓扑，核心是：

- **LSW1、LSW2 与 LSW3 之间要传递 VLAN10、20、30 数据**
- 使用 **Hybrid 模式传多个 VLAN 数据**
- 可控制哪些 VLAN 发送 tag / untag 数据，满足更精细化管理

------

## 📐 网络结构回顾（简化）

```
[PC2,PC5]      [PC3,PC4]
   |               |
 [LSW1]         [LSW2]
     \         /
      \       /
       [LSW3]（核心，三层交换）
          |
        [PC1]
```

------

## ✅ 配置目标

| 交换机             | 接口类型   | 配置内容                                     |
| ------------------ | ---------- | -------------------------------------------- |
| 所有下连 PC 接口   | Access     | 设置为 Access，绑定对应 VLAN                 |
| 上联交换机之间接口 | **Hybrid** | 允许 VLAN10、20、30 通过，tag/untag 可自定义 |

------

## 🔧 配置细节（华为 eNSP 示例）

### 🔹 核心交换机 LSW3

#### 1. VLAN & 三层接口配置

```bash
system-view
vlan batch 10 20 30

interface Vlanif10
 ip address 192.168.1.254 255.255.255.0

interface Vlanif20
 ip address 192.168.1.253 255.255.255.0

interface Vlanif30
 ip address 192.168.1.252 255.255.255.0
```

#### 2. 连接 PC1（Access）

```bash
interface GigabitEthernet0/0/1
 port link-type access
 port default vlan 10
```

#### 3. 连接 LSW1、LSW2 的 Hybrid 接口（G0/0/2，G0/0/3）

```bash
interface GigabitEthernet0/0/2  // to LSW1
 port link-type hybrid
 port hybrid tagged vlan 10 20 30
 port hybrid pvid vlan 10

interface GigabitEthernet0/0/3  // to LSW2
 port link-type hybrid
 port hybrid tagged vlan 10 20 30
 port hybrid pvid vlan 10
```

------

### 🔹 LSW1 配置（PC2/PC5）

#### 1. VLAN 创建

```bash
system-view
vlan batch 20 30
```

#### 2. 接口配置（Access）

```bash
interface Ethernet0/0/1  // PC2
 port link-type access
 port default vlan 20

interface Ethernet0/0/2  // PC5
 port link-type access
 port default vlan 30
```

#### 3. 上联 LSW3 的 Hybrid 接口（G0/0/1）

```bash
interface GigabitEthernet0/0/1
 port link-type hybrid
 port hybrid tagged vlan 10 20 30
 port hybrid pvid vlan 20
```

------

### 🔹 LSW2 配置（PC3/PC4）

#### 1. VLAN 创建

```bash
system-view
vlan batch 20 30
```

#### 2. 接口配置（Access）

```bash
interface Ethernet0/0/1  // PC3
 port link-type access
 port default vlan 30

interface Ethernet0/0/2  // PC4
 port link-type access
 port default vlan 20
```

#### 3. 上联 LSW3 的 Hybrid 接口（G0/0/1）

```bash
interface GigabitEthernet0/0/1
 port link-type hybrid
 port hybrid tagged vlan 10 20 30
 port hybrid pvid vlan 30
```

------

## 🖥️ PC 设置（在 eNSP 中配置）

| PC   | IP地址       | 子网掩码      | 网关          |
| ---- | ------------ | ------------- | ------------- |
| PC1  | 192.168.1.10 | 255.255.255.0 | 192.168.1.254 |
| PC2  | 192.168.1.1  | 255.255.255.0 | 192.168.1.253 |
| PC3  | 192.168.1.4  | 255.255.255.0 | 192.168.1.252 |
| PC4  | 192.168.1.3  | 255.255.255.0 | 192.168.1.253 |
| PC5  | 192.168.1.2  | 255.255.255.0 | 192.168.1.252 |

------

## ✅ 验证测试建议

1. **同 VLAN 测试**
   - PC3 ↔ PC5（VLAN30）✅
   - PC2 ↔ PC4（VLAN20）✅
2. **跨 VLAN 测试**
   - PC1 ↔ PC3、PC5 ✅（VLAN10 ↔ VLAN30）
   - PC1 ↔ PC2、PC4 ❌（VLAN10 ↔ VLAN20）

------

## 🔍 常见问题排查

| 问题             | 检查项                              |
| ---------------- | ----------------------------------- |
| VLANif 接口 Down | 检查是否该 VLAN 有 active 接口      |
| Ping 不通        | 检查 IP/网关、PVID、Hybrid tag 配置 |
| Hybrid 转发异常  | 确保 **三端口都配置了 tagged VLAN** |

------


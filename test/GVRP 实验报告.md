# **GVRP 实验报告**

## 一、实验目的

- 掌握 VLAN 的基本配置方法。
- 理解并掌握 GVRP（GARP VLAN Registration Protocol）动态 VLAN 注册协议的原理与配置方法。
- 实现交换机之间动态 VLAN 信息同步，实现 VLAN 自动创建。

------

## 二、实验拓扑

```
[LSW1] --- [LSW2] --- [LSW3]
```

- 连接链路：
  - LSW1 的 G0/0/1 ↔ LSW2 的 G0/0/1
  - LSW2 的 G0/0/2 ↔ LSW3 的 G0/0/1

------

## 三、实验设备

- 三台华为交换机（模拟或真实设备）
- 配置终端（Console、Telnet 或 SSH）

------

## 四、实验原理

GVRP 是一种基于 GARP（Generic Attribute Registration Protocol）协议的 VLAN 自动注册协议，主要作用是在支持 GVRP 的设备之间 **动态学习 VLAN 信息**，避免手动配置所有中间交换机。

GVRP 工作要求：

1. 所有相关端口必须为 **Trunk 模式**
2. 启用全局 GVRP 功能
3. 各端口配置 GVRP 注册类型（如：normal、fixed、forbidden）

------

## 五、实验步骤

### 步骤一：基础配置（LSW1、LSW2、LSW3）

```shell
<Huawei> system-view
[Huawei] sysname lswX
[lswX] undo info-center enable
```

### 步骤二：创建 VLAN（仅在边缘设备创建）

- 在 LSW1 上创建 VLAN 10、20、30、12、44、55：

```shell
[lsw1] vlan batch 10 20 30 12 44 55
```

- 在 LSW3 上创建 VLAN 10、20、30：

```shell
[lsw3] vlan batch 10 20 30
```

> 注：LSW2 不手动创建 VLAN，通过 GVRP 动态学习。

------

### 步骤三：配置 Trunk 和允许 VLAN

在三台交换机的连接端口配置 Trunk 模式，并允许所有 VLAN 通过：

```shell
[lswX]interface GigabitEthernet 0/0/Y
[lswX-GigabitEthernet0/0/Y] port link-type trunk
[lswX-GigabitEthernet0/0/Y] port trunk allow-pass vlan all
```

例如：

```shell
[lsw1]int g0/0/1
[lsw1-GigabitEthernet0/0/1] p l t
[lsw1-GigabitEthernet0/0/1] p t a v all
```

------

### 步骤四：启用 GVRP 全局和端口功能

- 启用全局 GVRP 功能：

```shell
[lswX] gvrp
```

- 配置接口启用 GVRP 并设置注册方式为 normal（或 fixed）：

```shell
[lswX]interface GigabitEthernet 0/0/Y
[lswX-GigabitEthernet0/0/Y] gvrp
[lswX-GigabitEthernet0/0/Y] gvrp registration normal
```

------

### 步骤五：查看 VLAN 传播情况

在中间交换机 LSW2 上查看 VLAN 表：

```shell
[lsw2] display vlan
```

> 初始只有 VLAN 1，启用 GVRP 并配置 trunk 后，自动学习到了 VLAN 10、20、30、12、44、55（状态为 dynamic）

------

## 六、实验现象与验证

- **LSW1 和 LSW3**：创建了静态 VLAN。
- **LSW2**：通过 GVRP 动态学习到了 VLAN 10、20、30、12、44、55。
- GVRP 状态下，三台交换机的 VLAN 信息保持同步，实现自动化传播。

------

## 七、总结与分析

- 成功通过 GVRP 实现了 VLAN 的动态注册与传播。
- 减少了中间交换机配置的复杂度，提升了网络部署效率。
- 实验中注意事项：
  - Trunk 模式必须配置
  - GVRP 需手动启用
  - VLAN ID 不能冲突，否则可能造成学习失败

------

## 八、附录：常用命令汇总

| 命令                             | 作用               |
| -------------------------------- | ------------------ |
| `vlan batch <id>`                | 批量创建 VLAN      |
| `port link-type trunk`           | 设置端口为 Trunk   |
| `port trunk allow-pass vlan all` | 允许所有 VLAN 通过 |
| `gvrp`                           | 启用 GVRP 全局功能 |
| `gvrp registration normal`       | 设置端口注册方式   |
| `display vlan`                   | 查看 VLAN 信息     |

------


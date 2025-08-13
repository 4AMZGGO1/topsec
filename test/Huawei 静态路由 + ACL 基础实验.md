#  Huawei 静态路由 + ACL 基础实验

## 一、实验拓扑

```
PC1(192.168.1.2) ----|
                    |----[SW]----[R1]----[R2]---- PC3(192.168.3.X)
PC2(192.168.1.3) ----|         G0/0/0  G0/0/1    G0/0/0  G0/0/1
                                  |      |         |       |
                                  |      |         |       |
                             192.168.1.1 10.1.1.1  10.1.1.2 192.168.2.1 / .3.1
```

- R1 左侧连接 PC1、PC2 所在的交换机，网段为 `192.168.1.0/24`
- R1 与 R2 之间为互联网段 `10.1.1.0/24`
- R2 向右连接两个网段：`192.168.2.0/24` 和 `192.168.3.0/24`

------

## 二、设备配置

### 1. R1 配置

```bash
<Huawei> system-view
[Huawei] sysname R1

[R1]int g0/0/0
[R1-GigabitEthernet0/0/0]ip address 192.168.1.1 255.255.255.0

[R1]int g0/0/1
[R1-GigabitEthernet0/0/1]ip address 10.1.1.1 255.0.0.0

# 添加静态路由指向 R2
[R1]ip route-static 192.168.2.0 255.255.255.0 10.1.1.2
[R1]ip route-static 192.168.3.0 255.255.255.0 10.1.1.2
```

------

### 2. R2 配置

```bash
<Huawei> system-view
[Huawei] sysname R2

[R2]int g0/0/0
[R2-GigabitEthernet0/0/0]ip address 10.1.1.2 255.255.255.0

[R2]int g0/0/1
[R2-GigabitEthernet0/0/1]ip address 192.168.2.1 255.255.255.0

[R2]int g0/0/2
[R2-GigabitEthernet0/0/2]ip address 192.168.3.1 255.255.255.0

# 配置返回路径回R1
[R2]ip route-static 192.168.1.0 255.255.255.0 10.1.1.1
```

------

## 三、ACL 配置：限制某主机访问某网段

> 目标：允许 PC1（192.168.1.2）访问网络，其它拒绝

### 步骤如下：

```bash
# 创建基础ACL，编号2000
[R2]acl 2000
[R2-acl-basic-2000]rule permit source 192.168.1.2 0.0.0.0
[R2-acl-basic-2000]rule deny source any

# 应用到接口g0/0/1出方向
[R2]int g0/0/1
[R2-GigabitEthernet0/0/1]traffic-filter outbound acl 2000
```

> ⚠️ `0.0.0.0` 是主机位掩码，表示精确匹配 `192.168.1.2`
>  ⚠️ `outbound` 方向表示从 R2 发出的流量进行限制，适用于 PC1 访问 192.168.2.0

------

## 四、连通性测试建议

在设备连接正常后，建议从 PC1 和 PC2 分别执行如下测试：

```bash
# PC1:
ping 192.168.2.1     # 成功
# PC2:
ping 192.168.2.1     # 应失败
```

------

![image-20250805105836763](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250805105836763.png)
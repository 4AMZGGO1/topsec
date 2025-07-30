静态路由表配置

------

## 📌 网络拓扑结构图（ASCII 图）

```
                    +-----------+
                    |   PC3     |
                    |192.168.1.100
                    +-----------+
                          |
                          |192.168.1.0/24
                     [R6]E0/0/1
                          |
                          |11.1.1.0/28
                     [R1]E0/0/0
                          |
                          |12.1.1.0/28
                     [R7]E0/0/0
                          |
        -------------------------------------
        |                                   |
 13.1.1.0/28                        172.16.10.0/24
        |                                   |
     [R2]E0/0/0                         G0/0/0[R7]
        |                                   |
 23.1.1.0/28                        +---------------+
        |                          |   Switch      |
     [R3]E0/0/0                    +---------------+
                                         |
                                     +--------+
                                     |  PC1   |
                                     |172.16.10.100
                                     +--------+
```

------

## 📋 IP地址配置

### 🔹 R7

```bash
[R7]int g0/0/0
[R7-GigabitEthernet0/0/0]ip address 172.16.10.254 255.255.255.0

[R7]int e0/0/0
[R7-Ethernet0/0/0]ip address 12.1.1.2 255.255.255.240

[R7]int e0/0/1
[R7-Ethernet0/0/1]ip address 13.1.1.1 255.255.255.240
```

------

### 🔹 R1

```bash
[R1]int e0/0/1
[R1-Ethernet0/0/1]ip address 12.1.1.1 255.255.255.240

[R1]int e0/0/0
[R1-Ethernet0/0/0]ip address 11.1.1.2 255.255.255.240
```

------

### 🔹 R6

```bash
[R6]int e0/0/0
[R6-Ethernet0/0/0]ip address 11.1.1.1 255.255.255.240

[R6]int e0/0/1
[R6-Ethernet0/0/1]ip address 192.168.1.254 255.255.255.0
```

------

### 🔹 R2

```bash
[R2]int e0/0/0
[R2-Ethernet0/0/0]ip address 13.1.1.2 255.255.255.240

[R2]int e0/0/1
[R2-Ethernet0/0/1]ip address 23.1.1.1 255.255.255.240
```

------

### 🔹 R3

```bash
[R3]int e0/0/0
[R3-Ethernet0/0/0]ip address 23.1.1.2 255.255.255.240
```

------

## 📦 静态路由配置

### ✅ **R1**

```bash
[R1]ip route-static 23.1.1.0 28 12.1.1.2
[R1]ip route-static 192.168.1.0 24 11.1.1.1
[R1]ip route-static 13.1.1.0 28 12.1.1.2
[R1]ip route-static 172.16.10.0 24 12.1.1.2
```

------

### ✅ **R2**

```bash
[R2]ip route-static 172.16.10.0 24 13.1.1.1
[R2]ip route-static 192.168.1.0 24 13.1.1.1
[R2]ip route-static 11.1.1.0 28 13.1.1.1
[R2]ip route-static 12.1.1.0 28 13.1.1.1
```

------

### ✅ **R3**

```bash
[R3]ip route-static 172.16.10.0 24 23.1.1.1
[R3]ip route-static 12.1.1.0 28 23.1.1.1
[R3]ip route-static 192.168.1.0 24 23.1.1.1
[R3]ip route-static 11.1.1.0 28 23.1.1.1
[R3]ip route-static 13.1.1.0 28 23.1.1.1
```

------

### ✅ **R6**

```bash
[R6]ip route-static 12.1.1.0 28 11.1.1.2
[R6]ip route-static 13.1.1.0 28 11.1.1.2
[R6]ip route-static 23.1.1.0 28 11.1.1.2
[R6]ip route-static 172.16.10.0 24 11.1.1.2
```

------

### ✅ **R7**

```bash
[R7]ip route-static 11.1.1.0 28 12.1.1.1
[R7]ip route-static 192.168.1.0 24 12.1.1.1
[R7]ip route-static 23.1.1.0 28 13.1.1.2
```

------

## ✅ 联通性测试结果

- ✅ PC3 成功 teacert通：
  - PC1（172.16.10.100）
  - R3（23.1.1.2）

📷 如下图所示：

> ![image-20250730194541470](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250730194541470.png)
>
> 📍 路由路径完全正确：**PC3 → R6 → R1 → R7 → PC1**
>
> ![image-20250730194706918](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250730194706918.png)
>
> ✅ PC3 → R3 的路径为：
>  **PC3 → R6 → R1 → R7 → R2 → R3**
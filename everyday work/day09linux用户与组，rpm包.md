# ✅ 作业一：用户和组管理操作

### 1. 建立名为 `top2022` 的组，组ID为 2000

```bash
groupadd -g 2000 top2022
```

- `-g 2000`：指定 GID
- `top2022`：组名称

![image-20250718171738529](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718171738529.png)

------

### 2. 创建用户 `allen`，UID 为 1500，基本组为 `top2022`，并添加至附加组 `top2023`

```bash
groupadd top2023
useradd -u 1500 -g top2022 allen
usermod -aG top2023 allen
```

- `-u` 指定 UID
- `-g` 设置基本组
- `-aG` 添加附加组

![image-20250718171822944](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718171822944.png)

------

### 3. 设置 `allen` 的密码并查看密码状态

```bash
passwd allen
passwd -S allen
```

- `passwd`：交互设置用户密码
- `-S`：查看密码状态（是否锁定/生效等）

![image-20250718171850626](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718171850626.png)

------

### 4. 锁定/解锁 `allen` 用户账号

```bash
passwd -l allen    # 锁定
passwd -u allen    # 解锁
```

![image-20250718171910439](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718171910439.png)

------

### 5. 设置密码有效期90天，账户失效时间为本月底（2025-07-31）

```bash
chage -M 90 allen
chage -E 2025-07-31 allen
```

- `-M` 设置最大密码使用天数
- `-E` 设置账户过期日期

![image-20250718171950016](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718171950016.png)

------

### 6. 创建 `topuser` 用户，UID 为 200，不能登录、无家目录

```bash
useradd -u 200 -M -s /sbin/nologin topuser
```

- `-M`：不创建 home 目录
- `-s /sbin/nologin`：禁用登录

![image-20250718172120535](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718172120535.png)

------

# ✅ 作业二：系统用户配置文件格式说明

## 1. `/etc/passwd` 文件格式

```
用户名:密码占位符:UID:GID:用户描述:家目录:Shell
```

示例：

```
root:x:0:0:root:/root:/bin/bash
```

## 2. `/etc/shadow` 文件格式

```
用户名:加密密码:最后改密时间:最小天数:最大天数:提前提醒:非活跃期:过期时间:保留
```

示例：

```
root:$6$xxx$xxx...:18262:7:90:7:30:0:
```

## 3. `/etc/group` 文件格式

```
组名:密码占位符:GID:附加组成员列表
```

示例：

```
wheel:x:10:root,allen
```

------

# ✅ 作业三：使用本地光盘挂载 YUM 仓库

## 1. 挂载光盘

```bash
sudo mkdir -p /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom
# 或使用 /dev/sr0：
# sudo mount /dev/sr0 /mnt/cdrom
```

------

## 2. 配置本地 YUM 仓库

编辑配置文件：

```bash
cd /etc/yum.repos.d/
sudo vi local.repo
```

添加内容：

```ini
[local-media]
name=Local Media Repo
baseurl=file:///mnt/cdrom
enabled=1
gpgcheck=0
```

> 若开启 GPG 校验，请添加 `gpgkey=...` 项。

![image-20250720162108580](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250720162108580.png)

------

## 3. 清缓存、建立缓存

```bash
sudo yum clean all
sudo yum makecache
```

![image-20250720162600236](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250720162600236.png)

------

## 4. 查询和安装 `lftp`

### 查询是否安装：

```bash
rpm -qa | grep lftp
```

### 查看 RPM 包信息：

```bash
rpm -qpi /mnt/cdrom/Packages/lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

### 查看安装后生成文件：

```bash
rpm -qpl /mnt/cdrom/Packages/lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

### 安装 RPM：

```bash
sudo rpm -ivh /mnt/cdrom/Packages/lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

### 用 YUM 安装：

```bash
sudo yum --disablerepo="*" --enablerepo="local-media" install lftp -y
```

![image-20250720162713191](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250720162713191.png)

------

## 5. 解决 lftp 中文乱码问题

```bash
set ftp:charset gbk
```

![image-20250718193545458](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718193545458.png)

------

# ⚠️ 作业四（选做）：伪造 UID=0 的账户（仅限学习环境）

## 步骤 1：编辑 `/etc/passwd`

备份并编辑：

```bash
cp /etc/passwd /etc/passwd.bak
vim /etc/passwd
```

添加：

```
fakeroot:x:0:0:Fake Root:/root:/bin/bash
```

![image-20250718193928750](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718193928750.png)

------

## 步骤 2：编辑 `/etc/shadow`

```bash
cp /etc/shadow /etc/shadow.bak
vim /etc/shadow
```

添加：

```
fakeroot:$6$xxx$hashhashhash...:19300:0:99999:7:::
```

验证：

```bash
grep fakeroot /etc/passwd
grep fakeroot /etc/shadow
```

![image-20250718195646413](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718195646413.png)

------

## 步骤 3：登录测试

```bash
su - fakeroot
whoami
```

应输出：

```
root
```

![image-20250718195703134](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718195703134.png)

------

## 检查是否有多个 UID=0 用户

```bash
awk -F: '$3 == 0' /etc/passwd
```

示例输出：

```
root:x:0:0:root:/root:/bin/bash
fakeroot:x:0:0:Fake Root:/root:/bin/bash
```

![image-20250718195740267](file:///C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20250718195740267.png)
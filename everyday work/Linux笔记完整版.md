# Linux 基础命令笔记（整理版）

## 一、命令提示符说明

```bash
[root@localhost ~]#
[当前用户名@主机名 当前所在路径]#
# 表示当前用户为超级用户（root）
$ 表示当前用户为普通用户
~ 代表当前用户的家目录
```

------

## 二、目录结构与常用命令

| 命令                    | 含义             |
| ----------------------- | ---------------- |
| `pwd`                   | 显示当前目录路径 |
| `ls`                    | 显示当前目录内容 |
| `cd`                    | 切换目录         |
| `clear` 或 `Ctrl+L`     | 清屏             |
| `Ctrl+-` `Ctrl+Shift++` | 缩放字体         |

### Linux 主要目录说明

| 目录                 | 说明                                          |
| -------------------- | --------------------------------------------- |
| `/`                  | 根目录，所有目录的起点                        |
| `/root`              | 管理员的家目录                                |
| `/home`              | 普通用户的家目录                              |
| `/tmp`               | 临时目录，所有用户可写                        |
| `/dev`               | 设备文件                                      |
| `/etc`               | 系统配置文件目录（如 `/etc/hosts`、DHCP配置） |
| `/var`               | 可变数据目录，如日志、邮件、ftp等             |
| `/lib` `/lib64`      | 系统库文件                                    |
| `/bin`               | 常用二进制命令，所有用户可执行                |
| `/sbin`              | 管理类命令，仅 root 可用                      |
| `/usr`               | 用户安装的软件目录                            |
| `/boot`              | 启动相关文件（内核、驱动）                    |
| `/proc`              | 内核与进程虚拟文件系统                        |
| `/opt`               | 第三方软件目录                                |
| `/mnt`               | 挂载点                                        |
| `/media`             | （已弃用）自动挂载设备目录                    |
| `/run` `/sys` `/srv` | 其他系统服务相关目录                          |

------

## 三、路径与文件操作

### 路径概念

- **绝对路径**：从根目录 `/` 开始的完整路径，如 `/tmp/test.txt`
- **相对路径**：相对于当前目录的路径，如进入 `/tmp` 后：`cat test.txt`

### 文件颜色说明（按 `ls` 输出颜色）

| 颜色     | 类型                       |
| -------- | -------------------------- |
| 黑色     | 普通文件（ASCII文本文档）  |
| 蓝色     | 目录                       |
| 红色     | 压缩文件                   |
| 绿色     | 可执行文件                 |
| 浅蓝     | 符号链接                   |
| 紫色     | 图片或模块文件             |
| 黑底黄字 | 设备文件（如 `/dev/null`） |

------

## 四、实践练习命令

### 练习 1：在 `/tmp` 中创建目录和文件

```bash
mkdir /tmp/topclass1
touch /tmp/topclass1/topuser.txt
echo "zyf" > /tmp/topclass1/topuser.txt
date >> /tmp/topclass1/topuser.txt
```

### 删除文件与目录

```bash
rm -rf /tmp/topclass1
```

### 练习 2：复制并移动目录

```bash
# 复制目录
cp -r /tmp/topclass1 /opt/

# 删除原目录
rm -rf /tmp/topclass1

# 移动目录回 /tmp
mv /opt/topclass1 /tmp/
```

### 练习 3：创建符号链接（桌面快捷方式）

```bash
ln -s /tmp/topclass1/topuser.txt /root/Desktop/topuser.lnk
```

> ⚠️ 链接源路径必须使用**绝对路径**。

------

## 五、命令格式与帮助文档

### 命令格式：

```bash
命令 [选项] [文件或目录]
```

### 使用 `man` 查看帮助

```bash
man ls
```

### man 查看技巧：

- `/关键字`：搜索关键字
- `n`：向下查找
- `N`：向上查找
- `q`：退出

------

## 六、ls 命令常用选项

| 命令            | 说明                             |
| --------------- | -------------------------------- |
| `ls -l`         | 列出详细信息                     |
| `ls -a`         | 显示所有（包括隐藏文件）         |
| `ls -lh`        | 人性化显示大小                   |
| `ls -R`         | 递归显示子目录内容               |
| `ls -ld 目录名` | 显示目录本身信息（不是内部内容） |

------

## 七、cp 与 rm 命令参数说明（man 查询结果）

```bash
cp -r      # 递归复制整个目录
rm -r      # 递归删除目录
rm -f      # 强制删除（忽略不存在的文件，不提示）
```

------

## 八、查看文件内容命令

| 命令   | 功能                          |
| ------ | ----------------------------- |
| `cat`  | 一次性查看整个文件            |
| `head` | 查看前 10 行                  |
| `tail` | 查看后 10 行                  |
| `more` | 分页查看                      |
| `less` | 逐页/逐行查看（支持上下翻页） |

### 实时查看日志文件

```bash
tail -f /var/log/secure
```

------

## 九、网络与端口查看

### 查看端口监听状态

```bash
netstat -antpl
```

- `-a`：显示所有连接和监听端口
- `-n`：数字方式显示地址和端口
- `-t`：显示 TCP 协议连接
- `-p`：显示对应的进程名称
- `-l`：仅显示监听状态端口

> ❓还有其他查看端口命令如：
>  `ss -tunlp`、`lsof -i:端口号`

------

## 十、远程登录与日志查看

### 使用 SSH 登录 Linux

```bash
ssh root@192.168.133.131
```

### 切换用户与退出

```bash
su - allen   # 切换为 allen 用户
exit         # 退出当前 shell
```

### 登录失败查看日志

```bash
tail -f /var/log/secure
```

> 登录失败、用户切换等信息都记录在该日志文件中。

------

以下是你提供内容的整理与补充，采用了清晰的结构与 Markdown 格式，方便查阅和继续学习。内容涉及日期命令、目录创建、链接类型、文件内容查看、统计与过滤、查找命令等实用操作。

------

# Linux 常用命令与技巧（二）

## 一、日期与时间格式化

```bash
date +%F
```

- 输出格式：`YYYY-MM-DD`
- `man date` 可查看更多格式化选项，如：
  - `%F`：完整日期（等同于 `%Y-%m-%d`）
  - `%T`：时间（等同于 `%H:%M:%S`）

------

## 二、目录创建

```bash
mkdir -p /path/to/dir
```

- `-p`：创建多级目录时不会报错，即使中间目录不存在也会自动创建。
- 如果目录已存在，不会报错。

------

## 三、链接（Link）

### 1. 硬链接（Hard Link）

```bash
ln 原文件 硬链接路径
```

- 只能对**文件**创建。
- 与源文件共享 inode（本质上是“同一个文件”）。
- **删除原文件不影响硬链接的使用**。
- 不可对目录建立硬链接（除非使用特殊权限）。

### 2. 符号链接（软链接 Symbolic Link）

```bash
ln -s 原路径 链接路径
```

- 可链接文件或目录。
- 类似 Windows 快捷方式，保存的是路径。
- **源文件删除，链接失效（变为“死链接”）**。

------

## 四、查看文件内容

| 命令        | 用途                    |
| ----------- | ----------------------- |
| `cat`       | 显示整个文件内容        |
| `cat -n`    | 带行号显示              |
| `head -n 6` | 显示前6行               |
| `tail -n 6` | 显示后6行               |
| `more`      | 分页显示（空格翻页）    |
| `less`      | 可上下滚动查看（q退出） |

------

## 五、磁盘与空间占用

### 查看磁盘分区与使用情况

```bash
df -Th
```

- `-T` 显示文件系统类型
- `-h` 人类可读单位（KB/MB/GB）

### 查看目录大小（当前目录下）

```bash
du -sh *
```

- `-s` 汇总每个子目录总大小
- `-h` 人类可读单位

------

## 六、文件统计命令

### 统计文件基本信息

```bash
wc /etc/passwd
```

输出示例：`43 86 2240 /etc/passwd`
 分别表示：**行数、单词数、字符数**

### 只查看行数

```bash
wc -l /etc/passwd
```

------

## 七、文本搜索与过滤（grep）

### 基本用法

```bash
grep "关键字" 文件
```

### 常见选项

| 命令      | 说明               |
| --------- | ------------------ |
| `-n`      | 显示匹配的行号     |
| `^字符串` | 匹配以该字符串开头 |
| `字符串$` | 匹配以该字符串结尾 |
| `-v`      | 反向匹配（不包含） |
| `-i`      | 忽略大小写         |

### 实例

- 判断是否存在 root 用户：

```bash
grep "^root" /etc/passwd
```

- 查看可登录账户（默认 shell 为 bash）：

```bash
grep "bash$" /etc/passwd
```

- 查看**不可登录**账户：

```bash
grep -v "bash$" /etc/passwd
```

------

## 八、日志攻击信息过滤练习（重点）

### 1. 查看所有 Failed 登录记录

```bash
grep "Failed password" /var/log/secure
```

### 2. 显示行号

```bash
grep -n "Failed password" /var/log/secure
```

### 3. 查看记录数量

```bash
grep "Failed password" /var/log/secure | wc -l
```

### 4. 提取攻击来源 IP（假设第11字段为 IP）

```bash
grep "Failed password" /var/log/secure | awk '{print $11}'
```

### 5. 排序并去重

```bash
grep "Failed password" /var/log/secure | awk '{print $11}' | sort | uniq
```

### 6. 统计每个 IP 攻击次数

```bash
grep "Failed password" /var/log/secure | awk '{print $11}' | sort | uniq -c
```

------

## 九、find 查找命令（重点）

> 与 `grep` 针对文件内容不同，`find` 是查找文件或目录本身。

### 基本语法

```bash
find [查找路径] [匹配条件]
```

### 示例

#### 1. 查找系统中包含 `passwd` 的文件或目录

```bash
find / -name "*passwd*"
```

#### 2. 查找 `/etc` 目录下扩展名为 `.conf` 的文件

```bash
find /etc -name "*.conf"
```

#### 3. 查找大小大于 100M 的文件

```bash
find / -type f -size +100M
```

#### 4. 查找最近7天内修改的文件

```bash
find / -type f -mtime -7
```

------

## 十、其他命令建议

| 命令              | 用途                            |
| ----------------- | ------------------------------- |
| `ss -tunlp`       | 更快替代 `netstat` 查看端口占用 |
| `lsof -i :端口号` | 查看指定端口被哪个进程占用      |
| `history`         | 查看命令历史                    |
| `who` / `w`       | 查看当前在线用户                |

------

你这段内容很实用，以下是我根据你的笔记内容整理和补充的 **`find` 命令讲解**，包括 `-exec` 的使用、逻辑运算符（如 `-a`、`-o`）、以及如何替代管道等。已整理为 Markdown 结构，便于复习使用。

------



# Linux `find` 命令详解与实用技巧

## 一、基本语法

```bash
find [查找路径] [匹配条件]
```

------

## 二、常用示例

### 1. 查找系统中名称为 `passwd` 的文件或目录

```bash
find / -name passwd
```

> 注意：此命令会同时查找**文件和目录**

------

### 2. 只查找文件（file）

```bash
find / -name passwd -a -type f
```

### 3. 只查找目录（directory）

```bash
find / -name passwd -a -type d
```

------

## 三、逻辑运算符说明（可用 `man find` 查看）

| 逻辑符 | 含义                                      | 示例                                 |
| ------ | ----------------------------------------- | ------------------------------------ |
| `-a`   | **与（AND）**，两个条件都满足（默认逻辑） | `-name xxx -a -type f`               |
| `-o`   | **或（OR）**，只需满足一个条件            | `-name aaa -o -name bbb`             |
| `!`    | 非（NOT）                                 | `! -name passwd` 表示名称不是 passwd |

------

## 四、`-exec` 进行二次处理

`find` 不能直接通过 `|` 管道传递给 `ls` 或其他命令，但可以使用 `-exec` 来实现类似效果。

### 正确方式：使用 `-exec`

```bash
find / -name passwd -exec ls -l '{}' \;
```

> 说明：
>
> - `{}` 表示 `find` 查找到的每一个文件/目录的占位符；
> - `\;` 表示命令结束（必须有转义符）；
> - 等效于对每个查找到的项执行一次 `ls -l`。

------

## 五、补充：批量处理多个文件（`+`）

```bash
find / -name passwd -exec ls -l '{}' +
```

> 与 `\;` 的区别是：`+` 会**将多个结果一次性传入 `ls -l`**，效率更高。

------

## 六、更多实用 find 示例

### 查找指定目录下所有 `.conf` 配置文件

```bash
find /etc -name "*.conf"
```

### 查找大小大于 100MB 的文件

```bash
find / -type f -size +100M
```

### 查找 7 天内修改过的文件

```bash
find / -type f -mtime -7
```

### 查找当前用户拥有的文件

```bash
find /home -user your_username
```

------

## 七、常见问题汇总

| 问题                                      | 解决方法                    |
| ----------------------------------------- | --------------------------- |
| 想用 `find` 查找后 `ls -l` 查看详细信息？ | 用 `-exec ls -l '{}' \;`    |
| 想对结果统一处理？                        | 使用 `-exec` 或搭配 `xargs` |
| `                                         | ls -l` 无效？               |
| 想要更高效处理？                          | 用 `-exec ... +` 替代 `\;`  |

------

以下是你这部分内容的整理与补充，涵盖了 `find` 查找、`dd` 创建大文件、压缩与解压、`tar` 打包归档，以及源码安装与封装软件包安装等，内容系统完整，适合用于日常运维操作与复习使用。

------

# Linux 命令实用笔记（三）

------

## 一、查找大文件

### 1. 查找 `/boot` 目录中大于 3M 小于 10M 的文件：

```bash
find /boot -size +3M -a -size -10M
```

- `+3M`：大于 3MB
- `-10M`：小于 10MB
- `-a`：逻辑与（AND）

------

## 二、使用 `dd` 创建大文件

### 创建一个 100MB 的二进制文件 `bigfile`，内容为 0：

```bash
dd if=/dev/zero of=/tmp/bigfile bs=1M count=100
```

- `if=`：输入文件（这里是 /dev/zero，持续输出 0）
- `of=`：输出文件路径
- `bs=1M`：每次写入块大小为 1MB
- `count=100`：写入 100 个块（总共 100MB）

------

## 三、压缩与解压缩（针对文件）

### 压缩

```bash
gzip filename      # 生成 filename.gz
bzip2 filename     # 生成 filename.bz2
```

### 解压缩

```bash
gunzip filename.gz
bunzip2 filename.bz2
```

------

## 四、打包与归档（tar）

### 1. 打包 `/tmp/topclass1` 目录，生成 `.tar` 文件并放置桌面：

```bash
tar -cf /root/Desktop/topclass1.tar /tmp/topclass1
```

- `-c`：创建归档
- `-f`：指定归档文件（必须紧跟文件名）

### 2. 对打包文件进行压缩

```bash
# gzip 压缩
gzip /root/Desktop/topclass1.tar

# bzip2 压缩
bzip2 /root/Desktop/topclass1.tar
```

> 最终生成 `.tar.gz` 或 `.tar.bz2` 文件。

------

## 五、解压缩与解包

### 解压 `.gz` 和 `.bz2`

```bash
gunzip topclass1.tar.gz
bunzip2 topclass1.tar.bz2
```

### 解包 `.tar` 文件到指定目录（例如 /opt）

```bash
tar -xf /root/Desktop/topclass1.tar -C /opt
```

------

### 打包 + 压缩 一步完成

| 压缩格式   | 命令示例                                                  |
| ---------- | --------------------------------------------------------- |
| `.tar.gz`  | `tar -zcf /root/Desktop/topclass1.tar.gz /tmp/topclass1`  |
| `.tar.bz2` | `tar -jcf /root/Desktop/topclass1.tar.bz2 /tmp/topclass1` |

### 解压 `.tar.gz` `.tar.bz2` 到指定目录

```bash
tar -zxf topclass1.tar.gz -C /opt
tar -jxf topclass1.tar.bz2 -C /opt
```

------

## 六、Linux 软件安装方式

### 方式一：**源码安装**

特点：灵活可控，但安装过程复杂

### 1. 下载并解压源码包

```bash
tar -zxf httpd-xxx.tar.gz
cd httpd-xxx
```

### 2. 查看安装说明

```bash
less INSTALL
./configure --help
```

### 3. 配置安装目录

```bash
./configure --prefix=/usr/local/webserver
```

> 检查环境依赖与安装选项

### 4. 编译源码

```bash
make
```

### 5. 安装

```bash
make install
```

### 6. 启动与关闭

视具体软件文档说明，一般在 `/usr/local/webserver/bin/` 中。

------

### 方式二：**封装包安装（推荐）**

#### Debian/Ubuntu 系统（`.deb` 包）

```bash
sudo dpkg -i linuxqq_2.0.0-b2-1089_amd64.deb
```

#### RedHat/CentOS 系统（`.rpm` 包）

```bash
sudo rpm -ivh package-name.rpm
```

------

## 七、总结：源码 vs 封装包

| 安装方式   | 优点                   | 缺点                     |
| ---------- | ---------------------- | ------------------------ |
| 源码安装   | 灵活、可定制、更新及时 | 操作复杂、需手动解决依赖 |
| 封装包安装 | 快速、简单             | 依赖预设、可定制性差     |

------

以下是你这部分关于 **Linux 软件安装、包管理、用户与组管理** 的完整整理和补充内容，采用清晰的 Markdown 结构，便于系统学习和复习。

------

# Linux 系统管理笔记（四）

------

## 一、RPM 包管理

### 1. 查看是否安装过某个软件包

```bash
rpm -qa | grep vim           # 检查是否安装 vim
rpm -qa | wc -l              # 查看已安装包的总数量
ls | wc -l                   # 当前目录下的文件数
```

------

### 2. 查看软件包说明

```bash
rpm -qpi lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

------

### 3. 查看软件包安装后文件路径

```bash
rpm -qpl lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

------

### 4. 安装 RPM 包

```bash
rpm -ivh lftp-4.4.8-8.el7_3.2.x86_64.rpm
```

- `-i`：安装
- `-v`：显示详细信息
- `-h`：显示安装进度条（#）

------

### 5. 编码乱码问题（如 lftp 中文乱码）

- 编辑配置文件：

```bash
vi /etc/lftp.conf
```

- 添加内容：

```conf
set charset utf-8
```

------

### 6. 卸载软件包

#### 通过文件查找所属包：

```bash
rpm -qf /usr/bin/lftp
```

#### 卸载软件：

```bash
rpm -e lftp
```

> ⚠️ 如果存在依赖关系（如 `vim-common`），需先卸载依赖的上层包。

------

## 二、YUM 软件管理（自动解决依赖）

### 配置路径：

```bash
/etc/yum.repos.d/
```

------

### 挂载光盘配置本地 yum 源

编辑或新建 `/etc/yum.repos.d/local.repo`：

```ini
[c7-media]
name=CentOS-$releasever - Media
baseurl=file:///mnt/cdrom
enabled=1
gpgcheck=0
```

> `baseurl` 指向挂载目录路径
>  `gpgcheck=0` 关闭 GPG 校验

------

### 常用命令：

```bash
yum clean all        # 清理缓存
yum makecache        # 重建缓存
yum install httpd    # 安装 httpd
yum remove httpd     # 卸载 httpd
```

------

## 三、练习任务建议：

1. RPM 包的安装、查看、卸载练习
2. lftp 字符集乱码处理
3. Vim 编辑器常规练习
4. CentOS/Kali 网络 YUM 源配置及软件更新

------

## 四、用户与组管理

### 用户类型

| 类型         | UID 范围        | 说明                             |
| ------------ | --------------- | -------------------------------- |
| 超级用户     | 0               | root 用户                        |
| 普通用户     | ≥1000（CentOS） | 可登录，有家目录                 |
| 系统服务用户 | 1–999           | 不可登录，无家目录，后台服务使用 |

------

### 三大关键文件

#### `/etc/passwd`

```bash
root:x:0:0:root:/root:/bin/bash
```

字段解释：

| 字段序号 | 含义                   |
| -------- | ---------------------- |
| 1        | 用户名                 |
| 2        | 占位符（以前用于密码） |
| 3        | UID                    |
| 4        | GID                    |
| 5        | 注释说明               |
| 6        | 家目录                 |
| 7        | 默认 shell（解释器）   |

> **如果直接伪造格式添加用户？**
>  不建议手动编辑 `/etc/passwd`，应使用 `useradd`、`usermod` 命令。否则缺少影子密码文件 `/etc/shadow` 对应信息，将导致无法登录或系统不识别。

------

#### `/etc/shadow`

```bash
allen:$6$NKiIdkd5k94tho1q$J3DRh2KYU...::0:99999:7:::
```

字段说明：

| 字段 | 含义                                   |
| ---- | -------------------------------------- |
| 1    | 用户名                                 |
| 2    | 密码密文（含加密算法标记）             |
| 3    | 最后修改密码的日期（从 1970 起的天数） |
| 4    | 最短密码使用天数                       |
| 5    | 最长使用天数                           |
| 6    | 密码过期前提示天数                     |
| 7    | 密码失效宽限天数                       |
| 8    | 账户失效日期                           |

##### 密码加密验证方式（Python 模拟）：

```python
import crypt
crypt.crypt('123456', '$6$NKiIdkd5k94tho1q')
```

> `$6$` 表示 SHA-512 加密算法

------

#### `/etc/group`

组成员管理命令：

```bash
gpasswd -a allen root     # 把 allen 加入 root 组
gpasswd -d allen root     # 把 allen 从 root 组移除
```

------

### 添加用户与组练习

#### 1. 创建组 top2022，GID 为 2000

```bash
groupadd -g 2000 top2022
```

#### 2. 创建组 top2023，再添加用户 allon：

```bash
groupadd top2023
useradd allon -u 1500 -g top2022 -G top2023
```

> `-g` 指定主组，`-G` 指定附加组

#### 3. 为用户设置密码：

```bash
passwd allon
```

输入两次密码 `123.com`

#### 4. 删除用户

```bash
userdel allon
```

------

# 7.22上

------

# Linux 权限与提权实验总结

## 1. 权限基础

| 权限字符 | 说明            | 文件作用 | 目录作用       |
| -------- | --------------- | -------- | -------------- |
| `r`      | 读取（read）    | 查看内容 | 列出目录内容   |
| `w`      | 写入（write）   | 修改内容 | 创建、删除文件 |
| `x`      | 执行（execute） | 运行文件 | 进入目录       |

> **注意：** `w` 权限对目录来说很敏感，意味着有删除该目录中文件的权限。

------

## 2. 权限实例分析

示例：

```bash
ll -d top2109 top2109dir/
```

假设用户 `tom` 和 `jerry` 都加入了 `root` 组：

- `top2109` 是文件，`top2109dir/` 是目录。
- `tom`：只有读权限（不可写、不可执行）
- `jerry`：读 + 写权限（不可执行）

------

## 3. 权限修改命令（chmod）

- 修改组权限：
   `chmod g+w,o-r top2109`
- 将组权限清空：
   `chmod g=--- top2109`

权限标记含义：
 `r`（读） `w`（写） `x`（执行）
 `s`（SUID/SGID） `t`（Sticky bit）

------

## 4. 练习：权限验证

### ✅ root 创建文件/目录权限验证

1. root 创建文件 `top2109` 和目录 `top2109dir`：

   ```bash
   touch top2109
   mkdir top2109dir
   ll -d top2109 top2109dir
   ```

2. tom 无法修改 top2109dir（无 `w` 权限）

### ⚠️ 有争议的权限：目录 `other=rw-`

- 不能进入目录（无 `x`）
- 不能修改内容（无权限）
- 可以查看？ → 不行，因为 `ls` 需要执行权限

------

## 5. 特殊权限实验：Sticky 位

目录权限给了所有用户 `w`，意味着任何人可删除其他人的文件。

```bash
mkdir dangerous_dir
chmod 777 dangerous_dir
touch dangerous_dir/root_file
chown root dangerous_dir/root_file

# tom 可以删除 root 的文件
su - tom
rm dangerous_dir/root_file
```

### 防护方案：

添加 Sticky 位：

```bash
chmod +t dangerous_dir
```

------

## 6. 权限练习

### 练习1：

```bash
# 修改目录权限
chmod g+w,o-wx top2109dir
chmod g=rw-,o=--- top2109dir
```

让 `tom/jerry` 分别测试 `cd`、`ls`、创建/删除文件是否成功。

### 练习2：

#### 自建目录验证

```bash
mkdir testdir
chmod 733 testdir
# tom 删除其他人的文件
```

#### /tmp 目录验证

```bash
ls -ld /tmp  # 默认应为 1777
```

------

## 7. 权限是从左向右生效

```bash
chmod u=--- myfile
# 即使是所有者也没有权限访问
```

------

## 8. 常用权限设置

```bash
chmod 755 top2109       # 文件：rwxr-xr-x
chmod 644 root.txt      # 文件：rw-r--r--
```

------

## 9. 八进制权限对照表

| 数字 | 二进制 | 含义 |
| ---- | ------ | ---- |
| 0    | 000    | ---  |
| 1    | 001    | --x  |
| 2    | 010    | -w-  |
| 3    | 011    | -wx  |
| 4    | 100    | r--  |
| 5    | 101    | r-x  |
| 6    | 110    | rw-  |
| 7    | 111    | rwx  |

------

## 10. 普通用户 vs 管理员 创建权限差异？

| 类型 | 默认权限 | 来源（最大权限 - umask） |
| ---- | -------- | ------------------------ |
| 文件 | 666      | 可读可写                 |
| 目录 | 777      | 可读可写可执行           |

------

## 11. umask 权限掩码

| umask | 创建目录权限 | 创建文件权限 |
| ----- | ------------ | ------------ |
| 002   | 775          | 664          |
| 022   | 755          | 644          |
| 0077  | 700          | 600          |

### 查看和修改 umask

```bash
umask          # 查看当前值
umask 0077     # 修改当前 shell 的掩码
```

配置文件：

- `/etc/profile`
- `/etc/bashrc`

------

## 12. 家目录管理

```bash
useradd -d /home/anyuser bob
rm -rf /home/anyuser

# bob 登录后提示无家目录，使用 /
```

### 恢复家目录

```bash
mkdir /home/bob
cp -r /etc/skel/.[a-z]* /home/bob
chown -R bob:bob /home/bob
```

------

## 13. 所属组与所有者修改

```bash
# 修改组
chgrp lisa top2109

# 修改所有者和组
chown jerry:jerry top2209dir/
```

------

## 14. 综合练习题建议

1. 创建用户 bob，指定家目录 `/home/anyuser`
2. 用 root 删除 bob 的家目录
3. 切换 bob 用户观察现象
4. 手动建立 `/home/bob`
5. 使用 skel 模板恢复默认结构
6. 修改所有者和组为 bob
7. 切换 bob 用户验证是否恢复成功

------

# 7.21下

------

# Linux 特殊权限与提权机制总结

## 1. 特殊权限概览

| 权限位 | 数值 | 含义                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| SUID   | 4    | 可执行文件：以 **文件所有者身份** 执行程序（仅限二进制）     |
| SGID   | 2    | **目录**：新建文件继承目录所属组；**文件**：执行时以文件组身份运行 |
| Sticky | 1    | **目录**：只有文件拥有者才能删除自己的文件                   |

设置示例：

```bash
# 添加粘滞位（Sticky Bit）
chmod 1777 top2109dir/

# 移除粘滞位
chmod o-t top2109dir

# 添加 SGID（组继承）
chmod 2777 top2109dir/

# 添加 SUID（权限提升）
chmod 4755 /usr/bin/某可执行文件
```

------

## 2. SUID 示例实验

### SUID 原理说明：

> **普通用户执行某文件时，以文件所有者身份运行。**

### 实验：cat 添加 SUID 查看 `/etc/shadow`

```bash
which cat         # 确认路径
chmod 4755 /usr/bin/cat

# jerry 用户执行
cat /etc/shadow   # 成功读取（应为 root 权限）
```

> ⚠️ **风险极大，不推荐对任意程序添加 SUID！**

------

## 3. 查找系统中 SUID 程序

```bash
# 查找全系统 SUID 程序
find / -perm -u=s -type f 2>/dev/null

# 或者简写为：
find / -perm -4000 -type f 2>/dev/null
```

### 常见 SUID 程序（例）：

```bash
ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root ... /usr/bin/passwd
```

说明：

- 属主为 root
- 拥有 SUID（`s` 替代 `x`）
- 普通用户运行该命令会临时以 root 身份执行

------

## 4. SGID 示例实验

```bash
chmod 2777 /testdir
# jerry 在 testdir 中创建文件，会继承 testdir 的所属组
```

------

## 5. 粘滞位 Sticky Bit 示例

```bash
mkdir /tmp/testdir
chmod 1777 /tmp/testdir

# jerry 和 tom 都可以写文件，但只能删除自己的
```

------

## 6. 权限组合对比

| 权限数值 | 说明                               | 安全性 | 用途                   |
| -------- | ---------------------------------- | ------ | ---------------------- |
| `0777`   | 所有人可读写删，无限制             | ❌ 危险 | 禁用（极不安全）       |
| `1777`   | 粘滞位，所有人可写，不能删他人文件 | ✅ 安全 | `/tmp` 等公共临时目录  |
| `2777`   | SGID 位，文件自动继承目录组        | ⚠️ 中等 | 小组协作目录（需谨慎） |
| `3777`   | SGID + 粘滞位，组继承+安全删除机制 | ✅ 推荐 | 安全共享目录           |

------

## 7. sudo 提权机制

### 场景：jerry 不能关闭服务

```bash
jerry:
systemctl stop autofs     # 权限不足

root:
visudo                    # 安全修改 sudo 配置
```

### 配置 sudo 权限+不要密码

```bash
# 编辑 /etc/sudoers 使用 visudo
NOPASSWD:jerry    ALL=(ALL)    /usr/bin/systemctl

# 多条命令：
jerry    ALL=(ALL)    /usr/bin/systemctl, /usr/bin/vim

# 用户所属组授权：
%wheel  ALL=(ALL)     ALL
```

查看 jerry 拥有哪些 sudo 权限：

```bash
sudo -l
```

------

## 8. find 命令 sudo 提权演示

### root 设置

```bash
visudo

jerry    ALL=(ALL)    /usr/bin/find
```

### jerry 用户使用：

```bash
sudo find /boot -size +3M -type f -exec /bin/bash \;
```

> 💡 可以通过 `-exec` 执行其他命令，从而间接获得更高权限。

------

## 9. 总结：特殊权限对比表

| 特殊权限 | 类型      | 作用范围             | 权限字符表示 | 数值 | 示例命令                     |
| -------- | --------- | -------------------- | ------------ | ---- | ---------------------------- |
| SUID     | 文件      | 程序以属主身份运行   | `s` 替代 `x` | 4    | `chmod 4755 /usr/bin/passwd` |
| SGID     | 文件/目录 | 文件同上，目录继承组 | `s` 替代 `x` | 2    | `chmod 2777 /project`        |
| Sticky   | 目录      | 限制删除权限         | `t` 替代 `x` | 1    | `chmod 1777 /tmp`            |

------



# 7.22

------

# Linux 系统管理与网络配置笔记

## 一、文件删除权限相关

### 粘滞位（Sticky Bit）

- 如果当前目录设置了粘滞位（Sticky Bit，`t`），即该目录的权限类似如下：

  ```bash
  drwxrwxrwt
  ```

- 则只有以下三种用户才能删除目录下的文件：

  - 文件的所有者
  - 目录的所有者
  - `root` 用户

**问题：**

> 普通用户 `tom` 属于 `root` 组，能否删除 `jerry` 用户的文件？

**答案：** 不能！即便 `tom` 是 `root` 组的成员，只要不是文件所有者、目录所有者或真正的 root 用户，就不能删除其他用户的文件。

------

## 二、忘记 root 密码的救援方法

### 1. 重启进入 GRUB 引导菜单

- 重启系统，在 GRUB 菜单界面按 `e` 进入编辑模式。
- 修改内核参数：
  - 找到以 `linux16` 开头的一行（或 `linux`）。
  - 把 `ro` 修改为 `rw`
  - 末尾添加：`rd.break`
- 按 `Ctrl + X` 启动进入救援模式。

### 2. 救援模式下操作

```bash
# 挂载根目录
chroot /sysroot

# 清除 root 密码
passwd -d root

# 创建重标记文件，重启后系统会重新设置 SELinux 标签
touch /.autorelabel

# 退出并重启系统
exit
reboot
```

------

## 三、GRUB 密码保护配置

### GRUB 文件位置

- `/boot/grub/`
- `/boot/grub2/`

### 添加 GRUB 密码用户

1. 编辑 `/etc/grub.d/10_linux` 文件，添加如下内容（不要直接编辑该文件主体，添加到末尾）：

   ```bash
   cat << EOF
   set superusers="bob"
   export superusers
   password_pbkdf2 bob grub.pbkdf2.sha512.10000.XXXX
   EOF
   ```

2. 更新 grub 配置文件：

   ```bash
   grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

------

## 四、Kali Linux 救援模式快速进入 root 权限

1. grub 菜单按 `e` 编辑

2. 将 `ro` 改为 `rw`

3. 把 `linux` 行末尾内容删除并添加：

   ```bash
   init=/bin/sh
   ```

4. 按 `Ctrl + X` 进入单用户模式。

------

## 五、进程管理

### 常用命令

- `ps aux`：查看所有进程  加-l多线程
- `pstree -p | grep bash`：树状结构查看进程
- `kill -9 PID`：强制杀死进程
- `top`：实时进程监控（输入 `k` 可杀进程）

### 常用快捷键

- `Ctrl + Alt + F1`：图形界面
- `Ctrl + Alt + F2~F6`：非图形终端
- `jobs`：查看后台任务
- `fg %编号`：恢复后台任务

### 异常退出文件恢复

```bash
rm -f .filename.swp
```

------

## 六、systemctl 管理服务

```bash
# 启动、停止、查看状态
systemctl start httpd
systemctl stop httpd
systemctl status httpd

# 设置开机启动
systemctl enable httpd

# 禁用开机启动
systemctl disable httpd

# 查看所有可以控制的服务
systemctl list-unit-files
```

------

## 七、网络地址配置（NAT 模式）

### 1. 临时设置 IP 地址

```bash
# 查看网卡信息
ip addr show ens33

# 删除 IP
ip address del 192.168.133.131/24 dev ens33

# 添加 IP
ip address add 192.168.133.131/24 dev ens33

# 查看网关路由
ip route

# 查看 DNS
cat /etc/resolv.conf
```

### 2. 永久配置 IP 地址

编辑配置文件：

```bash
vim /etc/sysconfig/network-scripts/ifcfg-ens33
```

内容如下：

```ini
DEVICE=ens33
TYPE=Ethernet
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.133.251
NETMASK=255.255.255.0
GATEWAY=192.168.133.2
DNS1=114.114.114.114
DNS2=8.8.8.8
```

重启网络服务：

```bash
systemctl restart NetworkManager
```

------



# Kali 网络配置与计划任务 + 日志管理笔记

## 📡 网卡静态 IP 配置（Kali）

配置文件：`/etc/network/interfaces`

```conf
auto eth0
iface eth0 inet static
    address 192.168.133.249
    netmask 255.255.255.0
    gateway 192.168.133.2
```

重启网络服务：

```bash
systemctl restart networking.service
```

------

## ⏰ 计划任务

### 一次性计划任务（at）

- 确保服务已启动：

  ```bash
  systemctl status atd
  ```

- 设置任务：

  ```bash
  at now + 2min
  at> echo "hello" > /tmp/test.txt
  <Ctrl+D>
  ```

- 查看任务：

  ```bash
  at -l        # 列表
  at -c 任务号 # 查看详情
  ```

- 时间格式：`at 12:30 2025-07-21`

------

### 周期性任务（crontab）

- 确保服务运行：

  ```bash
  systemctl status crond
  ```

- 编辑周期任务：

  ```bash
  crontab -e
  ```

- 查看：

  ```bash
  crontab -l
  crontab -u 用户名 -l
  ```

### 示例：

每年1、3、5月的周一到周五凌晨3点，打包 `/var/log/secure` 到 `/tmp/test.tar.gz`：

```cron
0 3 * 1,3,5 1-5 tar -zcf /tmp/test.tar.gz /var/log/secure
```

------

## ⏳ 练习示例：

7月23日 10:00–11:00 每分钟备份一次 `/var/log/source` 日志：

```cron
* 10-11 23 7 * cd /var/log && tar -zcf /tmp/source_`date +\%H:\%M`.tar.gz source
```

------

## 🧾 日志系统（rsyslog）

### 核心日志路径：

- `/var/log/secure`：记录认证和安全相关日志

### 配置文件：

- `/etc/rsyslog.conf`

### 日志规则语法：

```
facility.level      destination
```

### 示例规则：

```conf
authpriv.*     /var/log/secure
*.emerg        :omusrmsg:*
```

------

### 手动触发日志写入：

```bash
logger -p authpriv.error "+++error log+++"
logger -p authpriv.emerg "+++emerg log+++"
```

------

## 🌐 日志集中管理（远程）

### 客户端配置（发送日志到远程）：

`/etc/rsyslog.conf` 中添加：

```conf
authpriv.* @@192.168.1.200:514
```

### 服务器端配置（接收并处理日志）：

- 取消监听 TCP 514 的注释：

```conf
module(load="imtcp")
input(type="imtcp" port="514")
```

- 添加日志筛选规则：

```conf
:msg, contains, "Failed password" /var/log/class1/class2.txt
```

------



# Linux动态网站搭建教程

## 一、LAMP/LNMP基础介绍

- **LAMP架构：**
  - L：Linux 系统
  - A：Apache（Web服务器）
  - M：MySQL/MariaDB（数据库）
  - P：PHP（脚本语言）
- **LNMP架构：**
  - L：Linux
  - N：Nginx（Web服务器）
  - M：MySQL/MariaDB
  - P：PHP

> 静态网站只需要 Apache；动态网站需要数据库和PHP做桥接。

------

## 二、Apache安装与配置

### 1. 安装Apache

```bash
yum -y install httpd
```

### 2. 查看软件安装路径和主配置文件

```bash
rpm -ql httpd
主配置文件路径：/etc/httpd/conf/httpd.conf
默认发布路径：/var/www/html
```

### 3. 快速查看有效配置内容（去注释和空行）

```bash
grep -v "#" /etc/httpd/conf/httpd.conf | grep -v ^$
```

### 4. httpd.conf 配置重点

| 配置项                                 | 说明               |
| -------------------------------------- | ------------------ |
| `ServerRoot "/etc/httpd"`              | 主目录             |
| `Listen 80`                            | 监听端口           |
| `User apache`                          | 启动服务用户       |
| `Group apache`                         | 启动服务组         |
| `DocumentRoot "/var/www/html"`         | 默认网页根目录     |
| `<Directory "/var/www/html">`          | 控制目录权限和行为 |
| `DirectoryIndex index.html`            | 默认网页文件       |
| `CustomLog "logs/access_log" combined` | 日志位置与格式     |

### 5. 启动与重启服务

```bash
systemctl start httpd
systemctl restart httpd
```

------

## 三、Apache访问控制示例

### 1. 拒绝某IP段访问

**方法一：使用 `Require not ip`**

```apache
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride None
    <RequireAll>
        Require all granted
        Require not ip 192.168.126.0/24
    </RequireAll>
</Directory>
```

**方法二：传统方式（需支持）**

```apache
Order Deny,Allow
Deny from 192.168.133.1
```

### 2. 发布网站 & 查看访问日志

```bash
访问日志：/var/log/httpd/access_log
错误日志：/var/log/httpd/error_log
```

------

## 四、MariaDB数据库操作

### 1. 安装与启动

```bash
yum -y install mariadb-server
systemctl start mariadb
```

默认端口：`3306`

### 2. 基本数据库操作

```sql
-- 查看所有数据库
show databases;

-- 进入数据库
use mysql;

-- 查看表
show tables;

-- 查看字段
desc mysql.user;

-- 创建数据库
create database class1;

-- 创建表
create table class1.users(
  id int auto_increment,
  name varchar(15),
  age int,
  sex enum('b','g'),
  tel varchar(15),
  primary key(id)
);
```

### 3. 增删改查示例

```sql
-- 插入数据
insert into class1.users(name, age, sex, tel) value('tom', 26, 'b', 12345678901);

-- 更新数据
update class1.users set tel='13838383838' where id=1;

-- 查询所有女孩
select name, tel from class1.users where sex='g';

-- 查询年龄<20的女孩
select name, tel from class1.users where sex='g' and age<20;

-- 分页查询
select name, tel from class1.users limit 0,1;

-- 删除用户
delete from class1.users where id=3;

-- 删除表
drop table class1.users;

-- 删除库
drop database class1;
```

------

## 五、数据库备份与恢复

### 1. 备份数据库

```bash
mysqldump -u root -p123456 class1 users > /tmp/class1.users.sql
```

### 2. 恢复数据库

```bash
# 在bash中
mysql -u root -p123456 class1 < /tmp/class1.users.sql
# 或者在 mysql 命令行内：
source /tmp/class1.users.sql;
```

------

## 六、PHP安装与配置

### 1. 安装PHP及模块

```bash
yum -y install php php-mysql php-mbstring
```

### 2. 开启短标记功能

#### 编辑   ***php配置文件***  `  /etc/php.ini`，找到：

```ini
short_open_tag = On
```

### 3. 测试PHP是否正常

创建文件 `/var/www/html/index.php`

```php
<?php phpinfo(); ?>
```

------

## 七、Apache虚拟主机配置

### 示例配置文件（添加到 `/etc/httpd/conf/httpd.conf` 或单独vhost文件）

```apache
<VirtualHost *:80>
    ServerName farm.test
    DocumentRoot "/var/www/farm"

    <Directory "/var/www/farm">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

- 本地添加 hosts 解析：

```bash
echo "127.0.0.1 farm.test" >> /etc/hosts
```

------

## 八、文件权限配置

```bash
# 设置Apache为upload目录的所有者
chown -R apache /var/www/farm/upload
```

------


### 作业 1：在 `/tmp` 目录中创建 `topclass1` 目录及其子目录 `topgroup`，并在子目录中创建文件 `topuser.txt`，文件内容包含姓名和当前时间。

#### 1.1 创建 `/tmp/topclass1/topgroup` 目录

首先，我们需要通过 `mkdir` 命令来创建 `/tmp/topclass1` 和 `/tmp/topclass1/topgroup` 目录。通过 `man` 查看如何一次性创建两级目录。

```bash
man mkdir
```

在 `man mkdir` 中，你会发现 `-p` 选项，表示如果父目录不存在则一并创建。

![image-20250716162842763](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250716162842763.png)

#### 1.2 使用 `-p` 选项一次性创建两级目录

```bash
mkdir -p /tmp/topclass1/topgroup
```

这样，`mkdir` 会创建 `/tmp/topclass1` 和 `/tmp/topclassq1/topgroup` 目录（如果它们不存在的话）。

![image-20250716162946675](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250716162946675.png)

#### 1.3 在 `/tmp/topclass1/topgroup` 目录中创建文件 `topuser.txt`

我们接下来使用 `echo` 命令来创建 `topuser.txt` 文件，并写入内容。首先，我们获取当前时间并将其写入文件。

```bash
echo "zhangsan" >topuser.txt
date >> topuser.txt
```

- 第一行将 "姓名" 写入文件。
- 第二行使用 `date` 命令获取当前时间，并将其追加到文件中。

#### 1.4 验证文件内容

最后，我们可以使用 `cat` 命令来检查文件的内容是否正确：

```bash
cat /tmp/topclass1/topgroup/topuser.txt
```

![image-20250716163230266](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250716163230266.png)





### 作业 2：通过 Kali 进行远程登录和本地用户切换，观察日志文件内容，错误登录的关键词和登录成功的关键词。

#### 2.1 远程登录到目标主机

从 Kali 远程登录到目标主机（IP 地址：`192.168.126.129`）上的 `root` 账户：

```bash
ssh root@192.168.126.129
```

如果是第一次连接，它会提示确认主机的指纹，输入 `yes` 来继续。然后输入密码，成功登录后进入远程主机的命令行。

#### 2.2 本地用户切换

在kali上使用 `su` 或 `sudo` 命令切换到其他用户。

```bash
su - allen
```

#### 2.3 查看日志文件内容

#### **用户 `root` 成功登录**

```
Jul 16 16:35:49 localhost sshd[5336]: Accepted password for root from 192.168.126.128 port 51364 ssh2
Jul 16 16:35:49 localhost sshd[5336]: pam_unix(sshd:session): session opened for user root by (uid=0)
```

- 这些日志显示用户 `root` 使用密码成功通过 SSH 登录。登录来源是 `192.168.126.128`，端口 `51364`。
- `Accepted password for root` 表明 `root` 用户通过密码验证成功。
- `session opened for user root` 表示 SSH 会话成功开启，`root` 用户的会话被启动。

. **通过 `su` 切换用户（`root` 切换到 `allen`）**

```
Jul 16 16:36:00 localhost su: pam_unix(su-l:session): session opened for user allen by root(uid=0)
```

- 这条日志表示 `root` 用户成功通过 `su` 命令切换到 `allen` 用户。
- `session opened for user allen` 表示为 `allen` 用户打开了一个新的会话。

失败登录

```
Jul 16 16:45:54 localhost sshd[5554]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.126.128  user=root
```



### 关键词分析：

- **登录成功的关键词：**

  - `Accepted password for root`：这表示用户 `root` 成功使用密码登录。
  - `session opened for user root`：表示用户 `root` 的会话已成功开启。

- **失败成功的关键词**

​              authentication failure：登录失败



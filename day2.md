# 作业1

#### 首先关闭VMware提供的DHCP服务，并查看vmnet8的网关

![image-20250710161220996](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710161220996.png)

#### 在window service 2019中设置静态的地址，网关指向vmnat8的网关

![image-20250710161356311](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710161356311.png)

#### 在window2019中安装DHCP服务器，并分配100.10到100.50的地址池，并把路由器设置成vmnat8的网关地址



![image-20250710094848133](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710094848133.png)

![image-20250710161635230](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710161635230.png)

#### window 7获取到了DHCP服务器提供的地址，并且可以正常上网

![image-20250710161752718](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710161752718.png)



# 作业二

kali机安装DHCP-pigmaster和scapy-master，安装命令如下

```
sudo python2 ./setup.py install
```

对DHCP服务器展开攻击，用不同的mac地址抢占了DHCP池所有空余的位置

```
sudo pig.py eth0
```

![image-20250710104903748](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710104903748.png)

#### DHCP池全部占满

![image-20250710105124564](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710105124564.png)

#### win7无法从DHCP服务器获取IP地址，以169.254...进行通信

![image-20250710112056314](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710112056314.png)

# 作业三

#### DHCP服务器中修改dns为2019

![image-20250710162855095](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710162855095.png)

#### window7中自动获取的dns服务器变成了2019

![image-20250710163044482](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710163044482.png)

#### window7成功通过2019解析www.jd.com

![image-20250710163205589](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710163205589.png)

# 作业4

#### win2019设置转发器为114

![image-20250710163347248](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710163347248.png)

#### window7依然可以正常上网

![image-20250710163654991](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710163654991.png)



# 作业5

#### 给www.jd.com创建nba.jd.com的别名

![image-20250710163945110](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710163945110.png)

#### win7中可以解析nba.jd.com

![image-20250710164928869](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250710164928869.png)


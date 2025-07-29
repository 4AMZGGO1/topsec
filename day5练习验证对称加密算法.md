





# 1验证对称加密算法

### 📂 1️⃣ 创建 `test1.txt` 文件

```
cd /tmp
echo "这是一个测试文件。" > test1.txt
```

------

### 🔒 2️⃣ 使用对称加密（例如 AES-256-CBC）进行加密

```
openssl enc -aes-256-cbc -in test1.txt -out test1.txt.enc
```

执行后会让你输入一个密码（对称密钥），再次确认即可。
 加密后会生成 `test1.txt.enc` 文件。

------

### 🔓 3️⃣ 解密 `test1.txt.enc` 文件

```
openssl enc -d -aes-256-cbc -in test1.txt.enc -out test1_decrypted.txt
```

这里的 `-d` 表示解密（decode），也会要求输入当时加密用的同一个密码。

------

### ✅ 4️⃣ 检查解密后的内容

```
cat test1_decrypted.txt
```

![image-20250715111548473](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715111548473.png)



# 2.验证非对称加密算法

### 1️⃣ 生成 2048 位 RSA 密钥对

生成私钥（私钥文件中包含了私钥和公钥信息）：

```
openssl genrsa -out rsa.key 2048
```

------

### 2️⃣ 从私钥文件中提取公钥

```
openssl rsa -in rsa.key -pubout -out pub.key
```

生成后你会得到两个文件：

- `rsa.key`（私钥）
- `pub.key`（公钥）

------

### 📌 对比私钥和公钥内容

查看私钥内容：

```
cat rsa.key
```

查看公钥内容：

```
cat pub.key
```

你会发现它们内部有部分字段（如模数 `modulus`）是相同的。

------

### 3️⃣ 使用公钥加密文件

这里我们以 `test1.txt` 作为原始文件，生成加密文件 `test2.enc`：

```
openssl pkeyutl -encrypt -inkey pub.key -pubin -in test1.txt -out test2.enc
```

------

### 4️⃣ 使用私钥解密文件

用私钥解密刚才加密好的文件 `test2.enc`，输出解密后的文件 `test3.txt`：

```
openssl pkeyutl -decrypt -inkey rsa.key -in test2.enc -out test3.txt
```

![3fd6d3994a33e823a1eee064809fdc46](C:\Users\Administrator\Documents\Tencent Files\1282341070\nt_qq\nt_data\Pic\2025-07\Ori\3fd6d3994a33e823a1eee064809fdc46.png)



# 3.hash值加密练习（简单版）

#### 加密test1.txt,修改test1内容，再次加密，输出的结果不同

```
openssl dgst -sha256 test1.txt
```

![image-20250715115002694](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715115002694.png)

#### 还原test1，再次加密，得到与第一次相同的值

![image-20250715115307840](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715115307840.png)

#### 所以相同明文，不管加密多少次，最终结果相同

#### 接收端可以通过hash值得出数据是否完整



# 4.pki

## ⚙️ 📂 文件夹结构

- `/home/kali/Desktop/xuwei` — 徐伟的密钥、明文、签名等
- `/home/kali/Desktop/guotao` — 国涛的密钥、密文、收到后解密、验签等

------

## 🔑 1️⃣ 在各自目录生成密钥对（非对称）

先切到各自目录：

```
cd /home/kali/Desktop/xuwei
# 生成徐伟RSA私钥
openssl genrsa -out xuwei_private.pem 2048
# 导出公钥
openssl rsa -in xuwei_private.pem -pubout -out xuwei_public.pem
`
```

![image-20250715165218754](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715165218754.png)

## 🔗 2️⃣ 互换公钥

把：

- `/home/kali/Desktop/xuwei/xuwei_public.pem` 给国涛
- `/home/kali/Desktop/guotao/guotao_public.pem` 给徐伟

可以直接复制到各自目录：

```
cp /home/kali/Desktop/xuwei/xuwei_public.pem /home/kali/Desktop/guotao/
cp /home/kali/Desktop/guotao/guotao_public.pem /home/kali/Desktop/xuwei/
```

![image-20250715165516398](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715165516398.png)

## ✏️ 3️⃣ 徐伟准备明文

```
cd /home/kali/Desktop/xuwei
echo "你好" > message.txt
```



## 🗝️ 4️⃣ 用国涛公钥加密（保证只有国涛能解密）

```
openssl rsautl -encrypt -inkey guotao_public.pem -pubin -in message.txt -out message.enc
```

![image-20250715165845234](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250715165845234.png)

## 🧩 5️⃣ 徐伟生成哈希（SHA256）

```
openssl dgst -sha256 -out message.sha256 message.enc
```

查看一下：

```
cat message.sha256
```

------

## ✍️ 6️⃣ 徐伟用私钥对哈希签名（生成数字签名）

```
openssl dgst -sha256 -sign xuwei_private.pem -out signature.bin message.txt
```

------

## 📤 7️⃣ 徐伟把以下三个文件发给国涛

- `message.enc` — 加密的消息
- `signature.bin` — 数字签名
- `xuwei_public.pem` — 徐伟的公钥（如果国涛还没保存）

------

## ✅ 8️⃣ 国涛收到后，先解密

```
bash复制编辑cd /home/kali/Desktop/guotao
openssl rsautl -decrypt -inkey guotao_private.pem -in message.enc -out decrypted_message.txt
cat decrypted_message.txt
```

------

## 🕵️‍♂️ 9️⃣ 国涛验证签名

（1）先生成解密后明文的哈希：

```
bash
openssl dgst -sha256 -out decrypted_message.sha256 decrypted_message.txt
```

（2）用徐伟公钥验签：

```
openssl dgst -sha256 -verify xuwei_public.pem -signature signature.bin decrypted_message.txt
```

如果输出：

```
Verified OK
```

说明签名验证成功，内容没改，确实是徐伟签的。

------

## 📌 ✅ 全流程小结

| 步骤 | 用到的技术        | 用途               |
| ---- | ----------------- | ------------------ |
| 加密 | 非对称加密（RSA） | 保证只有国涛能解密 |
| 哈希 | SHA256            | 保证内容完整性     |
| 签名 | 徐伟私钥签名      | 保证身份真实性     |
| 验签 | 徐伟公钥          | 验证签名是否有效   |




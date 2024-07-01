[简述 OAuth 2.0 的运作流程 | 小胡子哥的个人网站 (barretlee.com)](https://www.barretlee.com/blog/2016/01/10/oauth2-introduce/)

整个OAuth2 的流程分为三个阶段：

1. 网站和 Github 之间的协商
2. 用户和 Github 之间的协商
3. 网站和 Github 用户数据之间的协商

![img](https://raw.githubusercontent.com/h1s97x/picture/main/Doc/aHR0cHM6Ly9pbWcubWVpd2VuLmNvbS5jbi9pMTcwODkxMS8zNTBlODg5ZDQxYTc0YmM1LmpwZWc)

*OAuth2流程图*





### 网站和 Github 之间的协商

Github 会对用户的权限做分类，比如读取仓库信息的权限、写入仓库的权限、读取用户信息的权限、修改用户信息的权限等等。如果我想获取用户的信息，Github 会要求我，先在它的平台上注册一个应用，在申请的时候标明需要获取用户信息的哪些权限，用多少就申请多少，并且在申请的时候填写你的网站域名，Github 只允许在这个域名中获取用户信息。

此时我的网站已经和 Github 之间达成了共识，Github 也给我发了两张门票，一张门票叫做 Client Id，另一张门票叫做 Client Secret。



[Developer applications (github.com)](https://github.com/settings/developers)

注册一个Oauth应用（github）

github生成了两个钥匙，Client ID和Client Secret。

![image-20240627171946523](https://raw.githubusercontent.com/h1s97x/picture/main/Doc/image-20240627171946523.png)

Client ID：Ov23ctoHnbS9GqRiihyV

Client Secret：2fe428f0157b077522fbc03a5f933e24e34e27d4
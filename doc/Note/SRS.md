## 一. 系统概述

### 1.1 项目背景

事情起因:

暑假时用hexo搭建了个人博客并部署到Github上，在实际使用中发现很多问题，使用一些主題后尝试自定义博客的样式以及增加新组件例如音乐模块时难以添加。恰逢有课程设计要求，顺水推舟之下就选择了做一个博客系统。

实际实现:

之前数据库已经做过一个系统，框架已经比较熟悉，但之前并未考虑过系统重用的问题，因此项目耦合比较严重，实际可重用的模块不多，因此最终开发时对新项目进行模块化设计。

### 1.2 技术选型


Web框架： Flask

前端开发： HTML, CSS, JavaScript，使用框架Bootstrap进行页面设计和交互。

编程语言： Python

集成开发环境： PyCharm、Visual Studio Code

版本控制： 项目由之前数据库课程设计重做，同时是个人项目，因此前期未使用版本控制，后期考虑使用Git进行版本管理。

数据库： MySQL

### 1.3 软件开发模型

增量模型（Incremental-Model）

![](blog/image/开发模型.png)


## 二、数据描述

#### 2.1 数据字典 

详细见table.pdf

#### 2.2 用例图

![](blog/image/用例图1.png)

![](blog/image/用例图2.png)

#### 2.3 时序图

注册登录

![](blog/image/时序图1.png)

关注管理

![](blog/image/时序图2.png)

留言管理

![](blog/image/时序图3.png)

### 三. 需求分析

#### 3.1 功能需求

系统主要完成以下几方面的功能：

1.用户管理：用户的注册和登录，发表博文和评论。

2.博文管理：用户可以在网站中发表和设置博文。

3.评论管理：用户可以评论博文和回复其他用户的评论。

4.分类管理：添加和删除分类，给文章设置分类。

5.标签管理：添加和删除标签，给文章设置标签。

#### 3.2 性能需求

##### 3.2.1数据精度
输入输出数据要求为三种类型：字符型、整型、double 型。传输过程中除字符型外一律 double 型。这样保证所有的相关数据的精确度都能达到相对较高的标准。
##### 3.2.2时间特性
响应时间：网速在 56 k/s 时每个页面响应时间 < 45 s，关键数据查询响应时间 < 4s。
更新处理时间 < 10 s。
数据转换和传送时间 < 8 s。
解题时间 < 5 s。

#### 3.3 安全需求
##### 3.3.1 重要数据加密

对一些重要或隐私的数据按一定的算法进行加密，如用户密码、管理员密码、用户电话、用户地址等等。
##### 3.3.2 数据恢复

将各个用户的数据进行备份，允许用户申请本月流水数据的恢复，防止用户数据丢失。
##### 3.3.3 记录日志

本系统应该能够记录系统运行时所发生的所有错误，包括本机错误和网络错误。这些错误记录便于查找错误的原因。日志同时记录用户的关键性操作信息。

#### 3.4 其他需求

##### 3.4.1 易用性与可扩充性需求

系统是直接面对计算机和非计算机专业的学生的，因此要求系统能够提供良好的用户接口，易用的人机交互界面。尽量选择用户熟悉的术语和语言界面；针对用户可能出现的问题，提供相应的帮助文档。

##### 3.4.2 运行环境需求

需要在 windows 7/windows 10 操作系统上运行。

##### 3.4.3 维护性需求

源代码格式标准化，各变量、文件、类、函数等命名规范进行统一。
文档格式标准化，对于软件开发的相关文档的格式进行统一。

### 四、可行性分析

#### 4.1 技术可行性

略

#### 4.2 应用可行性

本系统能够为高校学生提供便利，方便大家通过技术性博客进行学术上的交流。加之本软件界面简单，附有详细的使用说明，系统的研制和开发充分考虑了用户的工作流程且界面直观易于学习。系统兼备了以上的优点，用户只需懂得简单的计算机操作知识，就能自由应用本软件。因此，本系统的应用大众化得到了保障。 在系统设计和开发的过程中，应在考虑成本的基础上尽量采用当前主流并有良好发展前途的产品。

### 五、模型设计

#### 实体集

见table.pdf

表结构设计原则 

应该根据系统结构中的组件划分，针对每个组件所处理的业务进行组件单元的数据库设计，而不是针对整个系统进行数据库设计。 不同组件间所对应的数据库表之间的关联应该尽可能减少，为系统或表结构的重 构提供可能性。  采用领域模型驱动的方式和自顶向下的思路进行数据库设计，首先分析系业务， 根据职责定义对象。  应针对所有表的主键和外键建立索引，有针对性地建立组合属性的索引，提高检索效率。

#### ER图

见ER图.pdf

关系模型设计原则

DBMS 采用某种数据模型进行建模，提供了在计算机中表示数据的方式，其包括，数 据结构、数据操作、数据完整性三部分。在关系模型中，通过关系表示实体与实体之间的 联系，然后基于关系数据集合进行数据的查询、更新以及控制等操作同时对数据的更新操 作进行实体完整性、参照完整性、用户自定义完整性约束。 

### 六、系统实现

详见说明文档.md

### 七、系统界面

首页：

![](blog/image/首页.png)

登录页面：

![](blog/image/登录页.png)

注册页面：

![](blog/image/注册页.png)

登录主页：

![](blog/image/登录主页.png)

个人页面：

![image-20231211112753732](blog/image/个人页面.png)

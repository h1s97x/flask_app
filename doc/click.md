[欢迎点击 — 点击文档 （8.1.x） (palletsprojects.com)](https://click.palletsprojects.com/en/8.1.x/)

## 切换到 Setuptools

在你到目前为止编写的代码中，文件末尾有一个块，它 看起来像这样：`if __name__ == '__main__':` .这是传统上的 独立 Python 文件的外观。使用Click，您可以继续这样做，但通过 SetupTools 有更好的方法。

这有两个主要（以及更多）原因：

第一个是 setuptools 自动生成可执行文件 适用于 Windows 的包装器，因此您的命令行实用程序也可以在 Windows 上运行。

第二个原因是 setuptools 脚本在 Unix 上与 virtualenv 一起使用 无需激活 virtualenv。这是一个非常有用的 概念，允许您将脚本与所有需求捆绑到 一个virtualenv。

Click 完全有能力使用它，事实上，其余的 文档将假定您正在通过以下方式编写应用程序 设置工具。

我强烈建议在阅读其余部分之前先查看 [Setuptools 集成](https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration)一章，因为示例假设您将 正在使用 SetupTools。

## 介绍

要将您的脚本与 setuptools 捆绑在一起，您只需要将脚本放在 Python 包和文件。`setup.py`

想象一下这个目录结构：

```
yourscript.py
setup.py
```

内容：`yourscript.py`

```
import click

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')
```

内容：`setup.py`

```
from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourscript:cli',
        ],
    },
)
```

## 包中的脚本

如果你的脚本正在增长，并且你想切换到你的脚本 包含在 Python 包中，所需的更改是最小的。让我们 假设您的目录结构更改为：

```
project/
    yourpackage/
        __init__.py
        main.py
        utils.py
        scripts/
            __init__.py
            yourscript.py
    setup.py
```

在这种情况下，不要在文件中使用`py_modules` 可以使用和自动包查找支持`setup.py` 设置工具。除此之外，还建议包括其他`packages` 包数据。

这些将是修改后的内容：`setup.py`

```
from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',
        ],
    },
)
```
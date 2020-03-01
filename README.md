# PythonNote

记录在使用Python过程中见到的一些常见问题，和一些使用技巧。

# Python安装

- 打开 WEB 浏览器访问https://www.python.org/downloads/source/
- 选择适用 于Unix/Linux 的源码压缩包。比如：XZ compressed source tarball 	
- 下载及解压压缩包。
- 执行 ./configure 脚本
- make
- make install

执行以上操作后，Python 会安装在 /usr/local/bin 目录中，Python 库安装在 /usr/local/lib/pythonXX，XX 为你使用的 Python 的版本号。而且pip3和Python3的链接也会建好。

# [pip与pipfile](pip_pipenv/README.md)

requirments.txt与pipfile的关系，pip与pipenv的关系，细节见[pip与pipfile](pip_pipenv/README.md)


# [基本知识](BasicKnowladge/README.md)

快速上手的教学网站一般都不会有这些内容，但这些内容又很影响实际编程，所以我统一把我遇到的问题贴在这章节。

方便快速浏览内容标题如下：

- \_\_name\_\_ 作用
- python -m 的作用等。
- Python中is和==(is not和!=)的区别

# \_\_name\_\_ 作用

如果直接运行xxx.py文件（python3 xxx.py）Python解释器把__name__置为__main__，而如果在其他地方导入该hello模块时,该文件的__name__就不是__main__，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，而在import的时候又不会去执行,因为import的时候，给该模块__name__设置的是模块文件名。比如test.py,那么被import是，该模块__name__值是test.py

```python
if __name__=='__main__':
    do_something()
```

# python中-m

命令解释

`-m mod run library module as a script (terminates option list)`即“-m”选项后面的内容是 module（模块），其作用是把模块当成脚本来运行。“terminates option list”意味着“-m”之后的其它选项不起作用

常见到的实例：

```python
python -m http.server 8000
python -m pydoc -p xxx” //就能生成 HTML 格式的官方帮助文档
python -m pdb xxx.py” //以调试模式来执行“xxx.py”脚本

python -m pip install xxx
python3.6 -m pip3 install --upgrade pip
```

**1、对于普通模块**

以“.py”为后缀的文件就是一个模块，对于`python -m name`，一句话解释： Python 会检索 sys.path ，查找名字为“name”的模块或者包（含命名空间包），并将其内容当成`__main__`模块来执行。

以“.py”为后缀的文件就是一个模块，在“-m”之后使用时，**只需要使用模块名，不需要写出后缀**，但前提是该模块名是有效的，且不能是用 C 语言写成的模块。

在“-m”之后，如果是一个无效的模块名，则会报错“No module named xxx”。

如果是一个带后缀的模块，则首先会导入该模块，然后可能报错：Error while finding module specification for 'xxx.py' (AttributeError: module 'xxx' has no attribute '__path__'。

```python
python -m test
python test.py
```

两种写法都会把定位到的模块脚本当成主程序入口来执行，即在执行时，该脚本的 __name__ 都是”__main__“，跟 import 导入方式是不同的。

但它的前提是：在执行目录中存在着“test.py”，且只有唯一的“test”模块。对于本例，如果换一个目录执行的话，“python test.py”当然会报找不到文件的错误，然而，“python -m test”却不会报错，因为解释器在遍历 sys.path 时可以找到同名的“test”模块，并且执行。

由此差异，我们其实可以总结出“-m”的用法： 已知一个模块的名字，但不知道它的文件路径，那么使用“-m”就意味着交给解释器自行查找，若找到，则当成脚本执行。

以前文的“python -m http.server 8000”为例，我们也可以找到“server”模块的绝对路径，然后执行，尽管这样会变得很麻烦。比如`python_path/lib/http/server.py 8000`

直接运行脚本时，相当于给出了脚本的完整路径（不管是绝对路径还是相对路径），解释器根据 文件系统的查找机制， 定位到该脚本。然而执行使用“-m”方式时，解释器需要在不import的情况下，在所有模块命名空间中查找，定位到脚本的路径，然后执行。为了实现这个过程，解释器会借助两个模块：pkgutil和runpy，前者用来获取所有的模块列表，后者根据模块名来定位并执行脚本 

**2、对于包内模块**

如果“-m”之后要执行的是一个包，那么解释器经过前面提到的查找过程，先定位到该包，然后会去执行它的`__main__`子模块，也就是说，在包目录下需要实现一个`__main__.py`”`文件。

换句话说，假设有个包的名称是“pname”，那么， `python -m pname`，其实就等效于`python -m pname.__main__`。

用以前文创建 HTTP 服务为例，“http”是 Python 内置的一个包，它没有`__main__.py`”文件，所以使用“-m”方式执行时，就会报错：`No module named http.__main__; 'http' is a package and cannot be directly executed。`， 所以采用了`python -m 包.模块`的方式，而 pip 包因为有统一的入口模块，有`__main__.py`文件，最后只需要写`python -m 包`，简明直观。


## 为什么要用python -m

在存在多个 Python 版本的环境中，这种写法可以精确地控制三方库的安装位置。例如用“python3.8 -m pip”，可以明确指定给 3.8 版本安装，而不会混淆成其它的版本。如果直接使用pip，多版本环境下想要知道哪个python解析器被使用还真需要费些气力。如果多个版本安装位置不同，那么就看在PATH位置，谁在前面。如果安装位置一样，比如都在`/usr/local/bin`下，回答用的哪个python解释器就很难。
这个时候就要看，你最后一次安装的pip是由谁安转的了


当使用`python/python version_num -m pip`的时候，实际是指定了Python解析器。比如Python3.8 -m pip指定使用/usr/bin/python3.8作为解析器。

```
可以将容器整体作为一个环境，跳过虚拟环境

如果项目是容器化开发的，那么把每个容器当做成一个个独立的虚拟环境使用也是没有问题的。在容器里没有必要再单独去创建虚拟环境了。
```

# Python中is和==(is not和!=)的区别

在看这个之前，可以先看下id这个方法，id()函数是查看该对象所在内存地址。每个对象都有对应的内存地址，如：

```python
>>> id(1)
10914496
>>> id("abc")
140389597187016
>>> id([1,2,3])
140389499095496
```
后面说的到引用相等实际指的就是内存地址一样！

**结论：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。反之，is not 用于判断两个变量是否引用自不同的对象，而 != 用于判断引用变量的值是否不等。**

看个简单实例：

```python
>>> x=5
>>> y=5
>>> print(x==y)
True
>>> print(x is y)
True
>>> print(id(x))
10914624
>>> print(id(y))
10914624
```

如果内容一样，而内存地址不一样（即引用不一样）的实例如下：
```python
>>> x=[1]
>>> y=[1]
>>> print(x==y)
True
>>> print(x is y)
False
>>> print(id(x))
140389499095496
>>> print(id(y))
140389499214216
```


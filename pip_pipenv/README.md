# pip与pipfile


## pip是什么

pip 是一个 Python 包也是 Python 推荐的包管理程序，可以用于安装和管理 Python 包，Python 2.7.9+ 版本中已经自带了 pip 包。针对 Python2 和 3，pip 分别提供了 pip 和 pip3 两个命令。


## pip常用命令

**安装命令**： pip install package_name

    明确指定版本号：pip install package_name==1.0.0。
    指定最小版本号：pip install package_name>=1.0.0。
    指定版本号区间：pip install package_name>=1.0.0,<2.0.0。
    

pip 也支持直接从文件读取包列表以便批量安装，通常命名为 requirements.txt，可以使用 pip install -r requirements.txt 来安装。requirements.txt 文件内容是如下的扁平格式：

    package_name1
    package_name2>=1.0.0
    package_name3>=1.0.0,<2.0.0

**生成`requirements.txt`命令**： pip freeze > requirements.txt

**安装`requirments.txt`依赖命令**： pip install -r requirements.txt

**安装whl文件命令**： 
- pip3 install package_name.whl（本地） 
- pip3 install https://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl （网上） 

## Pipfile与pipfile.lock

Pipfile 与 Pipfile.lock 是社区拟定的依赖管理文件，用于替代过于简陋的 requirements.txt 文件。

* Pipfile 文件是 TOML 格式而不是 requirements.txt 这样的纯文本。
* 一个项目对应一个 Pipfile，支持开发环境与正式环境区分。默认提供 default 和 development 区分。
* 提供版本锁支持，存为 Pipfile.lock。

示例：

```TOML 
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
numpy = "==1.16.3"
torch = {file = "https://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl"}

[requires]
python_version = "3.6"
```

### pip支持

pip 提供了 -p/--pipfile 参数用于安装 Pipfile，类似 -r/--requirement 会默认寻找 requirements.txt 文件，如果没有指定 -p 的参数将会自动寻找 Pipfile 文件。

例如：

    pip install -p    # 没有参数会自动寻找 Pipfile 文件
    pip install -p Pipfile.lock  # 根据 Pipfile.lock 安装指定依赖

**Note:需要注意的是，pip install -p 安装时会自动生成或更新 Pipfile.lock 文件。**

`Pipfile.lock` 是根据 Pipfile 和当前环境自动生成的 JSON 格式的依赖文件，任何情况下都不要手动修改该文件！

生成命令：pip freeze -p Pipfile

或者：pip freeze -p different_pipfile，将会生成 different_pipfile.lock

## pipenv

pipenv 是 Pipfile 主要倡导者、requests 作者 Kenneth Reitz 的一个库，有机的结合了 Pipfile 、pip 和 virtualenv。

通过```pip install --user pipenv```来安装。这个命令在用户级别（非系统全局）下安装 pipenv。如果安装后 shell 提示找不到 pipenv 命令，你需要添加当前 Python 用户主目录的 bin 目录到 PATH 环境变量。如果你不知道 Python 用户主目录在哪里，用下面的命令来查看：```python -m site --user-base```

**主要特性**

* 根据 Pipfile 自动寻找项目根目录
* 如果不存在，可以自动生成 Pipfile 和 Pipfile.lock，用这两个文件代替requirements.txt
* 自动在项目目录的 .venv 目录创建虚拟环境。（暂时需要设置 export PIPENV_VENV_IN_PROJECT=1）这样可以在开发环境下使用多个python版本
* 自动管理 Pipfile 新安装和删除的包。
* 安全，广泛地使用 Hash 校验，能够自动曝露安全漏洞。
* 随时查看图形化的依赖关系。pipenv graph

**Shell 自动补齐**

Linux or Mac 环境下，把如下语句追加到.bashrc或者.zshrc即可实现自动补齐：`eval "$(pipenv --completion)"`

**pipenv 可使用的命令参数**

    Commands:
    check      检查安全漏洞
    graph      显示当前依赖关系图信息
    install    安装虚拟环境或者第三方库
    lock       锁定并生成Pipfile.lock文件
    open       在编辑器中查看一个库
    run        在虚拟环境中运行命令 
    shell      进入虚拟环境
    uninstall  卸载一个库
    update     卸载当前所有的包，并安装它们的最新版本

一些使用示例：

    pip install --user --upgrade pipenv #用户安装/升级
    pipenv pipenv --three  #会使用当前系统的Python3创建环境 
    pipenv --two  #使用python2创建 
    pipenv --python 3.6  #指定Python3.6版本创建环境 
    pipenv run python 文件名  # 运行
    #pipenv run pip install packagename  #安装
    pip pipenv shell  #激活虚拟环境 
    exit //或者 ctrl+d  #退出环境
    pipenv --where  #显示目录信息 
    pipenv --venv  #显示虚拟环境信息 
    pipenv --py  #显示Python解释器信息 
    pipenv graph  #显示依赖图 pipenv check #检查安全漏洞 
    pipenv uninstall requests  #卸载包并从Pipfile中移除 
    pipenv uninstall --all  #卸载全部包
    pipenv install urllib3==1.22  #安装指定版本包
    pipenv install httpie --dev  #安装开发环境下包
    pipenv update urllib3  #更新指定包
    pipenv check   #查看软件包有没有安全漏洞
    pipenv lock：确认 Pipfile 中所有包已安装，并根据安装版本生成 Pipfile.lock。
    pipenv install https://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl  #从网上安装whl

***pip/pip3出现的地方都可以用pipenv进行替换，目前使用过程中没有见到不可行方案***

**环境变量管理**

如果你开发调试时需要配一堆环境变量，可以写到 .env 文件中，在 pipenv shell 进入虚拟环境时，它会帮你把这些环境变量加载好，非常方便。

写一个.env 文件内容如下：

```bash
FOO=hello foo
```

之后 pipenv shell 进入虚拟环境，echo $FOO 就能看环境变量的值 hello foo 已经设置好了。
如下所示：

```
$ echo $FOO
hello foo
```

**通过pipenv虚拟环境运行脚本**

    使用pipenv管理的环境来运行：pipenv run python main.py  
    或者用pipenv shell激活后再用python main.py来运行
    或者直接.venv/bin/python main.py(.venv是pipenv创建的虚拟环境目录)

**自定义虚拟环境路径**

很多工具遵循Linux开发习惯，将东西全存在用户目录中，在Linux中可能没啥，但是在Windows下可能有人不喜欢把这些东西放在用户目录。当然pipenv也可以自定义，只需要设置或修改WORKON_HOME环境变量的值即可。

如果设置了 PIPENV_VENV_IN_PROJECT=1 环境变量，pipenv会把虚拟环境放在项目目录的.venv目录下。


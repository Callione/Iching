# Iching

build automatic Iching System, predict gua


## 环境配置

### 1. ollama安装和模型下载

1. 首先需要安装 [ollama](https://ollama.com/)
2. ollama安装成功后，在命令行运行如下指令

   ```shell
   ollama run gemma3：4b
   ```
3. 上述指令执行后，命令行将会下载 gemma3:4b 模型，大概会占用3.3G 存储空间。下载完成后可以在命令行直接打字和gemma3对话。想要退出的话输入 /bye


### 2. python环境配置


1. 创建一个conda环境，建议指定python版本为 3.11。可以在命令行输入如下指令：
   ```shell
   conda create -n Iching python=3.11
   ```

    输入指令后将创建一个conda虚拟环境，内置了python 3.11

    创建完成后输入如下指令启动该环境

```
conda activate Iching
```

    然后用 pip 安装需要用到的库(首先需要在cmd里面进入该项目的文件夹)

` pip install -r requirements.txt`

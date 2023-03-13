# Openbook Catalogue

## 环境搭建

第一次运行，请创建虚拟环境。

```shell
python -m venv .venv
```

然后激活：

```shell
source .venv/bin/activate
python -m pip install sphinx
```

> 如果是 Windows 操作系统，请使用 `.\.venv\Scripts\activate.bat`。下同。

检查安装成功：

```
sphinx-build --version
```

之后每次启动终端，都请先激活环境：

```
source .venv/bin/activate
```

## 生成文档

```shell
sh ./scripts/build.sh
```

## 本地预览

```shell
sh ./scripts/preview.sh
```

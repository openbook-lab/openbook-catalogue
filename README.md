# Openbook Catalogue

## 贡献指南

```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install sphinx

sphinx-build --version
```

```shell
sphinx-quickstart docs
sphinx-build -b html docs/source/ docs/build/html
```
参考： https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

## 创建新环境

```
<!--  https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html -->
conda create -n <env-name>
```

## 启动项目

```
 python run.py
 <!-- 或者 -->
 flask run
```

## 查看环境

```
conda env list
```

## 安装指定版本 Python

```
conda install python=3.9
```

## 切换环境

```
conda activate <env-name>
```

## 删除环境

```
conda remove -n  <env-name> --all
```

### flask 工程化最佳实践 参考：https://juejin.cn/post/7252976055093592120

## 安装依赖

```
pip install -r requirements.txt
```

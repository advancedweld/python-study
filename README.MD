## flask 实现用户注册登录（增删改查）

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

## 更新依赖到reqierement文件
```
pip freeze > requirements.txt

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

## 更新数据库

# 第一次初始化时使用

flask db init

# 后面每次修改数据库字段时使用

flask db migrate -m 'message'
flask db upgrade

<!-- 回退脚本 -->

flask db downgrade

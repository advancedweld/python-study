## 启动服务：
- 1.进入到service文件目录下
- 2. 运行命令：
```
mcp dev mcp_service.py
```
  或者
```
uv run --with mcp mcp dev mcp_service.py
```
- 一般可以看到控制台输出 🔍 MCP Inspector is up and running at http://localhost:5173 🚀
- 3. 打开浏览器，访问 http://localhost:5173/
- 4. 在界面中点击connect按钮，连接到服务




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
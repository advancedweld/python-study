# 参考： https://zhuanlan.zhihu.com/p/29001189476
#  https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart
# https://github.com/advancedweld/awesome-mcp-servers/blob/main/README-zh.md#%E6%95%99%E7%A8%8B
#  mcp官网： https://modelcontextprotocol.io/quickstart/user

from mcp.server.fastmcp import FastMCP

print("hello, FastMCP")
app = FastMCP("Echo Server")  # 给你的服务起个名字

@app.tool()  # 定义一个工具叫“echo”
async def echo(message: str) -> str:
    return f"You said: {message}"  # 收到啥，回啥

if __name__ == "__main__":
    app.run()  # 启动服务




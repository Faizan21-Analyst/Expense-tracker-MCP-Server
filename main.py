from fastmcp import FastMCP

mcp=FastMCP(name='Demo Server')

@mcp.tool 
def add(a,b):
    """this tool is use to add two number"""
    return a+b

if __name__=="__main__":
    mcp.run()
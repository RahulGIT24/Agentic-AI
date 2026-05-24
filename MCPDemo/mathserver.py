from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """Add 2 numbers

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: returns sum
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """Add 2 numbers

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: returns sum
    """
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")
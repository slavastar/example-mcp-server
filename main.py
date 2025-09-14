import os
from mcp.server.fastmcp import FastMCP
from pydantic import Field


port = int(os.getenv("PORT", 3000))


mcp = FastMCP(
    name="Hello MCP Server",
    host="0.0.0.0",
    port=port,
    stateless_http=True,
    debug=False,
)

@mcp.tool(
    title="Welcome a user",
    description="Welcome a user by returning a phrase",
)
def welcome(
    name: str = Field(description="Name of the user")
) -> str:
    return f"Welcome {name} to this amazing MCP server!"


@mcp.tool
def add_squares(a: int, b: int) -> int:
    """Return sum of squares of two numbers"""
    return a**2 + b**2


if __name__ == "__main__":
    mcp.run()
    
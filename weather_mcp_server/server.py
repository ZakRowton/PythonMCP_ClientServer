"""
Local MCP server exposing GetWeather(city) that returns 100°F for any city.
Run with streamable HTTP: python server.py
Or with stdio (for client subprocess): python server.py stdio
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Server", json_response=True)


@mcp.tool()
def GetWeather(city: str) -> str:
    """Get the current weather for a city. Returns temperature in Fahrenheit."""
    return "100 degrees F"


if __name__ == "__main__":
    import sys
    transport = "stdio" if (len(sys.argv) > 1 and sys.argv[1] == "stdio") else "streamable-http"
    mcp.run(transport=transport)

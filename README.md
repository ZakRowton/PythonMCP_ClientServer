# PythonMCP_ClientServer

Python examples for the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/): a small **MCP server** (weather tool) and a **MCP client** that uses the Gemini API to call it.

## Contents

| Folder | Description |
|--------|-------------|
| **weather_mcp_server** | MCP server exposing `GetWeather(city)` — returns a fixed temperature. Runs over HTTP or stdio. |
| **gemini_mcp_client** | Client that launches the weather server as a subprocess and uses **Gemini 3 Flash** to answer questions by calling the MCP tool. |

## Quick start

1. **Weather server** (optional if you only run the client):
   ```bash
   cd weather_mcp_server
   pip install -r requirements.txt
   python server.py          # HTTP at http://localhost:8000/mcp
   # or: python server.py stdio   # for subprocess use
   ```

2. **Gemini client** (starts the server automatically via stdio):
   ```bash
   cd gemini_mcp_client
   set GEMINI_API_KEY=your-key
   pip install -r requirements.txt
   python client.py
   ```

See each folder’s `README.md` for full setup and run options.

## Requirements

- Python 3.10+
- For the client: a [Gemini API key](https://aistudio.google.com/apikey) (set as `GEMINI_API_KEY` or `GOOGLE_API_KEY`)

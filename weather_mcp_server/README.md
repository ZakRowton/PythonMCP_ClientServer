# Weather MCP Server

Local MCP server that exposes a single tool:

- **GetWeather(city: str)** – returns `"100 degrees F"` for any city.

## Setup

```bash
pip install -r requirements.txt
```

## Run

**HTTP (default)** – for Cursor, Inspector, or other HTTP clients:

```bash
python server.py
```

Server listens at `http://localhost:8000/mcp`.

**Stdio** – for the Gemini client script (subprocess):

```bash
python server.py stdio
```

# Gemini + MCP Client

Python script that uses **Gemini 3 Flash Preview** and the Gemini API to talk to the weather MCP server. The SDK’s built-in MCP support is used: the MCP session is passed as a tool and Gemini calls tools automatically.

## Setup

1. Set your API key:
   ```bash
   set GEMINI_API_KEY=your-key
   ```
2. Install dependencies (from this directory):
   ```bash
   pip install -r requirements.txt
   ```
3. The weather MCP server is expected at `../weather_mcp_server/server.py`. No need to start it yourself; the client runs it as a subprocess over stdio.

## Run

```bash
python client.py
```

This starts the weather MCP server via stdio, connects Gemini to it, and asks for the weather in London. You should see a short reply that used the GetWeather tool (e.g. 100°F).

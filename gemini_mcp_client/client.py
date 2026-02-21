"""
Use Gemini 2.5 Flash and the Gemini API to connect to the weather MCP server.
Uses the SDK's built-in MCP support: the MCP session is passed as a tool and
Gemini automatically calls tools when needed.

Requires: GEMINI_API_KEY set in the environment.
Run: python client.py

Set SHOW_TIMING=1 to see where time is spent (e.g. set SHOW_TIMING=1 before running).
"""

import asyncio
import os
import sys
import time

from google import genai
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# Path to the weather MCP server (run with stdio)
SERVER_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "weather_mcp_server")
SERVER_SCRIPT = os.path.join(SERVER_DIR, "server.py")

SHOW_TIMING = os.environ.get("SHOW_TIMING", "").strip().lower() in ("1", "true", "yes")


async def run():
    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        print("Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your environment.")
        sys.exit(1)

    t0 = time.perf_counter()
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[SERVER_SCRIPT, "stdio"],
        env=os.environ.copy(),
    )

    async with stdio_client(server_params) as (read, write):
        t1 = time.perf_counter()
        if SHOW_TIMING:
            print(f"[timing] MCP server subprocess start: {t1 - t0:.2f}s")

        async with ClientSession(read, write) as session:
            await session.initialize()
            t2 = time.perf_counter()
            if SHOW_TIMING:
                print(f"[timing] MCP session init + list_tools: {t2 - t1:.2f}s")

            client = genai.Client()

            # Gemini 2.5 Flash with MCP: pass session as tool; SDK handles tool calls
            # This does 2 round-trips to Google: (1) model returns tool call, (2) we send result, model returns text
            response = await client.aio.models.generate_content(
                model="gemini-3-flash-preview",
                contents="What is the weather in London? Use the GetWeather tool.",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],
                ),
            )
            t3 = time.perf_counter()
            if SHOW_TIMING:
                print(f"[timing] Gemini API (both rounds): {t3 - t2:.2f}s")
                print(f"[timing] Total: {t3 - t0:.2f}s")

            print(response.text)


if __name__ == "__main__":
    asyncio.run(run())

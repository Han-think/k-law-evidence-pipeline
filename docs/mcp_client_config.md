# MCP Client Configuration

This page shows example client configuration. Adjust paths for your machine.

## Local command mode

```json
{
  "mcpServers": {
    "k-law-evidence-pipeline": {
      "command": "klep-mcp",
      "env": {
        "OPENLAW_OC": "your-openlaw-oc",
        "OPENLAW_BASE_URL": "https://www.law.go.kr"
      }
    }
  }
}
```

## Python module mode

```json
{
  "mcpServers": {
    "k-law-evidence-pipeline": {
      "command": "python",
      "args": ["-m", "klep.mcp_server"],
      "env": {
        "OPENLAW_OC": "your-openlaw-oc",
        "OPENLAW_BASE_URL": "https://www.law.go.kr"
      }
    }
  }
}
```

## Important

Do not commit real API values.

The server retrieves source candidates and metadata. It does not provide final legal advice.

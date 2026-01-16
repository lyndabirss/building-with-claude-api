# Implementing a Client

## Overview

Client enables application to communicate with MCP server and access its functionality. Acts as bridge between application logic and MCP server, handling connection details automatically.

## Client Architecture

**Two Main Components:**
1. **MCP Client** - Custom class to simplify session usage
2. **Client Session** - Actual connection to server (from MCP Python SDK)

**Important Note:**
- Real-world projects typically implement either client OR server, not both
- This project builds both for learning purposes
- Custom client class handles resource cleanup automatically

## Core Client Responsibilities

**Two primary operations:**
1. Get list of available tools (send to Claude)
2. Execute tools (when Claude requests them)

## Key Method Implementations

**List Tools Method:**
```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```
- Access session (connection to server)
- Call built-in `list_tools()` function
- Return tools from result

**Call Tool Method:**
```python
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```
- Accept tool name and input parameters (from Claude)
- Pass to server via session
- Return execution result

## Testing the Client

**Test harness pattern:**
```python
async with MCPClient(
    command="uv", args=["run", "mcp_server.py"]
) as client:
    result = await client.list_tools()
    print(result)
```

**Expected output:**
- Tool definitions printed (e.g., `read_doc_contents`, `edit_document`)
- Confirms client-server connection working
- Validates tool discovery

## Complete Application Flow

**Example: "What is the contents of the report.pdf document?"**

1. Application uses client to get available tools
2. Tools sent to Claude along with user's question
3. Claude decides to use `read_doc_contents` tool
4. Application uses client to execute tool
5. Result returned to Claude
6. Claude responds to user with document contents

**Flow diagram:**
```
User Question → Client.list_tools() → Send to Claude
                     ↓
Claude decides tool → Client.call_tool() → Execute on server
                     ↓
Tool result → Back to Claude → Response to user
```

## Key Concepts

**Resource Management**
- Client session requires proper cleanup
- Custom client class handles cleanup automatically
- Use `async with` context manager pattern

**Asynchronous Operations**
- Both methods are async (use `await`)
- Enables non-blocking communication with server
- Supports concurrent operations

## Client Role

- Simplifies access to server functionality
- Abstracts connection details from application code
- Provides clean interface for tool operations
- Handles session lifecycle management
- Enables seamless Claude integration

## Best Practices

- Use custom client class for session management
- Test client methods independently before integration
- Leverage async/await for efficient operations
- Keep client interface simple and focused
- Let client handle connection complexity

# The Server Inspector

## Overview

Built-in browser-based inspector for testing and debugging MCP servers without connecting to full applications. Essential tool for isolated functionality testing during development.

## Starting the Inspector

**Command:**
```bash
mcp dev mcp_server.py
```

- Starts development server on port 6277
- Provides local URL for browser access
- Opens MCP Inspector dashboard

**Prerequisites:**
- Python environment must be activated
- Check project README for exact activation command

## Inspector Interface

**Core Sections:**
- Resources
- Prompts
- Tools
- Other features

**Note:** Interface actively being developed - appearance may change, but core functionality remains consistent.

## Testing Workflow

**1. Connect to Server**
- Click "Connect" button (left side)
- Server starts and connection establishes

**2. Test Tools**
- Navigate to Tools section
- Click "List Tools" to view available tools
- Select specific tool to test
- Fill in required parameters
- Click "Run Tool" to execute
- View results in inspector

**3. Chain Operations**
- Test tool sequences to verify functionality
- Example: Edit document → Read document to confirm changes
- Validate end-to-end workflows

## Example Testing Scenario

**Testing document operations:**
1. Select read document tool
2. Enter document ID (e.g., "deposition.md")
3. Run tool and verify returned content
4. Select edit document tool
5. Provide old text and new text parameters
6. Run edit tool
7. Re-run read tool to confirm changes applied

## Development Loop

**Efficient workflow:**
1. Make changes to MCP server code
2. Test individual tools through inspector
3. Verify results in isolation
4. Debug issues without full application setup
5. Iterate quickly

## Key Benefits

- No need to wire server to Claude for basic testing
- Test tools in isolation
- Fast iteration cycle
- Real-time debugging
- Immediate result verification
- Eliminates complex setup for simple tests

## Best Practices

- Test tools individually before integration
- Chain operations to verify multi-step workflows
- Use inspector during development for rapid feedback
- Confirm changes before deploying to full application
- Leverage isolation for focused debugging

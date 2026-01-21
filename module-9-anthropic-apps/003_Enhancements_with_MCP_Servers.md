# Enhancements with MCP Servers

## What MCP Does
Claude Code has built-in MCP client to connect external services and tools
Extends Claude's capabilities beyond built-in features with custom functionality

## MCP Server Components
* **Tools** - For taking actions
* **Prompts** - For templates
* **Resources** - For accessing data

## Setup Command
```bash
claude mcp add [server-name] [command-to-start-server]
```

**Example:**
```bash
claude mcp add documents uv run main.py
```

Server auto-connects when Claude Code starts

## Practical Example
Document processing server with `document_path_to_markdown` tool
Ask: "Convert tests/fixtures/mcp_docs.docx to markdown"
Claude uses custom tool to read and convert document

## Popular MCP Integrations
* **sentry-mcp** - Auto-discover and fix bugs from Sentry
* **playwright-mcp** - Browser automation for testing
* **figma-context-mcp** - Access Figma designs
* **mcp-atlassian** - Access Confluence and Jira
* **firecrawl-mcp-server** - Web scraping capabilities
* **slack-mcp** - Post messages, reply to threads

## Workflow Power
Combine multiple MCP servers for your specific process:
- Sentry for production errors
- Jira for ticket requirements  
- Slack for team notifications
- Custom servers for internal tools/APIs

Creates seamless integration with all your existing development tools
# MCP Section 7: Defining Prompts - Quick Reference

## Core Concept
Prompts = pre-built, high-quality instruction templates that produce better results than ad-hoc user prompts.

## Why Use Prompts?
- Users can accomplish tasks on their own, but get better/consistent results with tested prompts
- Server authors provide expertise through carefully crafted templates
- Prompts should be high-quality and relevant to your MCP server's purpose

---

## Essential Code

### 1. Required Import
```python
from mcp.server.fastmcp import base
```

### 2. Define Prompt Function
```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary.
Use the 'edit_document' tool to edit the document.
"""
    
    return [
        base.UserMessage(prompt)
    ]
```

---

## Key Points
- Use `@mcp.prompt()` decorator with name and description
- Return list of messages (UserMessage, AssistantMessage)
- Prompts can include parameters that get interpolated
- Test in MCP Inspector before deployment

## Best Practices
- Focus on tasks central to your server's purpose
- Write detailed, specific instructions
- Test thoroughly with different inputs
- Include clear descriptions
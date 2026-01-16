# Defining Tools with MCP

## Overview

Python MCP SDK simplifies server creation by handling JSON schema complexity through decorators and type hints. Focus on business logic while SDK manages protocol details.

## Server Initialization

**Single-line server setup:**
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

**In-memory document storage:**
```python
docs = {
    "deposition.md": "This deposition covers...",
    "report.pdf": "The report details...",
    "financials.docx": "These financials outline..."
}
```

## Tool Definition Pattern

**Decorator-based tool creation (replaces manual JSON schemas):**
```python
@mcp.tool(
    name="tool_name",
    description="Clear description of tool purpose"
)
def tool_function(
    param: type = Field(description="Parameter description")
):
    # Implementation
    return result
```

## Core Tool Examples

**Read Document Tool:**
```python
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]
```

**Edit Document Tool:**
```python
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

## Key Concepts

**Automatic Schema Generation**
- `@mcp.tool` decorator generates JSON schema automatically
- Type hints provide schema structure
- Pydantic `Field()` adds parameter descriptions for Claude

**Error Handling**
- Use `ValueError` with descriptive messages
- Claude can understand and act on error messages
- Validate inputs before processing

## SDK Benefits

- Automatic JSON schema generation from type hints
- Clean, maintainable code
- Built-in parameter validation via Pydantic
- Reduced boilerplate vs manual schemas
- Type safety and IDE support
- Natural Python development experience

## Best Practices

- Keep tool names descriptive and action-oriented
- Provide clear, detailed descriptions for both tools and parameters
- Include explicit error handling with meaningful messages
- Use exact type hints for automatic schema generation
- Validate required parameters before execution

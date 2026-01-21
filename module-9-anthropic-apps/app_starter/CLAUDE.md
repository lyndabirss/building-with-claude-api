# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python package implementing document-related tools exposed through an MCP (Model Context Protocol) server interface for integration with AI assistants.

## Setup

**Important**: This project requires Python 3.13 due to dependency constraints with `onnxruntime`:

```bash
# Create virtual env with Python 3.13 and activate it
uv venv --python 3.13
source .venv/bin/activate

# Install the package in development mode
uv pip install -e .
```

## Running and Testing

```bash
# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_document.py

# Run specific test class/method
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

### MCP Server Structure

The application uses FastMCP to expose tools via the Model Context Protocol:

- **main.py**: Initializes FastMCP server instance, registers tools, starts server
- **tools/**: Tool implementations exposed via MCP
  - `math.py`: Example mathematical operations
  - `document.py`: Document conversion utilities (uses MarkItDown library)
- **tests/**: Test suite with fixtures in `tests/fixtures/`

### Tool Registration

Tools are Python functions registered with the MCP server using a decorator:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server_name")
mcp.tool()(my_function)
```

The server introspects the function to create the MCP tool definition automatically.

## Defining MCP Tools

### Tool Definition Requirements

Use `Field` from pydantic for parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """Comprehensive docstring here"""
    # Implementation
```

### Docstring Guidelines

Tool descriptions should:

- Begin with a one-line summary
- Provide detailed explanation of functionality
- Explain when to use (and not use) the tool
- Include usage examples with expected input/output

### Example Tool Definition

From `tools/math.py`:

```python
from pydantic import Field

def add(
    a: float = Field(description="First number to add"),
    b: float = Field(description="Second number to add"),
) -> float:
    """Add two numbers together.

    Takes two numerical inputs and returns their sum. This tool handles
    integers and floating point numbers.

    When to use:
    - When you need to perform simple addition
    - When you need precise numerical calculation

    Examples:
    >>> add(2, 3)
    5.0
    >>> add(2.5, 3.5)
    6.0
    """
    return a + b
```

### Key Points

1. **Type Annotations**: Always apply appropriate types to function arguments and return values - type hints are required for MCP to properly introspect and expose tools
2. **Parameter Descriptions**: Use `Field(description="...")` for all parameters - these descriptions are sent to the LLM
3. **Docstring Structure**: One-line summary, detailed explanation, "When to use" section, examples
4. **Registration**: Import and register in `main.py` with `mcp.tool()(function_name)`

## Testing

- Test files follow `test_<module>.py` naming convention
- Test classes group related tests (e.g., `TestBinaryDocumentToMarkdown`)
- Fixture files stored in `tests/fixtures/` (DOCX, PDF samples)
- Uses pytest framework

## Key Dependencies

- **mcp[cli]==1.8.0**: Model Context Protocol framework
- **markitdown[docx,pdf]>=0.1.1**: Document conversion with DOCX/PDF support
- **pydantic>=2.11.3**: Data validation (required for tool parameter definitions)
- **pytest>=8.3.5**: Testing framework

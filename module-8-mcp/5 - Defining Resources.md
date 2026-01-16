# Defining Resources

## Overview

Resources expose data to clients (similar to GET handlers in HTTP servers). Used for fetching information rather than performing actions. Perfect for scenarios like document mentions, file browsing, or data retrieval.

## Resources vs Tools

- **Resources**: Expose data (read operations)
- **Tools**: Perform actions (write operations)

## Resource Types

**1. Direct Resources (Static URIs)**
- Fixed URI that doesn't change
- Example: `docs://documents`
- Use for static data or lists

**2. Templated Resources (Parameterized URIs)**
- URI with parameters
- Example: `docs://documents/{doc_id}`
- SDK automatically parses parameters from URI
- Parameters passed as keyword arguments to function

## How Resources Work

**Request-Response Pattern:**
1. Client sends `ReadResourceRequest` with URI
2. MCP server responds with data
3. URI acts as address for resource

## Implementation Pattern

**Direct Resource Example (List Documents):**
```python
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

**Templated Resource Example (Fetch Document):**
```python
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

## MIME Types

**Common types:**
- `application/json` - Structured JSON data
- `text/plain` - Plain text content
- Any other valid MIME type

**Key points:**
- Gives clients hint about data format
- SDK automatically serializes return values
- No manual JSON conversion needed

## Real-World Use Case: Document Mentions

**Scenario:** User types `@document_name` to reference files

**Required operations:**
1. Get list of all available documents (for autocomplete)
2. Fetch contents of specific document (when mentioned)

**Workflow:**
- User types `@` → Show available documents (direct resource)
- User submits with mention → Inject document content into prompt (templated resource)

## Testing Resources

**Start inspector:**
```bash
uv run mcp dev mcp_server.py
```

**Inspector sections:**
- **Resources**: Lists direct/static resources
- **Resource Templates**: Shows templated resources with parameters

**Testing workflow:**
1. Connect to inspector in browser
2. Navigate to Resources or Resource Templates
3. Click on resource to test
4. View exact response structure client will receive

## Key Concepts

**Automatic Parameter Parsing**
- Parameter names in templated URIs become function arguments
- SDK handles parsing automatically
- Example: `{doc_id}` in URI → `doc_id: str` parameter

**Automatic Serialization**
- SDK converts return values to appropriate format
- No manual JSON stringification needed
- MIME type guides serialization

**Error Handling**
- Use `ValueError` for invalid resources
- Provide descriptive error messages
- Client receives error details

## Best Practices

- Use direct resources for lists or static data
- Use templated resources for item-specific queries
- Include appropriate MIME types
- Validate parameters before processing
- Provide clear error messages
- Keep resource URIs descriptive and logical
- Test resources in inspector before client integration

## Common Use Cases

- Document/file browsing
- Configuration retrieval
- Data lookup operations
- List generation for autocomplete
- Content fetching for mentions
- Any read-only data access scenario

# Accessing Resources - Quick Reference

## Core Concept
Resources = data exposed directly in prompts (no tool calls needed). More efficient than tools for static content.

## Key Flow
User types "@report.pdf" → Client fetches resource → Content included directly in Claude prompt

---

## Essential Code

### 1. Read Resource Function
```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
```

### 2. Handle Content Types
```python
if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)
    
    return resource.text
```

### 3. Required Imports
```python
import json
from pydantic import AnyUrl
```

---

## Key Advantages
- ✓ Faster than tool calls
- ✓ Direct content inclusion in prompts
- ✓ Supports autocomplete for resource selection
- ✓ Handles JSON and text formats automatically

## Use Case for Your Scanner
Resources could expose vulnerability scan reports, configuration data, or security documentation that the MCP chatbot references when explaining findings.
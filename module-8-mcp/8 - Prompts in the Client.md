# MCP Section 8: Prompts in the Client - Quick Reference

## Core Concept
Client retrieves and uses prompts from the server - prompts return message lists that can be sent directly to Claude.

## Workflow
1. User selects a prompt (e.g., "format")
2. System prompts for required arguments (e.g., document ID)
3. Prompt gets sent to Claude with interpolated values
4. Claude uses tools to fetch data and complete task

---

## Essential Code

### 1. List Available Prompts
```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

### 2. Get Specific Prompt with Arguments
```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

---

## How Arguments Work

**Server side prompt definition:**
```python
def format_document(doc_id: str):
    # doc_id gets interpolated into the prompt
```

**Client side usage:**
```python
# Arguments dictionary keys match prompt parameters
args = {"doc_id": "123"}
messages = await client.get_prompt("format", args)
```

---

## Key Points
- `list_prompts()` retrieves all available prompts from server
- `get_prompt()` returns messages ready to send to Claude
- Arguments get passed as keyword arguments to prompt functions
- Messages can be sent directly to Claude for processing
- Test prompts in CLI by typing forward slash to see available commands

## Best Practices
- Ensure prompts are relevant to server's purpose
- Test thoroughly before deployment
- Use clear, specific instructions
- Design to work well with available tools

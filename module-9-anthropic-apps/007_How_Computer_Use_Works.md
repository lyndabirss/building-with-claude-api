# How Computer Use Works

## Core Concept
Computer use = regular tool use system applied to desktop automation
Same underlying mechanism, just a special implementation

## Tool Use Flow (Refresher)
1. Send Claude a user message + tool schema
2. Claude decides to use tool
3. Claude responds with tool use request (name + parameters)
4. Server runs function and returns result
5. Send result back to Claude in tool result message

**Example:** "What's weather in SF?" → `get_weather` tool → returns "Sunny"

## Computer Use = Same Flow
* Include tool schema for computer interaction
* Claude decides to use computer tool
* Execute requested action in computing environment
* Send result (e.g. screenshot) back to Claude

## Computer Tool Schema

**Basic schema you send:**
```json
{
  "type": "computer_20250124",
  "name": "computer",
  "display_width_px": 1024,
  "display_height_px": 768,
  "display_number": 1
}
```

**Auto-expands to include actions:**
* `key` - Press keyboard keys
* `mouse_move` - Move cursor
* `left_click` - Click at specific coordinates
* `screenshot` - Take screenshot
* `scroll` - Scroll screen

## Computing Environment
Most common: Docker container with desktop environment (Firefox)

**Action workflow:**
1. Receive tool use request (e.g., "click at 500, 300")
2. Execute mouse click in Docker container
3. Take screenshot of result
4. Send screenshot back to Claude

## Setup (Using Anthropic Reference Implementation)

**Requirements:**
1. Install Docker
2. Run Docker command with API key
3. Access web interface

**Setup command:**
```bash
export ANTHROPIC_API_KEY="your_api_key"
docker run \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

**Reference:** github.com/anthropics/anthropic-quickstarts

## Key Takeaway
Claude doesn't directly control computers
Makes tool requests that your code fulfills in controlled environment
Powerful AND safe - you maintain full control over executed actions
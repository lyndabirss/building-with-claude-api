# Agents and Tools - Key Points

## What Makes Agents Different from Workflows

**Workflows**: Use when you know exact steps needed
**Agents**: Use when you're unsure what steps should be - give Claude a goal + tools, let it figure out the path

**Trade-off**: More flexibility, but less reliability and higher cost

## How Tools Make the Agent

**Example: Basic Datetime Tools**
- `get_current_datetime` - Gets current date/time
- `add_duration_to_datetime` - Adds time to date
- `set_reminder` - Creates reminder for specific time

**Simple tools → Complex capabilities through chaining:**
- "What's the time?" → `get_current_datetime`
- "What day is it in 11 days?" → `get_current_datetime` + `add_duration_to_datetime`
- "Set gym reminder next Wednesday" → All three tools in sequence
- "When does my 90-day warranty expire?" → Claude asks for purchase date first, then calculates

## Tools Should Be Abstract

**Claude Code Example - Generic, Flexible Tools:**
- `bash` - Run any command
- `read` - Read any file
- `write` - Create any file
- `edit` - Modify files
- `glob` - Find files
- `grep` - Search file contents

**What Claude Code DOESN'T have**: Specialized tools like "refactor code" or "install dependencies"

**Result**: Claude figures out how to use basic tools for complex tasks, handling scenarios developers never explicitly planned for

## Best Practice: Combinable Tools

**Example: Social Media Video Agent**
- `bash` - Access FFMPEG for video processing
- `generate_image` - Create images from prompts
- `text_to_speech` - Convert text to audio
- `post_media` - Upload to social platforms

**Benefits:**
- Enables simple workflows (create and post video)
- Supports interactive experiences (generate sample, get approval, proceed)
- Adapts based on user feedback and preferences
- Flexible for dynamic, user-responsive applications

---

**Agents = Goal + Abstract, Combinable Tools → Claude figures out the path**
# Environment Inspection - Key Points

## Why Environment Inspection Matters

**Claude operates blindly** - needs to observe and understand results of actions to work effectively

**Computer Use Example:**
- Claude performs action (type text, click button)
- Immediately receives screenshot to understand what happened
- **Essential, not optional** - clicking could navigate, open menu, trigger changes
- Without seeing results, Claude can't know if action succeeded or understand new state

## Reading Before Writing

**File Operations Pattern:** Always read before modifying

**Example: Adding route to Python file**
1. Claude reads existing code first
2. Understands current structure
3. Makes changes without breaking functionality

**This should ALWAYS be followed when building agents**

## System Prompts for Environment Inspection

**Video Creation Agent Example:**

Tools needed to inspect environment:
- `bash` + `whisper.cpp` → Generate caption files with timestamps to verify dialogue placement
- `FFmpeg` → Extract screenshots at regular intervals to visually inspect output
- Compare generated content against original requirements

## Benefits of Environment Inspection

- **Better progress tracking** - Gauge how close to completion
- **Error handling** - Detect and correct unexpected results
- **Quality assurance** - Verify output before marking complete
- **Adaptive behavior** - Adjust approach based on observations

## Practical Implementation

**Always ask:** "How will Claude know if this action worked?"

**Provide tools and instructions for:**
- Reading file contents before modifications
- Taking screenshots after UI interactions
- Checking API responses for expected data
- Validating generated content against requirements

---

**Environment Inspection = Claude observing results transforms it from blind executor to adaptive agent**

# Chaining Workflows - Key Points

## What is Workflow Chaining?

Breaking large, complex tasks into smaller, sequential subtasks that build on each other.

**Example: Social Media Marketing Tool**
1. Find trending topics on Twitter
2. Select most interesting topic (Claude)
3. Research the topic (Claude)
4. Write video script (Claude)
5. Create video with AI avatar/TTS
6. Post to social media

## Why Chain Instead of One Big Prompt?

**Key benefit**: Focus - Claude concentrates on one specific task at a time

**Advantages:**
- Split large tasks into smaller, non-parallelizable subtasks
- Optional non-LLM processing between tasks
- Keeps Claude focused on one aspect

## The Long Prompt Problem

**Common scenario**: Writing with many constraints
- Don't mention AI authorship
- No emojis
- Avoid clichéd/casual language
- Professional, technical tone

**Result**: Even with clear constraints, Claude often violates some rules in single-prompt approach

## The Chaining Solution

**Step 1: Initial Generation**
- Send prompt, accept imperfect first result
- Claude generates content (may violate constraints)

**Step 2: Focused Revision**
- Provide generated content with targeted revision instructions
- Claude focuses entirely on fixing specific issues
- Example: "1. Remove AI authorship mentions 2. Remove emojis 3. Replace cringey writing"

**Why it works**: Claude focuses on revision task instead of balancing creation + constraints

## When to Use Chaining

**Ideal situations:**
- Complex tasks with multiple requirements
- Claude consistently ignores constraints in long prompts
- Need to process/validate outputs between steps
- Want focused, manageable interactions

---

**Chaining = Sequential subtasks that build on each other for better focus and results**
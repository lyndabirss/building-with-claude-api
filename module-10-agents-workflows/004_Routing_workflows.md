# Routing Workflows - Key Points

## The Problem with Generic Prompts

**Example**: Social media video script generator
- "Programming" → needs educational content with explanations
- "Surfing" → needs entertainment content with excitement
- **Single generic prompt can't handle both effectively**

## Setting Up Content Categories

Define distinct content types with specialized characteristics:

- **Entertainment**: High-energy, trendy language, culturally relevant
- **Educational**: Clear explanations, relatable examples, engaging
- **Comedy**: Sharp, unexpected, clever observations, timing
- **Personal vlog**: Authentic, intimate, conversational storytelling
- **Reviews**: Decisive, experience-based, highlights strengths/weaknesses
- **Storytelling**: Immersive, vivid details, emotional connection

**Each category gets its own specialized prompt template**

## How Routing Works in Practice

### Two-Step Process

**Step 1: Categorization**
- Send user's topic to Claude
- Request categorization into predefined genres
- Example: "Python functions" → categorized as "Educational"

**Step 2: Specialized Processing**
- Use category result to select appropriate prompt template
- Generate content using specialized prompt

## Routing Workflow Architecture

**The Pattern:**
1. User input → Router component first
2. Router categorizes request (initial Claude call)
3. Based on category → forward to ONE specific pipeline
4. Each pipeline has optimized workflows/prompts/tools

**Key insight**: Input goes to ONE specialized pipeline, not all of them

## When to Use Routing

**Ideal situations:**
- Application handles diverse request types needing different approaches
- Can clearly define categories covering use cases
- Categorization step handled reliably by Claude
- Specialized processing benefit outweighs routing overhead

**Best for**: Customer service bots, content generation tools, applications where response depends on request type

---

**Routing = Categorize first, then send to specialized pipeline for optimized processing**
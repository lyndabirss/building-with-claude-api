# Parallelization Workflows - Key Points

## The Problem with Complex Single Prompts

**Naive approach**: Single prompt asking Claude to choose material (metal, polymer, ceramic, composite, elastomer, wood)
- Too much heavy lifting in one request
- Unreliable without specific criteria

**Improved but flawed**: One massive prompt with detailed criteria for all materials
- Claude juggles too many considerations simultaneously
- Leads to confusion and suboptimal results

## The Parallelization Solution

### How It Works
1. Send same image to Claude multiple times **simultaneously**
2. Each request evaluates ONE material with specialized criteria
3. Claude evaluates each material independently
4. Aggregate all analyses into final recommendation step

### The Pattern Structure
- **Split**: Break complex task into focused sub-tasks
- **Parallelize**: Run all sub-tasks simultaneously
- **Aggregate**: Combine specialized analyses into final decision
- **Note**: Sub-tasks don't need to be identical (different prompts, tools, criteria)

## Key Benefits

**Focused Attention**
- Claude concentrates on one aspect at a time
- More thorough and accurate analysis per material

**Easier Optimization**
- Test and improve each prompt independently
- Refine specific evaluations without affecting others

**Better Scalability**
- Add new materials easily (just add another parallel request)
- No need to rewrite existing prompts

**Improved Reliability**
- Reduces cognitive load on AI model
- More consistent, reliable results

## When to Use Parallelization

**Look for these signals:**
- Complex decisions with independent evaluations
- Multiple criteria to consider
- Comparing several options
- Decisions involving different domains of expertise

**Key requirement**: Sub-tasks must operate independently and contribute distinct analysis

---

**Parallelization = Split complex tasks into focused parallel requests, then aggregate results**
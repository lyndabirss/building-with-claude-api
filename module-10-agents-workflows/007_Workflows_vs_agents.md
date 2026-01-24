# Workflows vs Agents - Key Points

## What Are Workflows?

**Predefined series of calls to solve known problems**
- Use when you can picture the flow of steps ahead of time
- Know exact sequence needed to complete task
- Break big task into smaller, specific subtasks
- Each step focuses on single area for precision

## What Are Agents?

**Claude gets basic tools and formulates its own plan**
- Don't know exact tasks that will be provided
- System needs to be adaptive
- Creatively combines tools in unexpected ways
- Handles wide variety of challenges

## Benefits of Workflows

✓ Claude focuses on one subtask at a time → higher accuracy
✓ Easier to evaluate and test (know each exact step)
✓ Predictable and reliable execution
✓ Better for specific, well-defined problems

## Benefits of Agents

✓ More flexible user experience
✓ Flexible task completion - combines tools in unexpected ways
✓ Handles novel situations not anticipated during development
✓ Can ask users for additional input when needed

## Downsides of Workflows

✗ Less flexible - dedicated to specific task types
✗ More constrained UX - need exact inputs to flow
✗ Require more upfront planning and design work

## Downsides of Agents

✗ Lower successful task completion rate
✗ Harder to instrument, test, and evaluate (don't know step sequence)
✗ Less predictable behavior

## When to Use Each Approach

**Primary engineering goal**: Solve problems reliably

**General recommendation**: **Always focus on workflows where possible, only use agents when truly required**

**Choose Workflows when:**
- Well-defined processes
- Need reliability and predictability
- Production applications

**Choose Agents when:**
- Unpredictable, varied user requests
- Require creative problem-solving
- Exact requirements can't be predetermined

---

**Users care about products that work consistently, not fancy agents**
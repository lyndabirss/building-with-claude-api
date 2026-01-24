# Agents and Workflows - Key Points

## Core Distinction

**Workflows**: Predetermined series of steps for well-understood tasks
- Use when you can map out exact flow beforehand
- Best for constrained UX with specific task sets

**Agents**: Goal-oriented approach with flexible tool usage
- Use when task parameters are uncertain
- Claude determines the path to completion

## Example: Image to CAD Workflow

### The Problem
Convert user-uploaded metal part images to STEP files (3D CAD format)

### The Solution (4-Step Workflow)
1. Claude describes the object from image
2. Claude models object using CadQuery library
3. Generate rendering
4. Claude grades rendering vs. original → iterate if needed

## The Evaluator-Optimizer Pattern

Key components:
- **Producer**: Creates output (Claude + CadQuery)
- **Grader**: Evaluates against criteria
- **Feedback loop**: Returns issues to producer
- **Iteration**: Repeats until acceptance

## Why Patterns Matter

Workflow patterns = repeatable recipes for features
- Proven solutions from other engineers
- Framework for implementing your own apps
- Still requires actual code implementation

---

**Throughout this course you've been building both workflows and agents whenever Claude used tools to complete tasks.**
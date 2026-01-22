# Parallelizing Claude Code

## Core Concept
Run multiple Claude Code instances in parallel for massive productivity gains
Each instance works on different tasks simultaneously = virtual team of engineers

## The Challenge
File conflicts when multiple instances modify the same file
**Solution:** Give each instance its own separate workspace

## Git Worktrees
Perfect tool for parallel workflow
- Creates complete project copies in separate directories
- Each worktree = separate branch
- Isolated changes merge back to main branch

## Automating Worktree Creation
Have Claude handle the entire process:
1. Check if worktree already exists
2. Create new Git worktree in `.trees` folder
3. Symlink `.venv` folder (not tracked by Git)
4. Launch new VSCode instance in that directory

## Custom Slash Commands
Avoid typing long prompts repeatedly
- Add `.md` file to `.claude/commands`
- Put prompt inside file
- Use `$ARGUMENTS` as placeholder for dynamic values
- Run with `/project:filename argument`

**Example:** `/project:create_worktree feature_b`

## Parallel Development Workflow
1. Create multiple worktrees for different features
2. Launch Claude Code in each workspace
3. Assign different tasks to each instance
4. Let them work in parallel
5. Commit changes when tasks complete
6. Merge all branches back to main

## Automated Merging
Create custom merge command that:
1. Changes into worktree directory
2. Examines latest commit
3. Returns to root directory
4. Merges worktree branch
5. Handles merge conflicts automatically
6. Resolves conflicts based on context understanding

## Scaling Limits
Limited only by:
- Machine resources
- Ability to coordinate multiple tasks
- Complexity of potential merge conflicts

**Result:** Develop multiple features simultaneously vs sequentially
# git cheatsheat

## Common Git Commands

### Initialization
- `git init`: Initialize a new Git repository.

### Configuration
- `git config --global user.name "Your Name"`: Set your global username.
- `git config --global user.email "youremail@example.com"`: Set your global email.

### Basic Workflow
- `git status`: Check the status of your working directory.
- `git add <file>`: Stage changes for commit.
- `git commit -m "Commit message"`: Commit staged changes.

### Branching
- `git branch`: List branches.
- `git branch <branch-name>`: Create a new branch.
- `git checkout <branch-name>`: Switch to a branch.
- `git merge <branch-name>`: Merge a branch into the current branch.

### Remote Repositories
- `git remote add origin <url>`: Add a remote repository.
- `git push -u origin <branch-name>`: Push changes to a remote branch.
- `git pull`: Fetch and merge changes from the remote repository.

### Logs and History
- `git log`: View commit history.
- `git diff`: Show changes between commits or the working directory.

### Undoing Changes
- `git reset <file>`: Unstage a file.
- `git checkout -- <file>`: Discard changes in a file.

### Stashing
- `git stash`: Save changes temporarily.
- `git stash apply`: Reapply stashed changes.

### Cloning
- `git clone <url>`: Clone a repository.

### Deleting
- `git branch -d <branch-name>`: Delete a branch.
- `git rm <file>`: Remove a file from the repository.

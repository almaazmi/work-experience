# Introduction to Git Commands

Git is a version control system that helps track changes in your code. This guide introduces the essential Git commands every developer should know.

## Installing Git

Before you can use Git, you need to download and install it:

1. **Download Git**
   - Go to [git-scm.com](https://git-scm.com/downloads)
   - Select the appropriate version for your operating system (Windows, macOS, or Linux)
   - For Windows users: Click on the "Windows" link to download the installer

2. **Verify Installation**
   - Open a terminal or command prompt
   - Type `git --version` and press Enter
   - You should see the installed Git version number

## Setting Up Git

After installing Git, you need to configure it with your information:

```powershell
# Set your name
git config --global user.name "Your Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your_email@example.com"
```

## Basic Git Workflow

### 1. Creating a Repository

```powershell
# Initialize a new Git repository in your current directory
git init
```

### 2. Checking Status

```powershell
# Check which files are tracked, modified, or staged
git status
```

### 3. Staging Changes

```powershell
# Add a specific file to the staging area
git add filename.txt

# Add all files in the current directory
git add .
```

### 4. Committing Changes

```powershell
# Commit staged changes with a message
git commit -m "Add a descriptive message about your changes"
```

### 5. Viewing Commit History

```powershell
# See the commit history
git log

# See a simplified version of the history
git log --oneline
```

## Working with GitHub

### 1. Connecting to a Remote Repository

```powershell
# Connect your local repository to a GitHub repository
git remote add origin https://github.com/username/repository-name.git
```

### 2. Pushing Changes to GitHub

```powershell
# Push your changes to GitHub
git push -u origin main
```

Note: In newer Git versions, the default branch is called "main" rather than "master".

### 3. Pulling Changes from GitHub

```powershell
# Get updates from the remote repository
git pull origin main
```

### 4. Cloning a Repository

```powershell
# Copy a repository from GitHub to your local machine
git clone https://github.com/username/repository-name.git
```

## Branching

Branches let you work on features without affecting the main codebase.

```powershell
# Create a new branch
git branch branch-name

# Switch to a branch
git checkout branch-name

# Create and switch to a new branch (shorthand)
git checkout -b new-branch-name

# Merge a branch into your current branch
git merge branch-name
```

## Common Git Workflows

### Basic Individual Workflow

1. Make changes to your files
2. Check status: `git status`
3. Stage changes: `git add .`
4. Commit changes: `git commit -m "Description of changes"`
5. Push to GitHub: `git push`

### Feature Branch Workflow (For Teams)

1. Create a feature branch: `git checkout -b feature-name`
2. Make changes and commit them
3. Push the branch to GitHub: `git push -u origin feature-name`
4. Create a Pull Request on GitHub
5. After review, merge the Pull Request

## Git Best Practices

1. **Commit Often**: Make small, focused commits with clear messages
2. **Pull Before Push**: Always pull changes before pushing to avoid conflicts
3. **Use Meaningful Commit Messages**: Describe what you changed and why
4. **Create Branches for Features**: Keep your main branch clean by developing in feature branches
5. **Review Changes Before Committing**: Use `git diff` to review changes

## Next Steps

Now that you know the basic Git commands, try the [First Repository Exercise](first-repository-exercise.md) to practice these skills!

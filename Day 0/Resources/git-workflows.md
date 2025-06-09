# Common Git Workflows

This document outlines some common Git workflows that you might use in different scenarios.

## 1. Individual Developer Workflow

This is the simplest workflow, ideal for personal projects or when you're the only developer.

```
# Start with a fresh repository
git init
git add .
git commit -m "Initial commit"

# Connect to GitHub
git remote add origin https://github.com/username/repository.git
git push -u origin main

# Day-to-day work
git pull                                # Get latest changes
# Make your changes to files
git add .                               # Stage changes
git commit -m "Description of changes"  # Commit changes
git push                                # Push to GitHub
```

## 2. Feature Branch Workflow

This workflow is ideal for teams working on the same project.

```
# Start from the main branch
git checkout main
git pull

# Create a feature branch
git checkout -b feature/new-feature

# Work on your feature
# Make changes to files
git add .
git commit -m "Implement new feature"

# Push feature branch to GitHub
git push -u origin feature/new-feature

# On GitHub: Create a Pull Request and get it reviewed

# After PR is approved and merged, cleanup
git checkout main
git pull
git branch -d feature/new-feature
```

## 3. Git Flow

A more structured workflow for larger projects with regular releases.

```
# Feature development (similar to Feature Branch Workflow)
git checkout develop
git pull
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Implement feature"
git push -u origin feature/new-feature
# Create PR to merge into develop

# Preparing a release
git checkout develop
git pull
git checkout -b release/v1.0
# Testing and bug fixes happen here
git add .
git commit -m "Fix release bugs"
# When ready, merge to main and develop
git checkout main
git merge release/v1.0
git tag -a v1.0 -m "Version 1.0"
git push --tags
git checkout develop
git merge release/v1.0
git branch -d release/v1.0

# Hotfixes
git checkout main
git pull
git checkout -b hotfix/critical-bug
# Fix the bug
git add .
git commit -m "Fix critical bug"
# Merge to both main and develop
git checkout main
git merge hotfix/critical-bug
git tag -a v1.0.1 -m "Version 1.0.1"
git push --tags
git checkout develop
git merge hotfix/critical-bug
git branch -d hotfix/critical-bug
```

## 4. Forking Workflow

Common for open-source projects where you don't have direct write access.

```
# Fork the repository on GitHub first
# Then clone your fork
git clone https://github.com/your-username/repository.git
cd repository

# Add the original repository as "upstream"
git remote add upstream https://github.com/original-owner/repository.git

# Keep your fork updated
git fetch upstream
git checkout main
git merge upstream/main
git push

# Create a feature branch
git checkout -b feature/my-contribution
# Make changes
git add .
git commit -m "Add my contribution"
git push -u origin feature/my-contribution

# On GitHub: Create a Pull Request from your fork to the original repository
```

## Handling Merge Conflicts

Merge conflicts occur when Git can't automatically merge changes.

```
# When a merge or pull results in conflicts
git status  # Shows files with conflicts

# Open the files with conflicts and resolve them
# Look for markers like <<<<<<< HEAD, =======, and >>>>>>>

# After resolving
git add .  # Mark conflicts as resolved
git commit  # Complete the merge

# Or abort the merge if needed
git merge --abort
```

## Best Practices

1. **Pull before you push** to minimize merge conflicts
2. **Commit early and often** with clear messages
3. **Create a branch for each feature or bug fix**
4. **Keep the main branch stable** and deployable
5. **Review code** before merging to important branches
6. **Use meaningful commit messages** that explain what and why
7. **Don't commit generated files** or dependencies (use .gitignore)
8. **Regularly clean up old branches** that are no longer needed

# Git Commands Cheat Sheet

## Configuration
```
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --list
```

## Creating Repositories
```
git init
git clone <repository-url>
```

## Basic Snapshotting
```
git status
git add <file>
git add .
git commit -m "Commit message"
git reset <file>
git reset --hard
```

## Branching & Merging
```
git branch
git branch <branch-name>
git checkout <branch-name>
git checkout -b <new-branch-name>
git merge <branch-name>
git branch -d <branch-name>
```

## Remote Repositories
```
git remote add origin <repository-url>
git push -u origin <branch-name>
git pull
git fetch
```

## History & Comparison
```
git log
git log --oneline
git diff
git diff <file>
```

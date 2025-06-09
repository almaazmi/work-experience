# Git Troubleshooting Guide

This guide covers common Git issues and how to resolve them.

## Authentication Issues

### Problem: "Permission denied (publickey)" when pushing to GitHub

**Solution:**
1. Verify your SSH key is set up correctly:
   ```powershell
   ssh -T git@github.com
   ```
2. If it fails, add your SSH key to the SSH agent:
   ```powershell
   ssh-add ~/.ssh/id_ed25519
   ```
3. Or switch to HTTPS with a personal access token:
   ```powershell
   git remote set-url origin https://github.com/username/repository.git
   ```

### Problem: Git keeps asking for username and password

**Solution:**
1. Enable credential storage:
   ```powershell
   git config --global credential.helper store
   ```
2. Or use a credential manager:
   ```powershell
   git config --global credential.helper manager
   ```

## Commit Issues

### Problem: "Fatal: Not a git repository"

**Solution:**
1. Ensure you're in the correct directory
2. Initialize Git if needed:
   ```powershell
   git init
   ```

### Problem: Committed something you didn't mean to

**Solution:**
1. If not pushed yet, undo the last commit but keep changes:
   ```powershell
   git reset --soft HEAD~1
   ```
2. If you want to completely remove the last commit:
   ```powershell
   git reset --hard HEAD~1
   ```

### Problem: Need to modify the last commit message

**Solution:**
```powershell
git commit --amend -m "New commit message"
```

## Branch Issues

### Problem: "Cannot checkout branch - changes would be overwritten"

**Solution:**
1. Stash your changes first:
   ```powershell
   git stash
   git checkout other-branch
   git stash pop  # When you want to retrieve your changes
   ```

### Problem: Accidentally worked on the wrong branch

**Solution:**
1. Stash your changes:
   ```powershell
   git stash
   ```
2. Switch to the correct branch:
   ```powershell
   git checkout correct-branch
   ```
3. Apply your changes:
   ```powershell
   git stash pop
   ```

## Merge Conflicts

### Problem: Merge conflict during pull or merge

**Solution:**
1. Identify conflicted files:
   ```powershell
   git status
   ```
2. Open and edit the files, resolving the conflicts marked with `<<<<<<<`, `=======`, and `>>>>>>>`
3. After resolving:
   ```powershell
   git add .
   git commit -m "Resolve merge conflicts"
   ```
4. Or abort the merge:
   ```powershell
   git merge --abort
   ```

## Undo Changes

### Problem: Need to discard all local changes

**Solution:**
```powershell
git checkout -- .
```

### Problem: Need to revert a specific file to last commit

**Solution:**
```powershell
git checkout -- filename.txt
```

### Problem: Need to undo a pushed commit

**Solution:**
```powershell
git revert HEAD
git push
```

## Remote Repository Issues

### Problem: "Failed to push some refs"

**Solution:**
1. Pull changes first:
   ```powershell
   git pull origin main
   ```
2. Resolve any conflicts
3. Try pushing again:
   ```powershell
   git push origin main
   ```

### Problem: Need to change the remote URL

**Solution:**
```powershell
git remote set-url origin https://github.com/username/new-repository.git
```

## Git Configuration

### Problem: Need to check current configuration

**Solution:**
```powershell
git config --list
```

### Problem: Username/email is incorrect in commits

**Solution:**
```powershell
git config --global user.name "Correct Name"
git config --global user.email "correct.email@example.com"
```

## Advanced Issues

### Problem: Need to clean up repository (remove untracked files)

**Solution:**
1. Preview what will be deleted:
   ```powershell
   git clean -n
   ```
2. Delete untracked files:
   ```powershell
   git clean -f
   ```

### Problem: Repository is too large/slow

**Solution:**
1. Check large files:
   ```powershell
   git gc
   git count-objects -v
   ```
2. Consider using Git LFS for large files
3. Clean up history (advanced, use with caution):
   ```powershell
   git filter-branch --tree-filter 'rm -f large-file.bin' HEAD
   ```

Remember: If you're unsure about a Git command, especially ones that can alter history or delete files, it's always a good idea to make a backup of your repository first.

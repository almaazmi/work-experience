# First Repository Exercise

Let's practice what you've learned by creating your first Git repository and pushing it to GitHub!

## Prerequisites

Before starting this exercise, make sure you have:
1. [Installed Git](intro-to-git-commands.md#installing-git) on your computer
2. [Created a GitHub account](creating-github-account.md)
3. [Set up Git](intro-to-git-commands.md#setting-up-git) with your user information

## Exercise: Create and Share a Simple Project

### Part 1: Create a Local Repository

1. **Create a new directory for your project**
   ```powershell
   mkdir my-first-repo
   cd my-first-repo
   ```

2. **Initialize a Git repository**
   ```powershell
   git init
   ```

3. **Create a README file**
   ```powershell
   # Create and open the README file in Notepad
   notepad README.md
   ```
   
   Add some content to your README.md file:
   ```markdown
   # My First GitHub Repository
   
   This is my first GitHub repository, created as part of my programming journey.
   
   ## What I've Learned
   - How to create a GitHub account
   - Basic Git commands
   - How to create and manage repositories
   ```

4. **Add and commit your README file**
   ```powershell
   git add README.md
   git commit -m "Initial commit: Add README file"
   ```

### Part 2: Create a GitHub Repository

1. **Log in to your GitHub account**

2. **Create a new repository**
   - Click the '+' icon in the top-right corner and select 'New repository'
   - Name it "my-first-repo"
   - Add a description (optional)
   - Keep it as a public repository
   - Do NOT initialize with a README (since we already created one)
   - Click "Create repository"

3. **Connect your local repository to GitHub**
   
   GitHub will show instructions after you create the repository. Use these commands:
   ```powershell
   git remote add origin https://github.com/your-username/my-first-repo.git
   git branch -M main
   git push -u origin main
   ```

4. **Verify your repository is on GitHub**
   - Go to `https://github.com/your-username/my-first-repo`
   - You should see your README file displayed

### Part 3: Make Changes and Update Your Repository

1. **Create a simple HTML file**
   ```powershell
   # Create and open an HTML file in Notepad
   notepad index.html
   ```
   
   Add some basic HTML:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>My First GitHub Project</title>
   </head>
   <body>
       <h1>Hello, GitHub World!</h1>
       <p>This is my first project hosted on GitHub.</p>
   </body>
   </html>
   ```

2. **Add and commit your HTML file**
   ```powershell
   git add index.html
   git commit -m "Add simple HTML page"
   ```

3. **Push your changes to GitHub**
   ```powershell
   git push
   ```

4. **View your updated repository on GitHub**
   - Refresh your GitHub repository page
   - You should now see both your README.md and index.html files

### Part 4: Create a Branch and Make Changes

1. **Create and switch to a new branch**
   ```powershell
   git checkout -b add-css
   ```

2. **Create a CSS file**
   ```powershell
   # Create and open a CSS file in Notepad
   notepad styles.css
   ```
   
   Add some basic CSS:
   ```css
   body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 20px;
       background-color: #f5f5f5;
   }
   
   h1 {
       color: #333;
   }
   
   p {
       color: #666;
   }
   ```

3. **Update your HTML file to use the CSS**
   ```powershell
   # Open your HTML file to edit it
   notepad index.html
   ```
   
   Modify your HTML to include the CSS file:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>My First GitHub Project</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <h1>Hello, GitHub World!</h1>
       <p>This is my first project hosted on GitHub.</p>
   </body>
   </html>
   ```

4. **Add and commit your changes**
   ```powershell
   git add styles.css
   git add index.html
   git commit -m "Add CSS styling"
   ```

5. **Push your branch to GitHub**
   ```powershell
   git push -u origin add-css
   ```

6. **Create a Pull Request**
   - Go to your GitHub repository
   - You should see a notification about your recently pushed branch
   - Click on "Compare & pull request"
   - Add a description for your changes
   - Click "Create pull request"

7. **Merge your Pull Request**
   - Review your pull request
   - Click "Merge pull request"
   - Click "Confirm merge"

8. **Switch back to the main branch and pull the changes**
   ```powershell
   git checkout main
   git pull
   ```

Congratulations! You've now:
- Created a local Git repository
- Pushed it to GitHub
- Made changes directly to the main branch
- Created a feature branch
- Made changes in the feature branch
- Created and merged a pull request

These are the fundamental skills you'll use throughout your programming journey!

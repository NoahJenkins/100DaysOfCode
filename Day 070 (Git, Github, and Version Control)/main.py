# Git and GitHub Version Control Notes

# Git Basics in Bash:

# 1. Initialize a new Git repository:
#    git init

# 2. Check the status of your repository:
#    git status

# 3. Add files to the staging area:
#    git add <file1> <file2>

# 4. Commit changes with a descriptive message:
#    git commit -m "Your commit message"

# 5. View commit history:
#    git log

# 6. Create a new branch:
#    git branch <branch_name>

# 7. Switch to a different branch:
#    git checkout <branch_name>

# 8. Merge branches:
#    git merge <branch_name>

# 9. Resolve merge conflicts:
#    - Edit conflicted files
#    - Mark as resolved: git add <conflicted_file>
#    - Complete the merge: git merge --continue

# 10. Clone a repository from a remote URL:
#     git clone <remote_url>

# GitHub Integration:

# 1. Connect a local repository to a remote repository on GitHub:
#    git remote add origin <remote_url>

# 2. Push changes to the remote repository:
#    git push -u origin <branch_name>

# 3. Pull changes from the remote repository:
#    git pull origin <branch_name>

# 4. Fork a repository on GitHub:
#    - Click "Fork" on the GitHub repository page

# 5. Create a pull request:
#    - Push changes to your forked repository
#    - Click "New pull request" on GitHub

# 6. Review pull requests:
#    - Comment on code changes
#    - Approve or request changes

# 7. Merge pull requests:
#    - Click "Merge pull request" on GitHub

# 8. Update a fork with changes from the original repository:
#    - Add the original repository as a remote: git remote add upstream <original_repo_url>
#    - Fetch changes: git fetch upstream
#    - Merge changes into your fork: git merge upstream/main

# These are basic commands; refer to Git documentation for more advanced usage.

######################################################################################################

# Git Branching and Merging Notes:

# Branching:

# 1. Create a new branch:
#    git branch <branch_name>

# 2. Switch to the newly created branch:
#    git checkout <branch_name>

# 3. Create and switch to a new branch in one command:
#    git checkout -b <new_branch_name>

# 4. List all branches in the repository:
#    git branch

# 5. Delete a branch (only if changes are merged):
#    git branch -d <branch_name>

# Merging:

# 1. Switch to the branch where you want to merge changes:
#    git checkout <target_branch>

# 2. Merge changes from another branch:
#    git merge <source_branch>

# 3. Resolve merge conflicts:
#    - Git will mark conflicted files
#    - Edit conflicted files
#    - Mark as resolved: git add <conflicted_file>
#    - Complete the merge: git merge --continue

# 4. Fast-forward merge:
#    - Merging when no new commits have occurred on the target branch
#    - Simply move the pointer to the latest commit on the source branch

# 5. Rebase (optional, for a cleaner history):
#    - Move or combine a sequence of commits to a new base commit
#    - git rebase <base_branch>

# 6. Abort a merge or rebase:
#    - git merge --abort
#    - git rebase --abort

# 7. View a graphical representation of branches and commits:
#    git log --graph --oneline --all

# Branching Strategies:

# - Feature Branching:
#    - Create a new branch for each new feature
#    - Merge the feature branch back into the main branch when complete

# - Git Flow:
#    - Define specific branches for features, releases, and hotfixes
#    - Follow a defined workflow for a structured development process

# These are basic commands; refer to Git documentation for more advanced usage.

######################################################################################################

# Git Forking and Pulling Notes:

# Forking:

# 1. Fork a repository on GitHub:
#    - Click "Fork" on the GitHub repository page
#    - Creates a personal copy of the repository under your GitHub account

# 2. Clone your forked repository to your local machine:
#    git clone <your_fork_url>

# 3. Add the original repository as a remote for updates:
#    git remote add upstream <original_repo_url>

# 4. Fetch changes from the original repository:
#    git fetch upstream

# Pulling:

# 1. Pull changes from the original repository into your fork:
#    git pull upstream <branch_name>

# 2. Push changes to your forked repository:
#    git push origin <branch_name>

# 3. Update your local repository with changes from your fork:
#    git pull origin <branch_name>

# Pull Requests:

# 1. Push changes to your forked repository:
#    git push origin <branch_name>

# 2. Create a pull request on GitHub:
#    - Navigate to your forked repository on GitHub
#    - Click "New pull request"

# 3. Select the branches for the pull request:
#    - Base repository: the original repository
#    - Base branch: the branch you want to merge into
#    - Head repository: your forked repository
#    - Compare branch: the branch with your changes

# 4. Review the changes and create the pull request:
#    - Add a descriptive title and comment

# 5. Discuss changes with collaborators:
#    - Comment on specific lines of code
#    - Make additional commits based on feedback

# 6. Merge the pull request:
#    - Click "Merge pull request" on GitHub
#    - Optionally, delete the branch after merging

# These are basic commands; refer to Git documentation for more advanced usage.
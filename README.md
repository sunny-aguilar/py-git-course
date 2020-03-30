# py-git-course
This repo was created to hold the course work I create while I
complete the a Coursera course. The files contained will probably be
sporadic and have no real sense of order however I will use readme
file to organize it somewhat.

Coursera course:
> Introduction to Git and Github

This course is part of a series of courses to earn the the
certification  **Google IT Automation with Python**.

## Files
The following is a list of files and their purpose:
- **u:** bash script to automate git and compilation commands
- **diff_me:** used to test the diff linux command
- **diff_me_2:** used to test the diff linux command
- **cpu_usage.py:** used to test diff command
- **cpu_usage_edit.py:** used to see edits made to original file
- **cpu_usage.diff:** diff file (patch file) created using diff to highlight differences

## Git Commands
> git config --global user.name "<name>"
- set your name to associate with commits

> git config --global user.email "<email>"
- set your email to associate with commits

> git diff <file>
- Use this command to see changes in a file
- ++ shows new additions
- -- shows replacements/removal
- --staged flag: shows staged differences

> git log
- view commits
- -p flag: see specific changes made in commits
- --stat see meta info on commits

> git commit
- commits a message
- -m flag: allows you to enter a message with the command "message"
- -a flag: stages files (but not new files)
- example: git commit -am "message>

> git show <commit id>
- show specific commits

> git add -p
- see changes to commit

> git rm <file>
- untracks and removes files from git

> git mv <file1> <file2>
- renames file1 to file1

### Undoing Things
> git restore <file>
- discards changes in working directory
- -p flag: allows you to review each change

> git reset
- removes staged files that you don't intend to commit

> git commit --ammend
- takes whatever is currently in the staging area and overwrite the previous commit

> git revert HEAD
- undoes a prior commit while keeping history of the commits in the project; in other words, it creates a new commit with inverse changes.
- this only does the last commit made

> git revert <commit id>
- undoes a prior commit that wasnt the previous one
- enter the 40 char alphanumeric string of the commit ID you want to revert to

## Branching
> git branch <branch-name>
- creates a new branch

> git checkout <branch-name>
- change over to the new branch

> git checkout -b <branch-name>
- create a new branch and switch to it

> git branch -d <branch-name>
- deletes a branch
- -D flag: forcibly delete

> git merge <branch-name>
- merges a branch into the master branch

> git merge --abort
- if there are merge conflicts, --abort can be used to abor the merge action

> git log --graph --oneline
- see git branches and merges on a text graph
- shows a summarized view of the commit history for a repo

## Github Interactions
> git clone <url>
- clone a Github repo into your local machine

> git push
- uploads local repo commits to remote repository

> git pull
- download remote repo changes

> git config --global credential.helper cache
- lets you store your credentials for a limited time
- helps in preventing having to re-enter your credentials multiple times

### Working with Remotes
Github names repote repos as "origin" when cloned
> git remote -v
- view configuations of remote

> git remote show origin
- provides even more info about remote repo

> git branch -r
- see branches remote repo is currently tracking

> git fetch
- see work done on remote branches
- does not save to local repo

> git pull
- fetches the remote copy of the current branch and automatically tries to merge it into the current local branch

> git remote
- list remote repost

> git remote show <name>
- describes a single remote repo

git remote update
- fetches the most up-to-date objects

### Solving Conflicts
> git rebase <branch>
- branch is the branch to set as the new base
- rebase is used to fast-forward changes on a branch (such as the master branch) while developing on other branches
- ![rebase_1](https://i.ibb.co/y4Cq5NX/rebase-1.png)  Rebased branch ![rebase_2](https://i.ibb.co/L9zmMfX/rebase-2.png)
# Rebased branch ![rebase_2](https://i.ibb.co/L9zmMfX/rebase-2.png)



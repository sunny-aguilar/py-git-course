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
>git clone <url>
- clone a Github repo into your local machine






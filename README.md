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



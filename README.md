# Introduction

This repository is for learning triad members to store their hackerrank challenges solutions.

# Learning Objectives

By learning with the triad, you should be able to (from easiest to hardest):

- write clean, efficient code with comments
- use Git and Github as the [source version control](https://en.wikipedia.org/wiki/Version_control) software
- understand and effectively review other people's code
- research and troubleshoot errors
- write great documentations with [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- write unit test cases to test your code
- use and enhance the [automation pipeline ](https://www.mabl.com/blog/what-is-cicd) (.github/workflows/tests.yml)

# How to Get Started

**Note: for the sake of learning, many of these instructions are vague by nature, which requires you to research or learn how to do them by yourself. Some links are provided, but internet search and Youtube are your friends. If you are truly stuck, ask other people in the Slack channel. Also not responsible for any damages that you may have caused by entering wrong commands, deleting wrong folders, etc.**

## Hackerrank Account

[Hackerrank](http://hackerrank.com/) provides coding challenges. To access these challenges, sign up for an account on the site.

## Git

if you are using MacOS or Linux, you should already have git installed. If you are using Windows, you will have to download and install it. [This guide](https://www.computerhope.com/issues/ch001927.htm) has good instructions on how to do that.

## Clone Repository

Once you have git installed, follow instructions from [this Github doc)[https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository] to clone this repository to your local machine.

Open your code editor (see below for recommendations). From this editor, open the folder that was just created (it should be named hackerrank-challenges).

## Create Your Own Branch

Git has the concept of having multiple branches - each branch is a version of the files inside the repository. See [Git Branch tutorial](https://www.atlassian.com/git/tutorials/using-branches) on how to create your own branch and push the code.

## Set Up Your Own Folder

Look for a subfolder named `template`. Make a copy of that folder and rename it to your name.

In the `your-name` folder, you will see multiple folders, each correspond to a challenge in hackerrank. Some challenges folders may not have been created at the time of writing, so please create the folder similar to the way the other folders are structured. Do the same for the template folder as well so future members can copy the new challenges.

## Work on the Challenges

As you go through the challenges on Hackerrank, copy the template code and the requirements from the website to a `*.py` file. It is better to do it this way because your code editor can check syntax errors and do some code autocompletion for you. Once you are done, you can paste it back to the website's code console area and test.

Optionally... you can write test cases for yourself for practice. See some of the test files inside the `gary/python` subfolders.

## Git Push and Peer Review

Once you are done with the challenge, copy what you have and make some comments on the code to help your reviewers understand how the code works. Commit and push your code to the Github repository using [command line](https://howchoo.com/g/mzzloty4mzm/how-to-commit-and-push-in-git) (or use [VS Code](https://www.virtualizationhowto.com/2017/08/use-git-visual-studio-code/#attachment_10347) to do it).

Once your code is on the repository, Github will run some tests on your code and will email you if any of the tests fail, and you will have to fix them. Some of these errors can be extra spaces or extra lines, no big deal, but you will still have to make corrections.

After all the errors are fixed, create a pull request which is a peer review before merging your code to the master branch. See [this tutorial](https://yangsu.github.io/pull-request-tutorial/), Creating a Pull Request section, for help. Once your pull request has been approved, you can merge. That's it!

# Recommanded Software Programs

## Code Editor
- [Visual Studio Code](https://code.visualstudio.com/) aka VSCode. [Install the python extension](https://code.visualstudio.com/docs/editor/extension-gallery) from Microsoft ([more info](https://code.visualstudio.com/docs/languages/python)). 
- [Intellij IDEA Community Edition](https://www.jetbrains.com/idea/). [Install python plugin](https://www.jetbrains.com/help/idea/managing-plugins.html) from the marketplace

## Terminals
- For Windows, once you download Git, you can use Git Bash instead of Command Prompt
- For MacOS, you can use the default terminal or [iTerm2](https://iterm2.com/)

# Best Practices

- Try not to use the User Interface (UI) too much - practice using terminal instead (or in Windows, Command Prompt or Git Bash)
- Internet Search and Youtube are your friends when troubleshooting errors
- Use keyboard shortcuts (`ctrl/cmd + C` to copy, `ctrl/cmd + A` to select all, etc.) as much as possible for practice
- Ask questions in the right Slack Channel
- Help research and answer questions from other members

# Contact

[Slack Channel](https://learningtriad.slack.com/)
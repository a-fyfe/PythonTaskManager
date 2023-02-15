# PythonTaskManager

__Overview:

__A simple Python Task Manager with an in-built login function.

__The user can login, create new users and manage existing users.

__The user can also create, modify and display tasks - i.e. use the program as a convenient Task Manager productivity tool

This program was created as an exercise in working with files, lists, functions and string handling in Python.

## Contents

* 1. Installation
* 2. Features
* 3. Usage

## 1. Installation

All files (task_manager.py, task_overview.txt, tasks.txt, user.txt, user_overview.txt) to be stored in a single folder.

Install Python (https://www.python.org/downloads/).

Using a stable IDE (e.g. VSCode), open the task_manager.py file and run file.

## 2. Features

The main menu presents the user with the following options:

o reg_user — that is called when the user selects ‘r’ to register a user.
o add_task — that is called when a user selects ‘a’ to add a new task.
o view_all — that is called when users type ‘va’ to view all the tasks
listed in ‘tasks.txt’.
o view_mine — that is called when users type ‘vm’ to view all the
tasks that have been assigned to them.

Additional functionality lies behind these core menu options, such as 'add_task' allowing the user to specify the assignee
of each task.

Certain features have been locked so that only a user logged in as 'admin' can perform them. These include registering users
and a special menu option to display user and task statistics.

## 3. Usage

The user.txt file contains a list of usernames and passwords that can be used to log in to the program upon launch.

Note: additional users can be added upon reaching the main menu post login.

The user should run the file, login and choose their desired option from the main menu to either manager users or
engage with the display and management of tasks (stored in tasks.txt).


#===Python Project - Task Manager===

# The following program is designed to allow the user to login and create, modify and track tasks. 
# For more information, see README.md

#===importing libraries===

# Importing datetime modules for later use of current day/month/year

from datetime import date
from datetime import datetime
today = date.today()
file_user = open('user.txt', 'r')

#===Login Section===

# Splitting and stripping user.txt file to allow checking for existing usernames, and then associated passwords

contents = file_user.read()
contents = contents.split()
contents = [i.strip(',') for i in contents]
users = len(contents)

username = input("Please enter your username: \n").lower()

while True:
    if username in contents:
        print("Your username is recognised.")
        passnum = contents.index(str(username))
        break
    else:
        print("Username invalid.")
        username = input("Please re-enter your username: \n")

password = input("Please enter your password: \n")

while True:
    if password == contents[passnum + 1]:
        print("Your password is correct - proceeding to task manager.\n")
        break
    else:
        print("Password invald.")
        password = input("Please re-enter your password: \n")

file_user.close()

#===Task Manager===

# Defining variables used in the below 'menu()' function

menu_input = ""
new_username = ""
new_password = ""
passconf = ""
today_task = today.strftime("%d %b %Y")
file_task = ""
username_task = ""
title_task = ""
description_task = ""
due_task = ""
complete_task = ""
task = ""
contents = ""
task_num = 0

# Defining 'reg_user()' function to register new users if user is logged in as admin

def reg_user():
    if username == "admin": # Additional 'if' statement added to ensure only verified admin user can add new users
        file_user = open('user.txt', 'r')
        print("You have chosen to register a new user.\n")
        contents = file_user.read()
        contents = contents.split()
        contents = [s.strip(",") for s in contents]
        
        new_username = input("Please enter your new username here: \n").lower()
        print (contents)

        while True:
            if new_username in contents[0::2]: # Indexing added to 'contents' list to ensure passwords not included in check for username duplicates
                print("Error: username already exists!\n")
                new_username = input("Please enter your new username here: \n").lower()
            else:
                break
        file_user.close()

        new_password = input("Please enter your new password: \n")
        passconf = input("Please confirm your password: \n")
        while True:
            if new_password == passconf:
                file_user = open('user.txt', 'a')
                file_user.write("\n" + new_username + ", " + new_password)
                print("Thank you, your new user has now been added to our system. Returning to main menu...\n")
                file_user.close()
                break
            else:
                    new_password = input("Your passwords do not match. Please re-enter your password:")
                    passconf = input("Please confirm your password: \n")
    else:
        print("You do not have permission to add new users. Returning to menu...\n")
        menu()

# Defining 'add_task()' function to add new tasks to tasks.txt

def add_task():
        username_task = input("Please enter the username to whom you are assigning the task: \n")
        title_task = input("Please enter the title of the new task: \n")
        description_task = input("Please enter a description for your new task: \n")
        due_task = input("Please enter a due date for your new task (format example: 20 Oct 2022): \n")
        complete_task = input("If your task complete (Yes or No)?: \n")
        file_task = open('tasks.txt', 'a')
        file_task.write("\n" + username_task + ", " + title_task + ", " + description_task + ", " + due_task + ", " + str(today_task) + ", " + complete_task)
        print("Your new task has been successfully created. Returning to main menu...\n")
        file_task.close()
        menu()

# Defining 'view_all()' function to show user all tasks in tasks.txt

def view_all():
    with open('tasks.txt', 'r') as file_task:
        for line in file_task:
            line.split("\n")
            task = line.split(",")
            print("______________________________________________________________\n" + "\nTask:\t\t\t\t" + task[1]+ "\nAssigned to:\t\t\t" + task[0] + "\nDate assigned:\t\t\t" + task[4] + "\nDue date:\t\t\t" + task[3] + "\nTask complete?:\t\t\t" + task[5] + "\nTask Description:\n" + task[2] + "\n______________________________________________________________\n")
            file_task.close()
    print("All tasks displayed. Returning to main menu...\n")
    menu()

# Defining 'view_mine()' function to display a given user's tasks from tasks.txt

def view_mine():
    with open('tasks.txt', 'r') as file_task:
            task_num = 0
            for line in file_task:
                line.split("\n")
                task = line.split(",")
                task_num += 1

                if username == task[0]:
                    print(f"______________________________________________________________\n" + "\nTask number:\t\t\t" + str(task_num) + "\nTask name:\t\t\t" + task[1] + "\nAssigned to:\t\t\t" + task[0] + "\nDate assigned:\t\t\t" + task[4] + "\nDue date:\t\t\t" + task[3] + "\nTask complete?:\t\t\t" + task[5] + "\nTask Description:\n" + task[2] + "\n______________________________________________________________\n")
                else:
                    continue
    file_task.close()


    # Requesting task number input from user to provide task editing options
    task_num2 = int(input("Enter the task number you wish to edit (enter '-1' to return to main menu):\n"))
    if task_num == -1:
        print("Returning to main menu...\n")
        menu()

    elif task_num2 <= task_num:
        file_new = open('tasks.txt', 'r')
        contents = file_new.read()
        contents = contents.split("\n")
        file_new.close()
        edit_type = int(input("Type '1' to mark this task as complete.\n\nType '2' to edit task details.\n\nEnter your choice:\n"))
        
        # If option '1' chosen, then user can mark task as complete (achieved by splitting tasks.txt contents multiple times to locate and update completion status)
        if edit_type == 1:
            contents[task_num2 -1] = contents[task_num2 -1].split(', ')
            if contents[task_num2 -1][5] == 'Yes': # Printing error message if task is already marked as being complete
                print("Error: task already marked as 'complete'. Returning to main menu...\n")
                menu()
            contents[task_num2 -1][5] = "Yes"
            contents[task_num2 -1] = ', '.join(contents[task_num2 -1])
            contents = '\n'.join(contents)
            file_task = open('tasks.txt', 'w')
            file_task.write(contents)
            file_task.close()
            print("Your task status has been updated.\n")

        # If option '2' chosen, then user can update either the assigned user or due date (achieved by splitting tasks.txt contents multiple times to locate and update relevant data)
        elif edit_type == 2:
            edit_type = int(input("Type '1' to update the assigned user of this task.\n\nType '2' to edit the due date.\n\nEnter your choice:\n"))
            if edit_type == 1:
                contents[task_num2 -1] = contents[task_num2 -1].split(', ')
                if contents[task_num2 -1][5] == 'Yes': # Printing error message if task is already marked as being complete
                    print("Error: task already marked as 'complete'. Returning to main menu...\n")
                    menu()
                new_username = input("What is the new username you would like to assign this task to?:\n")
                contents[task_num2 -1][0] = new_username
                contents[task_num2 -1] = ', '.join(contents[task_num2 -1])
                contents = '\n'.join(contents)
                file_task = open('tasks.txt', 'w')
                file_task.write(contents)
                file_task.close()
                print("The username assigned to your task has been updated.\n")

            if edit_type == 2:
                contents[task_num2 -1] = contents[task_num2 -1].split(', ')
                if contents[task_num2 -1][5] == 'Yes': # Printing error message if task is already marked as being complete
                    print("Error: task already marked as 'complete'. Returning to main menu...\n")
                    menu()
                new_date = input("What is the new due date for your task (format example: 20 Oct 2022):\n")
                contents[task_num2 -1][4] = new_date
                contents[task_num2 -1] = ', '.join(contents[task_num2 -1])
                contents = '\n'.join(contents)
                file_task = open('tasks.txt', 'w')
                file_task.write(contents)
                file_task.close()
                print("The due date for your task has been updated.\n")


        elif edit_type != 1 or edit_type != 2:
            print("Input invalid, returning to main menu...\n")

    print("Returning to main menu...\n")
    menu()    

# Defining 'report()' function to generate and display different usage reports
# Note: 'report_gen()' has been made separately to 'report()' so that it can be used in the background of the admin 'stats()'

def report_gen():
    incomplete_task = 0
    complete_task = 0
    date_format = "%d %b %Y"
    check_date = ""
    past_date = 0

    # Generating task_overview.txt report
    with open('tasks.txt', 'r') as file_task:
        task = file_task.read()
        task = task.split('\n')
        task_total = len(task)
        task = [i.strip(',') for i in task]
        for i in range(0, task_total):
            if task[i].split(', ')[5] == 'Yes':
                complete_task += 1
            elif task[i].split(', ')[5] == 'No':
                incomplete_task += 1
                date_string = task[i].split(', ')[3]
                check_date = datetime.strptime(date_string, date_format)
                if check_date < datetime.now():
                    past_date +=1
        p_incomplete = (incomplete_task / task_total) * 100
        p_overdue = (past_date / task_total) * 100
    file_task.close()

    file_task = open('task_overview.txt', 'w')
    file_task.write("______________________________________________________________\n" + "\nTotal number of tasks in Task Manager:\t" + str(task_total) + "\nCompleted tasks:\t\t\t\t\t\t" + str(complete_task) + "\nIncomplete tasks:\t\t\t\t\t\t" + str(incomplete_task) + "\nOverdue tasks:\t\t\t\t\t\t\t" + str(past_date) + "\nPercentage of incomplete tasks:\t\t\t" + str(p_incomplete) + "%" + "\nPercentage of incomplete tasks:\t\t\t" + str(p_overdue) + "%" + "\n\n______________________________________________________________\n")
    file_task.close()

    # Generating user_overview.txt report
    with open('user.txt', 'r') as file_user:
        user_line = file_user.read()
        user_line = user_line.split('\n')
        user_line = [i.strip(',') for i in user_line]
        user = len(user_line)
        file_user.close()

    # Creating dictionary to allow for tracking of tasks assigned to various users
    user_dict = {}
    for i in range(0, len(user_line)):
        user_dict[user_line[i].split(', ')[0]] = 0

    # Creating additional dictionaries (using original user_dict) to allow tracking of complete/incomplete/overdue tasks
    comp_dict = dict.fromkeys(user_dict)
    for i in comp_dict:
        comp_dict[i] = 0

    incomp_dict = dict.fromkeys(user_dict)
    for i in incomp_dict:
        incomp_dict[i] = 0

    overdue_dict = dict.fromkeys(user_dict)
    for i in overdue_dict:
        overdue_dict[i] = 0

    # Printing first part of user_overview.txt (total users and total tasks)
    file_user = open('user_overview.txt', 'w')
    file_user.write("______________________________________________________________\n" + "\nTotal number of users in Task Manager:\t\t\t" + str(user) + "\nTotal number of tasks in Task Manager:\t\t\t" + str(task_total) + "\n\n______________________________________________________________\n\n" + "User stats:\n\n")
    file_user.close()

    file_user = open('user_overview.txt', 'a')
    file_task = open('tasks.txt', 'r')
    task = file_task.read()
    task = task.split('\n')
    task = [i.strip(',') for i in task]

    # 'for' statement to count number of tasks assigned to individual users and add info to dictionary
    for i in range (0, task_total): 
        if task[i].split(', ')[0] in user_dict.keys():
            user_dict[task[i].split(', ')[0]] += 1
            if task[i].split(', ')[5] == "Yes":
                comp_dict[task[i].split(', ')[0]] +=1
            if task[i].split(', ')[5] == "No":
                incomp_dict[task[i].split(', ')[0]] += 1
                date_string = task[i].split(', ')[3]
                check_date = datetime.strptime(date_string, date_format)
                if check_date < datetime.now():
                    overdue_dict[task[i].split(', ')[0]] += 1

    # Looping through user_line variable to compile all data stored in dictionaries to allow for writing to user_overview.txt
    for i in range(0, user):
        p_assigned = ((user_dict[user_line[i].split(', ')[0]]) / task_total) * 100
        if user_dict[user_line[i].split(', ')[0]] != 0:
            p_complete = ((comp_dict[user_line[i].split(', ')[0]]) / (user_dict[user_line[i].split(', ')[0]])) * 100
            p_incomplete = ((incomp_dict[user_line[i].split(', ')[0]]) / (user_dict[user_line[i].split(', ')[0]])) * 100
            p_overdue = ((overdue_dict[user_line[i].split(', ')[0]]) / user_dict[user_line[i].split(', ')[0]]) * 100
        file_user.write("User:\t" + user_line[i].split(', ')[0] + "\n")
        file_user.write(f"Total assigned tasks:\t\t\t\t\t{user_dict[user_line[i].split(', ')[0]]}\n")
        if user_dict[user_line[i].split(', ')[0]] != 0:
            file_user.write(f"Percentage of total tasks assigned:\t\t{p_assigned}%\n")
            file_user.write(f"Percentage of tasks complete:\t\t\t{p_complete}%\n")
            file_user.write(f"Percentage of incomplete tasks overdue:\t{p_overdue}%\n\n")
        file_user.write("\n\n")
    file_user.close()

# The 'report()' function serves to run 'report_gen()' and return users to the main menu

def report():
    report_gen()

    print("Task Overview and User Overview reports generated.\n\nSee 'task_overview.txt' and 'user_overview.txt' for more information.\n\n")
    print("Returning to main menu...\n")
    menu()

# Defining 'stats()' function to display task and user stats if user is logged in as admin

def stats():
    if username == "admin": # Only available when user logged in as 'admin'
        report_gen() 
        with open('task_overview.txt', 'r') as file_task:
            print("Task Overview:")
            task = file_task.read()
            print(task)
            file_task.close()
        with open('user_overview.txt', 'r') as file_user:
            print("\n\n\nUser Overview:")
            user = file_user.read()
            print(user)
            file_user.close()
            print("\n\nOverviews displayed. Returning to main menu...\n")
            file_task.close()
    else:
        print("You do not have permission to view this dashboard. Returning to main menu...\n")
    menu()

# Defining main Task Manager 'menu()' function

def menu():

# Displaying menu options in clear and concise manner

    print("______________________________________________________________\n")
    print("Welcome to the Task Manager!\n\nPlease choose an option from the following list:\n")
    print("r\t-\tRegistering a user \na\t-\tAdding a task \nva\t-\tView all tasks \nvm\t-\tView my task\ngr\t-\tGenerate report\ne\t-\tExit")
    if username == "admin": # 'Secret' statistics dashboard option only appears on list when user logged in as 'admin'
        print("s\t-\tAdmin Stats Dashboard")
    print("\n______________________________________________________________\n")
    menu_input = input("Please enter your choice: \n").lower()

    if menu_input == 'r':
        reg_user()

    elif menu_input == 'a':
        add_task()

    elif menu_input == 'va':
        view_all()

    elif menu_input == 'vm':
        view_mine()

    elif menu_input == 's':
        stats()

    elif menu_input == 'gr':
        report()

    elif menu_input == 'e':
        print("______________________________________________________________\n" + "Thank you for using Task Manager. Goodbye!" + "\n______________________________________________________________\n")
        exit()

    else:
        print("______________________________________________________________\n" + "Please select a valid option from the Task Manager menu." + "\n______________________________________________________________\n")
        menu()

menu()
    
# References - sources of information used during development:

# Researched a tidy way of stripping commas from 'contents' list in 'reg_user()' function (see: line 71)
# Source: https://stackoverflow.com/questions/7984169/remove-trailing-newline-from-the-elements-of-a-string-list
# Researched how to use datetime to use current date (see: line 8)
# Source: https://www.programiz.com/python-programming/datetime/current-datetime
# Researched how to convert strings into datetime object for use in 'report()' function (see: line 231)
# Source: https://www.freecodecamp.org/news/how-to-convert-a-string-to-a-datetime-object-in-python/
# Additional info on how to use dictionaries in combination with loops found on StackOverflow (see: report_gen() function)
# Source: https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python
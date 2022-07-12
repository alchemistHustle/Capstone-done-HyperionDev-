'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
from ast import Num
from datetime import datetime

#===========Functions===============

#function for registering user. 
def reg_user():

    #we create an empty list to store our users.
    users = []

    #we open our file using the with open(). 
    with open("user.txt", "r") as userFile:

        #we use the For loop.
        for u in userFile:

            #we created a variable to store our split username and password from the txt file. 
            usern, passwd = u.split(", ")

            #we add the the usernames to our users variable using the append().
            users.append(usern)


    user_input = input ("Please enter a username: ") #we create variable to collect username from user. 

    #we use the while loop to loop through the usernames. 
    while user_input in users:
        print('Username already exist')
        user_input = input ("Please enter a username: ") #we create variable to collect username from user. 

    user_password = input ("Please enter a password: ").lower() #we create variable to collect password from user and convert it automatically to lower().
    user_password_confirmation = input ("Please enter your password again for confirmation: ").lower() #we ask again for the password from the user. 
    if user_password == user_password_confirmation: #we use the IF statement. 
        print ("Thank you your password is correct!") 
        #we create a variable to store both username and password. 
        both_input = user_input + "," + " " + user_password 
    #we open and close the file. 
        with open("user.txt", "a") as f:
            f.write(f"\n{both_input}")
    elif user_password != user_password_confirmation: #we use the ELIF statement.
        print ("Both passwords must be in same case")


    
def add_task():
    user_input = input ("Please enter a username: ") #we create a variable to collect username.
    task_title = input ("Please input the title of your task: ") #we create a variable to collect task title. 
    task_description = input ("Task description: ") #we create a variable to collect task description.
    task_due_date = (input("Please input the due date for the task in this format mm/dd/yyyy: ")) #we create a variable to store task due date. 
    current_date = (input("Please enter the current date in this format mm/dd/yyyy: ")) #we create a variable to store current date. 
    completion_status = "No" #we create a variable to store the status of the task. 
    #we open and close the file. 
    with open("tasks.txt", "a") as f:
        #we use the Format function to get a readable output. 
        f.write (f'\n{user_input}, {task_title}, {task_description}, {task_due_date}, {current_date}, {completion_status}')


def view_all():
    #we open our txt file. 
    open_file = open("tasks.txt", "r")

        #we use a For loop. 
    for line in open_file:
        split_file = line.split(",") + line.split(" ") #we create a variable to store our data and we use the .split() to split the comma and space.
        print (split_file)
    open_file.close() #we close our file. 

def view_mine():
    #we open our file. 
    open_file = open("tasks.txt", "r")

    #we create a counter variable to store our task numners.
    task_num = 0

    #we create a empty variable to store our task list. 
    task_list = []


        #we use the For Loop. 
    for line in open_file:
            
            #we split the file.
            split_file = line.split(", ")
            task_list.append(split_file)
            
            #we use the IF statement to determine what our print out would be. (It has to be correct to get the correct output)
            if split_file[0] == user_input:
                print (f"Task Number: {task_num}")
                print (f"username: {split_file[0]}")
                print(f"Task Title: {split_file[1]}")
                print (f"Task Description: {split_file[2]}")
                print (f"Task Due Date: {split_file[3]}")
                print (f"Current Date: {split_file[4]}")
                print (f"Completion Status: {split_file[5]}")
            task_num += 1
            
                
        #we close our file.
    open_file.close()
    
    #we create a variable to store our user task number. 
    user_task_num = int(input("Select a task by entering task number or -1 to return: "))

    #we make use of the IF statements. 
    if user_task_num !=-1:

        #we print the output. 
        print(task_list[user_task_num])

        #we use the IF statements. 
        if task_list[user_task_num][-1].strip("\n") !="Yes":

            #we use the with open to open and close our file. 
            with open ("tasks.txt", "w") as write2file:

                #we create a variable to store the task edit feature.
                task_edit_menu = input ('''Select one of the following Options below:\n Yes - to complete task:\n No - to edit task\n -1 (To return to the main menu): ''').lower()

                #we use the IF statement.
                if task_edit_menu == "yes":
                    
                    #the condition if its "YES"
                    task_list[user_task_num][-1] = "Yes\n"

                #we use the Elif statement to determine if the user chooses No. 
                elif task_edit_menu =="no":

                    #variable storing the question for the user.
                    question4_user = int(input("Enter 1 to edit username or 2 to edit the task due date or -1 to return the main menu: "))

                    #we use the IF statement. 
                    if question4_user == 1:

                        #variable storing the username change. 
                        username_change_question = input("Enter the new username: ")

                        #comparing both variable to create an outcome for our condition. 
                        task_list[user_task_num][0] = username_change_question
                    
                        
                    #we use the ELIF statement to. 
                    elif question4_user == 2:

                        #variable storing the task due date.
                        username_date_change = input("Enter your desired task due date in this format (10 Jan 2022): ")

                        #comparing both variable to create an outcome for our condition. 
                        task_list[user_task_num][4] = username_date_change

                    #we use the ELSE statememt and pass function. 
                    else:
                        pass
                
                #we use the FOR loop which will make the code in the ELSE work.
                for l in range(len(task_list)):

                    #we use the writelines to join the taskj list with the L list.
                    write2file.writelines(", ".join(task_list[l]))

                
        #we use the ELSE statement. 
        else:
            print ("Task is completed!")
    else:
        
        pass

#function for task_overview.    
def task_overview():
    
    #we open our tasks.txt file and storing it in the task_file variable. 
    task_file = open("tasks.txt","r")

    #we create a counter variable to use to create an increment for the numb_task variable.
    numb_task = 0

    #we create a counter variable to use to create an increment for the incomplete_task variable.
    incomplete_task = 0

    #we create a counter variable to use to create an increment for the task_incomplete_overdue variable.
    task_incomplete_overdue = 0

    #we create a counter variable to use to create an increment for the complete_task variable.
    complete_task = 0
    

    #we use the FOR loop to loop over the tasks.txt file.
    for line in task_file:

        #we use the numb_task to create an increment.
        numb_task += 1

        #we use the variable split_file to store the split file from the task_file. 
        split_file = line.strip("\n").split(", ")

        #we use the IF statement to create a condition.
        if split_file[5] == "No":
            incomplete_task +=1  #we create an increment. 
        
        #we use the else statement. 
        else:
            complete_task +=1

        #date_object variable stores the datetime.strptime library.
        date_object = datetime.strptime(split_file[4], "%d %b %Y")

        #todays_date variable stores the datetime.today() library.
        todays_date = datetime.today()

        #we use the IF statement to create a condition.
        if todays_date > date_object and split_file[5]=="No":
            task_incomplete_overdue +=1 #we create an increment. 
    
    #incomplete_task_percentage stores the calculation for the incomplete task percentage. 
    incomplete_task_percentage = (incomplete_task / numb_task) * 100

    #percentage_of_overdue_task stores the calculation for the percentage of overdue task. 
    percentage_of_overdue_task = (task_incomplete_overdue / numb_task) * 100

    #we open the task_overview.txt file to write our answer to it.
    with open("task_overview.txt", 'w') as file:

        #we write the our task_overview file.
        file.write(f"Total number of task is {numb_task}")
        
        #we write the our task_overview file.
        file.write (f"\nThe number of complete task is# {complete_task}")
       
        #we write the our task_overview file.
        file.write (f"\nthe total number of uncompleted task is {incomplete_task}")

        #we write the our task_overview file.
        file.write (f"\nthe total number of tasks that hasn't been completed and overdue is {task_incomplete_overdue}")

        #we write the our task_overview file.
        file.write(f"\nThe percentage of task that #is incomplete is {incomplete_task_percentage}%")

        #we write the our task_overview file.
        file.write(f"\nThe percentage of task that are overdue is {percentage_of_overdue_task}%")


#we define the function to be used for each user.
def for_each_user(total_numb_task, user_name):

    #task_file stores the opened tasks.txt file and reads from it.
    task_file = open ("tasks.txt", "r")

    #numb_task is an empty counter variable that will be used to create an increment. 
    numb_task = 0   

    #completed_task is an empty counter variable that will be used to create an increment.  
    completed_task =0

    #task_assigned_not_completed is an empty counter variable that will be used to create an increment.  
    task_assigned_not_completed = 0

     #percentage_task_incomplete_overdue is an empty counter variable that will be used to create an increment. 
    percentage_task_incomplete_overdue = 0

    #we use our FOR loop to loop through the opened file. 
    for line in task_file:

        #we store the stripped lined in the split_file variable. 
        split_file = line.strip("\n").split(", ")

        #we use the IF statement to create a condition. 
        if split_file[0] == user_name: 

            #we create an increment. 
            numb_task += 1

            #we use an IF statement to create a condition.
            if split_file[5] =="Yes":

                #we create an increment.
                completed_task +=1
            
            #we use the ELSE statement.
            else:

                #this creates an increment in the ELSE statement.
                task_assigned_not_completed +=1

                #date_object variable stores the datetime.strptime library.
                date_object = datetime.strptime(split_file[4], "%d %b %Y")

                #todays_date variable stores the datetime.strptime library.
                todays_date = datetime.today()

                #we create an IF statement to form a contion.
                if todays_date > date_object:

                    #this creates an increment.
                    percentage_task_incomplete_overdue +=1
    

    #percentage_task_assigned_to_user_completed stores the calculation for percentage of task assigned to user completed.
    percentage_task_assigned_to_user_completed = round ((completed_task / numb_task) * 100, 2)

    #percentage_total_task_assigned_to_user stores the calculation for percentage of total task assigned to user completed.
    percentage_total_task_assigned_to_user = (numb_task/total_numb_task) * 100

    #percentage_of_task_not_completed stores the calculation for percentage of task not completed.
    percentage_of_task_not_completed = round((task_assigned_not_completed / numb_task) * 100, 2)

    #percentage_of_overdue_not_complete_tas stores the calculation for percentage of overdue task not completed.
    percentage_of_overdue_not_complete_task = round ((percentage_task_incomplete_overdue / numb_task) * 100, 2)


    #user_data stores the FORMATED output to the user.
    user_data = (f"Total number of task assigned to {user_name} is {numb_task}")

    #user_data stores the FORMATED output to the user.
    user_data += (f"\nThe percentage of the total number of task assigned to the user is {percentage_total_task_assigned_to_user} ")

    #user_data stores the FORMATED output to the user.
    user_data += (f"\nThe percentage of task assigned to the user that is completed is {percentage_task_assigned_to_user_completed}")

    #user_data stores the FORMATED output to the user.
    user_data += (f"\nThe percentage of task asssigned to the user that is still not completed is {percentage_of_task_not_completed}")

    #user_data stores the FORMATED output to the user.
    user_data += (f"\nThe percentage of task assigned to the user that is not complete and overdue is {percentage_of_overdue_not_complete_task}")
    return user_data



 #we define a function for the user overview.
def user_overview():

    #we open the user.txt file and reads from it. 
    user_file = open ("user.txt", "r")

    #we open the task.txt file and reads from it.
    task_file = open ("tasks.txt", "r")
    
    #we create a counter variable to be use to create an increment and stores the increment in the variable.
    numb_user = 0

    #we create a counter variable to be use to create an increment and stores the increment in the variable.
    all_task = 0

    #we use the FOR loop. 
    for line in user_file:

        #we create an increment.
        numb_user +=1
    
    #we use the FOR loop.
    for line2 in task_file:

        #we create an increment.
        all_task +=1

    #we close the user_file file.
    user_file.close()
    
    #we close the task_file file.
    task_file.close()


    #we use the open and close the user_overview file using the with open.
    with open("user_overview.txt", 'w') as file:

        #we write our FORMAT output to the file.
        file.write(f"\nThe total number of task that has been generated and tracked is {all_task}")

        #we write our FORMAT output to the file.
        file.write(f"\nThe number of users registered with task_manager is {numb_user}")

        #we use open the user.txt file and store it in the user_file. 
        user_file = open ("user.txt", "r")

        #we use the FOR loop to loop over the user_file.
        for line in user_file:

            #we split the file. 
            split_user_file = line.split(", ")

            #we write to the file. 
            file.write(f"\nDetails for user {split_user_file[0]}")

            #we write to the file. 
            file.write("\n------------------------------------------\n")

            #we write to file.
            file.write(for_each_user(all_task, split_user_file[0]))


#we define a function called gen_report to use to call our function.
def gen_report():

    #we call our function.
    task_overview()

    #we call our function.
    user_overview()


#we create a define function display_stats to do the display stats feature.
def display_stats ():

    #we open and close the task_overview file and reads from it. 
    with open ("task_overview.txt", "r") as file1:
        print (file1.read())

    #we open and close the user_overview file and reads from it. 
    with open ("user_overview.txt", "r") as file2:
        print (file2.read())


#====Login Section====
#we open the user.txt file to read from it.
reading_file = open ("user.txt", "r")

#we create a boolean expression, setting the login variable to false. 
login = False

#we create an empty user_input variable to store the username.
user_input = ""  
    
#we use the while loop and set the boolean expression to false. 
while login == False:
    user_input = input ("Please enter a username: ") #the user_input stores the username.
    user_password = input ("Please enter a password: ").lower() #the user_input stores the password.

    #we use the for loop to iterate over the user.txt file.
    for line in reading_file: 
        line_split= line.split(", ") #we split the data in the file.
        if user_input == line_split[0] and user_password == line_split[1] .strip("\n"): #we use the IF statement to get the correct username and password. 
            print ("This is correct")
            login = True #we create a boolean expression setting it to true since line 27 is correct.
            break #we use the break function to stop the loop.
        elif user_input != line_split[0] and user_password != line_split[1] .strip("\n"): #we use the Elif statement.
         pass #we use the pass so the code can continue to run even if its not correct.
    
    #we user the IF statement and Boolean expression to get a factual outcome when the wrong input is inputed. 
    if login == False: 
        print ("Incorrect login details")
        reading_file.seek(0) #we use the .seek function to make the code to run again from the beginning of the data in the txt file. 

#we close our file. 
reading_file.close() 

#we use the while loop.
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate report
ds - Display stats
e - Exit
: ''').lower()

    #we use an IF statement to determine what happens on line 61.
    if menu == 'r' and user_input == "admin":
       reg_user()

    elif menu == 'r' and user_input != "admin":
        print ("only admin is allowed to register.")

    #we use the ELIF statement to determine what happens on line 87.
    elif menu == 'a':
        add_task()
    #we use the ELIF statement.
    elif menu == 'va':
        view_all()
    #we use the Elif statment. 
    elif menu == 'vm': 
        view_mine()

    elif menu == 'ds':
        display_stats()

    elif menu == 'gr':
        gen_report()


    #we use the ELIF statement.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #we use the else statement. 
    else:
        print("You have made a wrong choice, Please Try again")
'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''

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

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

#we use the while loop.
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    #we use an IF statement to determine what happens on line 61.
    if menu == 'r' and user_input == "admin":
        user_input = input ("Please enter a username: ") #we create variable to collect username from user. 
        user_password = input ("Please enter a password: ").lower() #we create variable to collect password from user and convert it automatically to lower().
        user_password_confirmation = input ("Please enter your password again for confirmation: ").lower() #we ask again for the password from the user. 
        if user_password == user_password_confirmation: #we use the IF statement. 
            print ("Thank you your password is correct!") 
        elif user_password == user_password_confirmation: #we use the ELIF statement.
            print ("Both passwords must be in same case")
        else: #we use the else statement.
            print ("Password Incorrect!")
        #we create a variable to store both username and password. 
        both_input = user_input + "," + " " + user_password 
        #we open and close the file. 
        with open("user.txt", "a") as f:
            f.write(f"\n{both_input}")
    elif menu == 'r' and user_input != "admin":
        print ("only admin is allowed to register.")
        
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    #we use the ELIF statement to determine what happens on line 87.
    elif menu == 'a':
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
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
    #we use the ELIF statement.
    elif menu == 'va':
        #we open our txt file. 
        open_file = open("tasks.txt", "r")

        #we use a For loop. 
        for line in open_file:
            split_file = line.split(",") + line.split(" ") #we create a variable to store our data and we use the .split() to split the comma and space.
            print (split_file)
        open_file.close() #we close our file. 

        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
    #we use the Elif statment. 
    elif menu == 'vm': 
        #we open our file. 
        open_file = open("tasks.txt", "r")

        #we use the For Loop. 
        for line in open_file:
            #we split the file.
            split_file = line.split(", ")
            
            #we use the IF statement to determine what our print out would be. (It has to be correct to get the correct output)
            if split_file[0] == user_input:
                print (f"username: {split_file[0]}")
                print(f"Task Title: {split_file[1]}")
                print (f"Task Description: {split_file[2]}")
                print (f"Task Due Date: {split_file[3]}")
                print (f"Current Date: {split_file[4]}")
                print (f"Completion Status: {split_file[5]}")
                
        #we close our file.
        open_file.close()
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

    #we use the ELIF statement.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #we use the else statement. 
    else:
        print("You have made a wrong choice, Please Try again")
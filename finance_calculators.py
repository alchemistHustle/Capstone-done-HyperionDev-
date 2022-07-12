import math

#the user_chooses variable is used to collect data from user.
user_chooses = (input ("please choose your preffered financial calculator, investment or bond: ")).upper()

#now we make use of the boolean statement that will be used to calculate what the user enters. 
if user_chooses == "BOND":
    int (input ("please enter the amount you are depositing: "))
    
    property_value = int (input ("enter the current value of your property: "))

    interest_rate_for_bond= int (input ("enter the interest rate: "))

    num_months_to_repay = int (input ("enter the number of months you will repay the bond: "))

    #now we divide the interest rate by 12months. 
    monthly_interest_rate_calculation = interest_rate_for_bond / 12

    #now we make use of the bond repayment formulae to get the total amount the user will have to pay.
    calculation  = (monthly_interest_rate_calculation * property_value)/(1 - (1 + monthly_interest_rate_calculation) ** (-num_months_to_repay))
    calculation1 = round (calculation , 2)
    print (calculation1)

#on this line we create an elif statement for ''investment''. 
elif user_chooses == "INVESTMENT":
    amount_deposited = int (input ("please enter an amount you would like to deposit: "))

    interest_rate = int (input ("please input the interest rate: "))

    number_of_years_of_investment = int (input ("please enter the number of years: "))

    interest_question = input ("please confirm if you want a simple or compound interest: ")

    #now we make use of the interest formulae to get the total amount the user will have to pay. 
    if interest_question == "simple":
        calculation = amount_deposited * (1+(interest_rate /100) * number_of_years_of_investment)
        print (calculation)

    if interest_question == "compound":
        calculation = round (amount_deposited * math.pow ((1+interest_rate / 100), number_of_years_of_investment) ,2 )
        print (calculation)

#if user doesnt type in the correct or needed information, our program will print this. 
else:
    print ("You have entered the invalid input, please type in your input in simple english")






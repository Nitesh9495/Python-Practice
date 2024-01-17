#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 01 Create a program that displays your name complete mailing address formatted in the manner that you would usually use it on the of an envelop. Your program does not need to read any input from the user
def address():
    print('Nitesh Chavhan')
    print('Department of Data Scientist')
    print('University of Calgary')
    print('2500 University Drive NW')
    print('Calgory','Alberta TN2 1N4')
    print('Canada')
    
    
# 02 Write a program that task the user to enter his or her name.The program should respond with a massage that say hello to the usinghis or her name
def user_name():
    user_name=input('Enter your name here: ')
    print('Hello:', user_name)
    
    
# 03 Write a program that asks the user to enter the width and length of a room. Once the values have been read. Your program should compute and display the area of the room. The length and the width will be entered as floating point numbers.Include units in your promt and output message; either feet or meters,depending on which unit you are more comfortable working with.
##Compute the area of room
#Read the input values from th user
def area():
    D=width=float(input('Enter the width here of room: '))
    length=float(input('Enter the length here of room: '))
    #comput the area of room
    area=width*length
    #display the result
    print('The area of the room is',area,'sqaure feet')

    

# 04 Creat a program that reads the length and width of a farmer's field from the users in feet. Display the area of the field in acres.
#Compute the area of a field,reporting the resul in acres.
def sqft_per_acre():
    sqft_per_acre=43560
    #Read input from the user
    length=float(input('Enter the length of field in feet: '))
    width=float(input('Enter the length of field in feet:' ))
    #compute the area in acres
    acres=length*width/sqft_per_acre
    #Display the result
    print('The area of the field is', acres,'acres')
    

    
# 5 In Many juridiction a small deposit is added to drink containers to encourage people to recycle them. In one paricular juridiction, drink containers holdinng one leter or less have a $0.10 deposit, and drink containers holding more than one litre have a $o.25 deposit.
# Write a program that reads the number of containers of each soze from the user. Your program should continue by compuing and displaying the refund thaet will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactlu two decimal places.

## Compute the refund the amount for a collection of bottles.
def refund_deposit():
    less_deposit = 0.10
    more_deposit = 0.25

    # Redad input from the user

    less = int(input('How many containers 1 liter or less do you have? '))
    more = int(input('How many containers more than 1 littre do you have? '))

    # Compute the refund amount
    refund = less * less_deposit + more * more_deposit

    # Display the result
    print('Yore total refund will be $%.2f.' % refund)
    
    
    # 6 The program that you creat for theis exetcise will begin b rading the cost of a mesl ordered at a restarant from the user. Then youre program woll compute the rax and tip for the meal. Use your local tax rate when computing the amount of tax and tip for the meal. Use youre local tax rate when copmputing the amoun of tax owing. Coputer the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the rip. Format the output so that all of the values are displayed using two decimal places


    
# Compute the tax and tip for a restuarant meal.
def tax_rate():
    tax_rate = 0.05
    tip_rate = 0.18

    # Read the cost of meal from the user
    cost = float(input('Enter the cost of the meal: '))

    # Compute the tax and the tip

    tax = cost * tax_rate
    tip = cost * tip_rate
    total = cost + tax + tip

    # Display the result
    print('The tax is% .2f and the tip is% .2f, making the total% .2f'% (tax, tip, total))
    
    
#7 Sum of the First n Positive Integers
# Write a program that reads a positive integers n from the user and then displays by the sum of all of the integers from 1 to n. The sum odfthe first n positive integers can be computed dusing formula:
# sum=(n)(n+1)/2

# Compute sum of the first n positive integers
#Read input fromthe user

def possitive_integer():
    n=int(input('Enter a positive integers:'))

    # Compute the sum
    sum = n*(n+1)/2
    print('The sum of the first',n ,'positive integers is',sum)


#8 Widgets and Gizmos
# An online retailer sells two products: widgets and gomos. Each widget weight 75 grams. Each gizmo weight 112 grams. Write a program that reads the number of widgets and the numbe of gizmos in an order from the user. Then your program should compute an display the total weight of the order.
#Online retailer sells two product
# Each weight 75 grams
# Each gizmo weight weight 112
#Oders from the users

# constants for widget and gizmo per piece

def weight_calculation():
    widget_wt = 75
    gizmo_wt = 112
    # ask user to enter the widgets and gizmos and store them
    widgets = int(input('Enter the number of widgets: '))
    gizmos = int(input('Enter the number of gizmos: '))
    # compute the total weight for the order
    total_wt = widgets * widget_wt + gizmos *gizmo_wt

    # print the total weight of the order in grams
    print('The total weight of the order is', total_wt,'grams.')


#9 Compound interest
# Pretend that you have just opened a new savings account that earns 4 percent intrest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the saingds account. Write a program that begins by reading theamount of money deposited into the account from the userr. Then your program should compute and display the amount in the savings account after 1,2and 3, years. Display each amount so that it is rouded to 2 decimal places.
#New account
# 4 percent intrest per year
def saving_ammount():
    initial_amount = float(input("Enter the initial deposit amount: $"))
    interest_rate = 4  # 4 percent interest rate

    # Calculate and display savings balance for each year
    for year in range(1, 4):
        initial_amount = initial_amount* (1 + interest_rate / 100)
        print(f"After {year} year(s), the balance is: ${initial_amount:.2f}")

        
        
        
#10 Create a program that reads two integers, a and b, from the user. Your program should compute and display:
#1) The sum of a and b
#2) The difference when b is substraction
#2) The produt of a and b
#3) ThevThe quotient when a is divided by b
#4) The remainder when a is divided by b
#5) The result of log10a
#6) The result of ab
#Hint: You will probably find the log10 function in the math module helpful


#Demonstrate Python's mathematical operators and its math module
def math_module():
    from math import log10
    a=int(input('Eenter the value of a: '))
    b=int(input('Enter the value of b: '))

    #Compute and display the sum,differece,produnt,
    #uotient and remainder


    print(a, "+", b, "is", a+b)
    print(a,"-", b, "is", a-b)
    print(a,"*",b, "is", a*b)
    print(a, "/", b, "is", a/b)
    print(a,"%", b, "is", a%b)

    #Compute the logarithm and the power
    print("The base 10 logarithm of",a, "is", log10(a))
    print(a, "^", b, "is", a**b)



#13 Making change
# Cisider the software that runs on a sekf-checkout machine. One task that it must be able to performis to determine how much change to provie when the shoper pays for a purchse with cash.
# write a program that begins by reading a number of cents from the user an integer. Then your program should compute and display the denomination of the coins that should be given using as few coins as possible. Assume that the machine is loaded with pennies, nickels, quarter, loonies and toonies.

# A one dollar coin was inroduced in Canada in 1987. It is referred to as a loonie because one siddee of the coin has a loon (a typeof bird) on it. The two dllar coin reffred to as a toonie, was introduces 9 years later. It's name is derived from the combination of the number two and thehnae of the loonie.

# Compute the minimum collection of coins neededto represent a number of cetnt.

def cents():
    cents_per_toonie=200
    cents_per_loonie=100
    cents_per_quarter=25
    cents_per_dime=10
    cents_per_nickel=5

    # Read the number of cents fom the user
    cents=int(input("enter the number number of cent: "))

    #Determine the number of toonie byy performing an integer division by 200. The compute
    #The amount of change that still needs to be considered by
    # Cpmputing the remainder after dividing by 200.

    print(" ", cents // cents_per_toonie, "toonies")
    cents = cents % cents_per_toonie

    #Repeat the process for loonies, quarter,,dimes and nickels

    print(" ", cents // cents_per_loonie, "lonnies")
    cents = cent % cents_per_loonie

    print(" ", cents // cents_per_quarter, "quarters")
    cents = cents % cents_per_quarter

    print(" ", cents // cents_per_dime, "dimes")
    cents = cents % cents_per_dime

    print(" ", cents // cents_per_nickel, "nickels")
    cents = cent % cents_per_nickel
    #Diplay the nmber of pennis
    print(" ",cents,"pennies")
    
    
    
#14 Many people think about their height in feet and inches, even in some countries that primarilu use the metric system. Write a progam thea reads a number of feet from the user, followed by a number of inches. Once these values are read, your program should compute and display the equivalentnumber of centimeters.

#Convert a height in feet and inches to centimeters
def height_in_cm():
    in_per_ft = 12
    cm_per_in = 2.54

    # Read input from the user
    print('Enter your height: ')
    feet = int(input("Enter of feet: "))
    inches = int(input('Number of inches: '))

    # Compute the equivalent number of centimeters

    cm = (feet * in_per_ft + inches) * cm_per_in

    # Display the result

    print('Youre height is centimeters is: ', cm)    
    

    
    
#Library
import tkinter as tk


#Main window
window=tk.Tk()


#window size
window.geometry('600x460')


#Window title
window.title("Nitesh's Python Portfolio")


#Lable UI
tk.Label(window,text='Python Projects', font=('Halvetica',18,'bold')).place(x=220,y=20)
tk.Label(window,text='Made By: Nitesh C', font=('Halvetica',12,)).place(x=245,y=60)

#Button
tk.Button(window,text='Address',command=address,).place(x=30,y=140,width=160,height=40)
tk.Button(window,text='User Name',command=user_name).place(x=220,y=140,width=160,height=40)
tk.Button(window,text='Area',command=area).place(x=410,y=140,width=160,height=40)
tk.Button(window,text='SQFT Per Acre',command=sqft_per_acre).place(x=30,y=210,width=160,height=40)
tk.Button(window,text='Refund Ddeposit',command=refund_deposit).place(x=220,y=210,width=160,height=40)
tk.Button(window,text='Tax Rate',command=tax_rate).place(x=410,y=210,width=160,height=40)
tk.Button(window,text='Possitive Integer',command=possitive_integer).place(x=30,y=280,width=160,height=40)
tk.Button(window,text='Weight Calculation',command=weight_calculation).place(x=220,y=280,width=160,height=40)
tk.Button(window,text='Saving Ammount',command=saving_ammount).place(x=410,y=280,width=160,height=40)
tk.Button(window,text='Math Module',command=math_module).place(x=30,y=350,width=160,height=40)
tk.Button(window,text='Cents',command=cents).place(x=220,y=350,width=160,height=40)
tk.Button(window,text='Height in CM',command=height_in_cm).place(x=410,y=350,width=160,height=40)
                                                   
                                                   
                                                   
# Ye agar nahi likhenge to to UI nahi dikhega
window.mainloop()




# In[ ]:





# In[ ]:





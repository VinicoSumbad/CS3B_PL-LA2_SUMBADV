# Creating an array to store the informations
studentInfo = []

# using .append() to add an item to the array
studentInfo.append (input("Enter First Name: "))
studentInfo.append (input("Enter Last Name: "))
studentInfo.append (input("Enter Course: "))
studentInfo.append (input("Enter Year Level: "))
studentInfo.append (input("Enter Section: "))
studentInfo.append (input("Enter Username: "))
studentInfo.append (input("Enter Password: "))

# making a pinCode variable
pinCode = ""

# using while loop to get the exact pin code, and continous to loop if it doesn't meet the required pin code
# using len for convenient access and easier way to get the number of digits
# I set the shortest pin code to 6 digits because I based it to the pin codes of banks, just like PNB, LAND BANK etc.
while True:
    pinCode = input("Enter Pin Code (Max of 8 digits only): ") # Temps the user to enter a pin code of max digit of 8 digits

    if len(pinCode) == 0:
        print("You must Enter a Pin Code, Try Again!") # if the pin code is empty, temp the user to input a pin code
    
    elif len(pinCode) > 8:
        print("Your're Pin Code is too long, Try Again!") # temps the user if  the pin code is too long
    
    elif len(pinCode) < 6:
        print("Your're Pin Code is too short, Try Again!") # also temps the user if  the pin code is too short
    
    else:
         print("Pin Code Accepted!") # prints if it meets the required pin code
         break

print("\nCONGRATULATIONS! REGISTRATION COMPLETED.\n") #Congratulates the user 


# using while loop again to continously loop the program if doesn't meet the requirements that the condition is asking
while True:
    choice = input("Do you want to log in? ").upper() # I used .upper for easier recognition, so it doesn't matter
                                                      # how they typed it.

    if choice == "YES": # if the choice is equals to "YES", it will run the code or program inside the if statement
        
        while True:
            userName = input("Input Username: ") # making a variable to store the username
            password = input("Input Password: ") # and another for password

            if userName == studentInfo[5] and password == studentInfo[6]: # condition that if the current password and username is equals to the newly typed pass and username
                print("\nUsername and Password has been Authenticated!")

                while True:
                    pin = input("Please enter you Pin Code: ")  # making a vairable for pin
                    if pin == pinCode: # same here just like in the condition ealier, checks if the current pin is equals to the newly typed pin
                       
                        print("\nREGISTERED INFO")              # printing the info using studentInfo[] and adding the number inside the square brackets
                        print(f"First Name: {studentInfo[0]}")  # example studentInfo[0] until studentInfo[5]
                        print(f"Last Name: {studentInfo[1]}")   # it starts with 0 because that's how an array works
                        print(f"Course: {studentInfo[2]}")
                        print(f"Year Level: {studentInfo[3]}")
                        print(f"Section: {studentInfo[4]}")
                        print(f"Username: {studentInfo[5]}")
                        break
                    else:
                        print("Invalid Pin Code, Try Again!") # if the user inputs invalid characters like numbers, special characters etc.
                                                              # the program will ask the user to try again
            else:
                print("Incorrect Username or Password, Try again!") # if either the username or password is incorrect it will temp the user
                                                                    # to try it again
            break
    elif choice == "NO": 
        print("EXITING, THANK YOU AND HAVE A GREAT DAY!") # if the choice is "NO", it will exit the program
        break
    else:
        print("INVALID INPUT, PLEASE ENTER YES OR NO") # if the user inputs invalid characters the program ask the user to try again.
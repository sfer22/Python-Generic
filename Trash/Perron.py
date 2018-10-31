is_integer = False

# Error handling for a non integer selection.

while is_integer is False:
    print("-------------------------------------------------------------------------------------------")
    print("Please select the number of the Test you will like to perform")
    print("1-Rapid Ping , 2-Ping , 3-Traceroute , 4-Telnet , 5-Exit")
    print("-------------------------------------------------------------------------------------------")
    test_user_selection = input("Please choose from the above: ")

    try:
        test_integer = int(test_user_selection)

    except ValueError:
        print("\nERROR!!!! The selected value is either not integer or an empty selection\n")

    else:
        is_integer = True

# Error handling for numbers outside the menu options

while test_integer <= 0 or test_integer > 5:

    print("\nERROR!!!! Please select between 1 and 5")

    # In case they try again with a non integer

    while True:
        print("\n-------------------------------------------------------------------------------------------")
        print("Please select the number of the Test you will like to perform")
        print("1-Rapid Ping , 2-Ping , 3-Traceroute , 4-Telnet , 5-Exit")
        print("-------------------------------------------------------------------------------------------")
        test_user_selection = input("Please choose from the above: ")

        try:
            test_integer = int(test_user_selection)

        except ValueError:
            print("\nERROR!!!! The selected value is either not integer or an empty selection")

        else:
            break

# Start of cases

if test_integer == 1:
    print ('Rapid Ping Selected, logging into switch core, please wait....')
    print(" enter the commands to run the ssh session, rapid ping is: 'ping routing-instance '+ CUSTOMERCODE,'-CSW-EP-1-A '+ DESTINATIONIP, ' rapid'")

elif test_integer == 2:
    print ('Ping test selected, logging into switch core, please wait....')
    print(" enter the commands to run the ssh session, ping is: 'ping routing-instance '+ CUSTOMERCODE,'-CSW-EP-1-A '+ DESTINATIONIP, ' count 5'")

elif test_integer == 3:
    print ('Traceroute test selected, logging into switch core, please wait....')
    print(" enter the commands to run the ssh session, traceroute is: 'traceroute routing-instance '+ CUSTOMERCODE,'-CSW-EP-1-A '+ DESTINATIONIP")

elif test_integer == 4:
    print ('Telnet test selected, logging into switch core, please wait....')
    print(" enter the commands to run the ssh session, telnet is: 'telnet routing-instance '+ CUSTOMERCODE,'-CSW-EP-1-A '+ DESTINATIONIP, ' port '+ PORT")

elif test_integer == 5:
    print("Good bye!!")

# End of cases

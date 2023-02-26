

print('LegoLand @ Dubai')
choice = int(input("""
            1. LegoLand Dubai
            2. LegoLand Water Park
            3. Combo Ticket
            4. 0 for Exit
    """))
if choice == 1:
    option = str(input('Enter Booking Type: [Online or Gate]: '))
    if option.lower() == 'online':
        ticket_type = 'LEGOLAND Dubai'
        booking_type = 'Online'
        ticket_price = 295
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price

        print('Ticket')
        print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
            ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

    elif option.lower() == 'gate':
        ticket_type = 'LEGOLAND Dubai'
        booking_type = 'Gate'
        ticket_price = 330
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price
        if staffOrNot.lower() == 'staff':
            discount = (70/100 * ticket_price)
            total_tickets_pric = numberoftickets * discount
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_pric))

        elif staffOrNot.lower() == 'not staff':
            total_tickets_price = numberoftickets * ticket_price
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

        else:
            print('Wrong input')
    else:
        print('Wrong value entered')
elif choice == 2:
    option = str(input('Enter Booking Type: [Online or Gate]: '))
    if option.lower() == 'online':
        ticket_type = 'LEGOLAND Water Park'
        booking_type = 'Online'
        ticket_price = 231
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price

        print('Ticket')
        print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
            ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

    elif option.lower() == 'gate':
        ticket_type = 'LEGOLAND Water Park'
        booking_type = 'Gate'
        ticket_price = 330
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price
        if staffOrNot.lower() == 'staff':
            discount = (70/100 * ticket_price)
            total_tickets_pric = numberoftickets * discount
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_pric))

        elif staffOrNot.lower() == 'not staff':
            total_tickets_price = numberoftickets * ticket_price
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

        else:
            print('Wrong input')
    else:
        print('Wrong value entered')

elif choice == 3:
    option = str(input('Enter Booking Type: [Online or Gate]: '))
    if option.lower() == 'online':
        ticket_type = 'Combo Ticket'
        booking_type = 'Online'
        ticket_price = 355
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price

        print('Ticket')
        print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
            ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

    elif option.lower() == 'gate':
        ticket_type = 'Combo Ticket'
        booking_type = 'Gate'
        ticket_price = 395
        staffOrNot = str(input('Are you a staff?: [Staff or Not Staff]: '))
        numberoftickets = int(input('Enter the Number of Tickets: '))
        total_tickets_price = numberoftickets * ticket_price
        if staffOrNot.lower() == 'staff':
            discount = (70/100 * ticket_price)
            total_tickets_pric = numberoftickets * discount
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_pric))

        elif staffOrNot.lower() == 'not staff':
            total_tickets_price = numberoftickets * ticket_price
            print('Ticket')
            print('Ticket Type: {}\nNumber Of Tickets: {}\nBooking Type: {}\nStaff or Not: {} \nTicket Price: {}\nTotal Price: {:.2f}'.format(
                ticket_type, numberoftickets, booking_type, staffOrNot, ticket_price, total_tickets_price))

        else:
            print('Wrong input')
    else:
        print('Wrong value entered')

elif choice == 0:
    print('Thank you visiting the LegoLand ')
    exit()

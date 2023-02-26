from unicodedata import category


class LegoLand:
    def __init__(self):
        self.ticket_type = ''
        self.numberoftickets = ''
        self.booking_type = ''
        self.category = ''

    def set_tickettype(self, ticket_type):
        self.ticket_type = ticket_type

    def set_numberoftickets(self, numberoftickets):
        self.numberoftickets = numberoftickets

    def set_booking_type(self, booking_type):
        self.booking_type = booking_type

    def set_category(self, category):
        self.category = category

    def get_ticket_type(self):
        return self.ticket_type

    def get_category(self):
        return self.category

    def get_booking_type(self):
        return self.booking_type

    def get_numberoftickets(self):
        return self.numberoftickets

    def calculateGateLegoLandDubai(self):
        choice = str(input('\tAre you a staff member? Use Yes or No: '))
        if choice.lower() == 'yes':
            discount = (70 / 100 * 330)
            tickets_GateLegoLandDubai = (self.numberoftickets * discount)
            return tickets_GateLegoLandDubai
        elif choice.lower() == 'no':
            tickets_GateLegoLandDubai = self.numberoftickets * 330
            return tickets_GateLegoLandDubai
        else:
            print('Wrong input')
            exit()

    def calculateGateLegoLandWaterPark(self):
        choice = str(input('\tAre you a staff member? Use Yes or No: '))
        if choice.lower() == 'yes':
            discount = (70 / 100 * 330)
            tickets_Gate_WaterPark = self.numberoftickets * discount
            return tickets_Gate_WaterPark
        elif choice.lower() == 'no':
            tickets_Gate_WaterPark = self.numberoftickets * 330
            return tickets_Gate_WaterPark
        else:
            print('wrong input')
            exit()

    def calculateGateComboTicket(self):
        choice = str(input('\tAre you a staff member? Use Yes or No: '))
        if choice.lower() == 'yes':
            discount = (70 / 100 * 395)
            tickets_Gate_ComboTicket = self.numberoftickets * discount
            return tickets_Gate_ComboTicket
        elif choice.lower() == 'no':
            tickets_Gate_ComboTicket = self.numberoftickets * 395
            return tickets_Gate_ComboTicket
        else:
            print('wrong input')
            exit()

    def calculateOnlineLegoLandDUbai(self):
        ticketsOnlineLegoLandDubai = self.numberoftickets * 295
        return ticketsOnlineLegoLandDubai

    def calculateOnlineLegolandWaterPark(self):
        ticketsOnlineWaterPark = self.numberoftickets * 231
        return ticketsOnlineWaterPark

    def calculateOnlineComboTicket(self):
        ticketsOnlineComboTicket = self.numberoftickets * 355
        return ticketsOnlineComboTicket


def main():
    user = LegoLand()
    choice = int(input(
        '\tWelcome to LegoLand @ Dubai\n\tChoose Tickets: \n\t1.LegoLand Dubai\n\t2.Legoland Water Park\n\t3.Combo Ticket\n\n\t4. 0 For Exit> '))
    if choice == 1:
        gate_online = int(input(
            '\tDo you want the Gate booking or online Booking? \n\n\tEnter 1 for Gate and 2 for Online:'))
        if gate_online == 1:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Gate'
            ticket_type = 'LegoLand Dubai'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 330\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateGateLegoLandDubai()))
            main()
        elif gate_online == 2:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Online'
            ticket_type = 'LegoLand Dubai'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 295\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateOnlineLegoLandDUbai()))
            main()

        else:
            main()
    elif choice == 2:
        gate_online = int(input(
            '\tDo you want the Gate booking or online Booking? \n\n\tEnter 1 for Gate and 2 for Online:'))
        if gate_online == 1:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Gate'
            ticket_type = 'LegoLand Water Park'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 330\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateGateLegoLandWaterPark()))
            main()
        elif gate_online == 2:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Online'
            ticket_type = 'LegoLand Water Park'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 231\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateOnlineLegolandWaterPark()))
            main()

        else:
            main()

    elif choice == 3:
        gate_online = int(input(
            '\tDo you want the Gate booking or online Booking? \n\n\tEnter 1 for Gate and 2 for Online:'))
        if gate_online == 1:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Gate'
            ticket_type = 'Combo Ticket'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 395\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateGateComboTicket()))
            main()
        elif gate_online == 2:
            category = str(
                input('\tAre you a staff member? Use Staff or Not Staff: '))
            booking_type = 'Online'
            ticket_type = 'Combo Ticket'
            no = int(input('\tEnter the numbe of tickets needed: '))
            user.set_booking_type(booking_type)
            user.set_category(category)
            user.set_numberoftickets(no)
            user.set_tickettype(ticket_type)
            user.get_booking_type()
            user.get_category()
            user.get_ticket_type()
            user.get_numberoftickets()

            print('\t\tThank You. Your ticket is here: \n\n\t\tTicket Type: {}\n\t\tNumber of tickets: {}\n\t\tBooking Type: {}\n\t\tStaff or Not: {}\n\t\tTickets Price: 355\n\t\tTotal Price: {:.2f}\n\n'.format(
                user.get_ticket_type(), user.get_numberoftickets(), user.get_booking_type(), category,  user.calculateOnlineComboTicket()))
            main()

        else:
            main()

    elif choice == 0:
        print('Thank you for checking on us.')
        exit()


if __name__ == '__main__':
    main()

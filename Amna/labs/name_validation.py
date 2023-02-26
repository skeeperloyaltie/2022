


class NameValidation:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_lastName(self):
        return self.last_name

    def get_firstName(self):
        return self.first_name

    def check_names(self):
        if len(self.first_name) and len(self.last_name) < 3:
            print(
                'Not Valid \nYour first name and last name should have at least 3 characters each.')
        elif self.first_name.isnumeric() and self.last_name.isnumeric() == True:
            print(
                'Not valid name. \nYou should only use alphabets for the first name and last name.')
        else:
            print('Valid Name')
            print('\n\tFirst Name: {} \n\tLast Name: {}'.format(
                self.first_name, self.last_name))


def main():
    fName = input('Enter First Name: ')
    lName = input('Enter Last Name: ')

    v = NameValidation()
    v.set_first_name(fName)
    v.set_last_name(lName)
    v.get_firstName()
    v.get_lastName()

    print(v.check_names())


if __name__ == '__main__':
    main()

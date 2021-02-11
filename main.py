""" Greet users and ask for their name. Ask user what home currency
they have and print out conversion table based on their selected home currency.
The main menu is printed and asks users for their selected option.
"""

conversions = {
    "USD": 1,
    "EUR": .9,
    "CAD": 1.4,
    "GBP": .8,
    "CHF": .95,
    "NZD": 1.66,
    "AUD": 1.62,
    "JPY": 107.92
}

home_currency = ''


def print_menu():
    """
    Print the main menu options.
    :return: Dictionary of main menu choices.
    """

    print("Main Menu")

    # Dictionary containing menu options
    menu_options = {
        1: 'Print Average Rent by Location and Property '
           'Type',
        2: 'Print Minimum Rent by Location and Property '
           'Type',
        3: 'Print Maximum Rent by Location and Property '
           'Type',
        4: 'Print Min/Avg/Max by Location',
        5: 'Print Min/Avg/Max by Property Type',
        6: 'Adjust Location Filters',
        7: 'Adjust Property Type Filters',
        8: 'Load Data',
        9: 'Quit'}

    # Print main menu options
    for option_number, option in menu_options.items():
        print(f"{option_number} - {option}")

    return menu_options


class DataSet:
    header_max_length = 30
    copyright = "No copyright has been set"

    def __init__(self, header=""):
        try:
            self.header = header
        except ValueError:
            self.header = ""

        self._data = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        if len(header) <= DataSet.header_max_length:
            self._header = header
        else:
            raise ValueError("Header must be <= 30 characters")


def menu(dataset: DataSet):
    """
    Display the main menu and obtain users selection.
    :return:
    """

    # Print Currency Options
    currency_options(home_currency)

    # Print Copyright
    print(f"\n\n{dataset.copyright}")

    # Print Header
    print(f"{dataset.header}")

    # Print Main Menu
    main_menu = print_menu()

    # Ask the user for main menu selection
    while True:
        try:
            selected_option = int(input("What is your choice? "))
        except ValueError:
            print_menu()
            print("Try again. Please enter a valid number only.")
            continue
        if selected_option < 1 or selected_option > 9:
            print_menu()
            print("Try again. Please select a number from "
                  "1-9.")
            continue
        if selected_option == 9:
            print("Goodbye! See you next time")
            break

        print(f"Sorry, '{main_menu[selected_option]}' "
              f"functionality is not implemented yet.")
        break


def currency_converter(quantity: float, source_curr: str,
                       target_curr: str):
    """
    Convert from one currency to another.
    :param quantity:
    :param source_curr:
    :param target_curr:
    :return: source currency, target currency, conversion value
    """

    # Test to see if the currencies selected are in the dictionary
    if source_curr not in conversions or target_curr not in \
            conversions or quantity <= 0:
        raise KeyError

    source_in_usd = quantity / conversions[source_curr]

    target_currency_converted = source_in_usd * conversions[target_curr]

    return target_currency_converted


def unit_test():
    """
    Test currency converter function to see if it meets requirements.
    :return:
    """

    try:
        currency_converter(1, "USE", "USD")
    except KeyError:
        print("PASS: Invalid Source Currency Raises ValueError")
    else:
        print("FAIL: Invalid Source Currency Does Not Raise Error")
    try:
        currency_converter(1, "USD", "USE")
    except KeyError:
        print("PASS: Invalid Target Currency Raises ValueError")
    else:
        print("FAIL: Invalid Target Currency Does Not Raise ValueError")
    if currency_converter(10, "USD", "GBP") == 8:
        print("PASS: Conversion from USD to GBP")
    else:
        print("FAIL: Conversion from USD to GBP")
    if currency_converter(2.8, "CAD", "USD") == 2:
        print("PASS: Conversion from CAD to USD")
    else:
        print("FAIL: Conversion from CAD to USD")
    if currency_converter(1.8, "EUR", "CAD") == 2.8:
        print("PASS: Conversion from EUR to CAD")
    else:
        print("FAIL: Conversion from EUR to CAD")


def class_unit_test():
    test1 = DataSet()
    test2 = DataSet("Less than 30 characters")
    test3 = DataSet("More than 30 characters long is not going to work")
    test4 = DataSet()
    test5 = DataSet()

    if test1.header == "":
        print("Testing constructor with default parameter: Pass")
    else:
        print("Testing constructor with default parameter: Fail")
    if test2.header == "Less than 30 characters":
        print("Testing constructor with valid header argument: Pass")
    else:
        print("Testing constructor with valid header argument: Fail")
    if test3.header == "":
        print("Testing constructor with invalid header argument: Pass")
    else:
        print("Testing constructor with invalid header argument: Fail")
    try:
        test4.header = "This should work"
        if test4.header == "This should work":
            print("Testing setter with valid assignment: Pass")
    except ValueError:
        print("Testing setter with valid assignment: Fail")
    try:
        test5.header = "This should not work since more than 30"
        if test5.header == "This should not work since more than 30":
            print("Testing setter with invalid assignment: Fail")
    except ValueError:
        print("Testing setter with invalid assignment: Pass")
    DataSet.copyright = "copyright Matt Seminara unit test"
    if DataSet.copyright == "copyright Matt Seminara unit test":
        print("Checking that I can access Dataset.copyright: Pass")
    else:
        print("Checking that I can access Dataset.copyright: Fail")
    test6 = DataSet()
    if test6.copyright == "copyright Matt Seminara unit test":
        print("Setting Dataset.copyright = 'copyright Matt Seminara "
              "unit test'")
        print("Checking that I can access copyright after creating an object: Pass")
    else:
        print("Checking that I can access copyright after creating an object: Fail")


def currency_options(base_currency: str):
    print(f"Options for converting from {base_currency}:")

    currency_list = [currency for currency in conversions]

    currency_list.remove(base_currency)

    currency_list.insert(0, base_currency)

    quantities = range(10, 91, 10)

    # Print Header Line
    for currency in currency_list:
        print(f"{currency:10}", end=' ')

    for quantity in quantities:
        print()
        for currency in currency_list:
            print(f"{currency_converter(quantity, base_currency,currency):<10.2f}", end=' ')


def main():
    """
    Obtain the user's name and greet them. After welcoming the user,
    display the main menu and ask for users selection while
    responding accordingly.
    :return:
    """

    # Ask the user for their name and greet them
    name = input("Hello, please enter your name: ")
    print(f"Hey {name}, welcome to our class project!")

    # Select currency
    global home_currency

    while home_currency not in conversions:
        home_currency = input("What is your home currency?")

    DataSet.copyright = "copyright Matthew Seminara"
    air_bnb = DataSet()
    while True:
        try:
            if air_bnb.header == "":
                air_bnb.header = input("Enter a header for the menu:")
            break
        except ValueError:
            continue

    # Print main menu and ask for users input
    menu(air_bnb)


if __name__ == '__main__':

    main()

import re

# It takes a number and a dictionary of patterns and returns the prefix of the number that is in the
# dictionary.


class Teloperator:
    def __init__(self, name, data, number):
        """
        :param name: The name of the operator
        :param data:  list of offer price 
        :param number: The phonenumber
        """
        self.name = name
        self.data = data
        self.number = number
# this function looks for a parsed number in the operator list number
# return : dic

    def patternSearch(self, pattern_number):
        """
        It takes a pattern number as an argument and returns a dictionary with the name of the pattern,
        the pattern number, and the pattern itself
        :param pattern_number: The pattern number you want to search for
        :return: A dictionary with the name, key, and value of the pattern.
        """
        for key, val in self.data.items():
            if pattern_number == key:
                return {'name': self.name, 'key': key, 'val': val}

    def findPrefix(self):
        """
        It takes the number and iterates through it, adding each digit to the pattern_number variable. 
        Then it searches for the pattern_number in the dictionary. 
        If it finds a match, it returns the result. 
        If it doesn't find a match, it continues to the next digit
        :return: The prefix of the number that is in the dictionary.
        """
        pattern_number = ''
        result = ''
        for str in [*self.number]:
            pattern_number = pattern_number+str
            search_result = self.patternSearch(pattern_number)
            if search_result is not None:
                result = search_result
        return result


def findCheaperOperator(operator_list):
    """
    It takes a list of operators and returns the cheapest offer for the given prefix
    :param operator_list: list of operators
    :return: A dictionary with the cheapest operator and the cost of the call.
    """
    offer_list = []
    for operator in operator_list:
        result = operator.findPrefix()
        if result != '':
            offer_list.append(result)
    lower_cost = float(offer_list[0]['val'])
    cheaper_operator = offer_list[0]
    for item in offer_list:
        offer_cost = float(item['val'])
        if offer_cost < lower_cost:
            lower_cost = offer_cost
            cheaper_operator = item
    return cheaper_operator


def enterYourNumber():
    """
    It takes a phone number as input, validates and is 11 characters long , and returns it without +.
    :return: the dialed_number variable.
    """
    print(chr(27) + "[2J")
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    while True:
        dialed_number = input('Please Enter Your Phone Number: ')
        if re.search(validate_phone_number_pattern, dialed_number) is not None and len(dialed_number) == 11:
            dialed_number = dialed_number.replace('+', '')
            break
        else:
            print(
                f"{WARNING}Please Enter 11 Digits Phone number with correct format  +xxxxxxxxxxx {ENDC} ")
    return dialed_number


def yourNumber(number):
    """
    If the number is a valid phone number and is 11 characters long, remove the + sign and return the
    number
    :param number: The phone number you want to send the message to
    :return: The  str number is being returned.
    """
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    if re.search(validate_phone_number_pattern, number) is not None and len(number) == 11:
        number = number.replace('+', '')
    return number

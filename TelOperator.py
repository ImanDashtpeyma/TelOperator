import re

"""
    Name : class Teloperator     
"""
class Teloperator:
    def __init__(self, name, data, number):
        self.name = name
        self.data = data
        self.number = number
# this function looks for a parsed number in the operator list number
# return : dic

    def patternSearch(self, pattern_number):
        for key, val in self.data.items():
            if pattern_number == key:
                return {'name': self.name, 'key': key, 'val': val}
# Parse input number to find the longest pattern in the operator class number list
# return:str

    def findPrefix(self):
        pattern_number = ''
        result = ''
        for str in [*self.number]:
            pattern_number = pattern_number+str
            search_result = self.patternSearch(pattern_number)
            if search_result is not None:
                result = search_result
        return result


# This function looking for cheapest operator to offer to user
# operator_list: is list of Teloperator class
# return : dic like  {'name': str, 'key': str, 'val': float}
def findCheaperOperator(operator_list):
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

# this function have got and validate the user input number
# return: str
def enterYourNumber():
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




# Function for unit test because the terminal event is not working in unit test
# return:str
def yourNumber(number):
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    if re.search(validate_phone_number_pattern, number) is not None and len(number) == 11:
        number = number.replace('+', '')
    return number

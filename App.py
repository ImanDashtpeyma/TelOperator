import json
from TelOperator import *

#load Data from Json file we assume that the a,b,c,d,... operators send data  like standard API
a_operator = json.load(open('A.json'))
b_operator = json.load(open('B.json'))
#c_operator = json.load(open('C.json'))
#d_operator = json.load(open('D.json'))


# dialed_number = '+4673212345'


#het user number with area code 
dialed_number=enterYourNumber()

#operator_list keeps a list of candidate operators 
operator_list = [
    Teloperator('A', a_operator, dialed_number),
    Teloperator('B', b_operator, dialed_number),
    #Teloperator('C', c_operator, dialed_number),
    #Teloperator('D', d_operator, dialed_number),
]


#find cheapest operator 
best_price = findCheaperOperator(operator_list)
print(
    f"Operator {best_price['name']} has {best_price['val']} call cost per minute for your number {dialed_number} ")

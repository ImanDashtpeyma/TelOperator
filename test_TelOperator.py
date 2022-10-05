import unittest
import json
import  TelOperator

# The class TelOperator has two methods: yourNumber and findCheaperOperator
class TestTelOperator(unittest.TestCase):
    def test_enterYourNumber(self):      
        """
        The function takes a string as an argument and returns a string.
        """
        self.assertAlmostEqual(
            TelOperator.yourNumber('+4673212345'), '4673212345')      
        
        
    def test__findCheaperOperator(self):
        """
        It takes a list of operators and returns the cheapest operator
        """
        
        a_operator = json.loads('{"46732": 1.6,"1": 0.92}')       
        b_operator = json.loads('{"467": 1.5,"1": 0.92}')
        operator_list = [
        TelOperator.Teloperator('A', a_operator, '4673212345'),
        TelOperator.Teloperator('B', b_operator, '4673212345')
        ]               
        self.assertAlmostEqual(
            TelOperator.findCheaperOperator(operator_list), {'name': 'B', 'key': '467', 'val': 1.5})
            
        
        
        if __name__ == '__main__':
            unittest.main()
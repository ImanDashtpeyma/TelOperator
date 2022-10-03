import unittest
import json
import  TelOperator

class TestTelOperator(unittest.TestCase):
    def test_enterYourNumber(self):      
        self.assertAlmostEqual(
            TelOperator.yourNumber('+4673212345'), '4673212345')      
        
        
    def test__findCheaperOperator(self):
        
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
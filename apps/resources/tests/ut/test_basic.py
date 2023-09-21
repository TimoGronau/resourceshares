from django.test import TestCase

class TestBasicCalculation(TestCase):
    def test_basic_sum(self): #test_<unittestname>
        #Arrange
        x = 1
        y = 4
        expected_output = 5
        #Act
        result = x + y
        #Assert
        self.assertEqual(result, expected_output)
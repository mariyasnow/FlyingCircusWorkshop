#################
# @file - test_witch.py
# @author - Mariya Snow <mariyasnow@gmail.com>
# @brief - How do we tell it's a witch?
# @usage
'''python -m unittest -v test.test_witch

test_dressed_like_one (test.test_witch.TestWitch)
should check did you dress her up like this? ... ok
test_heavier_than_a_duck (test.test_witch.TestWitch)
should check if she weights the same as a duck, she's made of wood! ... ok
test_turned_me_into_a_newt (test.test_witch.TestWitch)
should check if she turned me into a newt ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''
#################
import unittest
from Witch import Witch

class MockDuck:
   def __init__(self):
      self.weight = 2
      
class TestWitch(unittest.TestCase):
   def setUp(self):
      self.witch = Witch()
      
   def test_dressed_like_one(self):
      ''' should check did you dress her up like this?'''
      actual = self.witch.dressed_like_one('carrot')
      expected = True
      self.assertEqual(actual, expected)
      
   def test_turned_me_into_a_newt(self):
      ''' should check if she turned me into a newt'''
      actual = self.witch.turned_me_into_a_newt()
      expected = True
      self.assertEqual(actual, expected)

   def test_heavier_than_a_duck(self):
      ''' should check if she weights the same as a duck, she's made of wood!'''
      duck = MockDuck()
      actual = self.witch.heavier_than_a_duck(duck)
      expected = True
      self.assertEqual(actual, expected)

if __name__ == '__main__':
   unittest.main()

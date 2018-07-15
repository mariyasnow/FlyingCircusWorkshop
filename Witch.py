#################
# @file - Witch.py
# @author - Mariya Snow <mariyasnow@gmail.com>
# @brief - How do we tell it's a witch?
# @usage Demo tests 
#################
class Witch:
   def __init__(self):
      ''' We have found a witch, may we burn her? '''
      self.weight = 20

   def dressed_like_one(self, fake_nose):
      ''' They dressed me up like this!'''
      if fake_nose:
         return True
      return False

   def turned_me_into_a_newt(self):
      ''' I got better.'''
      return True

   def heavier_than_a_duck(self, duck):
      ''' What also floats in water?'''
      if self.weight > duck.weight:
         return True
      return False

def main():
   pass

if __name__ == '__main__':
   main()

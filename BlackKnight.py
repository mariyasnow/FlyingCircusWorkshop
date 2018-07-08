#################
# @file - BlackKnight.py
# @author - Mariya Snow <mariyavsnow@gmail.com>
# @brief - Demo Generators
# @usage
'''bash-3.2$ python BlackKnight.py
python BlackKnight.py
Black Knight: None Shall Pass
Black Knight: It's just a flesh wound!
King Arthur: You're a looney
Black Knight: 'Tis but a scratch
King Arthur: You're a looney
Black Knight: I'm invincible!
King Arthur: You're a looney
Black Knight: All right, we'll call it a draw.
Black Knight: Running away, eh? You yellow bastards! Come back here and take what's coming to ya! I'll bite your legs off!
'''
#################

class BlackKnight():
   def __init__(self):
       self.right_arm = True
       self.left_arm = True
       self.right_leg = True
       self.left_leg = True

   def defend_bridge(self):
       fight = {1: self.remove_right_arm,
                2: self.remove_left_arm,
                3: self.remove_right_leg,
                4: self.remove_left_leg }

       for k,v in sorted(fight.items()):
           yield v()
           
   def remove_right_arm(self):
       print("Black Knight: It's just a flesh wound!")
       self.right_arm = False

   def remove_left_arm(self):
       print("Black Knight: 'Tis but a scratch")
       self.left_arm = False

   def remove_right_leg(self):
       print("Black Knight: I'm invincible!")
       self.right_leg = False

   def remove_left_leg(self):
       print("Black Knight: All right, we'll call it a draw.")
       self.left_leg = False

   @property
   def draw(self):
       if self.right_arm or self.left_arm or self.right_leg or self.left_leg:
           return False
       else:
           return True

   @staticmethod
   def stand_still():
       print("Black Knight: None Shall Pass")

def main():
  Cleese = BlackKnight()
  Cleese.stand_still()
  for i in Cleese.defend_bridge():
     if Cleese.draw == True:
        print("Black Knight: Running away, eh? You yellow bastards! Come back here and take what's coming to ya! I'll bite your legs off!")
     else:
        print("King Arthur: You're a looney")
           
if __name__ == '__main__':
   main()

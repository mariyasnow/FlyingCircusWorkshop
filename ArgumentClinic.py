################
# @file - ArgumentClinic.py
# @author - Mariya Snow <mariyavsnow@gmail.com>
# @brief - Demo argparse
# @usage
'''bash-3.2$ python ArgumentClinic.py -c

Oh my back hurts, it's not a very fine day and I'm sick and tired of this office.
'''
#################
import argparse
import random

def main():
   parser = argparse.ArgumentParser(description="Argument Clinic",
                                    epilog="""The sketch parodies modern consumer culture, implying
                                    that anything can be purchased, even absurd things such as arguing,
                                    abuse, or being hit over the head""")

   group = parser.add_mutually_exclusive_group()
   group.add_argument('-a', '--abuse', action='store_true', help= "Chapman's room [ABUSE]")
   group.add_argument('-arg', '--argument', action='store_true', help= "Cleese's room [ARGUMENT]")
   group.add_argument("-c", "--complaint", action='store_true', help="Complainer room[ COMPLAINT]")
   group.add_argument('-bh', '--being_hit_on_the_head', action='store_true', help= "being-hit-on-the-head lessons [BEING-HIT-ON-THE-HEAD]")



   args = parser.parse_args()

   if args.abuse:
       print(random.choice(["Don't give me that, you snotty-faced heap of parrot droppings!",
                            "Shut your festering gob, you tit! Your type really makes me puke, you vacuous, coffee-nosed, maloderous, pervert!!!",
                            "Stupid git!!"]))
   elif args.argument:
       print(random.choice(["No it isn't. It's just contradiction.",
                            "An argument is a connected series of statements intended to establish a proposition.",
                            "I'm sorry, but I'm not allowed to argue unless you've paid!",
                            "Not necessarily. I could be arguing in my spare time."]))
   elif args.complaint:
       print(random.choice(["You want to complain! Look at these shoes. I've only had them three weeks and the heels are worn right through.",
                            "If you complain nothing happens, you might as well not bother.",
                            "Oh my back hurts, it's not a very fine day and I'm sick and tired of this office."]))
   elif args.being_hit_on_the_head:
       print(random.choice(["No, no, no. Hold your head like this, then go Waaah. Try it again",
                            "What a stupid concept"]))
   else:
       print("Argument is an intellectual process. Contradiction is just the automatic gainsaying of any statement the other person makes.")



if __name__ == '__main__':
   main()

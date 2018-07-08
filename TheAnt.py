#################
# @file - TheAnt.py
# @author - Mariya Snow <mariyavsnow@gmail.com>
# @brief - Demo Logging - The Logger (Lumberjack) Song creates a log of the song
# @usage
'''
bash-3.2$ python TheAnt.py
/flying_circus:
 -rw-r--r--   1 user  staff  2777 Apr  3 00:00 LumberjackSong.log

bash-3.2$ tail LumberjackSong.log
DEBUG:TheAnt:And hangs around.... In bars???????
WARNING:TheAnt:I chop down trees, I wear high heels,
WARNING:TheAnt:Suspenders and a bra.
WARNING:TheAnt:I wish I'd been a girlie
'''
#################
import logging

def main():
   logging.basicConfig(filename='LumberjackSong.log', level=logging.DEBUG)
   log = logging.getLogger("TheAnt")
   EPISODE_NUM = 9
   logging.addLevelName(EPISODE_NUM, "CHORUS")
   def chorus(self, message, *args, **kws):
       if self.isEnabledFor(EPISODE_NUM):
           self._log(EPISODE_NUM, message, args, **kws)
   logging.Logger.chorus = chorus
   log.info("I never wanted to do this job in the first place!")
   log.info("I... I wanted to be...")
   log.info("A LUMBERJACK!")
   log.info("Leaping from tree to tree! As they float down the mighty rivers of")
   log.info("British Columbia! With my best girl by my side!")

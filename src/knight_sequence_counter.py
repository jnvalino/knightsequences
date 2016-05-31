#!/usr/bin/python

import sys

def is_vowel( keychar ):
   if keychar in 'AEIOU':
      return 1
   else:
      return 0

# static keypad assigned as a dictionary of dictionaries
keypad = {1: {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'},
          2: {1:'F', 2:'G', 3:'H', 4:'I', 5:'J'},
          3: {1:'K', 2:'L', 3:'M', 4:'N', 5:'O'},
          4: {       2:'1', 3:'2', 4:'3'       }}

def is_valid(row,col):
   return row in keypad and col in keypad[row]

def add_moves( row,col,vertical,horizontal ):
   moves = []
   if (is_valid(row-vertical,col) or is_valid(row,col-horizontal)) and is_valid(row-vertical,col-horizontal): moves += [(row-vertical,col-horizontal)]
   if (is_valid(row-vertical,col) or is_valid(row,col+horizontal)) and is_valid(row-vertical,col+horizontal): moves += [(row-vertical,col+horizontal)]
   if (is_valid(row+vertical,col) or is_valid(row,col-horizontal)) and is_valid(row+vertical,col-horizontal): moves += [(row+vertical,col-horizontal)]
   if (is_valid(row+vertical,col) or is_valid(row,col+horizontal)) and is_valid(row+vertical,col+horizontal): moves += [(row+vertical,col+horizontal)]
   return moves

def to_keychar( keylocation ):
   return keypad[keylocation[0]][keylocation[1]]

knightmoves = {}

# --- MAIN ---

# command line arguments
if len(sys.argv) == 2:
   length = int(sys.argv[1])
else:
   print "usage: %s [length]" % sys.argv[0]
   quit()

# build knightmoves table
for row in keypad.keys():
   for col in keypad[row].keys():
      knightmoves[(row,col)]  = add_moves(row,col,2,1) # 2 steps vertical, 1 step horizontal
      knightmoves[(row,col)] += add_moves(row,col,1,2) # 1 step vertical, 2 steps horizontal

# The keyresults table keeps track of the number of sequences that
# *end* with a particular keypress and contains zero, one, or two vowels.
# The sum of the tallies of all of these sequences yields the total
# number of n-key sequences.
keyresults = {}

# initialize keyresults table using each key on the keypad
for row in keypad.keys():
   for col in keypad[row].keys():
      keyresults[(row,col)] = {0:0, 1:0, 2:0} # {0 vowels, 1 vowel, 2 vowels}
      keyresults[(row,col)][is_vowel(keypad[row][col])] += 1

# build and grow keyresults table to desired length
for count in range (2,length+1):
   newresults = {}

   # traverse every row and column in the keypad
   for row in keypad.keys():
      for col in keypad[row].keys():

         # look at only legal knight moves from the current key
         for nextkey in knightmoves[(row,col)]:
            nextrow = nextkey[0]
            nextcol = nextkey[1]

            # calculate new result for this knight move
            if nextkey not in newresults: newresults[nextkey] = {0:0, 1:0, 2:0}
            for vowel in range (0,3):
               nextvowel = vowel + is_vowel(keypad[nextrow][nextcol])

               # only update if the knight move doesn't exceed 2 vowels
               if nextvowel <= 2:
                  # transfer tally of current key to the knight move
                  newresults[nextkey][nextvowel]+=keyresults[(row,col)][vowel]

   keyresults = newresults

print "Valid %d-key sequences = " % length,

keycount=0

# add up all of the key counts
for row in keypad.keys():
   for col in keypad[row].keys():
      for vowel in range(0,3):
         keycount += keyresults[(row,col)][vowel]

print keycount
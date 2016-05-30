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

# Creates bigger sequences from a sequence.
def expand( seq ):
   bigger_sequences = []
   currentkey = seq["keypath"][-1]
   row = currentkey[0]
   col = currentkey[1]
   for nextkey in knightmoves[(row,col)]:
      nextchar = to_keychar(nextkey)
      vowelcount = seq["vowels"] + is_vowel(nextchar)
      if vowelcount <= 2:
         newseq={"keypath":seq["keypath"]+[nextkey],
                 "keycode":seq["keycode"]+nextchar,
                 "vowels" :vowelcount}
         bigger_sequences += [newseq]
   return bigger_sequences

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

# initialize list with 1-key sequences
sequences = []
for row in keypad.keys():
   for col in keypad[row].keys():
      keylocation = (row,col)
      keychar = to_keychar(keylocation)
      vowels = is_vowel(keychar)
      sequence = {"keypath":[keylocation], "keycode":keychar, "vowels":vowels}
      sequences += [sequence]

# Build and grow sequences to desired length.
for count in range (2,length+1):
   new_sequences = []
   for sequence in sequences:
      new_sequences += expand(sequence)
   sequences = new_sequences

print "Valid %d-key sequences = %d" % (length, len(sequences))

for sequence in sequences:
   print sequence["keycode"]
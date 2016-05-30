#!/usr/bin/python

# static keypad assigned as a dictionary of dictionaries
keypad = {1: {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'},
          2: {1:'F', 2:'G', 3:'H', 4:'I', 5:'J'},
          3: {1:'K', 2:'L', 3:'M', 4:'N', 5:'O'},
          4: {       2:'1', 3:'2', 4:'3'       }}


def vowel_count(key_code):
   count=0
   for key in key_code:
      if key in 'aeiouAEIOU':
         count+=1
   return count

# initialize list of sequences
sequences = []

def knightmoves(from_key):

   def legal(row,col):
      return row in keypad and col in keypad[row]

   def add_moves(row,col,vertical,horizontal):
      moves = []
      if (legal(row-vertical,col) or legal(row,col-horizontal)) and legal(row-vertical,col-horizontal): moves += [(row-vertical,col-horizontal)]
      if (legal(row-vertical,col) or legal(row,col+horizontal)) and legal(row-vertical,col+horizontal): moves += [(row-vertical,col+horizontal)]
      if (legal(row+vertical,col) or legal(row,col-horizontal)) and legal(row+vertical,col-horizontal): moves += [(row+vertical,col-horizontal)]
      if (legal(row+vertical,col) or legal(row,col+horizontal)) and legal(row+vertical,col+horizontal): moves += [(row+vertical,col+horizontal)]
      return moves

   row = from_key[0]
   col = from_key[1]

   new_moves  = add_moves(row,col,2,1) # 2 steps vertical, 1 step horizontal
   new_moves += add_moves(row,col,1,2) # 1 step versical, 2 steps horizontal

   return new_moves

def key_code(from_seq):
   key_code = ""
   for key in from_seq:
      key_code += keypad[key[0]][key[1]]
   return key_code

def expand( seq ):
   newseq = []
   for nextkey in knightmoves(seq[-1]):
      if vowel_count(key_code(seq + [nextkey])) <= 2:
         newseq.append(seq + [nextkey])
   return newseq

for row in keypad.keys():
   for column in keypad[row].keys():
      sequences += [[(row,column)]]

for count in range (2,16):
   print "Generating %d-key sequences..." % count,
   new_sequences = []
   for sequence in sequences:
      new_sequences += expand(sequence)
   sequences = new_sequences
   print "found %d" % len(sequences)

for sequence in sequences:
   print key_code(sequence)

print len(sequences)
# print sequences

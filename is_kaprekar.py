"""
A Kaprekar number is one whose square can be split into two parts that add up to the original number again. The second part of the split should have the same number of digits as the original (unsquared) number. 

For instance, 45 is a Kaprekar number because 45 ** 2 = 2025 and 20 + 25 = 45.

The following definition calculates whether a base-10 number is a Kaprekar.
"""
def is_kaprekar(k):
  
  # guardian
  if type(k) != int or k <= 0:
      print "Error: please use only positive whole numbers for your argument."
      return
      
  # get the number of digits in k
  num_digits_k = len(str(k))
    
  square = k ** 2
  
  # get the number of digits in the square of k
  num_digits_square = len(str(square))
  
  
  # break the square into two segments, with the length of the second 
  # (that is, segment2) being equal to the length of k. 
  segment2 = square % (10 ** num_digits_k)
  segment1 = (square - segment2) / 10 ** (num_digits_k)

  print k == segment1 + segment2

is_kaprekar(9)              # True
is_kaprekar(45)             # True
is_kaprekar(297)            # True
is_kaprekar(4325)           # False
is_kaprekar(23)             # False
is_kaprekar(-1)             # Error
is_kaprekar(5.4)            # Error
is_kaprekar("trickster")    # Error
  
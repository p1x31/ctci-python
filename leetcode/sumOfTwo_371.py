# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	Sets each bit to 1 if one of two bits is 1
#  ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
# The simplest is to simply use the leftmost digit of the number as 
# a special value to represent the sign of the number: 0 = positive, 
# 1 = negative. For example, a value of positive 12 (decimal)
# would be written as 01100 in binary, but negative 12 (decimal)
# would be written as 11100.
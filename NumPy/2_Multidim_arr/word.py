import numpy as np

# we'll create a three-dimensional array of letters
array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]])

# and we'll use multidimensional indexing to form a word, 
# and since they are characters, we'll use string concatenation
# in this case, the order is (layer, row, column)
word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
print(word)
#indexing: accessing elements of a sequenze via [] (indexing operator)
# we can access a starting point, an ending point or a step: [start: end: step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0])

#it prints the first 4 characters of the string (start is inclusive, end is exclusive)
print(credit_number[0:4]) 
print(credit_number[5:9])

#if you leave the left part of the semi column, it takes all of the characters from the fifth above
print(credit_number[5:]) 

#if you use negative numbers, it'll count from the end:
print(credit_number[-1]) 

#to use steps, we can count by twos, threes and so on, we use this synthax:
print(credit_number[::2]) #this prints every other 2 characters

last_digits = credit_number[-4:] #here is how you can take the last four numbers:
print(f"XXXX-XXXX-XXXX-{last_digits}")

#we can also reverse the string:
print(credit_number[::-1])
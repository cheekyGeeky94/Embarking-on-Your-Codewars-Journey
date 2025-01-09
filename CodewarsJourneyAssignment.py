'''Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.'''

num = int(input('Enter a number and we will tell you if it is Even or Odd: '))

if num % 2 == 0: # if the number divided by 2 with a remainder of zero, the number is even, if 1 it is odd
    print('This is an Even number') # if true this will be the prompt of the code
else:
    print('This is an Odd number') # else, this will be the prompt of the code


'''We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?'''

num = int(input("Enter a number: ")) # Using int input so that the user enters a number and the machine recognizes it as such

numStr = str(num) # This will convert the number from an integer to a string

print(numStr) # it will print as a string; however, it will not let us know the type

print(type(numStr)) # added this function to confirm the variable type


'''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''

word = input('Enter a word and we will count the vowels in it: ')

vowels = 'aeiou'

count = 0 # count variable initialized

for character in word: # loop will iterate each char
    if character in vowels: # check if a character is in the vowel
        count +=1  #if it is the value will count it as 1
print(f'The number of vowels in this string is {count}')
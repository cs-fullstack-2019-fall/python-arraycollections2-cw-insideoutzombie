# Problem 1:
# Create code and define the variable below outside of any function.
# After you create the list variable write a function called ```stupid_array_tricks```
# that takes an array as a parameter, and performs the functions listed below in the instructions.
#
# ```
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# ```
# a) Print the 2nd and 3rd elements of the person_array using a *range*
# b) Print the last 2 elements of the person_array using a *range*
# c) Insert the new element ```Chuck``` between the 2nd (```Kevin```) and 3rd (```Erin```) element
# d) Take out the 2nd element (```Kevin```) from the list
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
def stupid_array_tricks():
    for person_array in range([1]): # !! : for indexInteger in range(startInt,storInt,stepInt)
        person_array.append(eachElement) # !! : what is eachElement?
    print(person_array) # !! : this is not in the for loop
    return person_array # !! : why print AND return? 
# stupid_array_tricks() # !! : this does not run bc of syntax errors 
# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ''
    while userInput != 'q':
        userInput = input("Try again ")
problem2()
# Problem 3:
# Create a function that uses the data list below.
# ```
# ['GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'DECENT_DATA',
# 'GOOD_DATA'
# 'BAD_DATA',
# 'GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'GOOD_DATA']
#  ```
# Write the code to do the following:
# * Print the length of the original DATA list/array (ex. ```Starting length of data list is 10```)
# * Remove all ```BAD_DATA``` from the DATA list/array
# * Print the length of the final DATA list/array (ex. ```Ending length of data list is 7```)
def problem3():
    listArr = ['GOOD_DATA',
    'DECENT_DATA',
    'BAD_DATA',
    'DECENT_DATA',
    'GOOD_DATA',
    'BAD_DATA',
    'GOOD_DATA',
    'DECENT_DATA',
    'BAD_DATA',
    'GOOD_DATA']
    print(len(listArr)) # !! : correct - partial credit 
    if listArr != 'BAD_DATA':
        return listArr # !! : this prints the entire array BUT it should be one element in the array listArr[indexInteger]
    else:
        print(listArr) # !! : this prints the entire array BUT it should be one element in the array listArr[indexInteger]
problem3()
### Problem 4:
# Use the following list of 5 numbers.
# ```score_list = [21,14,6,8,28,42,21]```
# Write the code to do the following:
# * Print the sum of the numbers (ex. ```The SUM of the numbers is 140 ```)
# * Print the maximum value from the numbers (ex. ```The MAX of the numbers is 140 ```)
# * Print the minimum value from the numbers (ex. ```The MIN value of the numbers is 6 ```)
score_list = [21,14,6,8,28,42,21]
print(sum(score_list)) # sum of the array
print(max(score_list)) # max of the array
print(min(score_list)) # min of the array
# !! : what is this?
# def zeroTo100():
#     tempArray = []
#     for eachElement in range(100):
#         tempArray.append(eachElement)
#     print(tempArray)
#     return tempArray
# zeroTo100()
### Challenge:
# Create a program that will let the User build a list words. Prompt the User for a word.
# Add the word the User enters and add it to the list.
# Allow the User to keep entering words until they enter 'x' to exit the program.
# Print the final word list prior to exiting the program.
# def twoArr(arr1, arr2):
#     while arr1 != 'x':
#     # newArray = list(range(arr1, arr2))
#     return emptyArray
# twoArr()
# arr1 = int(input('enter a wordstart '))
# arr2 = int(input('enter another word o hit x to quit '))

# Have the function PalindromeSwapper(str) take the str parameter being passed and determine
# if a palindrome can be created by swapping two adjacent characters in the string.
# If it is possible to create a palindrome, then your program should return the palindrome,
# if not then return the string -1. The input string will only contain alphabetic characters.
# For example: if str is "rcaecar" then you can create a palindrome by swapping the second and
# third characters, so your program should return the string racecar which is the final palindromic string.

# Examples
# Input: "anna"
# Output: anna
# Input: "kyaak"
# Output: kayak

def IsPalindrom(strParam):
    return strParam == strParam[::-1]


def PalindromeSwapper(strParam):
    if IsPalindrom(strParam):
        return strParam

    for i in range(0, len(strParam) - 1):
        temp = strParam[:i:] + strParam[i + 1] + strParam[i] + strParam[i + 2::]
        if IsPalindrom(temp):
            return temp

    return -1

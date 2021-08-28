# KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains k unique characters, where k will be the first character from the string. The substring will start from the second position in the string because the first character will be the integer k. For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring. If there are multiple longest substrings, then return the first substring encountered with the longest length. k will range from 1 to 6.
# Examples
# Input: "3aabacbebebe"
# Output: cbebebe
# Input: "2aabbcbbbadef"
# Output: bbcbbb

def IsValid(strParam, approprNumber):
  chars = []
  chars.append(strParam[0])

  for character in strParam:
    if character not in chars:
      chars.append(character)

  return approprNumber == len(chars)

def KUniqueCharacters(strParam):

  lenght = int(strParam[0])
  strParam = strParam[1::]
  strings = []

  for i in range(lenght, len(strParam) - lenght): # len of str for check
    for j in range(0, len(strParam) - i + 1): # start str position
      if IsValid(strParam[j:j + i:], lenght):
        if len(strings) == 0:
          strings.append(strParam[j:j + i:])
        elif len(strings[0]) < len(strParam[j:j + i:]):
          strings.clear()
          strings.append(strParam[j:j + i:])
        else :
          strings.append(strParam[j:j + i:])

  return strings[0]


# keep this function call here
print(KUniqueCharacters("2aabbacbaa"))
print(KUniqueCharacters("3aabacbebebe"))



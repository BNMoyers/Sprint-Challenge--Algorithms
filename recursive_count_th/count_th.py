'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#notes:
# if there are less than 2 letters in the string, then return 0.
# move recursively through the word two letters at a time
# return final count
def count_th(word):
    if len(word) < 2:
        return 0
    elif word[:2] == 'th':
        return count_th(word[1:]) +1 
    return count_th(word[1:])

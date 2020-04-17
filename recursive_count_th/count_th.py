'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # BASE CASE - if len(word) < 2, return 0
    if len(word) < 2:
        return 0
    # CHECK to see if first two characters == 'th'
    if word[0:2] == 'th':
        # If yes, slice off first two characters and call function again # add 1
        return count_th(word[2:]) + 1    
    else:
        # If no, slice off first character and call function again
        return count_th(word[1:])

print(count_th("abcthxyz"))

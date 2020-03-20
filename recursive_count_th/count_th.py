'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    def count_th_recursion(word, length):
        if length == len(word):
            return 0
        count = word.startswith('th', length)

        return count + count_th_recursion(word, length+1)

    return count_th_recursion(word, 0)
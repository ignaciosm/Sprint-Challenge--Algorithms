'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if word.find('th') < 0:
        # print('not found', word.find('th'))
        return 0

    count = 0

    if word.find('th') >= 0:
        # print('found in word', word.find('th'))
        word = word.replace('th', 'xx', 1)
        # print('new_word:', word)
        count += 1
        # print('count', count)

    return count_th(word) + count


test = 'abcthxyz'
print(count_th(test))

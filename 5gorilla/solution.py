
#gap penalty score
delta = -4

chars = input().split()

# kostnader
c = [[int(x) for x in input().split()] for _ in range(len(chars))]

# dict med char som KEY och index som value.
# Snabbare än .index()
# Kan säkert göras snabbare genom någon custom hash, alternativt kombinera c och letter_i

letter_i = {letter: nbr for (letter, nbr) in zip(chars, range(len(chars)))}

print(letter_i)
for p in c:
    print(p)
# Inte så många bokstäver ~ O(1)
def change_cost(letter1, letter2):
    i = letter_i.get(letter1)
    j = letter_i.get(letter2)

    return c[i][j]


# construct matrix - Needleman-Wunsch algoritm , O(nm)
def make_matrix():
    m, n = len(s), len(t)

    opt = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        opt[i][0] = delta * i
    for j in range(1, n + 1):
        opt[0][j] = delta * j
    # max from Match, insert, Delete


    for i in range(1, m + 1):
        for j in range(1, n + 1):
                opt[i][j] = max(opt[i - 1][j - 1] + change_cost(s[i - 1], t[j - 1]),
                                opt[i - 1][j] + delta,
                                opt[i][j - 1] + delta)
            #Vi kollar bakåt, från den rutan nu är i nu
    return opt


# rekonstruera strängarna, O(n+m)
# Samma tre fall
def backtrack():

    new_s, new_t = '', ''
    i, j = len(s), len(t)
    while i > 0 or j > 0:
        p
        if opt[i][j] == opt[i - 1][j - 1] + change_cost(s[i - 1], t[j - 1]):
            new_s += s[i - 1]
            new_t += t[j - 1]
            i, j = i - 1, j - 1

        elif opt[i][j] == opt[i - 1][j] + delta:
            new_s += s[i - 1]
            new_t += '*'
            i -= 1

        else:
            new_s += '*'
            new_t += t[j - 1]
            j -= 1



    return new_s[::-1], new_t[::-1]


Q = int(input())

for _ in range(1):
    s, t = input().split()

    opt = make_matrix()
    str1, str2 = backtrack()
    print(str1 + " " + str2)

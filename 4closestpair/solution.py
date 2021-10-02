'''
4
0 1
0 0
1 0
1 1

answer 1.00000
'''
'''
the output should contain a single floating point number containing the shortest distance between two players on the
battle field. The output should be a floating point number rounded to exactly 6 decimal digits'''

#     def hypot(self, other_x, other_y):
#         return math.hypot(self.x - other_x, self.y - other_y)
import math


def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


# O(n). Inner loop runs at most 15 times
#
def closest(px, delta, midx):
    Sy = [i for i in px if i[0] < midx + delta and i[0] > midx - delta]
    s_y = sorted(Sy, key=lambda k: k[1])
    #print("hello")
    min_temp = delta

    for i in range(len(s_y)):

        j = i + 1
        c = 0
        while c < 15 and j < len(s_y) and s_y[j][1] - s_y[i][1] < min_temp:

            d = dist(s_y[j], s_y[i])

            if d < min_temp:
                min_temp = d

            j += 1
            c += 1
    return min_temp

# Snabbare att bara sätta upp två fall, för 2 och 3?

def bruteforce(points):
    min_dist = math.inf

    for i, p1 in enumerate(points):
        j = i + 1
        while j < len(points):
            p2 = points[j]
            min_dist = min(dist(p1, p2), min_dist)
            j += 1

    return min_dist


# O(nLogn)
def procedure(px, py, N):

    if N < 4:
        return bruteforce(px)

    # split px into Lx , Rx
    mid = N // 2
    Lx = px[:mid]
    Rx = px[mid:]

    # split py into Ly, Ry
    Ly = py[:mid]
    Ry = py[mid:]

    # recursivly call to find minimums of both sets

    min_left = procedure(Lx, Ly, mid)
    min_right = procedure(Rx, Ry, N - mid)
    delta = min(min_left, min_right)


    midx = Rx[0][0]


    return closest(px, delta, midx)


def main():
    N = int(input())

    points = [[int(x) for x in input().split()] for _ in range(N)]

    # sort px by x. py by y

    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])

    # print("%.6f" % bruteForce(px))

    # showing 6 decimal digits of float

    print("%.6f" % procedure(px, py, N))


if __name__ == '__main__':
    main()
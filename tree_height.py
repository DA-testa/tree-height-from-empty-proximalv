# python3
# Jānis Ozoliņš 201REC073
import sys
import threading


def compute_height(n, parents):

    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            r = i
        else:
            tree[parents[i]].append(i)
    q = [(r, 1)]
    max_height = 0
    while q:
        x, h = q.pop(0)
        if h > max_height:
            max_height = h
        for j in tree[x]:
            q.append((j, h + 1))
    return max_height


def main():
    veids = input()

    if "F" in veids:
        filename = input()
        if 'a' not in filename:
            with open("test/" + filename) as f:
                skaits = int(f.readline())
                p = list(map(int, f.readline().split()))
                garums = compute_height(skaits, p)
                print(garums)
    elif "I" in veids:
        skaits = int(input())
        p = list(map(int, input().split()))
        garums = compute_height(skaits, p)
        print(garums)
    else:
        print("Vai I vai F lucu")

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

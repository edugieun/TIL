def process_solution(a, k):
    print(a)
def construct_candidates(a, k, input, c):
    used = [False] * (input + 1)
    for i in range(k):
        used[a[i]] = True

    idx = 0
    for i in range(1, input + 1):
        if used[i]: continue
        c[idx] = i
        idx += 1
    return idx

def backtrack(a, k, input):
    if k == input:
        process_solution(a, k)
    else:
        k += 1
        c = [0] * 3
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


MAXC = 4
arr = [0] * 4
backtrack(arr, 0, 3)
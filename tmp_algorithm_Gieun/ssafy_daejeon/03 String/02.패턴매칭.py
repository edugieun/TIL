p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

# 1. 문자열.find() 사용
idx = t.find(p)
print(p)
print(t[idx:])


# 2. Brute-Force1
m, n = len(p), len(t)
for i in range(n - m + 1):
    j = 0
    while j < m:
        if p[j] != t[i + j]: break
        j += 1

    if j == m:
        print(t[i:])
        break


# 3. Brute-Force2
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(t[i- j:])
        break

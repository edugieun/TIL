p = 'abcdabcef'                                                                    # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


n = len(t)
m = len(p)

th, ph, h0 = 0, 0, 1
for i in range(m):
    th = (th * 10 + ord(t[i])) % 997
    ph = (ph * 10 + ord(p[i])) % 997

for i in range(m - 1):
    h0 = (h0 * 10) % 997

for i in range(n - m + 1):
    if ph == th:
        j = 0
        while j < m:
            if t[i + j] != p[j]:
                break
            j += 1
        if j == m:
            print(i, t[i:])
            break


    if i == n - m: break
    th = ((th - ord(t[i]) * h0) * 10 + ord(t[i + m])) % 997
    if th < 0: th += 997

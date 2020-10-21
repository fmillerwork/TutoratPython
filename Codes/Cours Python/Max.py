S=[55, 51, 50, 49, 53, 44, 56, 52]

max = S[0]

for i in range (len(S)):
    if S[i] > max:
        max = S[i]

print(max)

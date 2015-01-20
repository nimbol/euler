# Find the largest palindrome made from the product of two 3-digit numbers.
# I suspect it's a 6-digit number that starts and ends with 9,
# so find factors that will result in a 9 first.
endings = {}
for i in range(10):
    for j in range(i,10):
        if (i * j) % 10 == 9:
            endings[i] = j
            endings[j] = i

palindromes = []
# 900*999 < 900000, so use numbers between 900 and 999
for i in range(999, 900, -2):
    if (i % 10) not in endings: continue
    for j in range(i, 900, -2):
        if (j % 10) != endings[i % 10]: continue
        # sifting criteria met, check for palindrome
        n = i * j
        if str(n) == str(n)[::-1]: #''.join(reversed(str(n))):
            palindromes.append(n)

print max(palindromes)  # there's actually only one!

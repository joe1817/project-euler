'''
Joe Walter

difficulty: 5%
run time:   0:01
answer:     5482660

	***

044 Pentagonal Numbers

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

	***

Observations

Looking for 2 pentagonal numbers, a & b, s.t. pent(a+b) and pent(a-b) is the same  as looking for 2 pentagonal numbers, c=(a-b) & b, s.t. pent(c+b) and pent(c+2b)
'''

from itertools import combinations
from bisect import bisect
from lib.sequences import pentagonal

def contains(arr, n):
	i = bisect(arr, n)
	return arr[i-1] == n

pent = list(pentagonal(10**7))

# TODO this actually doesn't guarantee the minimum -- pent might not be large enough
min = float("inf")
for p1, p2 in combinations(pent, 2):
	if p2-p1 < min:
		if contains(pent, p1+p2) and contains(pent, p2-p1):
			min = p2-p1

print(min)

'''
def solve():
	# rationale: the difference between adjacent terms increases, so look at smallest numbers first
	for i in range(1, len(pent)):
		for j in range(i-1, -1, -1):
			p1, p2 = pent[j], pent[i]
			if contains(pent, p1+p2) and contains(pent, p2-p1):
				return p2-p1

print(solve())
'''

'''
Joe Walter

difficulty: 10%
run time:   0:00
answer:     -6999033352333308

	***

918 Recursive Sequence Summation

The sequence a_n is defined by a_1 = 1, and then recursively for n >= 1:

	a_2n = 2a_n
	a_2n+1 = a_n - 3a_n+1

The first ten terms are 1, 2, -5, 4, 17, -10, -17, 8, -47, 34.

Define S(N) = Sum(a_n, n=1, N). You are given S(10) = -13.

Find S(10^12).
'''

def val_at(row, index):
	# row is 1-indexed
	# index is 1-indexed
	row -= 1
	index -= 1

	if not index and not row:
		return 1

	x = f"{index:0{row}b}"
	m, n = 1, 2
	for y in x:
		if y == "0":
			# move down
			m, n = 2*m, m-3*n
			right_edge = False
		else:
			# move down-right
			m, n = m-3*n, 2*n
	return m

def S(n):
	if not n%2:
		delete_last = True
		n += 1

	sum = 1

	# add full rows
	i = 1 # number of "a" elements summed
	r = 1 # number of whole rows summed
	a = 1 # first element of the last row summed
	while i + 2**r <= n:
		sum += -3*a
		i += 2**r
		r += 1
		a *= 2
		#print(f"{sum=} {i=} {r=} {a=} ")

	# add partial row
	remainder = n-i
	b = val_at(r, remainder//2+1)
	sum += 3*(a-b)

	if delete_last:
		sum -= val_at(r+1, remainder)

	return sum

assert S(10) == -13

print(S(10**12))

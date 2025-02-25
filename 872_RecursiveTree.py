'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     2903144925319290239

	***

872 Recursive Tree

A sequence of rooted trees T_n is constructed such that T_n has n nodes numbered 1 to n.

The sequence starts at T_1, a tree with a single node as a root with the number 1.

For n>1, T_n is constructed from T_n-1 using the following procedure:

    1. Trace a path from the root of T_n-1 to a leaf by following the largest-numbered child at each node.
	2. Remove all edges along the traced path, disconnecting all nodes along it from their parents.
	3. Connect all orphaned nodes directly to a new node numbered n, which becomes the root of T_n.

Let f(n,k) be the sum of the node numbers along the path connecting the root of T_n to the node k, including the root and the node k. For example, f(6,1) = 6+5+1 = 12 and f(10,3) = 29.

Find f(10**17, 9**17).

	***

Observations

1. Add k to each node in T_n and you get a tree that exists as a sub-tree in T_n+k.
2. Node 1 is on the max-path when the root is a power of 2.
3. The parent of the 1-node is the largest integer 2**k+1 <= root.
'''

from math import log, floor

def parent(root, node):
	diff = node - 1
	return 2**floor(log(root - diff - 1, 2)) + 1 + diff

def f(n, k):
	sum = k
	while k != n:
		k = parent(n, k)
		sum += k
	return sum

assert f(6, 1) == 12
assert f(10, 3) == 29

print(f(10**17, 9**17))

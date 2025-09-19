# Homework1

第一次作业的相关内容整理在这里，以供后续复习使用。

## Problem 0

The resources I use when I solve the homework problems:

* CS160's slides and recitation resources
* geeksforgeeks.org: Properties of Asymptotic Notations
* L'Hôpital's rule (Wikipedia)

## Problem 1

(a) Abstract Proofs

i. If f = O(g) then g = O(f)

The statement is false.

Proof:

For this  statement, we can find a counterexample, and if f = O(g) is true but g = O(f) is false, then the statement can be proved false.

Let f  = n, g = n^2

By the definition of Big O, choose c = 1, n0 = 1, then:

n < n^2, for all n >= 1.

So f = O(g) is true.

By the definition of Big O, if g = O(f) is true, then there must has c and n0 fits:

n^2 < c * n,  for n >= n0

since we are analyzing growth, n0 is at least 1, and n should be a positive number. so we can multiply by n, for  each side, and get:

n < c, for n >= n0

since c is a constant, and n is growing to infinite, no matter how large is the constant c, the n will sometime greater than c. therefore, g = O(f) is false.

In conclusion, we have found a counterexample where `f = n` and `g = n²`. This counterexample satisfies the premise `f = O(g)` but fails to satisfy the conclusion `g = O(f)`. Therefore, the original statement is false.

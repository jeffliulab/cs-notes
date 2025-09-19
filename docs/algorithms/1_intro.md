# 算法导论：序言与概论

---

## 算法简介

CLRS 1.1， 1.2

## 算法分析框架

一个完整的算法分析一般包含如下内容：

* Example
* **Description**
* Pseudocode
* Actual Code
* **Justification**
* **Time Analysis**
* **Space Analysis**

以插入排序为例：

- Example

Input: \[5, 3, 4, 1, 2\]Process:Step 1: \[3, 5, 4, 1, 2\]Step 2: \[3, 4, 5, 1, 2\]Step 3: \[1, 3, 4, 5, 2\]Step 4: \[1, 2, 3, 4, 5\]Output: \[1, 2, 3, 4, 5\]

- Description

Given an array of n numbers, insertion sort works by considering each
element (starting from the second) and inserting it into its correct
position among the already sorted part of the array. It keeps moving the
element left until it is not smaller than the element before it. The
process repeats until the entire array is sorted.

- Pseudocode

```
INSERTION-SORT(A[1...n])
        for i = 2 to n
            j = i
            while j > 1 and A[j] < A[j-1]
                swap A[j] and A[j-1]
                j = j - 1
```

- Actual Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
```

.

---

**Justification**

**Loop invariant:**

At the beginning of each iteration i, the subarray A\[1...i-1\] is sorted.

1. Initialization: When i=2, the subarray A\[1\] is trivially sorted.
2. Maintenance: If A\[1...i-1\] is sorted before iteration i, then inserting A\[i\] into its correct position keeps A\[1...i\] sorted.
3. Termination: When i=n+1, the invariant tells us that A\[1...n\] is sorted, so the algorithm is correct.

注意这里的Loop Invariant（循环不变量）：

插入排序的 **核心承诺** ，也就是它的**循环不变量 (Loop Invariant)** 是：

> **“在 `for` 循环的每次迭代 `i` 开始时，子数组 `A[1...i-1]` 都包含该范围内的原始元素，并且是排好序的。”**

下面我们用三个步骤来验证这个承诺的有效性。

**1、初始化（证明起点）**

这一步检查的是，在循环 **第一次执行之前** ，我们的承诺是否成立。

* `for` 循环是从 `i = 2` 开始的。
* 在这个起点，不变量所指的子数组是 `A[1...i-1]`，代入 `i=2` 就是 `A[1...2-1]`，即 `A[1]`。
* 一个只包含**单个元素**的子数组，根据定义，它本身就是有序的。
* 因此，我们的承诺在最开始的时候是成立的。✅

**2、保持（证明过程）**

这一步要证明的是：如果在某一次迭代开始时承诺是成立的，那么在这次迭代结束、下一次迭代开始时，承诺 **依然会成立** 。这证明了我们的承诺在循环中是能够一直维持下去的。

* **假设** ：在第 `i` 次迭代开始时，承诺为真，也就是说子数组 `A[1...i-1]` 已经排好序了。
* **操作** ：在这次迭代中，循环体（内部的 `while` 循环）会取出下一个元素 `A[i]`，并将它插入到前面已经有序的 `A[1...i-1]` 中的正确位置。
* **结果** ：当 `A[i]` 插入后，这个新的、更长的子数组 `A[1...i]` 现在整体就是有序的了。这个状态是第 `i` 次迭代结束时的状态。
* 当循环进入下一次迭代，也就是第 `i+1` 次时，它所面对的 `A[1...(i+1)-1]` 正是我们刚刚排好序的 `A[1...i]`。
* 因此，承诺成功地维持并传递到了下一次迭代。✅

**3、终止（证明终点）**

这一步展示的是，当循环 **结束时** ，这个一直保持为真的承诺能告诉我们什么。

* `for` 循环的终止条件是当 `i` 增加到 **n + 1** 时，循环不再执行。
* 在循环终止的这一刻，我们可以最后一次运用我们的不变量，将 `i = n + 1` 代入不变量的陈述中。
* 这个陈述就变成了：“子数组 `A[1...(n+1)-1]`，即 `A[1...n]`，是排好序的。”
* 这个最终的陈述意味着**整个数组**都已有序。这正是我们算法想要达成的目标，所以证明完成。我们通过循环不变量，严谨地说明了插入排序算法是正确的。✅

---

**Time Analysis**

Best Case: Array already sorted → n-1 comparisons → Θ(n).

Worst Case: Array in reverse order → 1+2+...+(n-1) = n(n-1)/2 comparisons → Θ(n\^2).

Average Case: Random input → about n\^2/4 comparisons → Θ(n\^2).

---

**Space Analysis**

Insertion Sort is an in-place sorting algorithm. It only requires a constant amount of additional memory for indices and temporary variables.

Space complexity: O(1).

Stability: Stable (equal elements retain their relative order)

## 算法设计

CLRS 2.3

## 复杂性分析

（待办：过一遍CLRS 3.1，3.2，3.3，补充一下遗漏掉的内容）

在算法分析中，我们采用Asymptotic Notation，也即渐进记法，来分析算法的效率。其包含三个核心概念：

* Big O
* Big Omega $\Omega$
* Big Theta $\Theta$

### Big O

- **Definition:** The function $f(n)$ is $O(g(n))$ if there exist constants $c > 0$ and $n_0$ such that

  $$
  0 \leq f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n_0.
  $$
- **Example:** $2n^2 + 3n + 1$ is $O(n^2)$ because for $c = 3$ and $n_0 = 1$, we have

  $$
  0 \leq 2n^2 + 3n + 1 \leq 2n^2 + 3n^2 + 1 \cdot n^2 \leq 6n^2 , \quad \text{for all } n \geq 1
  $$

一般来说，Big O描述了一个函数增长速度的**上限（Upper Bound）**。可以这样理解：“当输入规模 `n` 足够大时，函数 `f(n)` 的增长速度**不会超过**函数 `g(n)` 的 `c` 倍。

通常n0选取为1，或者大于1的一个整数。（**虽然在上述定义中没有说明n0必须大于等于1，但是一般在算法分析中我们默认n0是大于等于1的。因为我们在分析复杂性的时候，关心的是渐进性为，目的是描述函数的长期增长趋势，因此如果n0起始于负数，在这个应用中是没有意义的。**）

也就是说，在算法分析中，g(n)是f(n)的太牛花瓣，并且我们不关注常数因子。所以当我们去分析一个算法的Big O的时候，我们只需要找到合适的c和n，找到g(n)就可以了。

从数学定义上来说，上面的例子就算给出 `O(n³)` ，仍然也是一个正确的上限，但它是一个很“松”的上限，没有精确地反映出函数 `2n` 的增长趋势。这就像问一个小孩多高，你说：“他肯定不超过3米高。” 这句话虽然没错，但没什么用。我们更想听到的是：“他大概1米2高。”所以，当我们分析算法复杂度时，虽然有无数个正确的 Big O 答案，但我们总是约定俗成地去寻找并给出一个**最简单、最贴近**的那个，也就是 **最小的那个增长率** 。如果能找到严格上界，有时候也会写作o记号（小o）。

在记录Big O的时候，一般有两种常见写法：

* **`f(n) = O(n²)`** ：这是最常见、最通用的写法。它读作 “f(n) is O of n-squared”（f(n) 是 n 平方的 Big O）。虽然这里用的是等号 `=`，但它并不表示数学上严格的“相等”，而是一种约定俗成的表示法，意思是“f(n) 的增长率属于 O(n²) 这个级别”。
* **`f(n) ∈ O(n²)`** ：这是从数学集合角度来看**更严谨**的写法。这里的 `∈` 符号表示“属于”（is an element of）。`O(n²)` 实际上代表一个 **函数的集合** ，这个集合包含了所有增长速度不超过 `n²` 的函数。所以 `f(n) ∈ O(n²)` 的意思是 “f(n) 是 O(n²) 这个集合中的一员”。

#### 证明Big O性质

**如果 `f(n) = O(g(n))` 并且 `h(n) = O(g(n))`，那么 `f(n) + h(n) = O(g(n))`。**

**用通俗的语言解释就是：** 如果两个函数 `f(n)` 和 `h(n)` 的增长率都最多和 `g(n)` 一样快（或者更慢），那么这两个函数的和 `f(n) + h(n)` 的增长率也最多和 `g(n)` 一样快。

这在算法分析中非常有用。比如，如果你有两个连续的代码块，它们的运行时间分别是 `O(n)` 和 `O(n)`，那么整个过程的运行时间就是 `O(n) + O(n)`，根据这个定理，结果依然是 `O(n)`。

**PROOFS**

证明过程是严格按照大O表示法的定义来进行的。我们一步一步来看：

**1. 假设 (Suppose)**

> `Suppose f = O(g) and h = O(g).`

证明的第一步是假设论点的前提条件成立。这里我们假设 `f` 的增长率是 `O(g)`，`h` 的增长率也是 `O(g)`。
（图片右上角提示，`f` 是 `f(n)` 的简写，这在数学证明中很常见。）

**2. 展开 `f = O(g)` 的定义**

> `f = O(g) means f ≤ c*g for n ≥ n₀.`

这是大O表示法的正式定义。`f(n) = O(g(n))` 的意思是：
存在一个正常数 `c` 和一个整数 `n₀`，使得当 `n` 大于等于 `n₀` 时，`f(n)` 的值总是不超过 `c` 乘以 `g(n)` 的值。

* `c` 是一个常量系数，它允许我们忽略常数倍的差异。
* `n₀` 是一个阈值，它表示我们只关心当输入规模 `n` 足够大时的情况。

**3. 展开 `h = O(g)` 的定义**

> `h = O(g) means h ≤ d*g for n ≥ n₁.`

同理，`h(n) = O(g(n))` 的意思是：
存在另一个正常数 `d` 和另一个整数 `n₁`，使得当 `n` 大于等于 `n₁` 时，`h(n)` 的值总是不超过 `d` 乘以 `g(n)` 的值。
**注意：** 这里的常数 `d` 和阈值 `n₁` 可能与上面 `f(n)` 的 `c` 和 `n₀` 不同。

**4. 相加 (Adding gives)**

> `Adding gives f + h ≤ (c+d)g for n ≥ ?`

现在，为了证明 `f(n) + h(n)` 的情况，我们将上面两个不等式相加：
`f(n) ≤ c*g(n)`
`h(n) ≤ d*g(n)`
两式相加得到：
`f(n) + h(n) ≤ c*g(n) + d*g(n)`
提取公因式 `g(n)`，得到：
`f(n) + h(n) ≤ (c+d)g(n)`

**5. 确定新的阈值 `n`（图片中未写完的部分）**
关键问题来了：这个新的不等式 `f+h ≤ (c+d)g` 在什么条件下成立呢？

* 第一个不等式 `f ≤ c*g` 要求 `n ≥ n₀`。
* 第二个不等式 `h ≤ d*g` 要求 `n ≥ n₁`。
  为了让**两个**不等式同时成立，`n` 必须同时满足 `n ≥ n₀` 和 `n ≥ n₁`。因此，我们只需要取两者中较大的那个值作为新的阈值即可。
  所以，我们定义一个新的阈值 `n₂ = max(n₀, n₁)`。当 `n ≥ n₂` 时，上面两个不等式都成立，因此它们的和也成立。

所以，图片中那个空白的地方应该填 `max(n₀, n₁)`。

**结论**

我们已经证明了：
存在一个新的常数 `C = c+d` 和一个新的阈值 `n₂ = max(n₀, n₁)`，使得当 `n ≥ n₂` 时，`f(n) + h(n) ≤ C * g(n)`。

这完全符合大O表示法的定义！因此，我们得出结论：`f(n) + h(n) = O(g(n))`。证明完毕。

**简单例子**

假设 `f(n) = 2n + 10`，`h(n) = 3n + 5`，我们要证明 `f(n) + h(n)` 是 `O(n)`。

1. **证明 `f(n) = O(n)`** :
   我们需要找到 `c` 和 `n₀` 使得 `2n + 10 ≤ c*n`。
   如果我们选 `c = 3`，那么 `2n + 10 ≤ 3n` -> `10 ≤ n`。所以，当 `c₁=3, n₀=10` 时，`f(n) = O(n)` 成立。
2. **证明 `h(n) = O(n)`** :
   我们需要找到 `d` 和 `n₁` 使得 `3n + 5 ≤ d*n`。
   如果我们选 `d = 4`，那么 `3n + 5 ≤ 4n` -> `5 ≤ n`。所以，当 `c₂=4, n₁=5` 时，`h(n) = O(n)` 成立。
3. **证明 `f(n) + h(n) = O(n)`** :
   `f(n) + h(n) = (2n+10) + (3n+5) = 5n + 15`。
   根据上面的证明，我们应该有 `f(n) + h(n) ≤ (c₁+c₂)n` 对于 `n ≥ max(n₀, n₁)` 成立。

* 新常数 `C = c₁ + c₂ = 3 + 4 = 7`。
* 新阈值 `n₂ = max(n₀, n₁) = max(10, 5) = 10`。
* 我们来验证一下：`5n + 15 ≤ 7n` 是否在 `n ≥ 10` 时成立？
  `15 ≤ 2n` -> `7.5 ≤ n`。
  因为 `n ≥ 10` 已经满足了 `n ≥ 7.5` 的条件，所以这个不等式是成立的。

因此，我们成功证明了 `f(n) + h(n) = O(n)`。

### Big Omega

- **Definition:** The function $f(n)$ is $\Omega(g(n))$ if there exist constants $c > 0$ and $n_0$ such that

  $$
  0 \leq c \cdot g(n) \leq f(n) \quad \text{for all } n \geq n_0.
  $$
- **Example:** $2n^2 + 3n + 1$ is $\Omega(n^2)$ because for $c = 2$ and $n_0 = 1$, we have

  $$
  0 \leq 2n^2 \leq 2n^2 + 3n + 1, \quad \text{for all } n \geq 1
  $$

一般来说，Big Omega描述了一个函数增长速度的**下限（Lower Bound）**。可以这样理解：“当输入规模 `n` 足够大时，函数 `f(n)` 的增长速度**至少**和函数 `g(n)` 的 `d` 倍一样快。” 也就是说，`g(n)` 是 `f(n)` 的一种“地板”，`f(n)` 的增长再慢也慢不过 `g(n)`。在算法分析中，它常用来描述一个算法的 **最好情况下的时间复杂度** 。

对于所有增长的函数 `f(n)`（比如算法的运行时间），我们几乎总可以说 `f(n) = Ω(1)`（因为运行时间至少是一个常数，不会是负数）。**但是，这同样是一个没有信息量的“松”的下限。**

我们使用 Big Omega 是想知道：“这个算法的运行时间**最少**也要增长得多快？” 说 `Ω(1)` 等于在说：“这个算法总得花点时间才能运行完。” 这是一句废话。说一个排序算法是 `Ω(n)` 意味着：“不管输入的数据有多好（比如已经排好序了），你至少也得把每个元素看一遍，所以时间下限是线性增长的。” 这个信息就非常有用了。

所以在实际分析中，和 Big O 一样，我们一半呢寻找的是**最紧的下限（Tightest Lower Bound）**，也就是增长最快的那个下界函数，来提供有意义的分析。如果能找到严格下界，记录时也用小omega，也即$\omega$来表示。

### Big Theta

- **Definition:**  The function $f(n)$ is $\Theta(g(n))$ if it is both $O(g(n))$ and $\Omega(g(n))$.
- **Example:** $2n^2 + 3n + 1$ is $\Theta(n^2)$ because it is both $O(n^2)$ and $\Omega(n^2)$.

`f(n) = Θ(g(n))` 的意思是：存在正常数 `c`, `d` 和 `n₀`，使得对于所有 `n ≥ n₀`，都有 `d * g(n) ≤ f(n) ≤ c * g(n)`。Big Theta 描述了一个函数增长速度的 **紧密界限 (Tight Bound)** 。它其实是 Big O 和 Big Omega 的结合。`f(n) = Θ(g(n))` 意味着 `f(n)` 的增长速度既不比 `g(n)` 快，也不比 `g(n)` 慢，它们的增长速率是**相同**的。也就是说，`f(n)` 被 `g(n)` 从上下两个方向“夹住”了。这是对一个算法复杂度最精确的描述。

一般来说，如果我们在找Big O和Big Omega的时候，找到的如果已经是最紧的上限和最紧的下限，那么这个时候用这两个最紧的上下限就能轻松找到那个被夹住的紧密界限。

## 数学基础

本节整理了一些本书中经常涉及到的一些数学相关的知识，基本都是比较基础的数学内容。

### 指数增长快于多项式函数

在算法分析中有一个至关重要的规律：**任何指数函数的增长速度都比任何多项式函数快。**

* **多项式函数 (Polynomials)** ：形如$n^b$的函数，其中 `b` 是一个常数。例如：$n^2$, $n^{100}$都是多项式。
* **指数函数 (Exponentials)** ：形如$a^n$的函数，其中 `a` 是一个大于 1 的常数。例如：$2^n$, $1.1^n$都是指数函数。

对于多项式函数和指数函数，如果a > 1，那么我们有：

$$
\lim_{n \to \infty} \frac{n^b}{a^n} = 0
$$

这个极限公式表明当n趋向于无穷大时，一个多项式函数和一个指数函数的比值会趋近于0。这意味着分母的增长速度远快于分子的增长速度，因此在极限情况下他们的比值几乎为0。

通过这个我们可以得到如下推论：

$$
n^b = O\!\left(a^n\right)
$$

即指数函数一定是多项式函数的上限。（在a>1的情况下）

### 指数

#### Notation

- $\log_b n = a \iff b^a = n$  (definition of log)
- $\ln n = \log_e n$  (natural log)
- $\lg n \ \text{or} \ \log n = \log_2 n$  (base-2 shorthand)
- $\lg^2 n = (\lg n)(\lg n)$  (multiplication)
- $\lg \lg n = (\lg(\lg n))$  (composition)

#### Properties

- $(a^m)^n = a^{mn}$
- $a^m \cdot a^n = a^{m+n}$
- $a^n = 2^{n \lg a}$
- $a^{\log_b n} = n^{\log_b a}$
- $\log_b a = \dfrac{\log_c a}{\log_c b}$  (A way to change from base $b$ to base $c$)
- $\lg ab = \lg a + \lg b$
- $\lg(a^x) = x \lg a$
- $\lg(1/a) = -\lg a$

### Quantifiers

Quantifiers就是量词，用来限定一个陈述在某个集合中是对全部成立，抑或是对至少有一个成立。

- **Universal Quantifier ($\forall$):** The symbol $\forall$ is used to express that a statement holds for every element in a given set. For example:

  $$
  \forall x \in \mathbb{R}, \; x^2 \geq 0
  $$
- **Existential Quantifier ($\exists$):** The symbol $\exists$ is used to express that there exists at least one element in a given set for which a statement holds. For example:

  $$
  \exists x \in \mathbb{R} \;\; \text{such that} \;\; x^2 = 4
  $$

简单来说：

* **`∀` (任意)：** 要求很高，必须对集合里**所有**成员都成立才算对。`∀` 符号看起来像一个倒过来的字母 "A"，可以联想英文单词 "**A**ll" (所有)。
* **`∃` (存在)：** 要求很低，只需要在集合里找到**至少一个**符合条件的成员就算对。`∃` 符号看起来像一个反过来的字母 "E"，可以联想英文单词 "**E**xists" (存在)。

这两个符号在定义数学概念（比如我们之前讨论的 Big O 定义）和进行逻辑证明时非常关键。

### Summation Formulas

求和公式

#### Arithmetic series

等差数列求和公式

For integer $n \geq 1$, we have

$$
1 + 2 + \dots + n \;=\; \sum_{k=0}^n k 
\;=\; \frac{n(n+1)}{2}
$$

#### Geometric series

等比数列求和公式

For real $r \neq 1$, we have

$$
1 + r + r^2 + \dots + r^k \;=\; \sum_{i=0}^k r^i
\;=\; \frac{1 - r^{k+1}}{1-r}
$$

When the summation is infinite and $|r| < 1$, we have

$$
1 + r + r^2 + \dots \;=\; \sum_{i=0}^{\infty} r^i
\;=\; \frac{1}{1-r}
$$

### 离散数学和集合

Let $A$ and $B$ be sets.

Union并集，Intersection交集，Difference差集：

- **Union:** $A \cup B =$ The set of elements that appear in either $A$ or $B$ or both.
- **Intersection:**$A \cap B =$ The set of elements that appear in both $A$ and $B$.
- **Difference:**$A \setminus B$ or $A - B =$ The set of elements that appear in $A$ and not in $B$.

基数：（集合A中元素的个数）

- **Cardinality:**$|A| =$ The number of elements in $A$.

阶乘

- **Factorial:** The notation $n!$ is read “$n$ factorial” and is defined for integer $n > 0$ as follows:

  $$
  n! = 1 \times 2 \times \dots \times (n-1) \times n
  $$

  By convention, $0! = 1$.

Choose选择，Permutations排列，Combinations组合：

- **“Choose”:** The notation $\binom{n}{k}$ is read “$n$ choose $k$” because it represents the number of ways to choose $k$ items from $n$ distinct items.For integers $0 \leq k \leq n$, we have:

  $$
  \binom{n}{k} = \frac{n!}{k!(n-k)!}
  = \binom{n}{n-k}
  $$
- **Permutations and Combinations:**
  In a set of elements $A$, the number of ordered permutations of all $|A|$ elements is $|A|!$.
  The number of combinations of $k$ elements is

  $$
  \binom{|A|}{k}.
  $$

排列和组合的最重要区别就是：排列中顺序很重要，而组合中顺序不重要。比如ABC和CAB是两种不同的排列，但是却是2同一个组合。

### Probability

- **Random Variables:**In probability theory, a *random variable* is a variable whose possible values are outcomes of a random phenomenon.For example, let $X$ represent the outcome of rolling a six-sided die.$X$ can take values $\{1,2,3,4,5,6\}$.
- **Notation:**$P(X = 5) = \tfrac{1}{6}$ means “The probability that $X$ takes the value $5$ is $\tfrac{1}{6}$.”

Expectation 期望

- **Expectation:**
  The *expectation* (or mean) of a random variable $X$ is denoted by $E[X]$ and represents the average value it takes.
  For a discrete random variable, it is computed as:

  $$
  E[X] = \sum_x x \cdot P(X = x)
  $$

  where the sum is taken over all possible values of $X$.

**Example:**
Consider a fair six-sided die. Let $X$ be the outcome of a single roll.
The expectation of $X$ is:

$$
E[X] = \tfrac{1}{6}(1) + \tfrac{1}{6}(2) + \tfrac{1}{6}(3) + \tfrac{1}{6}(4) + \tfrac{1}{6}(5) + \tfrac{1}{6}(6) 
= \tfrac{7}{2}
$$

Properties of Expectation:

- $E[aX + b] = aE[X] + b$ for constants $a$ and $b$.
- $E[X + Y] = E[X] + E[Y]$ for independent random variables $X$ and $Y$.

### Ceilings and Floors

- $\lceil x \rceil = \text{ceiling}(x) =$ the least integer greater than or equal to $x$
- $\lfloor x \rfloor = \text{floor}(x) =$ the greatest integer less than or equal to $x$

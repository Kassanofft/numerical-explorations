# Mathematical Derivation

## 1. The approximation

We want to approximate the derivative \(f'(x)\) using values of \(f\) at nearby points.

The limit definition of the exact derivative is:

$$
\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

The approximation, however, uses a small \(h\). Therefore, we want to understand how accurately the expression approximates \(f'(x)\).

## 2. Taylor expansion

To measure the error term, we first Taylor expand at a point to the right and to the left.

Let \(f(x+h)\) and \(f(x-h)\) be points at a distance \(h\) from \(f(x)\):

$$
f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + O(h^4)
$$

$$
f(x-h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f'''(x) + O(h^4)
$$

## 3. Forward Approximation

Using the equation from our limit definition and our Taylor expansions, we get an approximation of the forward difference:

$$
\frac{f(x+h) - f(x)}{h} = f'(x) + \frac{h}{2}f''(x) + \frac{h^2}{6}f'''(x) + O(h^3)
$$

Through inspection, we see the first term is the derivative \(f'(x)\) of our function. The terms that follow are then error terms. We see that as the term order increases, they scale down in magnitude. Therefore, our forward Taylor approximation has first-order accuracy due to the leading term after \(f'(x)\).

## 4. Central Difference Approximation

The central difference approximation uses the values on both sides of \(f(x)\):

$$
\frac{f(x+h) - f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f'''(x) + O(h^3)
$$

Through inspection, we see the first error term leads with \(h^2\). Therefore, our central difference approximation has second-order accuracy.

## 5. Expected convergence

From the forward difference approximation, the leading error term is proportional to \(h\):

$$
E_f(h) \approx Ch
$$

The constant \(C\) is a coefficient that depends on the function and the point at which it is evaluated.

For the central difference, the leading error term is proportional to \(h^2\):

$$
E_c(h) \approx Ch^2
$$

Therefore, we can represent our general error as:

$$
E(h) \approx Ch^p
$$

The constant \(p\) represents the order of accuracy.

Taking the logarithm of both sides gives:

$$
\log(E(h)) \approx \log(C) + \log(h^p)
$$

Using the logarithm power rule:

$$
\log(E(h)) \approx \log(C) + p\log(h)
$$

This is in the form of a linear equation:

$$
y = mx + b
$$

where:

$$
y = \log(E(h))
$$

$$
x = \log(h)
$$

$$
m = p
$$

Therefore, plotting the error against \(h\) on a log-log scale should produce an approximately linear relationship. The slope of this line should correspond to the order of accuracy of the approximation.

For the forward difference, we expect:

$$
p = 1
$$

and therefore expect a slope of approximately 1.

For the central difference, we expect:

$$
p = 2
$$

and therefore expect a slope of approximately 2.

The numerical experiment will test whether these theoretical convergence rates are observed as \(h\) decreases.

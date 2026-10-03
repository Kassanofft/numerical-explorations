# Convergence of Finite Difference Approximations

Comparing the convergence rates of forward and central methods
for $f'(x)$.

## Problem

Approximate $f'(x_0)$ for $f(x) = x^3$ at $x_0 = 3$ using $N$ equally spaced points, and measure the error as $N$ grows.

## Methods

- **Forward difference:** $D_f = \frac{f(x+h) - f(x)}{h}$
- **Central difference:** $D_c = \frac{f(x+h) - f(x-h)}{2h}$

Error measured: $E(x_0) = D_i(x_0,h) - f'(x_0)$

## Results

See [results.md](results.md) for the tables and plots.

**TL;DR:** Forward converges at $O(h)$ and central at $O(h^2)$.

## Why these rates?

See [derivation.md](derivation.md) for the Taylor series argument.

## Reproducing

Requires Python 3.10+, `numpy`, `matplotlib`, `sympy`.

```bash
pip install numpy matplotlib sympy
python experiment.py


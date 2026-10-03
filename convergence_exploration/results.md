# Results 

# Setup

- **Test function:** $f(x) = x^3$
- **Evaluation Point:** $x_0 = 3$
- **$h$ range:** log-spaced from $10^{-1}$ to $10^{-3}$, 1000 points
- **Error:** $|D(x_0) - f'(x_0)|$

## Table

| $h$ | Forward error | Central error |
|-----|:------------:|:------------:|
| 1.0000e-01 | 9.1000e-01 | 1.0000e-02 |
| 9.9770e-03 | 8.9892e-02 | 9.9540e-05 |
| 1.0000e-03 | 9.0010e-03 | 9.9999e-07 |

## Observed rates

| Method | Observed rate | Expected rate |
|--------|:------------:|:------------:|
| Forward difference | 1.00 | $O(h^1)$ |
| Central difference | 2.00 | $O(h^2)$ |

## Plot
![Convergence plot](Finite_Difference_Plot(1).png)

## Observations
Both schemes match their expected rate. 

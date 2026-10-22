# Example API

```python
center(values: Iterable[float]) -> tuple[float, ...]
```

Subtract the arithmetic mean from each input value, preserving order. The input
is materialized once; the function returns a new tuple and does not mutate the
input. Numeric inputs are converted to Python floats.

Empty inputs, NaNs, and positive or negative infinities raise `ValueError`.
An unrepresentable sum or centered result raises `OverflowError`. Nonconvertible
inputs raise the normal `float` conversion error. Missing-value behavior is
explicitly outside this example's scope.

This example is not an R package port. Real methods need their own shape,
dtype, missing-value, categorical, convergence, and error contracts.

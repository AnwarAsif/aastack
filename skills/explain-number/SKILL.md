---
name: explain-number
description: Use before trusting or reporting any measured number (metric, count, rate, speedup). Forces a noise floor, a limiter and a check for what else it measures.
---

Before running, write the decision the number drives and what result would change it.

After running, store these five lines next to the number:
1. How computed: which rows, which window, which baseline.
2. Spread: run at least 3 times (seeds, splits, samples). If the spread is as large as the effect, there is no effect.
3. Limiter: why is it not much higher or lower? Look at counters and a sample of rows, not only the code.
4. What else could it measure: leakage, duplicates, skipped or null rows, an easy majority class, caching.
5. Sanity: recompute one value by hand from raw data.

A number without these lines does not go in a report.

## Rationalizations
| Excuse | Reality |
|---|---|
| "One run is enough" | Without the spread you cannot tell an effect from noise. |
| "It is higher than baseline, so it works" | A large jump is a leakage alarm until the limiter is explained. |
| "The job status says success" | Read the actual table or file; status is a proxy. |

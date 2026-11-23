---
name: tdd
description: Use when adding logic that has a cheap test path, or fixing a bug you can reproduce. Test first, then fix.
disable-model-invocation: true
---

1. Write a test that fails for the right reason (a wrong value fails it; a refactor does not).
2. Run it and see it fail. 3. Write the smallest change that passes. 4. Run all tests. Derive expected values from the requirement, not from the code under test. Skip when a test is expensive and say so.

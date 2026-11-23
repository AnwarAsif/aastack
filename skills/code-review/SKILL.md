---
name: code-review
description: Use to review a change on two axes: standards and spec. Works for code, queries and notebooks.
disable-model-invocation: true
---

Run two reviewers in parallel. Standards: does it follow the repo's rules and RULES.md? Spec: does it do what SPEC.md and the ticket asked, nothing more? Each returns findings with file and line. Report side by side, most severe first.

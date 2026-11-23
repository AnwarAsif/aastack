# Playbook: fix a bug
1. Reproduce on the real artifact. Save the repro as a failing test or command.
2. Find the first wrong decision: ask why until you reach it (not the surface symptom).
3. Fix it there. Fix every other instance of the same pattern.
4. Run the repro: it must now pass. Run all tests.
5. If a human had to point this out, run the `correct` skill so a check catches it next time.

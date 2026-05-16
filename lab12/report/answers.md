# Lab 12: Final Questions

**1. What is the difference between unit tests and behavior tests?**

A unit test isolates one function or method and calls it directly, with controlled inputs and a precise assertion on the output. In this lab the unit tests for `process_item` import the coroutine and `await` it — there is no event loop running the CLI, no JSON, no argparse, no subprocess. A behavior (black-box) test, on the other hand, treats the program as the user does: it runs the actual CLI with `subprocess.run`, feeds it an input file, and inspects the exit code and stdout. It does not care *how* the result is produced — only that the externally observable behavior is correct. Unit tests pin down the building blocks; behavior tests pin down the contract with the user.

**2. Why is `subprocess` used for CLI testing?**

Because the CLI's behavior is defined precisely by what happens when the user runs `python -m async_tool ...` from a shell — argument parsing, logging configuration, exit codes, stdout content, even how `asyncio.run` is invoked. Importing the package and calling a Python function would skip half of that and silently let bugs through (a broken `argparse`, a missing `sys.stdout.write`, a wrong exit code). `subprocess.run` actually launches a fresh interpreter process, so it exercises the program exactly as a real user would. The trade-off is that subprocess tests are slower than direct calls and harder to debug — that is why this lab uses them for end-to-end behavior, and uses direct `await` calls for the unit layer.

**3. What happens if one async task fails without error handling?**

`asyncio.gather(*coros)` with its default `return_exceptions=False` re-raises the first exception immediately. The failing coroutine raises, `gather` propagates that exception to the caller, and all other still-running coroutines are cancelled (the event loop sends them `CancelledError`). In our tool, that exception leaks out of `run_async`/`run_limited`, is caught by `main`'s `try/except`, logged at ERROR level, and the program exits with code `1`. No JSON output is printed. That is exactly what the "error without `--continue-on-error`" tests assert. With `--continue-on-error`, each task is wrapped in `_safe_run` which catches the exception and produces an error result instead, so `gather` never sees an exception and the batch finishes normally.

**4. When should you test internal functions vs full system behavior?**

Test internal functions when the function has interesting logic of its own that is hard to exercise through the outside interface — complicated branches, edge cases, calculations, validation rules. Tests at this level are fast, precise, and pinpoint the failing line. Test full system behavior when you want to lock down what the user actually sees: exit codes, output format, error messages, side effects. The risk of testing internals too aggressively is that the tests become coupled to the implementation: a harmless refactor (renaming a helper, splitting a function) breaks the test suite even though the user-visible behavior is unchanged. A reasonable balance is a thin layer of behavior tests on top of a focused set of unit tests for the parts where logic actually lives.

**5. What are the risks of time-based tests?**

Time-based tests assert things like "async mode is at least 0.5s faster than sync mode". They are tempting because they directly verify the claim that asynchrony brings speedup, but they are also fragile. On a slow CI runner, a loaded laptop, or a Windows worker with high process-startup overhead, the absolute difference shrinks or even flips sign for short delays. Strict thresholds (`assert async_t < 0.4`) flake constantly; loose ones (`assert async_t < sync_t - 1.0`) only catch huge regressions. They also slow the whole suite down — every assertion costs at least the delay it measures. The general rule is to test *behavior* (results, order, exit codes) rather than *performance*, and treat any timing assertion as an optional smoke check with a generous margin — not a real test.

# Lab 11: Final Questions

**1. Why does `await` inside a loop lead to sequential execution?**

`await` suspends the current coroutine until the awaited coroutine finishes. When `await` sits inside a `for` loop, each iteration must fully complete before the next one even starts — the loop body cannot move forward while it is waiting. Even though `process_item` is asynchronous and yields control to the event loop, the loop itself only ever has one task in flight at a time, so the total runtime is the sum of all delays. The total order of operations is identical to writing the tasks one after another with `time.sleep`.

**2. How does `asyncio.gather` change the behavior?**

`asyncio.gather(*coros)` schedules all coroutines on the event loop at once and then waits for all of them to finish together. While one task is waiting on `await asyncio.sleep`, the event loop is free to run the others, so the work overlaps in time. The total runtime drops from the sum of all delays to roughly the maximum delay across the batch. The order of the returned results matches the order of the arguments passed to `gather`, not the order in which the coroutines actually finished — which is exactly what the lab needs to keep the output aligned with the input.

**3. What happens if one task fails in async mode without `--continue-on-error`?**

By default, `asyncio.gather` propagates the first exception immediately: the failing coroutine raises, `gather` re-raises that exception to the caller, and all other still-running coroutines are cancelled. In this tool that exception bubbles up to `main`, gets logged as an error, and the program exits with code `1`. No JSON output is produced. With `return_exceptions=True` (or by wrapping each task in a try/except, which is what `--continue-on-error` does via `_safe_run`), the failing task would instead produce an error result and the batch would complete normally.

**4. Why is a semaphore needed?**

`asyncio.gather` with N tasks launches all N at the same time. For real I/O — HTTP requests, database queries, file writes — this is often too aggressive: the remote service rate-limits us, the OS runs out of sockets, or a connection pool overflows. `asyncio.Semaphore(limit)` is a counter that an `async with` block decrements on entry and increments on exit, blocking when the counter hits zero. Wrapping each task in `async with semaphore:` guarantees that at most `limit` tasks run concurrently, while the rest queue up and start as soon as a slot frees. It is the standard pattern for bounded concurrency in `asyncio`.

**5. When should `async` NOT be used?**

`asyncio` only helps when tasks spend time waiting on something external — network, disk, sleep, subprocess. For CPU-bound work (number crunching, parsing, heavy computation) async gives no speedup, because a single thread still runs only one Python operation at a time, and the GIL prevents real parallelism inside one process. In that case `multiprocessing` or `concurrent.futures.ProcessPoolExecutor` is the right tool. Async is also overkill for genuinely simple, short scripts that do one or two requests in sequence — the added cognitive cost of coroutines, event loops, and proper exception handling is not worth it. And mixing blocking calls (`time.sleep`, classic `requests`) into an async program silently stalls the entire event loop, defeating the whole purpose — so if the libraries you rely on are blocking-only, async will not help either.

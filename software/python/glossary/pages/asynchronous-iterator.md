# Asynchronous iterator

An asynchronous iterator implements `__aiter__()` and `__anext__()`. Each `__anext__()` call returns an awaitable, and exhaustion is signaled by `StopAsyncIteration`.

Source: [Python glossary](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
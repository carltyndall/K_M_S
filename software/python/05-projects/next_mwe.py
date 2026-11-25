iterator = iter([10])
print("first:", next(iterator))
print("exhausted:", next(iterator, "no more"))
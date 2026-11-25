values = frozenset([1, 2, 2])
print("unique values:", sorted(values), "hashable:", isinstance(hash(values), int))
import builtins


if hasattr(builtins, "frozendict"):
    values = builtins.frozendict(a=1, b=2)
    print("immutable mapping:", values, "a:", values["a"])
else:
    print("frozendict requires Python 3.15 or later")
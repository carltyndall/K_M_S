import builtins


if hasattr(builtins, "sentinel"):
    missing = builtins.sentinel("MISSING")
    value = missing
    print("missing:", value is missing, "representation:", repr(missing))
else:
    print("sentinel requires Python 3.15 or later")
import sys


def report_breakpoint(*args, **kwargs):
    print("breakpoint reached:", args, kwargs)


original_hook = sys.breakpointhook
try:
    sys.breakpointhook = report_breakpoint
    breakpoint("example", line=1)
finally:
    sys.breakpointhook = original_hook
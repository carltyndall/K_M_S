import contextlib
import io


output = io.StringIO()
with contextlib.redirect_stdout(output):
    help(len)
print("len help:", output.getvalue().strip().splitlines()[0])
# Only execute trusted code, never untrusted input.
namespace = {}
exec("answer = 6 * 7", namespace)
print("answer:", namespace["answer"])
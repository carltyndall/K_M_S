# Python Projects & Learning Artifacts

This folder holds lightweight sample scripts, exercises, and minimal working examples (MWEs).

## 📂 Included Artifacts
- **[`hello_world.py`](./hello_world.py)** — Starter demonstration script.
- **[`print_mwe.py`](./print_mwe.py)** — Minimal example of Python's `print` function.
- **[`input_mwe.py`](./input_mwe.py)** — Read a name with Python's `input` function.

## Built-in examples

Run any example from the repository root with `python3 software/python/05-projects/<name>_mwe.py`, replacing `<name>` with the built-in name. `aiter` and `anext` require Python 3.10 or later; `frozendict` and `sentinel` require Python 3.15 or later.

- [__import__](./__import___mwe.py), [abs](./abs_mwe.py), [aiter](./aiter_mwe.py), [all](./all_mwe.py), [anext](./anext_mwe.py), [any](./any_mwe.py), [ascii](./ascii_mwe.py)
- [bin](./bin_mwe.py), [bool](./bool_mwe.py), [breakpoint](./breakpoint_mwe.py), [bytearray](./bytearray_mwe.py), [bytes](./bytes_mwe.py)
- [callable](./callable_mwe.py), [chr](./chr_mwe.py), [classmethod](./classmethod_mwe.py), [compile](./compile_mwe.py), [complex](./complex_mwe.py)
- [delattr](./delattr_mwe.py), [dict](./dict_mwe.py), [dir](./dir_mwe.py), [divmod](./divmod_mwe.py)
- [enumerate](./enumerate_mwe.py), [eval](./eval_mwe.py), [exec](./exec_mwe.py)
- [filter](./filter_mwe.py), [float](./float_mwe.py), [format](./format_mwe.py), [frozendict](./frozendict_mwe.py) (Python 3.15+), [frozenset](./frozenset_mwe.py)
- [getattr](./getattr_mwe.py), [globals](./globals_mwe.py)
- [hasattr](./hasattr_mwe.py), [hash](./hash_mwe.py), [help](./help_mwe.py), [hex](./hex_mwe.py)
- [id](./id_mwe.py), [int](./int_mwe.py), [isinstance](./isinstance_mwe.py), [issubclass](./issubclass_mwe.py), [iter](./iter_mwe.py)
- [len](./len_mwe.py), [list](./list_mwe.py), [locals](./locals_mwe.py)
- [map](./map_mwe.py), [max](./max_mwe.py), [memoryview](./memoryview_mwe.py), [min](./min_mwe.py)
- [next](./next_mwe.py), [object](./object_mwe.py), [oct](./oct_mwe.py), [open](./open_mwe.py), [ord](./ord_mwe.py)
- [pow](./pow_mwe.py), [property](./property_mwe.py), [range](./range_mwe.py), [repr](./repr_mwe.py), [reversed](./reversed_mwe.py), [round](./round_mwe.py)
- [sentinel](./sentinel_mwe.py) (Python 3.15+), [set](./set_mwe.py), [setattr](./setattr_mwe.py), [slice](./slice_mwe.py), [sorted](./sorted_mwe.py), [staticmethod](./staticmethod_mwe.py), [str](./str_mwe.py), [sum](./sum_mwe.py), [super](./super_mwe.py)
- [tuple](./tuple_mwe.py), [type](./type_mwe.py), [vars](./vars_mwe.py), [zip](./zip_mwe.py)

## Creating an MWE

Add a small, self-contained script to this folder that demonstrates one Python concept. For example, run the print MWE from the repository root:

```bash
python3 software/python/05-projects/print_mwe.py
```

Expected output:

```text
Hello, world!
```

Run the input MWE from the repository root:

```bash
python3 software/python/05-projects/input_mwe.py
```

Type a name and press Enter. For example:

```text
Name: Ada
Hello, Ada!
```

List new examples here and link them from the relevant Python reference page. See the [MWE guidelines](../../../patterns/02-minimal-working-examples.md) for what makes an example useful.

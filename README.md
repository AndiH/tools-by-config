# Tools By Config

This is a generalization of [Rsync By Config](https://github.com/AndiH/rsync-by-config) which reads in a hidden `.tbc.toml` file and runs commands in there.

**This is only a rough sketch. Basically no sanity checks are done and no additional features are implemented beyond the core features.**

## Rationale

Do you launch CLI applications with complex arguments repeatedly and use your Shell history to find the last invocation? _TBC_ tries to solve this by creating a folder-specific place for such frequently used commands; `.tbc.toml`.

## Usage

Add `tbc.py` to your `$PATH`. Create a `.tbc.toml` file in a directory and add a command with arguments like:

```TOML
[my_echo]
    exe = "echo"
    args = ["Hello", "World"]
```

Now call `tbc.py` in the directory and see it print "Hello World". That's it.

If no explicit command is given to `tbc.py`, the first command specified in `.tbc.toml` is used. See `tbc.py --help`

## Requirements

The following Python packages are required

* `click`
* `toml`
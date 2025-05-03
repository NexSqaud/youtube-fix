# YouTube Main Page grid fix

Browser extension that fixes huge ass main page grid on YouTube main page.

Sets items per row to 4.

## Building

You can use any of your favorite build systems to build:

`Python script`:
```shell
$ python3 build.py
```

`nob.h`:
```shell
$ cc -o nob nob.c
$ ./nob
```

`Bash script`:
```shell
$ ./build.sh
```

Or manually:
```shell
$ mkdir build
$ zip build/extension.zip fix.css manifest.json
```

After building you can find `extension.zip` in `build` folder
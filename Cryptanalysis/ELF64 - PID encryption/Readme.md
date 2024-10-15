Quite simply :
```sh
./binary4 `python -c 'import crypt; import os; print(crypt.crypt(str(os.getpid() + 1), "$1$awesome"))'`
```
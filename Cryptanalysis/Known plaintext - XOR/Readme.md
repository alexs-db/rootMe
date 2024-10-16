Using the xortool python tool provided by hellman on GitHub, we analyze the file :
```markdown
## XOR Tool Usage

```bash
$ python xortool.py ch3.bmp
```

### The most probable key lengths:
- 1: 10.6%
- 3: 11.6%
- **6: 18.5%**
- 9: 8.8%
- 12: 13.8%
- 15: 6.6%
- 18: 10.4%
- 24: 8.1%
- 30: 6.4%
- 36: 5.2%

Key-length can be `3*n`. The most possible character is needed to guess the key!

**Download:** It seems that the pass is composed of 6 characters.

The doc states:
> “The most common use is to pass just the encrypted file and the most frequent character (usually 00 for binaries and 20 for text files)”.

### Trying with `00`:

```bash
$ python xortool.py -c 00 ch3.bmp
```

1 possible key(s) of length 6:
```
fallen
```

Found 0 plaintexts with 95.0%+ printable characters. Cool.

As a bonus, the program outputs the photo in plain text in the `xortool_out` directory.
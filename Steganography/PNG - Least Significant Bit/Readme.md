A reusable tool written with the Python Tinyscript package is available on this Gist. In particular, it allows you to brute-force a readable string by trying LSB steganography parameters (such as taking only every other bit).

The solution is as follows:

```bash
$ stegolsb bruteforce ch9.png
12:34:56 [INFO] 16:TFdmMDdyc01iaUE2

$ echo -en "TFdmMDdyc01iaUE2" | base64 -d
```

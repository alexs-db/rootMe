Resolution:

```sh
$ strings ch1.bin
/lib/ld-linux.so.2
__gmon_start__
libc.so.6
_IO_stdin_used
puts
realloc
getchar
__errno_location
malloc
stderr
fprintf
strcmp
strerror
__libc_start_main
GLIBC_2.0
PTRh@
[^_]
%s : “%s”
Allocating memory
Reallocating memory
123456789
############################################################
## Welcome to this cracking challenge ##
############################################################
Please enter the password :
Well done, you can validate the challenge with the pass: %s!
Too bad, try again.
```

We see the message strings at the end, preceded by a string “[...]”. We can assume that this has something to do with the pass we're looking for. If you try to validate with this string, you'll see that it is indeed the unencrypted pass.
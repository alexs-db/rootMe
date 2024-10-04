First, we open the executable in a new project using Ghidra, the NSA's reverse engineering framework.
Then search for the strings present: `Search > For Strings > Search`

There are several interesting strings: `“Usage : %s pass”`, `“Gratz man :)”` and `“Wrong password”`.

```
s_Usage:_%s_pass_00404044 XREF[2]:     FUN_00401700:00401706(*),
                                      FUN_00401700:00401712(*)  
00404044 55 73 61 ds “Usage: %s pass”
         67 65 3a
         20 25 73
s_Gratz_man_:)_00404053 XREF[2]:     FUN_00401726:00401791(*),
                                      FUN_00401726:00401796(*)  
00404053 47 72 61 ds “Gratz man :)”
         74 7a 20
         6d 61 6e
s_Wrong_password_00404060 XREF[1]:     FUN_00401726:004017aa(*)  
00404060 57 72 6f ds “Wrong password”
         6e 67 20
         70 61 73
0040406f 00 ??         00h
```

We can see that the strings `“Gratz man :)”` and `“Wrong password”` are used in the function `FUN_00401726`.

So we look at the contents of this function (by double-clicking on the label), and in the decompiler we see the following C code:

```c
void __cdecl FUN_00401726(char *param_1,int param_2)
{
 if (((((param_2 == 7) && (*param_1 == 'S')) && (param_1[1] == 'P')) &&
     ((param_1[2] == 'a' && (param_1[3] == 'C')))) &&
    ((param_1[4] == 'I' && ((param_1[5] == 'o' && (param_1[6] == 'S')))))) {
   printf(“Gratz man :)”);
                   /* WARNING: Subroutine does not return */
   exit(0);
 }
 puts(“Wrong password”);
 return;
}
```

Note that the characters tested in the cascade conditions form the flag.
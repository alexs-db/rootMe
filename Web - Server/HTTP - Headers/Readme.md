Use the free Postman software to make a GET request http://challenge01.root-me.org/web-serveur/ch5/

We can see in the query responses the line "header-rootme-admin →none" which is unusual.

Postman allows us to make a GET request with pre-configured Headers. So now you just have to repeat the same GET request with Header: Key: header-rootme-admin; Value: Any value works and the response displays the correct password!

If you want you can also use curl for requests.
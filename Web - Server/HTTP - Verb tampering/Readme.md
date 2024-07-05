No need to look very far, just send any REST request, other than GET or POST. The query doesn't even need to exist. In fact, the authentication request is only triggered if GET or POST requests are present in the http header, whereas it should be triggered for any type of request to this page (even the most absurd).

Example :

curl -v http://challenge01.root-me.org/web-serveur/ch8/ -X SOMETHING
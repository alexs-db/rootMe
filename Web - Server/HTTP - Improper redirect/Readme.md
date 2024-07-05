First of all we know that we are dealing with a redirection, in php..
so probably something like "header(’location: ...’) "
Then we also know that if there is no exit() after a redirection like this,
we are not forced to leave the page right away and we can continue
to read the stream, we can use curl to do this:

$ curl -v http://challenge01.root-me.org/web-serveur/ch32/

we then obtain the rest of the flow following the header(’location: ...’) where the flag is located.
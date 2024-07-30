We click on the link allowing us to view saved emails, and we see that the url changes as follows:

http://challenge01.root-me.org/web-serveur/ch7/?c=visiteur

We then change the visitor value to admin, but this returns an error.

Let's take a look at the header with curl :

curl -v “http://challenge01.root-me.org/web-serveur/ch7/?c=visiteur”

We see a cookie with the value: ch7=visitor

Now all you have to do is deduce what to replace the cookie value with. You can do this directly with the browser or with curl.

Good luck ^^
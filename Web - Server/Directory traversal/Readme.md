When we launch the challenge, we arrive at the following page “http://challenge01.root-me.org/web-serveur/ch15/ch15.php”, which doesn't give us much information. Looking at the various links, we see that the “gallery” parameter could well be exploited, as it seems to take the page we wish to display as a parameter.

Enter “http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=/” and you'll see 5 images corresponding to the page links and 1 image giving no information. Looking at the source code, we see that the link for this new image points to “86hwnX2r”, which is our hidden page.

Entering “http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=86hwnX2r” as the url, we obtain three icons. If we look again at the source code of this page, we can see a rather telling file: “galerie/86hwnX2r/password.txt”, which contains the password we're looking for.

Enter “http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt” to obtain the password.
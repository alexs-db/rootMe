In the "forgotten files" series, a very common flaw is forgetting php framework installation files in the web tree. Here, we look at the source code of the page http://challenge.root-me.org/web-serveur/ch6/ We find an HTML comment there:

/web-server/ch6/phpbb
We google a bit with keywords like "install file phpbb" and we quickly find that the installation file is called "/install/install.php". So we run to our challenge, we ask for the page /web-serveur/ch6/phpbb/install/install.php and there we find the flag :)
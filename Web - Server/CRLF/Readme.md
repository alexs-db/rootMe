First of all, what is 'CRLF'? CRLF stands for CR and LF: Carriage Return and Line Feed, or in hexadecimal 0x0d and 0x0a (\r\n). These two characters simply represent a line feed.

Each operating system uses these characters differently:

First of all, if you type any “Login/Password”, a message is automatically added to the Log file.

Example :

User failed to authenticate.
And we note that the GET parameters are :

http://challenge01.root-me.org//web-serveur/ch14/index.php?username=User&password=test

Exploitation : 

Let's return to the challenge, which asks us to insert erroneous data in the Log file. Let's play with these parameters. Of course, we'll need to do some URL encoding (%20 for ' ', %0D for 'CR' and %0A for 'LF').

First test

http://challenge01.root-me.org//web-serveur/ch14/index.php?username=injected%20file%0D%0AUser&password=test

in the log file, we find :

"injected file
User failed to authenticate."

Now we have our flaw. Now we're going to make the admin think he's tried to log in but failed. To do this, we insert in place of the other sentence an exact phrase that already exists in the log file, such as “admin failed to authenticate.” or successfully “admin authenticated.”

Now I will let you to find the flag with this clues, GL ! ^^
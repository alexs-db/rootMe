This challenge is always like the four first challenges of hash.

First you have to install HashCat which is a password recovery tool (like John the Ripper e.g). You have a lot of documentation, which explain how to install and use this tool.

I will give you a clue of what you have to do to find the flag.

After install Hashcat, you have to use a dictionary of passwords (rockyou.txt is the best) to brut force the NT hash on the file of the subject.

Indeed you have to use a dictionary file and a file with the hash to find the flag. But this time I will let you find the NT hash alone ;)

Here a little clue to help you : hashcat -a 0 -m 0 hashs.txt rockyou.txt (don't forget to adapt this command).

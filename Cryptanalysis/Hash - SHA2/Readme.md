This challenge is a little bit different than the others.

First you have to install HashCat which is a password recovery tool (like John the Ripper e.g). You have a lot of documentation, which explain how to install and use this tool.

I will give you a clue of what you have to do to find the flag.

After install Hashcat, you have to use a dictionary of passwords (rockyou.txt is the best) to brut force the  hash on the file of the subject.

Indeed you have to use a dictionary file and a file with the hash to find the flag. But be attentive to what it ask on the subject, you have a little manipulation to do after find the decrypt SHA2 hash.

To correctly decode the hash you have to remove 'k' from the string.

Here a little clue to help you : hashcat -a 0 -m 0 hashs.txt rockyou.txt (don't forget to adapt this command).

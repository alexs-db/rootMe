By reading the rfc, we know that the format of the md5 will be:

<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>motdepasse

so I use a dictionary attack and with awk, I create a new file ‘new_file’ with the addition at the beginning of each line ‘<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72> ’ :

awk ‘$0=’<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>‘$0’ rockyou.txt > new_file

Then, to decrypt the password, I use hashcat on my new file:
hashcat -m 0 ‘4ddd4137b84ff2db7291b568289717f0’ new_file
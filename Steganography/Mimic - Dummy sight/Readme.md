Downloading the challenge archive, we end up with two files: “plaintext” and “ciphertext”.

Reading the page provided in the resources, we come across a user's commentary presenting a script called Plainsight, which hides a message in readable text from the text contained in another file. In the example given by the script's author, we notice that one of the execution parameters is called “ciphertext”, exactly like the challenge file. Let's take a closer look.

The script is based on an additional text file that serves as a key for encrypting or decrypting a message.

Since “ciphertext” is the encrypted file, we'll try to decrypt it using the “plaintext” file as the key:

```bash
$ cat ciphertext | plainsight -m decipher -f plaintext > deciphered
$ cat deciphered
```

The resulting code is :

```bash

$ROO = “MV93!fbjB0X200bDFjMTB1NV#F80b^h”.Replace(“!”, “NHN”).Replace(“@”, “q”).Replace(“#”, “80d”).Replace(“<”, “ZXI=”). Replace(“%”, “GVF”).Replace(“^”, “Gw”).Replace(“&”, “cTW”).Replace(“*”, “zb2Z”).Replace(“[”, “T”).Replace(“]”, “iZW1”).Replace(“{”, “Fdi”);
$TME = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($ROO));
```

After executing this code, we get the flag.
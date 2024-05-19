We therefore have an exchange of Hello Packets between 12.0.0.x and 224.0.0.5.

OSPF packets are made up of 3 ‘sub-parts’:
 OSPF Header
 OSPF Hello Packet
 OSPF LLS Data Block

In the Header part, there is an Auth Crypt Data field: xxxxxx

A look at the Cisco website shows that this field includes an authentication part managed by an md5 hash in most cases.

To extract the hashes from the pcapng capture, we can use the ettercap command, with the arguments Tqr for :
 
--> Text
--> Quiet
--> Read

 We can therefore use John The Ripper to manage the hash format and then find the authentication key.
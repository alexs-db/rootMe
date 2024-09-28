As already mentioned in the previous solutions, we ask around with the resource provided, but the tool quoted, Hydan, only works on x86 and seems to have disappeared from the web many, many years ago.
After some research into alternatives, we came across steg86's GitHub. So we installed this tool by following the instructions in their README. To do this, you need to install Rust, as the tool is written in this language and uses its cargo package manager.

The README suggests doing a `cargo install steg86`, which seems the simplest option. However, as I write this solution, using this command doesn't work (I've opened an issue on their GitHub to get the problem fixed). So I opted to clone the repository and recompile it with `cargo build` (the generated executable can be found in `./target/debug`).

Let's try using the tool on our binary:

```sh
$ ./steg86 extract innocent.bin
Fatal: incompatible steg86 version (expected 1, got 0)
```

We get a nice incompatible version error. It seems to be the wrong steg86 version. To check, I run the same command on an executable that I know contains no message hidden by steg86:

```sh
$ ./steg86 extract /bin/ls
Fatal: bad steg86 magic (expected 119, got 0)
```

This is not the same error, so steg86 seems to use a magic byte to make sure the file uses it. This means that our `innocent.bin` file does indeed use steg86!

As the problem seems to lie with the tool, I decided to take a step back in the repository versions. As this challenge was released in November 2021, I chose to revert the repository to a commit from that month, using a `git log` to track commits to that period and then `git checkout [commit id]`.

All I had to do was recompile one shot, and this time, the tool worked and the flag was retrieved:

```sh
$ ./steg86 extract innocent.bin

y0u_*****du41s
```

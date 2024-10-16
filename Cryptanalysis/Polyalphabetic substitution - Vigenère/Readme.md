With all the punctuation at our disposal, we can try to recognize words instead of making a classic attack, in order to simplify our task. One word in particular is somewhat unusual in form: “nnxfnyh'tyv”. Since the only French word with an apostrophe followed by three letters (or at least the most common one) is “aujourd'hui”, we assume NNXFNYH'TYV = aujourd'hui.
# Vigenère Cipher Decryption

We use a Vigenère square and apply the inverse operation to the Vigenère cipher on this assumption:

- To obtain `N` from `a`, the key is `N`
- To obtain `N` from `u`, the key is `T`
- To obtain `X` from `j`, the key is `O`

We obtain: `NTORTHEMEN`.

We have an `N` at the beginning and one at the end. An additional assumption is that the key is the same letter, so it would be 9 characters long.

We therefore assume that the key is `NTORTHEME`.

From here, decryption can be easily automated: either write a script, or use an online tool.

We test with this key on our tool, and get nothing conclusive. But nothing says that `N` is the beginning of the key: the key can also be one of the 9 possible “shifts” (or rather, permutations):

- `TORTHEMEN`
- `ORTHEMENT`
- ...

So we try out these permutations and get a convincing result with `THEMENTOR`, which is, incidentally, the pseudonym of the author of the decrypted text, The Hacker Manifesto.

After a little search on web, you will find the name of the auhtor, so the flag.
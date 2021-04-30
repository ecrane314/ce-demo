Notes from guide at https://www.devdungeon.com/content/gpg-tutorial

# Install
Mac:  `brew install gnupg`
Linux Debian: `sudo apt install gpg`
`gpg --help` prints version

# Encrypt, Decrypt, Sign, Verify
Symmetric and Asymmetric encryption where Symmetric is same password to encrypt
and decrypt and asymmetric.

Message == binary file == document == viable input for all functions here

Output can be `--armor` (ascii characters) or binary, which is more efficient

`file.gpg` is binary encrypted and `file.asc` is armor and can be processed as text

--cipher-algo aes256 is strong and fast, good general pick for asymmetric
--opengpg  use strict OpenPGP behavior.....  As opposed to what? Some GNU specific?
Resets all packet, cipher and digest options to strict OpenPGP behavior. This option implies 
--allow-old-cipher-algos. Use this option to reset all previous options like --s2k-*, --cipher-algo,
 --digest-algo and --compress-algo to OpenPGP compliant values. All PGP workarounds are disabled.

gpg --gen-key  will creat public, private, a keybox entry, and a revocation certificate file

~/.gnupg$ kbxutil [--stats] pubring.kbx
This will show blobs in keybox file (.kbx)

WHEN SIGNING, the output is unencrypted original document with signature at the end. Not used to encrypt
and secure the information and guarantees no confidentiality

gpg --decrypt message will include the verification at the bottom. 
Of course, in that example, the body wasn't encrypted. Alternatively,
gpg --verify message will show just the verification.

As another option, the signature may have been created separately, in a .sig file. In this case,
Calling verify on the sig will look for a matching original file by same name (less .sig)

# Key Servers

If you sign a commit, then you must post your public key so others may verify it
gpg --keyserver hkp://pgp.blah.edu --send-keys XXXXXX
hkp is http key protocol for passing them around.

gpg --keyserver pgp.mit.edu --search-keys name@email.com
Let's you search for a public key and pull down

Remember you don't necessarily have to sign a message. Can encrypt anonymously.

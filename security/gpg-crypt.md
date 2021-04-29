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

`file.gpg` is binary encrypted and `file.gpg.asc` is armor and can be processed as text
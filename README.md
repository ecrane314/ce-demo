# Demos and scripts
My Customer Engineer demo utilities for GCP

### Authenticating with cloud credentials

1) See set_auth to source your credentials to use other tools

### Authenticating new machines for github
From [Github docs](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

1) $ ssh-keygen -t ed25519 -C "your_email@example.com"  
Legacy alternative: $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

2) $ eval "$(ssh-agent -s)"  
Run agent in separate process and return

3) $ ssh-add ~/.ssh/id_ed25519  
Add private key to local agent

4) Copy public key, add to account

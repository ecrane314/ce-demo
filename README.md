# Demos and scripts
My Customer Engineer demo utilities for GCP

### Authenticating with cloud credentials

1) See set_auth to source your credentials to use other tools

### Authenticating new machines for github
From [Github docs](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

1) $ ssh-keygen -t ed25519 -C "your_email@example.com"  
Legacy alternative: $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

2a) Try this before 2 and 3 and skip to 4 to test. In your `~/.ssh/config` file, put the following. Remember the github user name is github, not your email address etc. That's specific to their sshd implementation.

```
Host raspberrypi.local
	HostName raspberrypi.local
	User <user name>
	IdentityFile ~/.ssh/<key name>

Host github.com
    HostName github.com
    User github
    IdentityFile ~/.ssh/github
```

2) $ eval "$(ssh-agent -s)"  
Run agent in separate process and return

3) $ ssh-add ~/.ssh/id_ed25519  
Add private key to local agent

4) Copy public key, add to account


self link `git clone https://github.com/ecrane314/ce-demo.git`

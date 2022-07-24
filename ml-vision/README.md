# Coral DevBoard Setup
https://coral.ai/docs/dev-board/get-started

## 1 Gather Reqs
For Serial Connection, make sure you'e using a USB data cable and not just power. On Mac, go to system profile and USB section. Then make sure when you plug in your device and refresh the page, you see a new device listed.

If nothing new is listed, the kext probably didn't load and the host is not talking to device, regardless of any lights lit on the board.

## 2 Flash the Board

Using your SD card you made with, optionally, the Raspi installer tool or Balena etcher. Raspi does both and let's you plug in config on that end so why not. Worked for me

## 3 Install MDT
Using env, installed `python3 -m pip install mendel-development-tool` no `--user` like in guide because on Mac you're probably using virtualenv where user packages aren't a thing

## 4 Connect via MDT
Connect via Serial Connection. We will manually copy an ssh key over the serial console instead of the USB OTG business with the USB-C connector and MDT. This will let us connect totally wireless going forward. https://coral.ai/docs/dev-board/mdt/#mdt-on-macos

On Coral
`mkdir /home/mendel/.ssh && vi /home/mendel/.ssh/authorized_keys`

On Mac
`ssh-keygen -t rsa -m PEM` and name coral_rsa or similar. Confirm permissions are equiv to
chmod 600

copy private to ~/.config/mdt/keys/

On Mac, added a block to ~/.ssh/config as follows

```
Host xenial-dog
	User mendel
	HostName xenial-dog.local
	IdentityFile ~/.ssh/coral_rsa.pub
```

copy the public to coral authorized_keys file as above

`nmtui` over serial connection will let you setup wifi such that you can test your ssh key was set correctly and you can connect.

`mdt shell` to connect once keys and wifi are ready.

#TODO Stuck here. mdt shell and ssh not connecting. I suspect the key creation instructions are buggy as the ssh agent asks to verify ECDSA fingerprints when the key creation string uses RSA. Start that over.

##Android Tools
Only if needed. May no longer be needed with MicroSD flashing procedure.
Download from https://developer.android.com/studio/releases/platform-tools#downloads
mv ~/Download/fastboot ~/.local/bin
fastboot --version # verify it works from path




# Counting objects

#TODO Read and do https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/

sudo apt-get install libx11-dev libgtk-3-dev  
sudo apt-get install libopenblas-dev liblapack-dev  

Installing dlib in target environment  
https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/  
"Examples of object tracking algorithms include MedianFlow, MOSSE, GOTURN, kernalized correlation filters, and discriminative correlation filters, to name a few."


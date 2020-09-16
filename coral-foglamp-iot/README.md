Coral Foglamp Lab Friction Log
evancrane@
Sep 16 2020

Internal link
https://docs.google.com/document/d/1D8Ed47S6h7z2MUvLN3fOqf3qrY4Az9-wtbigBQ0vCCw/edit#

#Repository
https://github.com/kingman/coral-environ-stream-processing

Set-env.sh script could be converted to a config file that's sourced. There could be extra lines to define project variables. Modifying a config file allows better persistence if rerunning this step after cloudshell times out. Using bash "source" command works better than running it as a script given subroutine context.

Step 1 about Cloud Shell could include requirements list ie docker (incl. maven) and terraform are required.

Terraform main.tf uses default network, will fail in Dataflow if custom networks in use, as was my case. Added network and subnet definition to fix.

"Verify the result data" This skips over the North and South bridge configuration in foglamp. Should we expect data to flow yet?

Why not configure the dev board before establishing the dataflow pipeline and cloud resources which cost money if left unatended? You also can't confirm that your data pipeline is working correctly until you have a source. Fake source to start?

# Foglamp
Installing Foglamp where Fledge was previously installed and removed returns errors. sudo apt clean && sudo apt autoremove don't seem to fix the issue.

```
Resolving data directory
Data directory already exists. Updating data/extras/fogbench/fogbench_sensor_coap.template.json only.
cp: cannot stat '/usr/local/foglamp/data.new/extras/fogbench/fogbench_sensor_coap.template.json': No such file or directory
dpkg: error processing package foglamp (--configure):
 installed foglamp package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 foglamp-gui
 foglamp
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
Enviro board - Don't have enviro board, skipped this section. Consider splitting the enviro and person apt install commands so that the branches of the lab can be followed independently. The enviro board installation errored out "impossible situation", likely because an enviro board is not present.

```
mendel@undefined-snail:~$ sudo apt clean && sudo apt auto-remove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
5 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Setting up foglamp (1.8.1) ...
Install python dependencies
Requirement already satisfied: aiohttp==3.6.2 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 2)) (3.6.2)
Requirement already satisfied: aiohttp_cors==0.7.0 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 3)) (0.7.0)
Requirement already satisfied: cchardet==2.1.4 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 4)) (2.1.4)
Requirement already satisfied: pyjwt==1.6.4 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 5)) (1.6.4)
Requirement already satisfied: pyjq==2.3.1 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 8)) (2.3.1)
Requirement already satisfied: zeroconf==0.27.0 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 11)) (0.27.0)
Requirement already satisfied: async-timeout<4.0,>=3.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.0.1)
Requirement already satisfied: multidict<5.0,>=4.5 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (4.7.6)
Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (1.5.1)
Requirement already satisfied: chardet<4.0,>=2.0 in /usr/lib/python3/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.0.4)
Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (20.1.0)
Requirement already satisfied: six in /usr/lib/python3/dist-packages (from pyjq==2.3.1->-r /usr/local/foglamp/python/requirements.txt (line 8)) (1.12.0)
Requirement already satisfied: ifaddr in /usr/local/lib/python3.7/dist-packages (from zeroconf==0.27.0->-r /usr/local/foglamp/python/requirements.txt (line 11)) (0.1.7)
Requirement already satisfied: typing-extensions>=3.7.4; python_version < "3.8" in /usr/local/lib/python3.7/dist-packages (from yarl<2.0,>=1.0->aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.7.4.3)
Requirement already satisfied: idna>=2.0 in /usr/lib/python3/dist-packages (from yarl<2.0,>=1.0->aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (2.6)
Resolving data directory
Data directory already exists. Updating data/extras/fogbench/fogbench_sensor_coap.template.json only.
cp: cannot stat '/usr/local/foglamp/data.new/extras/fogbench/fogbench_sensor_coap.template.json': No such file or directory
dpkg: error processing package foglamp (--configure):
 installed foglamp package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of foglamp-south-person-detection:
 foglamp-south-person-detection depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-south-person-detection (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-north-gcp:
 foglamp-north-gcp depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-north-gcp (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-filter-expression:
 foglamp-filter-expression depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-filter-expression (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-south-sinusoid:
 foglamp-south-sinusoid depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-south-sinusoid (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 foglamp
 foglamp-south-person-detection
 foglamp-north-gcp
 foglamp-filter-expression
 foglamp-south-sinusoid
E: Sub-process /usr/bin/dpkg returned an error code (1)
mendel@undefined-snail:~$ 
```

Installing after cleaning and updating doesn't seem to work, even after I removed the old fledge apt source definition.
```
mendel@undefined-snail:~$ sudo apt-get -y install foglamp-filter-expression foglamp-south-person-detection foglamp-north-gcp 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
foglamp-filter-expression is already the newest version (1.8.1).
foglamp-south-person-detection is already the newest version (1.8.1).
foglamp-north-gcp is already the newest version (1.8.1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
5 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Setting up foglamp (1.8.1) ...
Install python dependencies
Requirement already satisfied: aiohttp==3.6.2 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 2)) (3.6.2)
Requirement already satisfied: aiohttp_cors==0.7.0 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 3)) (0.7.0)
Requirement already satisfied: cchardet==2.1.4 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 4)) (2.1.4)
Requirement already satisfied: pyjwt==1.6.4 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 5)) (1.6.4)
Requirement already satisfied: pyjq==2.3.1 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 8)) (2.3.1)
Requirement already satisfied: zeroconf==0.27.0 in /usr/local/lib/python3.7/dist-packages (from -r /usr/local/foglamp/python/requirements.txt (line 11)) (0.27.0)
Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (20.1.0)
Requirement already satisfied: multidict<5.0,>=4.5 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (4.7.6)
Requirement already satisfied: chardet<4.0,>=2.0 in /usr/lib/python3/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.0.4)
Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (1.5.1)
Requirement already satisfied: async-timeout<4.0,>=3.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.0.1)
Requirement already satisfied: six in /usr/lib/python3/dist-packages (from pyjq==2.3.1->-r /usr/local/foglamp/python/requirements.txt (line 8)) (1.12.0)
Requirement already satisfied: ifaddr in /usr/local/lib/python3.7/dist-packages (from zeroconf==0.27.0->-r /usr/local/foglamp/python/requirements.txt (line 11)) (0.1.7)
Requirement already satisfied: idna>=2.0 in /usr/lib/python3/dist-packages (from yarl<2.0,>=1.0->aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (2.6)
Requirement already satisfied: typing-extensions>=3.7.4; python_version < "3.8" in /usr/local/lib/python3.7/dist-packages (from yarl<2.0,>=1.0->aiohttp==3.6.2->-r /usr/local/foglamp/python/requirements.txt (line 2)) (3.7.4.3)
Resolving data directory
Data directory already exists. Updating data/extras/fogbench/fogbench_sensor_coap.template.json only.
cp: cannot stat '/usr/local/foglamp/data.new/extras/fogbench/fogbench_sensor_coap.template.json': No such file or directory
dpkg: error processing package foglamp (--configure):
 installed foglamp package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of foglamp-south-person-detection:
 foglamp-south-person-detection depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-south-person-detection (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-north-gcp:
 foglamp-north-gcp depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-north-gcp (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-filter-expression:
 foglamp-filter-expression depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-filter-expression (--configure):
 dependency problems - leaving unconfigured
dpkg: dependency problems prevent configuration of foglamp-south-sinusoid:
 foglamp-south-sinusoid depends on foglamp (>= 1.8); however:
  Package foglamp is not configured yet.

dpkg: error processing package foglamp-south-sinusoid (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 foglamp
 foglamp-south-person-detection
 foglamp-north-gcp
 foglamp-filter-expression
 foglamp-south-sinusoid
E: Sub-process /usr/bin/dpkg returned an error code (1)
mendel@undefined-snail:~$ 
```


**South Service**  Can we add an option for Raspberry Pi with SenseHat? The south plugin worked great for getting that data into Foglamp.

**Event Notifications** Include instructions or a link on how to do this via config file or API. Running through GUI doesn't scale. I like the prebuilt options for guiding adoption. What's the runtime for the notification engine? For more advanced customers or if logic already exists, might we instead run containers on the gateway for this purpose?


**Installing GCP North Plugin in FogLAMP**
Why not point to the readthedocs on the public site? In this way they can follow any updates to the public site. Please include some info or a link as to why we're using the google cert. This step seems strange and isn't required for regular iot demo work. Is this a foglamp requirement? Step 6 describes copying the key to the store, which I imagine is similar to the GUI version in the public doc. I followed GUI and north bridge doesn't seem to be pushing anything to the pubsub topic.  https://foglamp.readthedocs.io/en/latest/plugins/foglamp-north-gcp/index.html#upload-your-certificates 

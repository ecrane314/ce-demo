Coral Foglamp Lab Friction Log


Internal link
https://docs.google.com/document/d/1D8Ed47S6h7z2MUvLN3fOqf3qrY4Az9-wtbigBQ0vCCw/edit#


Set-env script has extra lines I added to define my project. Sourcing works better than running it as a script.

docker (incl. maven)  and terraform are required. Cloud shell better

Issue :dataflow uses default network, will fail if custom networks in use



When installing Foglamp where Fledge was previously installed and removed:

Resolving data directory
Data directory already exists. Updating data/extras/fogbench/fogbench_sensor_coap.template.json only.
cp: cannot stat '/usr/local/foglamp/data.new/extras/fogbench/fogbench_sensor_coap.template.json': No such file or directory
dpkg: error processing package foglamp (--configure):
 installed foglamp package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 foglamp-gui
 foglamp
E: Sub-process /usr/bin/dpkg returned an error code (1)

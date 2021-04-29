#Set desired keys to file names in current directory
#[WIP] was used as part of lab, still evaluating usage

sudo apt-get install -y wget openssl python-pip
openssl ecparam -genkey -name prime256v1 -noout -out $PRV_KEY
openssl ec -in $PRV_KEY -pubout -out $PUB_KEY
wget -N https://pki.goog/roots.pem


#https://cloud.google.com/docs/authentication/production#automatically
#Application Default Credentials will be found automatically by most client
#   libraries but ONLY when running inside GCP

#https://cloud.google.com/docs/authentication/production#manually
#ADC must be defined when external to GCP, ie local or edge
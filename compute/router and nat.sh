# Create a Cloud Router in your region and create a Cloud NAT instance for that router
# This is useful for GCE instances with only internal IP addresses

gcloud compute routers create <router-name-central1> --project=<your project> \
--region=us-central1 --network=default

gcloud compute routers nats create <nat-name> --router <name-from-previous-step> \
   --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges
# Compute and Networking in GCP

## Cloud Router and NAT
Create a Cloud Router in your region and create a Cloud NAT instance for that router.
This is useful for GCE instances with only internal IP addresses

`gcloud compute routers create <router-name-central1> --project=<your project> \
--region=us-central1 --network=default`

`gcloud compute routers nats create <nat-name> --router <name-from-previous-step> \
   --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges`

## Load Balancing
[explained](https://cloud.google.com/load-balancing/docs/https#component)
1. Frontend is synonymous with Forwarding rules in various UI. This is a config that goes to a common GFE
This provides an IP address and port and passes traffic on to a chosen target. This target can be a target proxy of 
various types. NOTE: Regional Externals also require their own subnet.
1. The target proxy terminates SSL and makes decisions on where to route traffic based on an associated...
1. compute#urlMap resource. In simplest form, this is config that points default and other traffic to backend-services, backend-buckets, or redirects
1. backend-services object. A backend-services object targets one of 4 backends.
 Instance group, or NEGs for internet, serverless, or gce/gke. 
 1. Optionally, 
 [configure cloud armor](https://cloud.google.com/armor/docs/configure-security-policies#https-load-balancer)
 Armor is not used in the sdk naming convention. To attach, `gcloud compute backend-services update <backen-service-name>
 --security-policy mobile-clients-policy`
1. compute#networkEndpointGroup resource. Which points to a...
1. Cloud function deployment

## Private Services Connect / Access incl Cloud SQL

Open your VPCs page, open your network of choice, and navigate to the private services tab.

For your current subnets, observe their CIDR blocks. Swap network name
```
gcloud compute networks subnets list --network custom-vpc
```

In console, reserve your IP range, create your PSC connection, and then look at peering it created
```
gcloud compute networks peerings list
```

Observe the route for your peering relationship
```
gcloud compute networks peerings list-routes --direction INCOMING servicenetworking-googleapis-com --network custom-vpc --region us-central1
```

Create a Cloud SQL instance with private addresses and observe that your instance was placed in that block
```
gcloud sql instances list
```
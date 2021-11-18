gcloud compute instances create-with-container gpu-vm-instance --project=ce-demo1 \
--zone=us-central1-a --machine-type=n1-standard-8 \
--network-interface=subnet=default,no-address --maintenance-policy=TERMINATE \
--service-account=990799180178-compute@developer.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
--accelerator=count=1,type=nvidia-tesla-t4 --min-cpu-platform=Intel\ Skylake \
--container-image=gcr.io/deeplearning-platform-release/base-cu113 \
--container-restart-policy=always \
--create-disk=auto-delete=yes,boot=yes,device-name=gpu-vm-instance,image=projects/cos-cloud/global/images/cos-stable-93-16623-39-21,mode=rw,size=10 \
--shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring \
--labels=container-vm=cos-stable-93-16623-39-21

#removing boot flag
gcloud compute instances create-with-container gpu-vm-instance --project=ce-demo1 \
--zone=us-central1-a --machine-type=n1-standard-8 \
--network-interface=subnet=default,no-address --maintenance-policy=TERMINATE \
--service-account=990799180178-compute@developer.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
--accelerator=count=1,type=nvidia-tesla-t4 --min-cpu-platform=Intel\ Skylake \
--container-image=gcr.io/deeplearning-platform-release/base-cu113 \
--container-restart-policy=always \
--create-disk=auto-delete=yes,device-name=gpu-vm-instance,image=projects/cos-cloud/global/images/cos-stable-93-16623-39-21,mode=rw,size=10 \
--shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring \
--labels=container-vm=cos-stable-93-16623-39-21
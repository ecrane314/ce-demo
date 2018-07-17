gcloud compute --project=ce-demo2 firewall-rules create allow-hadoop \
	--description=created-by-script --direction=INGRESS --priority=1000 \
	--network=default --action=ALLOW --rules=tcp:9870,tcp:8088 \
	--source-ranges=${IP}/32 --target-tags=hadoopacess


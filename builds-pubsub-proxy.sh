gcloud builds submit "gs://sureskills-ql/challenge-labs/tech-bash-2021/data-analytics/data_analytics.tar.gzip" \
    --tag=gcr.io/ce-demo1/pubsub-proxy 
    
    

#  Not using because have a tag, which requires a Dockerfile, which we also have
# --config=pubsub_ecommerce/package.json
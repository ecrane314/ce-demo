# Don't run this one until sql instance is ready

export SERVICE_ACCOUNT=$(gcloud sql instances describe ${MYSQL_INSTANCE} | grep serviceAccountEmailAddress | awk '{print $2;}')
export DB_IP_ADDRESS=$(gcloud sql instances describe ${MYSQL_INSTANCE} | grep ipAddress | awk '{print $3}')
export DB_PORT="Not assigned unless not the standard 3306"
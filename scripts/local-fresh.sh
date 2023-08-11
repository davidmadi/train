removeImage() {
    docker image rm train-app-api
}

docker-compose down
removeImage

docker-compose up


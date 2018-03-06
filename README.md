# k8s-workshop

## Running hello world

```
cd hello/
FLASK_APP=hello.py flask run
```

```
docker build -t gcr.io/YOUR-sandbox/hello .
gcloud docker -- push gcr.io/YOUR-sandbox/hello
```

On Cloud Shell:
```
gcloud docker -- pull gcr.io/YOUR-sandbox/hello
docker run gcr.io/YOUR-sandbox/hello
```

Deploying on Kubernetes:
```
$ kubectl create -f hello.yaml
deployment "hello-deployment" created
$ kubectl expose deployment hello-deployment --type=LoadBalancer --port 80 --target-port 5000
```

Rock Paper Scissors:
```
docker build -t gcr.io/YOUR-sandbox/rpsserver . -f Dockerfile.server
gcloud docker -- push gcr.io/YOUR-sandbox/rpsserver

docker build -t gcr.io/YOUR-sandbox/rpsclient . -f Dockerfile.client
gcloud docker -- push gcr.io/YOUR-sandbox/rpsclient

kubectl create -f server.yaml
kubectl create -f service-backend.yaml
kubectl create -f client.yaml
kubectl create -f service-frontend.yaml
kubectl describe services
```
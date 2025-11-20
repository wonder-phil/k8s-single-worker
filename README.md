# k8s-single-worker

## Set up minikube k8s on Ubuntu 24.02 running on an AMD64 AKA x86-64 architecture


https://kubernetes.io/docs/tutorials/kubernetes-basics/

> Testing a basic echo server with a load balancer

curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start  # Will take some time while giving lots of output


> add to .bashrc file:

alias k="minikube kubectl --"

source ~/.bashrc


k get po -A

docker ps

>
> Set up a load balancer for an echo server
>

k create deployment balanced --image=kicbase/echo-server:1.0

k expose deployment balanced --type=LoadBalancer --port=8080

minikube tunnel          # set up Exposed IP

k get services balanced  # find Exposed IP

> you will get an IP address such as,
http://10.106.25.147


> Test it
> 
curl -H "Content-Type: application/json" -d "{\"heads\":6 }" -X POST http://10.106.25.147:8080


## remove echo service test



k scale deployment balanced --replicas=0  # stop deployment

k get deploy

k get svc

k delete deployment balanced

k delete service balanced

minikube stop

## Set up worker service

> Go to the Docker subdirectory

minikube image build -t myworker .

Alternatively:
>> eval $(minikube docker-env)
>> docker build -t myworker .  

> Go back to the origional directory

k apply -f app.yaml

minikube tunnel          # set up Exposed IP

k port-forward svc/worker-service 8080:8080

curl http://localhost:8080/                # Test endpoint

curl -H "Content-Type: application/json" -d '{"heads": 8}' -X POST http://localhost:8080/compute

> Increase the replicas and run the following in the shell


EXTERNAL_IP=$(k get svc worker-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

for i in {1..20}; do   curl -s -H 'Connection: close' "http://$EXTERNAL_IP:8080/"; done


# k8s-single-worker

## Set up minikube k8s on Ubuntu 24.02 running on an AMD64 AKA x86-64 architecture


https://kubernetes.io/docs/tutorials/kubernetes-basics/

> Testing a basic echo server with a load balancer

curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start  # Will take some time while giving lots of output

minikube kubectl -- get po -A

docker ps

> add to .bashrc file:

alias k="minikube kubectl --"
source ~/.bashrc

>
> Set up a load balancer for an echo server
>

k create deployment balanced --image=kicbase/echo-server:1.0
k expose deployment balanced --type=LoadBalancer --port=8080

minikube tunnel          # set up Exposed IP
k get services balanced  # find Exposed IP


http://10.106.25.147


> Test it
> 
curl -H "Content-Type: application/json" -d "{\"heads\":6 }" -X POST http://10.106.25.147:8080


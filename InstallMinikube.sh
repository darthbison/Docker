#!/bin/sh

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube

minikube start --driver=$1
minikube addons enable dashboard
minikube addons enable metrics-server
minikube status


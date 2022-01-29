#!/bin/sh

IPADDR="10.0.0.10"
NODENAME=$(hostname -s)

kubeadm init --apiserver-advertise-address=$IPADDR  --apiserver-cert-extra-sans=$IPADDR  --pod-network-cidr=192.168.0.0/16 --node-name $NODENAME --ignore-preflight-errors Swap

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubectl get po -n kube-system

kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
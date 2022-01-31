#!/bin/sh

swapoff -a
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine

yum update -y
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

yum install docker-ce docker-ce-cli containerd.io

cat <<EOF | sudo tee /etc/docker/daemon.json {"exec-opts": ["native.cgroupdriver=systemd"], "log-driver": "json-file", "log-opts": {"max-size": "100m"}, "storage-driver": "overlay2"} EOF

systemctl enable docker
systemctl daemon-reload
systemctl restart docker

cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo [kubernetes] name=Kubernetes baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch enabled=1 gpgcheck=1 repo_gpgcheck=1 gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg exclude=kubelet kubeadm kubectl EOF

# Set SELinux in permissive mode (effectively disabling it)
setenforce 0
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl enable --now kubelet

yum -y install yum-versionlock
yum versionlock add kubelet
yum versionlock add kubeadm
yum versionlock add kubectl

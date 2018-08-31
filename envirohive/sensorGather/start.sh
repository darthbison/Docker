#!/bin/sh

systemctl enable mosquitto.service
service mosquitto restart

python gather.py

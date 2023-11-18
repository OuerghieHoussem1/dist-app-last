#!/bin/bash

nohup python3 /root/dist-app-last/test_app.py > /root/dist-app-last/logs/flask_server_log.log 2>&1 &1
nohup python3 /root/dist-app-last/stop_all.py > /root/dist-app-last/logs/stop_all_log.log 2>&1 &1
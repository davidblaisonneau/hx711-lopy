#!/bin/bash
TTY=$1

ampy --port $TTY put hx711.py /flash/hx711.py
ampy --port $TTY put config.py /flash/config.py
ampy --port $TTY put main_otaa_node.py /flash/main.py
ampy --port $TTY reset

miniterm.py $TTY 115200

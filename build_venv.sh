#!/usr/bin/env bash
rm -rf venv
mkdir venv
c:\\python\\python37\\python.exe -m venv venv
c:\\python\\python37\\python.exe -m pip install --upgrade pip
#venv/Scripts/pip.exe install --upgrade pip
#venv/Scripts/pip.exe install --user --upgrade pip
venv/Scripts/pip.exe install -r requirements.txt

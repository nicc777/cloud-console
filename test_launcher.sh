#!/bin/sh

SRC=$PWD

mkdir -p ~/tmp
cd ~/tmp
rm -frR venv
python3 -m venv venv
. venv/bin/activate
wp=`which python3`
echo "PYTHON: ${wp}"
pip3 install $SRC/dist/cloud_console-0.0.3.tar.gz
deactivate

echo
echo "Package installed in Python Virtual Environment at ~/tmp/venv"
echo

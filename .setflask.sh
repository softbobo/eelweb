#!/bin/bash
##mini-script to set up the environment for the tutorial

##set up three terminal tabs
xfce4-terminal --tab --drop-down --title='Flask Shell' -x bash -c "source venv/bin/activate; flask shell"
xfce4-terminal --tab --title='Flask Run' -x bash -c "source venv/bin/activate; flask run"
xfce4-terminal --tab --title='Virtual Mailserver' -x bash -c "source venv/bin/activate; 
python -m smtpd -n -c DebuggingServer localhost:8025"
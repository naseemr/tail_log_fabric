from fabric.api import *

env.user = 'userName'
env.key_filename = 'Path to ssh-key file'


svrlist1 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist2 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist3 = ['IP1','IP2','IP3','IP4',  ..,'IPN']
svrlist4 = ['IP1','IP2','IP3','IP4',  ..,'IPN']

@hosts(svrlist1)
def svrlist1tailf():
    try:
        sudo(' tail -f /var/log/messages')
    except KeyboardInterrupt:
        print("Stopped")
@hosts(svrlist2)
def svrlist2tailf():
    try:
        sudo(' tail -f /var/log/messages')
    except KeyboardInterrupt:
        print("Stopped")

@hosts(svrlist3)
def svrlist3tailf():
    try:
        sudo(' tail -f /var/log/messages')
    except KeyboardInterrupt:
        print("Stopped")
@hosts(svrlist4)
def svrlist4tailf():
    try:
        sudo(' tail -f /var/log/messages')
    except KeyboardInterrupt:
        print("Stopped")

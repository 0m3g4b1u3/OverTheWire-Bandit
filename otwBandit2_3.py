"""#############################################################################
##  PROGRAM:    OverTheWire BANDIT 2 -> BANDIT 3
##  FILENAME:   otwBandit2_3.py
##  AUTHOR:     0m3g4b1u3
#############################################################################"""
##  IMPORT(S)  ##
import paramiko

##  VARIABLE(S)  ##
host = 'bandit.labs.overthewire.org'
port = 2220
username = 'bandit2'
password = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'

##  START SSH CLIENT  ##
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

##  COMMAND(S)  ##
cmd = 'ls -la\n'
cmd += 'cat "spaces in this filename"'

##  RUN COMMAND(S)  ##
stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)

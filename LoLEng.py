import subprocess
import shlex
import time
import csv
import os
print("Please note this script requires adminstrator privileges.")
print("Waiting of League of Legends instance.")
def check_TW_league():
    output = subprocess.check_output(('TASKLIST', '/FI', 'IMAGENAME EQ LeagueClient.exe'))
    if output == b'INFO: No tasks are running which match the specified criteria.\r\n':
        return False
    else:
        args = subprocess.check_output(('wmic.exe', 'path', 'Win32_Process', 'where', 'name=\'LeagueClient.exe\'', 'get', 'commandline', '/format:csv'))
        parsed_args = shlex.split([x.replace('\r','') for x in args.decode().split('\n')][-2].split(',')[1])
        #print(parsed_args)
        if parsed_args[1]!="--locale=en_US":
            output = subprocess.check_output(('TASKKILL', '/F', '/FI', 'IMAGENAME EQ LeagueClient.exe'))
            new_args = parsed_args
            new_args[0] = "\"%s\"" % (new_args[0],)
            new_args[1] = "--locale=en_US"
            command = " ".join(new_args)
            print("Non-english League of Legends instance detected, restarting in English.")
            print(command)
            os.system(command)
            return True
        else:
            print("English League of Legends instance detected and ignored.")
            return False

while True:
    time.sleep(0.5)
    check_TW_league()

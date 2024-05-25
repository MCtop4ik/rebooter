import subprocess
import time


def run_command(command):
    process = subprocess.Popen(command, shell=True)
    time.sleep(10)
    process.terminate()


command_to_run = "./../../Desktop/xTunnel 4200"
while True:
    run_command(command_to_run)

# process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
#
# print("STDOUT:", stdout.decode())
# print("STDERR:", stderr.decode())

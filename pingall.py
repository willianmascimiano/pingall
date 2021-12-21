from os import kill
import subprocess
import sys


try:
    ip_list_file = sys.argv[1]
     
except IndexError as e:
    print("You must specify the source file name. \n e.g: python3 pingall.py source.txt"  )
    sys.exit(1)




ip_list_source= open(ip_list_file, 'r')
ips = ip_list_source.read()

result_online = []
result_offline=[]


with open(ip_list_file) as file:
    for line in file:
        domain = line.rstrip()
        command = "ping {} -t 1 | grep '1 packets received' ".format(domain)
        r = subprocess.run(command, shell=True, capture_output=True)
        r = str(r.stdout)
        print(r)
        if(len(r)>0):
            result_online.append(domain)
        else:
            result_offline.append(domain)



with open('servers_online.txt', 'w') as file:
    for l in result_online: 
        file.write(l)
        file.write('\n')


with open('servers_offline.txt', 'w') as file:
    for l in result_offline: 
        file.write(l)
        file.write('\n')


def help():
     print('Run: python3 pingall.py source.txt')
     sys.exit(1)
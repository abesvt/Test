import subprocess 
import time
import logging
import shutil
import os
import socket
import json
from telnetlib import IP


def startApp(app, testpath):
    with open(testpath + "\\stdout.txt","wb") as out, open(testpath + "\\stderr.txt","wb") as err:
        subprocess.run("node " + testpath + "\\app.js " + testpath + app, shell = True, stdout = out, stderr=err)
        time.sleep(5)
        
        
def downloadAndInstallApps(downloadPath, testpath, hostIPs, username, password):
    targets = []
    shutil.copytree(downloadPath, testpath)

    
    for host, ip in hostIPs.items():
        
        if host == "Agent": #since switch case is quite extensive coding in python
            with open(testpath + "\\agent\\outputs.json", 'r') as f:
                json_data = json.load(f)
                json_data['tcp']['host'] = gethostname(ip)
        
            with open(testpath + '\\agent\\outputs.json', 'w') as f:
                f.write(json.dumps(json_data))
                           
            connectRemoteShare(ip, username, password)
            shutil.copytree(testpath, "\\\\"+gethostname(ip)+"\\C$\\test")
            
        elif "Target" in host:
            targets.append(ip)
                        
            connectRemoteShare(ip, username, password)
            shutil.copytree(testpath, "\\\\"+gethostname(ip)+"\\C$\\test")
            
        elif host == "Splitter":
            for i, target in enumerate(targets):
                with open(testpath + "\\splitter\\outputs.json", 'r') as f:
                    json_data = json.load(f)
                    json_data['tcp'][i]['host'] = gethostname(target)
                            
                with open(testpath + '\\splitter\\outputs.json', 'w') as f:
                    f.write(json.dumps(json_data))
                   
            connectRemoteShare(ip, username, password)
            shutil.copytree(testpath, "\\\\"+gethostname(ip)+"\\C$\\test")
                
            
def connectRemoteShare(hostIP, username, password):
    cmd = r"net use \\" + hostIP + "c$ /user:" + username + " " + password
    os.system(cmd)
    
def gethostname(hostIP):
    return socket.gethostbyaddr(hostIP)[0]
    
    
    
            
    
    

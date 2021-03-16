import subprocess 
import time
import logging


def startApp(app, testpath):
    with open(testpath + "\\stdout.txt","wb") as out, open(testpath + "\\stderr.txt","wb") as err:
        subprocess.run("node " + testpath + "\\app.js " + testpath + app, shell = True, stdout = out, stderr=err)
        time.sleep(10000)
        

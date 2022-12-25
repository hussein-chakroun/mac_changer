#import the subprocess module
import subprocess

#use the subprocess and the call to input arguments
#type the adapter that you want to change it's mac address
#get you adapter down to edit it
subprocess.call("ipconfig wlan0 down", shell=True)

#enter the connection type then enter the new mac address
subprocess.call("ipconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)

#get your adapter back up 
subprocess.call("ipconfig wlan0 up", shell=True)




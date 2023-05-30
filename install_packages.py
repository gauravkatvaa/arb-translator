import os, platform
 
if(platform.system() == "Windows"):
    os.system("pip install googletrans==4.0.0rc1")
else:
    os.system("pip3 install googletrans==4.0.0rc1")
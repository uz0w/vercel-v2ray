import sys, urllib.request, os
URL_Param = sys.argv[1]
core = urllib.request.urlopen("https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip")
with open("core.zip", "wb") as binaryCode:
  binaryCode.write(core.read())
  binaryCode.close()
setupFileContent = "unzip core.zip v2ray v2ctl geoip.dat geosite.dat\nchmod +x *\nrm core.zip\nnohup ./v2ray -config=" + URL_Param
setupFile = open("setup.sh", "a")
setupFile.write(setupFileContent)
setupFile.close()
os.system("chmod +x setup.sh")
os.system("./setup.sh")


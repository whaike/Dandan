# -*- encoding: utf-8 -*-
import json
import time
import os


def savefile(line):
	with open("Tbox_new.log","a") as f:
		f.write(line+os.linesep)

def search(Tbox_data):
	d = {}
#	d["receiveTime"] = Tbox_data["receiveTime"]
	d["receiveTime"]= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Tbox_data.get("receiveTime")))
	d["imei"] = Tbox_data.get("imei")
#	d["timestamp"] = Tbox_data.get("timestamp"]
	d["timestamp"]= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Tbox_data.get("timestamp")))
	d["dxpTripData"] = Tbox_data.get("dxpTripData")
	d["dxpTripData"]["startTime"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Tbox_data.get("dxpTripData")["startTime"]))
	d["dxpTripData"]["endTime"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Tbox_data.get("dxpTripData")["endTime"]))
	d["dxpGpsData"] ={}
	d["dxpGpsData"]["gpsTime"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Tbox_data.get("dxpGpsData")["gpsTime"]))
	d["dxpGpsData"]["latitude"] = Tbox_data.get("dxpGpsData")["latitude"]
	d["dxpGpsData"]["longitude"] = Tbox_data.get("dxpGpsData")["longitude"]
	d["dxpGpsData"]["fixType"] = Tbox_data.get("dxpGpsData")["fixType"]
	json.dump(d,open("Tbox_new.log","a"),sort_keys=False,indent =4,separators=(',', ': '),encoding="gbk",ensure_ascii=True)
	savefile("\n")

	# savefile(str(d))


def translate(keyword):
	with open("test.log.2018","r") as f:
#		lines = f.readlines()
		for line in f:
			if "adas_dxpfullprotodata:" in line and keyword in line :
				data = line.split("adas_dxpfullprotodata:" )[1]
				Tbox_data = json.loads(data)
				search(Tbox_data)
translate("865473038819143F")
# receiveTime 
# imei 
# dxpGpsData
# 	gpsTime 
# 	latitude 
# 	longitude 
# 	fixType 
# timestamp 
# dxpTripData
# 	startTime 
# 	endTime 

# timestamp = 1462451334

# #转换成localtime
# time_local = time.localtime(timestamp)
# #转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)










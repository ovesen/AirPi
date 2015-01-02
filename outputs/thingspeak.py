import output
import requests
import json

class Thingspeak(output.Output):
	requiredData = ["ApiKey"]
	optionalData = []
	def __init__(self,data):
		self.ApiKey=data["ApiKey"]
	def outputData(self,dataPoints):
		query_str = "&field1=" + str(dataPoints[0]["value"])
		query_str += "&field2=" + str(dataPoints[1]["value"])
		query_str += "&field3=" + str(dataPoints[2]["value"])
		query_str += "&field4=" + str(dataPoints[3]["value"])
		query_str += "&field5=" + str(dataPoints[4]["value"])
		query_str += "&field6=" + str(dataPoints[5]["value"])
		query_str += "&field7=" + str(dataPoints[6]["value"])
		#for i in dataPoints:
		#	query_str = query_str + "&" + i["name"].lower() + "=" + str(i["value"])
			
		url = "https://api.thingspeak.com/update?api_key=" + self.ApiKey + query_str
		#print "Thingspeak url: " + url
		try:
			z = requests.post(url,headers={})
			if not z.text.isdecimal(): 
				print "Thingspeak Error: " + z.text
				return False
		except Exception:
			print "Exception, by url: " + url
			return False
		return True

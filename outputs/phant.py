import output
import requests
import json

class Phant(output.Output):
	requiredData = ["PublicKey","PrivateKey"]
	optionalData = []
	def __init__(self,data):
		self.PublicKey=data["PublicKey"]
		self.PrivateKey=data["PrivateKey"]
	def outputData(self,dataPoints):
		arr = []
		query_str = ""
		for i in dataPoints:
			#print "Datapoint: " + i["name"] + "=" + str(i["value"])
			query_str = query_str + "&" + i["name"].lower() + "=" + str(i["value"])
			#arr.append({"id":i["name"],"current_value":i["value"]})
		#a = json.dumps({"version":"1.0.0","datastreams":arr})
		url = "https://data.sparkfun.com/input/" + self.PublicKey + "?private_key=" + self.PrivateKey + query_str
		try:
			z = requests.post(url,headers={})
			if not "1 success" in z.text: 
				print "Phant Error: " + z.text
				return False
		except Exception:
			print "Exception, by url: " + url
			return False
		return True

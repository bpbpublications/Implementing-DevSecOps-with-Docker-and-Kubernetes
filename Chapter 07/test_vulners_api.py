import vulners
vulners_api = vulners.Vulners(api_key="API_KEY")
Shellshock = vulners_api.search("Shellshock", limit=10)
for i, val in enumerate(Shellshock):
	for key,value in val.items():
		print(key,":",value)
	

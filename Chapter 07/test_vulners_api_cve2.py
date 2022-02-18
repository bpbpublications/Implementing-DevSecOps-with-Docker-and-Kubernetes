import vulners
vulners_api = vulners.Vulners(api_key="API_KEY")
references = vulners_api.references("CVE-2016-6515")
for key,value in references.items():
	for key,val in enumerate(value):
		for key,value in val.items():
			print(key,":",value)

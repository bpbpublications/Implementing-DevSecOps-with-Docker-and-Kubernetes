import vulners
vulners_api = vulners.Vulners(api_key="API_KEY")
CVE_2016_6515 = vulners_api.document("CVE-2016-6515")
print(type(CVE_2016_6515))
for key,value in CVE_2016_6515.items():
	print(key,":",value)

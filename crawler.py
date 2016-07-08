import urllib,re,time


with open('log.txt', 'w') as fobj:
	html = fobj.read

for line in open('usernames.txt'):
	address = str.rstrip("https://localhost:8080/people/" + str(line)) + "/activity"
	print address
	response = urllib.urlopen(address)
	html = response.read()
	output = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",html)
	output.remove('support@localhost.com')
	if output <> []:
		print output
		out_str = ",".join(output)
		with open("log.txt", "a") as outp:
			outp.write(out_str + ",")
	time.sleep(1)
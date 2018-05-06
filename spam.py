import mechanize
import random

wordlist = ["answer 1","answer 2","answer 3"]
url = ""

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open(url)
br.form = list(br.forms())[0]

i=0
for control in br.form.controls:
   if control.type == "text":
      control.value = ''.join(wordlist[i])
      i+=1
br.submit()

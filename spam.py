import mechanize
import random
import sys

wordlist = []
go=True

def help():
   print ("Usage: python spam.py [OPTION]... [URL]\nSpam Web Form with Custom or Random Input.\n\n"
   "   -l num       sends num amount of loops.\n"
   "   -i           sends form submits on infinite loop. Ctrl+C to quit.\n"
   "   -w file      uses wordlist file for textbox submissions."
   "\n"
   )

if '--help' in sys.argv:
   help()

if len(sys.argv) < 2:
   help()
   go=False
else:
   url=sys.argv[-1]
   if '-i' in sys.argv and '-l' in sys.argv:
      help()
      go=False
   elif '-l' in sys.argv:
      try:
         loops=int(sys.argv[sys.argv.index('-l')+1])
      except:
         help()
         go=False
   elif '-i' in sys.argv:
      loops='i'
   else:
      loops=1

   if '-w' in sys.argv:
      try:
         with open(sys.argv[sys.argv.index('-w')+1]) as f:
            wordlist = f.readlines()
            wordlist = [n.strip() for n in wordlist]
      except:
         print "File does not exist."


def makeBrowser(url):
   br = mechanize.Browser()
   br.set_handle_robots(False)
   br.set_handle_refresh(False)
   br.addheaders = [('User-agent', 'Firefox')]
   try:
      br.open(url)
      br.form = list(br.forms())[0]
      return [br,True]
   except:
      print "Invalid url or form.\n"
      return [False,False]

def randStr():
   word=""
   chars="abcdefghijklmnopqrstuvwxyz"
   uChars=chars.upper()
   ints=range(0,10)
   for i in range(3):
      word+=chars[random.randrange(len(chars))]
      word+=uChars[random.randrange(len(uChars))]
      word+=str(random.choice(ints))
   return word

def randChoice(control):
   choices=len(control.get_items())
   choice=str(random.choice(control.get_items()))
   return [choice]

ctr=0

while go:
   try:
      if ctr>=loops and loops!="i":
         go=False
         break

      pack = makeBrowser(url)
      if pack[1]:
        br = pack[0]
      else:
         go=False
         break

      i=0
      for control in br.form.controls:

         if control.type == "text" or control.type == "textarea":
            if i>(len(wordlist)-1):
               wordlist.append(randStr())
            control.value = ''.join(wordlist[i])
            i+=1
         if control.type == "radio" or control.type == "select":
            control.value=randChoice(control)

      br.submit()
      print ctr+1,"sent."
   except:
      print "Ambiguous HTTP Error Occured.\n"
   ctr+=1

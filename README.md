# Surveymonkey-Form-Spammer
Python script made with intention to spam surveymonkey forms. May work on other forms as well.
# Setup
On Windows: python.exe -m pip install mechanize
On Linux: python -m pip install mechanize

# Usage
Usage: python spam.py [OPTION]... [URL]
Spam Web Form with Custom or Random Input.

   -l num       sends num amount of loops.
   -i           sends form submits on infinite loop. Ctrl+C to quit.
   -w file      uses wordlist file for textbox submissions.

examples:
   "python spam.py url" - will randomly fill in the form one time.
   "python -l 2 spam.py url" - will randomly fill in the form two times.
   "python -i spam.py url" - will randomly fill in the form until the user quits the program.
   "python -w wordlist.txt spam.py url" - will fill in the form one time, and where there is a text box, it will enter the text in order.
   "python -l 2 -w wordlist.txt spam.py url" - fills in form with wordlist twice.
   "python -i -w wordlist.txt spam.py url" - fills in form with wordlist until user exits.
   

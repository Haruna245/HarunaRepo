Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import webbrowser
>>> web_add = ["www.google.com","www.amazon.com"]
>>> #you can paste the  address in the web_add list
>>> #use a for loop to automate opening of the links
>>> for i in web_add:
	webbrowser.open(i)

	
True
True
>>> 
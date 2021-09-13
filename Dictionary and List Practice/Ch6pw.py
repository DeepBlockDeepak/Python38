#! python3
# ch6pw.py - program will allow user to copy passwords from a dictionary to the clipboard 
#code can be ran from any directory in the command line/PowerShell

PASSWORDS= {
	"email": 'F879988jkjkslein,dkFsLoO',
	"blog": "vVmei9eu8!(Lkkk",
	"luggage": '12345'
}



import sys, pyperclip

print ("\n")

if len(sys.argv) < 2:
	print(
		"Usage: python ch6pw.py [account] - copy account password\n"
		)
	sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print ("Password for " + account+ " copied to clipboard. \n")
else:
	print ("There is no account named " + account)

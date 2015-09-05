#PASSHWORD
I'm really bad at remembering passwords and even worse at making them up. I didn't want to pay for a password manager, and I thought it would be more fun to make this little python thing to help me out with that than to research the open source ones that exist. 

To be clear, it doesn't use SSH as authentication, I called it that because I made it to be hosted on a server that I can SSH into from my phone so I can access my passwords anywhere.

Also this isn't great code or anything, I wrote it in like 2 hours while watching Truman Show. 

##TODO
1. Stop using plain text
2. Make queries less strict
3. Save all sites as lower case, check for lower case only in get query
4. Make local updates to db push to the server
5. Use a config file with default username, database name/path, idk some other config type stuff. 
6. Better constraints for arguments
7. Write a better install/setup script
8. Add update option

##USAGE
```
	-c	create, no argument
	-g	get password, argument should be sitename
	-u	username (flag is optional, argument is not if flag is included)
	-p	password (flag is optional, argument is not if flag is included)
	-r	rules for password creation delimited by comma, ie <8, 12, CLS> for a password between 8 and 12 characters containing capital, lower case, and special character
		(C = capital, L = lower case, D = digit, S = special character)
```

##EXAMPLES
Generate a new password for 'themoon.com' for your username 'steve' that is between 1 and 99 characters and contains lower case letters, digits, and special characters but no capital letters:
```
	$ passhword -u steve -r "1, 99, DSL" "themoon.com"
```

Add an already existing password that you don't want to change that uses your default username(probably smart to set as your email address) for the site dank.services:
```
	$ passhword -p br0w$3d@nKm3m#s dank.services
```

Get your password for Guild Wars. Just do it. :
```
	$ passhword -g "guild wars"
```

Delete your password for linkedin bc you're not a pleb:
```
	$ passhword -d linkedin
```

##SETUP
If you want to do something more permanent than this, go for it, this is good enough for me. 
```	
	$ git clone
	$ chmod 700 app.py
	$ chmod 700 init.sh
	$ python setup.py
	$ ./init.sh #this is optional, see the instructions in the init.sh file itself for an example
	$ vim ~/.bashrc and add alias passhword='python /path/to/passhword.py'
	$ source ~/.bashrc
```	
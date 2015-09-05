#! /usr/bin/python
import sys
import getopt
import random
import sqlite3
DEFAULT_USER_NAME = 'user'
CONN = sqlite3.connect('pw.db')
CURSOR = CONN.cursor()

def get_capital():
	return chr(random.randint(65, 90))

def get_lower():
	return chr(random.randint(97, 122))

def get_num():
	return chr(random.randint(48, 57))

def get_special_char():
	return chr(random.choice([64, 37, 43, 35, 33, 36]))

POSSIBLE_CHAR_FUNCTIONS = [get_capital, get_lower, get_num, get_special_char]

def delete_password(site):
	CURSOR.execute('DELETE FROM plain_passwords WHERE site=?', (site,))
	CONN.commit()
	return

def get_password(site):
	CURSOR.execute('SELECT * FROM plain_passwords WHERE site=?', (site,))
	return CURSOR.fetchone()

def generate_password(rule_string):

	rules = rule_string.split(',')
	print rules
	min_length = int(rules[0].strip())
	max_length = int(rules[1].strip())
	requirements = rules[2].strip()

	character_functions = []
	if 'C' in requirements or 'c' in requirements:
		character_functions.append(POSSIBLE_CHAR_FUNCTIONS[0])
	if 'L' in requirements or 'l' in requirements:
		character_functions.append(POSSIBLE_CHAR_FUNCTIONS[1])
	if 'D' in requirements or 'd' in requirements:
		character_functions.append(POSSIBLE_CHAR_FUNCTIONS[2])
	if 'S' in requirements or 's' in requirements:
		character_functions.append(POSSIBLE_CHAR_FUNCTIONS[3])

	new_password = ''
	for x in range(0, random.randint(min_length, max_length)):
		choice_function = random.choice(character_functions)
		new_password += choice_function()
	print new_password
	return new_password


def save_db_entry(entry):
	try:
		CURSOR.execute('''INSERT INTO plain_passwords VALUES (?, ?, ?)''', entry)
		CONN.commit()
	except Exception as e:
		print e
		return

def usage():
	print '''Usage options:\n
			-g\tget password, argument should be sitename
			-c\tcreate, no argument
			-u\tusername (flag is optional, argument is not if flag is included)
			-p\tpassword (flag is optional, argument is not if flag is included)
			-r\trules for password creation delimited by comma, ie <8, 12, CLS> for a password between 8 and 12 characters containing capital, lower case, and special character
		'''
def main(argv):
	if len(argv) == 0:
		usage()
		CONN.close()
		sys.exit(2)

	try:
		opts, args = getopt.getopt(argv, 'd:g:u:p:r:', ['delete=','get=', 'username=', 'password=', 'rules='])
	except getopt.GetoptError:
		print 'that\'s not how you do it'
		usage()
		CONN.close()
		sys.exit(2)
	except Exception as e:
		print e
		CONN.close()
		sys.exit(2)
	site = argv[-1]

	username = None
	password = None
	rules = None

	for opt, arg in opts:
		if opt in ('-d', '--delete'):#case 1 : delete a password entry
			print arg
			if get_password(arg):
				delete_password(arg)
				print "\t%s has been deleted" % arg
				sys.exit()
			else:
				print "\tNo record found for %s" % arg
				sys.exit()
		elif opt in ('-g', '--get'):#case 2 : get a password entry
			if get_password(arg):
				site, username, password = get_password(arg)
				print "\t%s, %s, %s" % (site, username, password)
				sys.exit()
			else:
				print '\tNo record found for %s' % arg
				sys.exit()
		elif get_password(site):#case 3 : trying to set a password when one already exists in db
			site, username, password = get_password(site)
			print "You don't have to add that, the info is:\n\t%s, %s, %s" % (site, username, password)
			sys.exit()
		else:#case 4: adding a password to the db
			if opt in ('-u', '--username'):
				username = arg
			elif opt in ('-p', '--password'):
				password = arg
			elif opt in ('-r', '--rules'):
				rules = arg
			else:
				print opt, arg

	if not username:
		username = DEFAULT_USER_NAME
	if rules and not password:
		password = generate_password(rules)

	entry = (site, username, password)
	save_db_entry(entry)
	print "\tSaved ", entry
	return
	
	CONN.close()
	sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])

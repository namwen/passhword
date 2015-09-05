#!/bin/bash

#just make an array of whatever existing passwords/usernames you want to populate the db with as arg strings for passhword.py script
#each entry should look something like this:
#	'-p C00lp4ssBr0 -u ranchlovr420 pornhub'
#	or
#	'-r "8, 12, CDLS" somedumbsite.reviews'

array=('-p C00lp4ssBr0 -u ranchlovr420 pornhub' '-r "8, 12, CDLS" somedumbsite.reviews')

for i in "${array[@]}"; do
	python passhword.py $i
done
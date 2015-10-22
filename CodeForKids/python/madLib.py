print ("\nWelcome to madlib\n")
print ("You will be asked to contribute some words to this madlib story")


wordlist = []


words = ('city', 'item of clothing', 'item of clothing', 'day of the week', 'type of action', 'body part', 'country' )


for word in words:
        i = input('Please input a ' + word + ' ?')
        wordlist.append(i)        








print ("""
Just a mile outside the city limits of """ + wordlist[0] + """ , a man in dirty """ + wordlist[1] + """
and a soiled gray """ + wordlist[2] + """ stood above Interstate 40 on the Route 81 overpass.
It was an early """ + wordlist[3] + """ morning, the sun just becoming visible in the East, and
he """ + wordlist[4] + """ed his hands together in an attempt to alleviate the chill in his """ + wordlist[5] + """.
Eighteen wheelers were starting to fly by in both directions. Trucks headed east
went on into """ + wordlist[0] + """, from """ + wordlist[6] + """ who knows. They could meet up with I-35
and travel south to Dallas or Houston. North to Kansas City, Omaha or maybe all
the way to the Twin Cities. Possibly keep driving east over to Memphis or
Nashville. Might take I-44 and go straight on to St. Louis. Be there by mid-
afternoon.""")

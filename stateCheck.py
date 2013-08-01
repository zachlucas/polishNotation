print "<<<<<<<<<<<Welcome to the state letter checker!>>>>>>>>>>>" 
print "Enter a word, and I will give you the states that don't share any letters with that word"
checker=raw_input("What word you want to check against? (lowercase only please)")

states = ["Alabama",
"Alaska",
"American Samoa",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"District of Columbia",
"Florida",
"Georgia",
"Guam",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Northern Marianas Islands",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Puerto Rico",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Virgin Islands",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming",
]


                
for letter in checker:
    for state in states:
        for stateLetter in state:
            if (stateLetter.lower() == letter):
                #print "MATCH DAWG"
                #print state
                #print stateLetter
                #states.remove(state)
                states = [x for x in states if x != state]
                break

print states






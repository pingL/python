points=0
qs=0
nrc=["Armenia", "Isreal", "Palestine", "Abkhazia", "Kosovo", "Nagorno-Karabakh", "Northern Cyprus", "Somaliland", "South Ossetia", "Transnistria"]
ac=["Afghanistan","Albania","Algeria","Andorra","Antigua and Barbuda", "Antigua","Argentina","Australia","Austria","Azerbaijan"]   
bc=["Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina", "Burundi", "Burma"]
cc=["Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Rep", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Dem Rep Congo", "Democratic Rep Congo", "Democratic Republic Congo", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Rep", "Czech Republic"]
dc=["Denmark", "Djibouti", "Dominica", "Dominican Rep", "Dominican Republic"]
ec=["East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia"]
fc=["Fiji", "Finland", "France"]
gc=["Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana"]

hc=["Haiti", "Honduras", "Hungary"]
ic=["Iceland", "India", "Indonesia", "Iran", "Irag", "Ireland", "Rep of Ireland", "Rep Ireland", "Ireland Rep", "Republic of Ireland", "Israel", "Italy", "Ivory Coast", "Cote d'Ivoire"]
jc=["Jamaica", "Japan", "Jordan"]
kc=["Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan"]
lc=["Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania","Luxembourg"]
mc=["Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar"]
nc=["Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway"]
oc=["Oman"]
pc=["Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal"]
qc=["Qatar"]
rc=["Romania", "Russia", "Rwanda"]
sc=["St Kitts and Nevis", "St Kitts & Nevis", "St Kitts", "St Nevis", "St Lucia", "St Vincent and the Grenadines", "Senegal" "St Vincent & the Grenadines", "St Vincent", "Samoa", "San Marino", "Sao Tome and Principe", "Sao Tome & Principe", "Sao Tome", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "South Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria"]
tc=["Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Trinidad & Tobago", "Trinidad", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu"]
uc=["Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan"]
vc=["Vanuatu", "Vatican City", "Venezuela", "Vietnam"]
wc=[]
xc=[]
yc=["Yemen"]
zc=["Zambia", "Zimbabwe"]



print("Countries in Alphabet")
print("You will be asked a name of one country for every letter in the alphabet. Answer by typing the name of the country; use capitals at the start and spell it correctly or you will not get the points")
print("You will get 5 points for getting it right, 3 for getting a country with disputed sovereignty and 2 points will be deducted for a worng answer.") 

ans1=input("Enter a country's name beginning with A: ")
if ans1 in ac:
    print("Correct; 5 points")
    points=points+5
elif ans1 in nrc:
    print("Correct, however the sovereignty of ", ans1, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)


ans2=input("Enter a country's name beginning with B: ")
if ans2 in bc:
    print("Correct; 5 points")
    points=points+5
elif ans2 in nrc:
    print("Correct, however the sovereignty of ", ans2, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans3=input("Enter a country's name beginning with C: ")
if ans3 in cc:
    print("Correct; 5 points")
    points=points+5
elif ans3 in nrc:
    print("Correct, however the sovereignty of ", ans3, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans4=input("Enter a country's name beginning with D: ")
if ans4 in dc:
    print("Correct; 5 points")
    points=points+5
elif ans4 in nrc:
    print("Correct, however the sovereignty of ", ans4, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans5=input("Enter a country's name beginning with E: ")
if ans5 in ec:
    print("Correct; 5 points")
    points=points+5
elif ans5 in nrc:
    print("Correct, however the sovereignty of ", ans5, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans6=input("Enter a country's name beginning with F: ")
if ans6 in fc:
    print("Correct; 5 points")
    points=points+5
elif ans6 in nrc:
    print("Correct, however the sovereignty of ", ans6, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans7=input("Enter a country's name beginning with G: ")
if ans7 in gc:
    print("Correct; 5 points")
    points=points+5
elif ans7 in nrc:
    print("Correct, however the sovereignty of ", ans7, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans8=input("Enter a country's name beginning with H: ")
if ans8 in hc:
    print("Correct; 5 points")
    points=points+5
elif ans8 in nrc:
    print("Correct, however the sovereignty of ", ans8, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong; -2 points")
    points=points-2
print("Your score is ", points)

ans9=input("Enter a country's name beginning with I: ")
if ans9 in ic:
    print("Correct; 5 points")
    points=points+5
elif ans9 in nrc:
    print("Correct, however the sovereignty of ", ans9, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans10=input("Enter a country's name beginning with J: ")
if ans10 in jc:
    print("Correct; 5 points")
    points=points+5
elif ans10 in nrc:
    print("Correct, however the sovereignty of ", ans10, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans11=input("Enter a country's name beginning with K: ")
if ans11 in kc:
    print("Correct; 5 points")
    points=points+5
elif ans11 in nrc:
    print("Correct, however the sovereignty of ", ans11, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans12=input("Enter a country's name beginning with L: ")
if ans12 in lc:
    print("Correct; 5 points")
    points=points+5
elif ans12 in nrc:
    print("Correct, however the sovereignty of ", ans12, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans13=input("Enter a country's name beginning with M: ")
if ans13 in mc:
    print("Correct; 5 points")
    points=points+5
elif ans13 in nrc:
    print("Correct, however the sovereignty of ", ans13, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans14=input("Enter a country's name beginning with N: ")
if ans14 in nc:
    print("Correct; 5 points")
    points=points+5
elif ans14 in nrc:
    print("Correct, however the sovereignty of ", ans14, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans15=input("Enter a country's name beginning with O: ")
if ans15 in oc:
    print("Correct; 5 points")
    points=points+5
elif ans15 in nrc:
    print("Correct, however the sovereignty of ", ans15, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans16=input("Enter a country's name beginning with P: ")
if ans16 in pc:
    print("Correct; 5 points")
    points=points+5
elif ans16 in nrc:
    print("Correct, however the sovereignty of ", ans16, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans17=input("Enter a country's name beginning with Q: ")
if ans17 in qc:
    print("Correct; 5 points")
    points=points+5
elif ans17 in nrc:
    print("Correct, however the sovereignty of ", ans17, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans18=input("Enter a country's name beginning with R: ")
if ans18 in rc:
    print("Correct; 5 points")
    points=points+5
elif ans18 in nrc:
    print("Correct, however the sovereignty of ", ans18, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans19=input("Enter a country's name beginning with S: ")
if ans6 in sc:
    print("Correct; 5 points")
    points=points+5
elif ans19 in nrc:
    print("Correct, however the sovereignty of ", ans19, " is disputed; 3 points")
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans20=input("Enter a country's name beginning with T: ")
if ans20 in fc:
    print("Correct; 5 points")
    points=points+5
elif ans20 in nrc:
    print("Correct, however the sovereignty of ", ans20, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans21=input("Enter a country's name beginning with U: ")
if ans21 in uc:
    print("Correct; 5 points")
    points=points+5
elif ans21 in nrc:
    print("Correct, however the sovereignty of ", ans21, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)

ans22=input("Enter a country's name beginning with V: ")
if ans22 in vc:
    print("Correct; 5 points")
    points=points+5
elif ans22 in nrc:
    print("Correct, however the sovereignty of ", ans22, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)


ans23=input("Enter a country's name beginning with W: ")
if ans23=="None" or "No countries":
    print(" There are no offically sovereign countries whose names start with W, So if you put no countries then you are correct.; 5 points")
    points=points+5
elif ans23 in nrc:
    print("Correct, however the sovereignty of ", ans24, " is disputed; 3 points")
    points=points+3
else:
    print("If you put no countries, you are correct. There are offically sovereign countries whose names start with W")
    points=points+0
print("Your score is ", points)


ans24=input("Enter a country's name beginning with X: ")
if ans24=="None" or "No countries":
    print(" There are no offically sovereign countries whose names start with X, So if you put no countries then you are correct.; 5 points")
    points=points+5
elif ans24 in nrc:
    print("Correct, however the sovereignty of ", ans24, " is disputed; 3 points")
    points=points+3
else:
    print("If you put no countries, you are correct. There are offically sovereign countries whose names start with X")
    points=points+0
print("Your score is ", points)


ans25=input("Enter a country's name beginning with Y: ")
if ans21 in yc:
    print("Correct; 5 points")
    points=points+5
elif ans25 in nrc:
    print("Correct, however the sovereignty of ", ans25, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2
print("Your score is ", points)


ans26=input("Enter a country's name beginning with Z: ")
if ans26 in zc:
    print("Correct; 5 points")
    points=points+5
elif ans26 in nrc:
    print("Correct, however the sovereignty of ", ans26, " is disputed; 3 points")
    points=points+3
else:
    print("Wrong;-2 points")
    points=points-2


print("Great work, you have finished the Alphabetical Countries, your final score is ", points, " out of 130!")

if points==130:
    print(":-) Great job, you've got full marks - GRADE A*")
elif points<130 and points>=80:
    print("Well done, you have got GRADE A")
elif points<80 and points>=50:
    print("Nice work, but there is still room for improvement - GRADE B")
elif points<50 and points>=30:
    print("Good effort, you have achieved the average GRADE C")
elif points<30 and points>=15:
    print("Try and do better next time - GRADE D")
elif points<15 and points>0:
    print("Disappointing, you should be able to do better -GRADE E")
elif points==0:
    print("You got them all wrong; go learn some geography! - GRADE F FAIL")
else:
    print("Thanks for playing!")

print("Thanks for playing, I hope you have enjoyed it!")




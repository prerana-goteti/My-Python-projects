student_record = [{
    'Name' : "Prerana",
    'Student Id' : "1",
    'Grade' : "8",
    'Library Books' : "New Moon",
    'Food Preferences' : "Pizza and Ice Cream",
    'School Bus' : "#02"
},
{
    'Name' : "Akhil",
    'Student Id' : "2",
    'Grade' : "11",
    'Library Books' : "Zodiac Academy",
    'Food Preferences' : "Tacos and Popcorn",
    'School Bus' : "#19"
},
{
    'Name' : "Sairam",
    'Student Id' : "3",
    'Grade' : "7",
    'Library Books' : "Keeper of the Lost Cities",
    'Food Preferences' : "Biriyani and Nachos",
    'School Bus' : "#05"
}
]

stid = input("enter the student id: ")

res = None
for st_rec in student_record:
    if  st_rec['Student Id']  == stid:
        res= st_rec

print((res))

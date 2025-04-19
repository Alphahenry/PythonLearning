#A list inside a dictionary


cars_owned = {
    
    "lydia": "Atenza",
    "Alpha": ["Land cruiser", "Land rover", "Range rover"],
    "sister": "v8",
    "gidi" : "GTR"
    
}


for key, value in cars_owned.items():
    print(f"{key.title()} owns a {value}")
    
    
#dictionary within a dictionary

programmers = {
 
      "investor1" : {
        "name": "Tache",
        "Role": "Hacker",
        "language":"C",
    },
      
        "investor2" : {
        "name": "Alpha",
        "Role": "Network Engineer",
        "language":"Java",
    },

      "investor3" : {
     "name": "Hussein",
    "Role": "Pentester",
    "language":"Python",
    }




}



for programmer, info in programmers.items():
    print( f"psition of programmer is {programmer}")
    print(f"Name =  {info["name"]}")
    print(f"role is {info["Role"]} and proficient language is {info["language"]}")
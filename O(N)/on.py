# def find_name(names, target):
#     for name in names:    
#         if name == target:
#             return f"{target}  "
#     return f"{target}    "


 
# students = ["Sajib", "Rahim", "Karim", "Jamil"]

# print(find_name(students, "Rahim"))    
# print(find_name(students, "Hasan"))    
def find_name(names,target):
    for name in names:
        if name == target:
            return f"{target}  find Name"
    else:
        return f"{target} Did Not find Name"
students = ["Sajib", "Rahim", "Karim","Jamil"]
print(find_name(students,"Rahim"))
print (find_name(students,"Munmun"))
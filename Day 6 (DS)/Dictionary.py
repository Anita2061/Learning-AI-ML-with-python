student={
    "names":{
        "name1":"misti",
        "name2": "riya",
        "name3": "sunita",
        "name4":"siya"
    },
    "marks":{
        "python":90,
        "maths":56,
        "dsa":67,
        "os":56
    }
    

}
print(student["names"])
print(student["marks"])




student={

    "student1":{
      "name1":"misti",
      "python":90,"maths":56,"dsa":67,"os":56,
   },
   "student2":{
       "name2":"astha",
       "python":93,"maths":58,"dsa":60,"os":54,
   }
}
print(student.get("student1").get("name1"))  #nesting in dictionary



college={
      "bitm":{
    "s001":{
      "name1":"misti",
      
      "python":90,"maths":56,"dsa":67,"os":56,
   },
   "s002":{
       "name2":"astha",
       "python":93,"maths":58,"dsa":60,"os":54,
   }
      }   
}

print(college.get("student1").get("name1"))


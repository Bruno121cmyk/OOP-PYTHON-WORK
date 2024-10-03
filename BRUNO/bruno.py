class registration:
    def __init__(self,name,reg_no,course,year):
        self.name=name
        self.reg_no=reg_no
        self.course=course
        self.year=year

    def __str__(self):
        return(f"name:{self.name} reg_no:{self.reg_no} course:{self.course} year:{self.year}")

student1=registration("Nasasira Bruno","S23B13/044","BSIT","2023")
print(student1)    

student1=registration("Aine Blair","S23B14/054","BSIT","2022")
print(student1) 

student1=registration("Natamba Jesca","S23B13/003","BSCS","2021")
print(student1)    

student1=registration("Tayebwa Thomas","S23B13/204","BSCS","2020")
print(student1)    
       
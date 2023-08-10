#Malik Stockton Cis 129
#This program will give patient info and procedure infoprmation
#creating a class named patient for their information
class patient:
    def __init__(self,fName,mName,lName,City,State,zipCode,pNumber,ecName,ecpNumber):
        #defining self
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.City = City
        self.State = State
        self.zipCode = zipCode
        self.pNumber = pNumber
        self.ecName = ecName
        self.ecpNumber = ecpNumber
#Creating accesors and mutator method for each field
    def getFirstName(self):
        return self.fName 
    def getMiddleName(self):
        return self.mName 
    def getLastName(self):
        return self.lName 
    def getCity(self):
        return self.City
    def getState(self):
        return self.State
    def getzipCode(self):
        return self.zipCode
    def getpNumber(self):
        return self.pNumber 
    def getecName(self):
        return self.ecName 
    def getecpNumber(self):
        return self.ecpNumber 
    #creating insstance for patient class
patient = patient(fName = "John", mName = "Micheal", lName = "Smith", City = "Anytown", State = "CA",zipCode = 23098,pNumber = '123-456-7890', ecName = 'Jane Doe',ecpNumber = '123-456-7891')
     
 # class that will get procedure information
class procedure:
    def __init__(self,pCost,nProcedure,dPractioner,nPractioner):
        self.nProcedure = nProcedure
        self.dPractioner = dPractioner
        self.nPractioner = nPractioner
        self.pCost = pCost
    #defining mutators and acessors for eah field
    def getnProcedure(self):
        return self.nProcedure
    def getdPractioner(self):
        return self.dPractioner
    def getnPractioner(self):
        return self.nPractioner 
    def getpCost(self):
        return self.pCost
    #creating an instacne of the procedure class
procedure1 = procedure(nProcedure = "physical exam", dPractioner = "2021-03-08",nPractioner= "Dr. Smith", pCost = 100.00)
procedure2 = procedure(nProcedure = "prostate exam", dPractioner = "2022-04-08", nPractioner= "Dr. Steven", pCost= 300.00)
procedure3 = procedure(nProcedure = "prostate exam", dPractioner = "2023-09-11", nPractioner= "Dr. Cantu", pCost= 800.00)
#display all the information
print("First Name:",patient.getFirstName())
print("Middle Name:",patient.getMiddleName())
print("Last Name:",patient.getLastName())
print("City:",patient.getCity())
print("State:",patient.getState())
print("Zipcode:",patient.getzipCode())
print("Patient Phone number:",patient.getpNumber())
print("Patient Emergency Contact Name:",patient.getecName())
print("Patient emergency Contact Phone Number:",patient.getecpNumber())
#procedure number #1
print("Procedure # 1")
print("Procedure Performed:",procedure1.getnProcedure())
print("Date Of The Procedure:",procedure1.getdPractioner())
print("Name Of The Doctor:",procedure1.getnPractioner())
print("Procedure Cost:",procedure1.getpCost())
#procedure number #2
print("Procedure # 2")
print("Procedure Performed:",procedure2.getnProcedure())
print("Date Of The Procedure:",procedure2.getdPractioner())
print("Name Of The Doctor:",procedure2.getnPractioner())
print("Procedure Cost:",procedure2.getpCost())
#procedure number #3
print("Procedure # 3")
print("Procedure Performed:",procedure3.getnProcedure())
print("Date Of The Procedure:",procedure3.getdPractioner())
print("Name Of The Doctor:",procedure3.getnPractioner())
print("Procedure Cost:",procedure3.getpCost())

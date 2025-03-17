class Patient:
    def __init__(self, id, name, age, bloodgroup, next=None, prev=None):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        self.next = next
        self.prev = prev

class WRM:
    def __init__(self):
        self.d_head = Patient(None, None, None, None, None, None)
        self.d_head.next = self.d_head
        self.d_head.prev = self.d_head

    def registerPatient(self, id, name, age, bloodgroup):
        n_patient = Patient(id, name, age, bloodgroup, self.d_head, self.d_head.prev)
        self.d_head.prev.next = n_patient
        self.d_head.prev = n_patient
        print("Success")

    def servePatient(self):
        if self.d_head.next == self.d_head:
            print("No patients to serve")
            return
        patient_to_serve = self.d_head.next
        self.d_head.next = patient_to_serve.next
        patient_to_serve.next.prev = self.d_head
        print(f"Serving Patient: {patient_to_serve.name}")

    def showAllPatient(self):
        if self.d_head.next == self.d_head:
            print("No patients waiting")
            return
        current = self.d_head.next
        while current != self.d_head:
            print(f"Patient ID: {current.id}, Name: {current.name}, Age: {current.age}, Blood Group: {current.bloodgroup}")
            current = current.next

    def canDoctorGoHome(self):
        if self.d_head.next == self.d_head:
            print("Yes")
            return True
        else:
            print("No")
            return False

    def cancelAll(self):
        self.d_head.next = self.d_head
        self.d_head.prev = self.d_head
        print("Success")

    def ReverseTheLine(self):
        if self.d_head.next == self.d_head:
            print("No patients to reverse")
            return
        current = self.d_head
        while True:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
            if current == self.d_head:
                break
        print("Success")

# Tester Code
print("Welcome to Waiting Room Management System")
wrm = WRM()

while True:
    print("\nOptions:")
    print("1. Register Patient")
    print("2. Serve Patient")
    print("3. Show All Patients")
    print("4. Can Doctor Go Home?")
    print("5. Cancel All Appointments")
    print("6. Reverse The Line")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        bloodgroup = input("Enter Patient Blood Group: ")
        wrm.registerPatient(id, name, age, bloodgroup)
    elif choice == '2':
        wrm.servePatient()
    elif choice == '3':
        wrm.showAllPatient()
    elif choice == '4':
        wrm.canDoctorGoHome()
    elif choice == '5':
        wrm.cancelAll()
    elif choice == '6':
        wrm.ReverseTheLine()
    elif choice == '7':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
#we didn't create object for calling constractor
# def __init__():


#default constractor:
class employee:
    employee_name = ''
    employee_id = ''

    def __init__(self):
        self.employee_name = 'Arun Prasath'
        self.employee_id = '1111'

        print("it's a constructor")

    def display(self):
        print("Employee Name", self.employee_name)
        print("Employee id", self.employee_id)
        



a=employee()
a.display()


#parametterized constractor
class employee:
    employee_name = ''
    employee_id = ''

    def __init__(self,name,eid):
        self.employee_name = name
        self.employee_id = eid

        print("it's a constructor")

    def display(self):
        print("Employee Name", self.employee_name)
        print("Employee id", self.employee_id)
        
b=employee('Arun prasath','111')
b.display()

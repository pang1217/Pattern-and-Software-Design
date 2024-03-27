class EmployeeVisitor:
    def visitFullTimeEmployee(self, f):
        pass

    def visitPartTimeEmployee(self, p):
        pass
    
    def visitContractEmployee(self, c):
        pass

class ShowEmployeeInfo(EmployeeVisitor):
    def visitFullTimeEmployee(self, f):
        print(f"Full Time Employee --> Name : {f.name} Salary : {f.salary}")

    def visitPartTimeEmployee(self, p):
        print(f"Part Time Employee --> Name : {p.name} Hourly rate : {p.hourlyRate}")
    
    def visitContractEmployee(self, c):
        print(f"Contract Employee --> Name : {c.name} Contract amount : {c.contractAmount}")

class ShowEmployeeBenefit(EmployeeVisitor):
    def visitFullTimeEmployee(self, f):
        print(f"Benefits for full-time employee {f.name}: Health insurance, retirement plan")

    def visitPartTimeEmployee(self, p):
        print(f"Benefits for part-time employee {p.name}: None")

    def visitContractEmployee(self, c):
         print(f"Benefits for contract employee {c.name}: None")

class TaxCalculate(EmployeeVisitor):
    def visitFullTimeEmployee(self, f):
        tax_rate = 0.2 # 20% tax rate for full-time employees
        tax_amount = f.salary * tax_rate
        print(f"Taxes for full-time employee {f.name}: ${tax_amount}")

    def visitPartTimeEmployee(self, p):
        tax_rate = 0.1 # 10% tax rate for part-time employees
        tax_amount = p.hourlyRate * 40 * tax_rate # Assuming 40 hours of work per week
        print(f"Taxes for part-time employee {p.name}: ${tax_amount}")

    def visitContractEmployee(self, c):
        tax_rate = 0.15 # 15% tax rate for contract employees
        tax_amount = c.contractAmount * tax_rate
        print(f"Taxes for contract employee {c.name}: ${tax_amount}")

class Employee :
    def __init__(self, name):
      self.name = name
      
    def accept(self, v):
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.salary = salary
        super().__init__(name)
        
    def accept(self, v):
        v.visitFullTimeEmployee(self)
        
class PartTimeEmployee(Employee):
    def __init__(self, name, hourlyRate):
        self.hourlyRate = hourlyRate
        super().__init__(name)
        
    def accept(self, v):
        v.visitPartTimeEmployee(self)
        
class ContractEmployee(Employee):
    def __init__(self, name, contractAmount):
        self.contractAmount = contractAmount
        super().__init__(name)
        
    def accept(self, v):
        v.visitContractEmployee(self)
        
if __name__ == "__main__":
    emp1 = FullTimeEmployee('Alice', 15000)
    emp2 = PartTimeEmployee('John', 300)
    emp3 = ContractEmployee('Brandon', 25000)
    emps = [emp1, emp2, emp3]
    
    showInfo = ShowEmployeeInfo()
    for emp in emps :
        emp.accept(showInfo)
        
    print()
    showBenefit = ShowEmployeeBenefit()   
    for emp in emps :
        emp.accept(showBenefit)
     
    print()   
    taxCalculate = TaxCalculate()
    for emp in emps :
        emp.accept(taxCalculate)
class TaxCalculator:
    def __init__(self):
        # Defining the tax slabs as a list of tuples
        # Each tuple contains (lower_limit, upper_limit, tax_rate)
        self.tax_slabs = [
            (0, 300000, 0),
            (300001, 400000, 0.10),
            (400001, 650000, 0.15),
            (650001, 1000000,0.20),
            (1000001,1500000, 0.25),
            (1500001, float('inf'), 0.30)
        ]
    def calculate_tax_by_slab(self, taxable_income):
         # Initialize tax to 0
        tax = 0
        for slab in self.tax_slabs:
        # If the taxable income falls within the current slab
            if taxable_income <= slab[1]:
            # Calculate tax for the remaining income in the slab
                tax += (taxable_income - slab[0])* slab[2]
                
                break # Break out of the loop since we found the correct slab
             
             # Otherwise, calculate tax for the entire slab
            tax += (slab [1]- slab[0]* slab[2])
            # Return the calculated tax
            return tax

class Employee:
    def __init__(self, name, income, organization_type, employment_type):
        # Return the calculated tax
        self.name = name
        self.income = income
        self.organization_type = organization_type
        self.employment_type = employment_type
        self.tax_calculator = TaxCalculator()
        self.tax_rate = 0
        self.taxable_income = 0
        self.tax_payable = 0
        self.education_allowance = 0
    
    def calculate_tax(self):
        # Initialize deductions to 0
        deducation = 0

        # Calculate deductions based on employment type and organization type
        if self.employment_type == "Regular":
            deducations += self.income *0.05
        if self.organization_type == "Government" and self.employment_type == "Contract":
            deducation += 2400
        elif self.organization_type != "Government":
            if self.employment_type != "Contract":
                deducations += self.income *0.05
        
    # Add education allowance to deductions
        deducation += self.education_allowance
     # Calculate taxable income by subtracting deductions from income 
        taxable_income = self.income - deducation
    
     # Calculate tax using the calculate_tax_by_slab method   
        self.tax_payable = self.tax_calculator.calculate_tax_by_slab(taxable_income)
        
    # Add an additional 10% tax if taxable income is above 1,000,000
        if taxable_income > 1000000:
            self.tax_payable += self.tax_payable *0.1
    
    # Calculate tax rate and store taxable income
        self.tax_rate= self.tax_payable / taxable_income
        self.taxable_income = taxable_income
    
    def display_tax_details(self):
    # Print employee's tax details
        print(f"Name:{self.name}")
        print(F"Income: Nu. {self.income}")
        print(f"Organization Type: {self.organization_type}")
        print(f"Employment Type:{self.employment_type}")
        print(f"Taxable Income:Nu.{self.taxable_income}")
        print(f"Tax Rate:{self.tax_rate*100:.2f}%")
        print(f"Tax Payable: Nu.{self.tax_payable:.2f}")
   
    def set_education_allowance(self, amount):
         # Setting education allowance for the employee
        self.education_allowance = amount
try:
     # Get employee details from user input
    name = input("Enter employee's name: ")
    income = float(input("Enter employee's income: "))
    organization_type = input("Enter employee's organization type(Government/Private/Corporate):").capitalize()
    employment_type = input("Enter employee's employment type (Regualr/Contract):").capitalize()
   
   # Creating an Employee object with the provided details
    employee = Employee(name,income, organization_type, employment_type)
    employee.set_education_allowance(float(input("Enter education allowance:")))
    
    # Calculating  and displaying the employee's tax details
    employee.calculate_tax()
    employee.display_tax_details()


except ValueError:
     # Handle ValueError exception (e.g., invalid input for income)
    print("Please enter a valid numerical value for income.")
except Exception as e:
    # Handle any other exceptions
    print("An error occurred:", str(e))
   





    

    

          



        

    
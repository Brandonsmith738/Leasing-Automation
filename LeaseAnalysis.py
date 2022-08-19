import xlwings as xw
import TenantData
from TenantData import Tenant
from TenantData import NewTenant
import numpy as np

def createTemplate(PropertyIndex):
    # Assign Space Square Feet
    # Initialize Template with xw
    # wb = xw.Book('Lease_Analysis_Template.xlsx')
    try:
        wb = xw.Book(r'C:\Users\GlocktorSeuss\OneDrive\Desktop\Work\Occidental\CodeCleanup\Lease_Analysis_Template.xlsx')
        sheet = wb.sheets['Analysis']
        data = wb.sheets['Data Grid']
        proposal = wb.sheets['Proposal']
        sheet.range('C7').value = NewTenant.getTenant()
        sheet.range('C10').value = NewTenant.getLeaseTerm()
        sheet.range('C9').value = data.range('F' + str(PropertyIndex + 7)).value
        sheet.range('C5').value = data.range('A' + str(PropertyIndex + 7)).value
        # Test
        # Pull total rent
        NewTenant.setTotalRent(proposal.range('I29').value)
        # Setting the property from drop down list
        NewTenant.setPropertySF(sheet.range('C9').value)
        NewTenant.setProperty(data.range('A' + str(PropertyIndex + 7)).value)
        NewTenant.setTrippleNets(data.range('U' + str(PropertyIndex + 7)).value)

        NewTenant.setLandlordTI(sheet.range('C12').value)
        NewTenant.setSecurityDepost(proposal.range('O18').value)
    except:
        print("Save Error (Excel Update)")
        
    n = float(NewTenant.getLeaseTerm())
    step = 0.5
    possibleValues = np.arange(0, 201)*0.25


    # C43 is negative so we subtract to make it positive
    def calculateFirstMonthTerm(ROI):
        x0 = ((1 / (1 - sheet.range('C15').value)) * (ROI * float(sheet.range('C53').value) * n - sheet.range('C43').value * n)
              - step * (0.5 * (n - 1) * n)) / (n * (1 - (1 / (12 * n * sheet.range('C11').value * (1 - sheet.range('C15').value)))))
        return x0

    differenceArray = np.absolute(possibleValues - calculateFirstMonthTerm(0.15))
    index = differenceArray.argmin()
    NewTenant.setFirstMonthBase(possibleValues[index])
    # Appends from the initial base rent += step_size up to i=n. This pushes to one array in NewTenant
    for i in range(int(n)):
        NewTenant.appendRentSqft(possibleValues[index]+step*i)
        print(NewTenant.getRentBaseElement(i))
    # Push each value from base rent list to Lease Analysis sheet
    for i in range(int(len(NewTenant.getRentBase()))):
        sheet.range('C' + str(i + 20)).value = NewTenant.getRentBaseElement(i)
        # Append the rest of the table to their corresponding lists
        NewTenant.appendMonthlyBase(proposal.range('D' + str(i + 18)).value)
        NewTenant.appendMonthlyImprovement(proposal.range('E' + str(i + 18)).value)
        NewTenant.appendEstAdditionalRent(proposal.range('F' + str(i + 18)).value)
        NewTenant.appendTotalMonthly(proposal.range('G' + str(i + 18)).value)
        NewTenant.appendTotalYearly(proposal.range('I' + str(i + 18)).value)

        wb.save(NewTenant.getTenant() + "/" + NewTenant.getTenant() + 'LA.xlsx')
        wb.close()

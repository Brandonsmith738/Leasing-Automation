import os, sys
from datetime import date


# Pull the current date
today = date.today()
def getTodayMonth():
    return int(today.strftime("%m"))
def getTodayYear():
    return int(today.strftime("%Y"))
def getToday():
    return int(today.strftime("%d"))

# Format the date of writing LOI
todays_date = today.strftime("%B %d, %Y")

# Lease Analysis Variables
class Tenant():
    def __init__(self):
        self._Property = 0
        self._PropertySF = 0
        self._FirstName = 0
        self._Tenant = 0
        self._LeaseTerm = 0
        self._RentAbatement = 0
        self._CommissionRate = 0
        self._AnnualRent = 0
        self._SpaceAddress = 0
        self._SpaceLocation = 0
        self._PossessionDate = 0
        self._CommencementDays = 0
        self._DeltaDate = 0
        self._TrippleNets = 0
        self._TenantWork = ""
        self._LandlordWork = ""
        self._ExtraConstingency = ""
        self._LandlordTI = 0
        self._SecurityDeposit = 0
        self._TenantFinishCheckbox = False
        self._LandlordWorkExist = False

    #     Tenant Rent Table
        self._rent_sqft = []
        self._monthly_base = []
        self._monthly_improvement = []
        self._est_additional_rent = []
        self._total_monthly = []
        self._total_yearly = []
        self._total_rent = 0

    def getRentBase(self):
        return self._rent_sqft

    def setTotalRent(self, x):
        self._total_rent = x
    def getTotalRent(self):
        return self._total_rent

    def getRentBaseElement(self, x):
        return self._rent_sqft[x]
    def getMonthlyBaseElement(self, x):
        return self._monthly_base[x]
    def getMonthlyImprovementElement(self, x):
        return self._monthly_improvement[x]
    def getEstAdditionalRentElement(self, x):
        return self._est_additional_rent[x]
    def getTotalMonthlyElement(self, x):
        return self._total_monthly[x]
    def getTotalYearlyElement(self, x):
        return self._total_yearly[x]
    # Rent Table Append
    def appendRentSqft(self, x):
        self._rent_sqft.append(x)
    def appendMonthlyBase(self, x):
        self._monthly_base.append(x)
    def appendMonthlyImprovement(self, x):
        self._monthly_improvement.append(x)
    def appendEstAdditionalRent(self, x):
        self._est_additional_rent.append(x)
    def appendTotalMonthly(self, x):
        self._total_monthly.append(x)
    def appendTotalYearly(self, x):
        self._total_yearly.append(x)

    def setTenant(self, x):
        self._Tenant = x
    def getTenant(self):
        return self._Tenant
    def setPropertySF(self, x):
        self._PropertySF = x
    def getPropertySF(self):
        return self._PropertySF
    def setFirstName(self, x):
        self._FirstName = x
    def getFirstName(self):
        return self._FirstName
    def setSpaceAddress(self, x):
        self._SpaceAddress = x
    def getSpaceAddress(self):
        return self._SpaceAddress
    def setProperty(self, x):
        self._Property = x
    def getProperty(self):
        return self._Property
    def setLeaseTerm(self, x):
        self._LeaseTerm = x
    def getLeaseTerm(self):
        return self._LeaseTerm
    def setSpaceLocation(self, x):
        self._SpaceLocation = x
    def getSpaceLocation(self):
        return self._SpaceLocation
    def setPossessionDate(self, x):
        self._PossessionDate = x
    def getPossessionDate(self):
        return self._PossessionDate
    def setCommencementDays(self, x):
        self._CommencementDays = x
    def getCommencementDays(self):
        return self._CommencementDays
    def setDeltaDate(self, x):
        self._DeltaDate = x
    def getDeltaDate(self):
        return self._DeltaDate
    def setTrippleNets(self, x):
        self._TrippleNets = x
    def getTrippleNets(self):
        return self._TrippleNets
    def setTenantWork(self, x):
        self._TenantWork = x
    def getTenantWork(self):
        return self._TenantWork
    def setLandlordWork(self, x):
        self._LandlordWork = x
    def getLandlordWork(self):
        return self._LandlordWork
    def setExtraConstingency(self, x):
        self._ExtraConstingency = x
    def getExtraConstingency(self):
        return self._ExtraConstingency
    def setLandlordTI(self, x):
        self._LandlordTI = x
    def getLandlordTI(self):
        return self._LandlordTI
    def getSecurityDeposit(self):
        return self._SecurityDeposit
    def setSecurityDepost(self, x):
        self._SecurityDeposit = x
    def setTenantFinishCheckbox(self, x):
        self._TenantFinishCheckbox = x
    def getTenantFinishCheckbox(self):
        return self._TenantFinishCheckbox
    def setLandlordWorkExist(self, x):
        self._LandlordWorkExist = x
    def getLandlordWorkExist(self):
        return self._LandlordWorkExist
    def setFirstMonthBase(self, x):
        self._FirstMonthBase = x
    def getFirstMonthBase(self):
        return self._FirstMonthBase
    def setSignageExists(self, x):
        self._SignageExists = x
    def getSignageExists(self):
        return self._SignageExists
    def setSignage(self, x):
        self._Signage = x
    def getSignage(self):
        return self._Signage

NewTenant = Tenant()

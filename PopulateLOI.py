import os, sys
import inflect
import LeaseAnalysis
import TenantData
from TenantData import NewTenant
import docx
import docxtpl
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

p = inflect.engine()

def initDirectories():
    try:
        if not os.path.exists(NewTenant.getTenant()):
            os.mkdir(NewTenant.getTenant())
    except:
        print("Invalid Business Name")


def createTemplate():
    template = DocxTemplate('LOI_Template.docx')
    lease_year_col = []
    tenant_finish_list = ['Tenant’s written request for reimbursement of the Construction Allowance.',
                     'Copies of invoices from Tenant’s contractor, showing account paid in full.',
                     'Lien waiver associated with Tenant’s work, from Tenant’s contractor.']
    tenant_finish_col = []
    tenant_finish_exists_title = ""
    tenant_finish_exists = ""
    landlord_work_title = ""

    for i in range(int(NewTenant.getLeaseTerm())):
        lease_year_col.append({
                               'rent_sqft': NewTenant.getRentBaseElement(i),
                               'monthly_base': NewTenant.getMonthlyBaseElement(i),
                               'monthly_improvement': NewTenant.getMonthlyImprovementElement(i),
                               'est_additional_rent': NewTenant.getEstAdditionalRentElement(i),
                               'total_monthly': NewTenant.getTotalMonthlyElement(i),
                               'total_yearly': NewTenant.getTotalYearlyElement(i)})
    # if statement checking if tenant finish exists
    if (NewTenant.getTenantFinishCheckbox()):
        for i in range(3):
            tenant_finish_col.append(tenant_finish_list[i])
        tenant_finish_exists_title = "Tenant Finish:"
        tenant_finish_exists = "Landlord will provide to Tenant, within thirty (30) days after Tenant’s Work is complete, a Construction Allowance of up to " + str(NewTenant.getLandlordTI()) + " payable to Tenant upon receipt of the following:"
    # if statement checking if landlord work exists
    if (NewTenant.getLandlordWorkExist()):
        landlord_work_title = "Landlord's Work:"
    def LA_O18_to_words():
        index = str(NewTenant.getSecurityDeposit()).index('.')
        ToWordsEnding = str(NewTenant.getSecurityDeposit())[index+1:len(str(NewTenant.getSecurityDeposit()))]+'/100'
        LA_O18_to_word = p.number_to_words(NewTenant.getSecurityDeposit()).split("point")[0] + "and " + ToWordsEnding + " Dollars"
        return LA_O18_to_word

    context = {'size': NewTenant.getPropertySF(),
               'tenant': NewTenant.getTenant(),
               'todays_date': TenantData.todays_date,
               'firstname': NewTenant.getFirstName(),
               'space_address': NewTenant.getSpaceAddress(),
               'term_length': NewTenant.getLeaseTerm(),
               'space_location': NewTenant.getSpaceLocation(),
               'lease_year': lease_year_col,
               'rent_total': NewTenant.getTotalRent(),
               'possession_date': NewTenant.getPossessionDate(),
               'commencement_days': NewTenant.getDeltaDate(),
               'commencement_days_word': p.number_to_words(int(NewTenant.getDeltaDate())).capitalize(),
               'term_length_word': p.number_to_words(NewTenant.getLeaseTerm()).capitalize(),
               'nnn_rates': NewTenant.getTrippleNets(),
               'landlord_work': NewTenant.getLandlordWork(),
               'landlord_work_title': landlord_work_title,
               'tenant_work': NewTenant.getTenantWork(),
               'extra_contingency': NewTenant.getExtraConstingency(),
               'LA_C12': NewTenant.getLandlordTI(),
               'LA_O18': NewTenant.getSecurityDeposit(),
               'LA_O18_words': LA_O18_to_words(),
               'tenant_finish_col': tenant_finish_col,
               'tenant_finish_exists_title': tenant_finish_exists_title,
               'tenant_finish_exists': tenant_finish_exists,
               }
    try:
        template.render(context)
        template.save(NewTenant.getTenant() + "/" + NewTenant.getTenant() + "LOI.docx")
    except:
        print("LOI Error")
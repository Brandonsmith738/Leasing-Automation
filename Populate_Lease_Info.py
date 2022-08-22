import os, sys
import inflect
import LeaseAnalysis
import TenantData
from TenantData import NewTenant
import docx
import docxtpl
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# Here we populate everything in the lease info sheet
def createTemplate():
    # Make sure this saves in the proper location
    lease_info_template = DocxTemplate('Lease_Info_Template.docx')
    context = {
        'tenant': NewTenant.getTenant(),
        'org_type': 'needs fill',
        'state_of_business': 'needs fill',
        'notice_address': 'needs fill',
        'billing_address': 'needs fill',
        'guarantor': 'needs fill',
        'guarantor_notice_address': 'needs fill',
        'space_location': NewTenant.getSpaceLocation(),
        'space_address': NewTenant.getSpaceAddress(),
        'leased_premise': 'needs fill',
        'leased_area': 'needs fill',
        'term_length': NewTenant.getLeaseTerm(),
        'possession_date': NewTenant.getPossessionDate(),
        'commencement_days_word': NewTenant.getCommencementDays(),
        'commencement_days': NewTenant.getCommencementDays(),
        'tenant_improvements': 'needs fill',
        'tenant_improvement_allowance': 'needs fill',
        'landlord_work': NewTenant.getLandlordWork(),
        'special_term_title': 'needs fill',
        'special_term': 'needs fill'
    }
    lease_info_template.render(context)
    lease_info_template.save(NewTenant.getTenant() + "/" + NewTenant.getTenant() + "LI.docx")

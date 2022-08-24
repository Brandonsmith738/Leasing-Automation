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
        'org_type': NewTenant.getORGTypeSelected(),
        'state_of_business': 'Kansas',
        'notice_address': 'needs fill',
        'billing_address': 'needs fill',
        'guarantor': NewTenant.getFirstName(),
        'guarantor_notice_address': 'needs fill',
        'space_location': NewTenant.getSpaceLocation(),
        'space_address': NewTenant.getSpaceAddress(),
        'leased_premise': NewTenant.getLeasedPremise(),
        'leased_area': NewTenant.getLeasedArea(),
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
import tkinter
import tkcalendar
from datetime import date
from tkinter import *
from tkcalendar import Calendar
import PopulateLOI
import TenantData
from TenantData import NewTenant
import LeaseAnalysis
import QuerySalesforceLead
import os, sys

class Window(Frame):
    def __init__(self, master=None):
        # Init GUI
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.TenantFN = ""

    def init_window(self):
        # Packing TK GUI
        self.master.title("Leasing Process Automation")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        # Create a Tkinter variable
        PropertiesDropdown = StringVar(root)

        # Dictionary with options // This can be looped through LA doc in the future
        choices = ['21 Webb',
                   '127 Pawnee',
                   'Auburn Pointe',
                   'Bel Pointe',
                   'Central Plaza',
                   'Douglas',
                   'NDV Real Estate, LLC',
                   'Northwest Centre',
                   'NR6, LLC - Office',
                   'North Rock Retail',
                   'North Rock 14',
                   'Occidental Property, LLC',
                   'OPX, LLC',
                   'Royal 1',
                   'RP 21st, LLC',
                   'Springcreek, LLC',
                   'Tyler Pointe',
                   'Union Station',
                   'Wood 96',
                   'Comotara',
                   'Edgemoor',
                   'The Ice House'
                   ]
        PropertiesDropdown.set('21 Webb')  # set the default option

        # Row 1
        TenantLabel = Label(root, text="Tenant Business Name")
        TenantLabel.pack(side=LEFT)
        TenantLabel.place(relx=0, rely=0)
        TenantEntry = Entry(root, bd=5)
        TenantEntry.pack(side=RIGHT)
        TenantEntry.place(relx=0.11, rely=0)

        LeadFirstNameLabel = Label(root, text="Lead First Name")
        LeadFirstNameLabel.pack(side=LEFT)
        LeadFirstNameLabel.place(relx=0.25, rely=0)
        LeadFirstNameEntry = Entry(root, bd=5)
        LeadFirstNameEntry.pack(side=RIGHT)
        LeadFirstNameEntry.place(relx=0.33, rely=0)

        SpaceLocationLabel = Label(root, text="Space Address")
        SpaceLocationLabel.pack(side=LEFT)
        SpaceLocationLabel.place(relx=0.45, rely=0)
        SpaceLocationEntry = Entry(root, bd=5)
        SpaceLocationEntry.pack(side=RIGHT)
        SpaceLocationEntry.place(relx=0.52, rely=0)

        drop = OptionMenu(root, PropertiesDropdown, *choices)
        drop.pack()
        drop.place(relx=0.63, rely=0)
        print(choices.index(PropertiesDropdown.get()))

        # def pushToBaseRentList():
        #     # Append each entry onto the NewTenant Obj
        #     NewTenant.appendRentSqft(BaseRentEntry.get())
        #     # For development
        #     print(NewTenant.getRentBase())
        #     # Here we loop through the list of base rent, we are displaying it onto the GUI
        #     # This will actually be DELETED. NEW PROJECT: Giant Linear Algebra problem that gives the below as possible solutions
        #     # Problem,,,,, How to show the possible solutions with Tkinter
        #     for i in range(int(len(NewTenant.getRentBase()))):
        #         ShowBaseRentList = Label(root, text='Year '+str(i+1)+'      '+str(NewTenant.getRentBaseElement(i)))
        #         ShowBaseRentList.pack(side=LEFT)
        #         ShowBaseRentList.place(relx=0.85, rely=0.1+(i/40))

        BaseRentLabel = Label(root, text="Yearly Base Rent")
        BaseRentLabel.pack(side=LEFT)
        BaseRentLabel.place(relx=0.76, rely=0)
        BaseRentEntry = Entry(root, bd=5)
        BaseRentEntry.pack(side=RIGHT)
        BaseRentEntry.place(relx=0.85, rely=0)

        # PushBaseRent = Button(self, text='Add Base Rent', command=pushToBaseRentList)
        # PushBaseRent.place(x=1023, y=30)

        # Row 2
        TermLengthLabel = Label(root, text="Term Length (yrs)")
        TermLengthLabel.pack(side=LEFT)
        TermLengthLabel.place(relx=0, rely=0.1)
        TermLengthEntry = Entry(root, bd=5)
        TermLengthEntry.pack(side=RIGHT)
        TermLengthEntry.place(relx=0.11, rely=0.1)

        LandlordWorkLabel = Label(root, text="Landlord's Work: ")
        LandlordWorkLabel.pack(side=LEFT)
        LandlordWorkLabel.place(relx=0, rely=0.15)
        LandlordWorkEntry = Text(root, height=5, width=52)
        LandlordWorkEntry.pack(side=RIGHT)
        LandlordWorkEntry.place(relx=0.1, rely=0.15)

        TenantWorkLabel = Label(root, text="Tenant's Work: ")
        TenantWorkLabel.pack(side=LEFT)
        TenantWorkLabel.place(relx=0, rely=0.3)
        TenantWorkEntry = Text(root, height=5, width=52)
        TenantWorkEntry.pack(side=RIGHT)
        TenantWorkEntry.place(relx=0.1, rely=0.3)

        ExtraContingencyLabel = Label(root, text="Extra Contingencies: ")
        ExtraContingencyLabel.pack(side=LEFT)
        ExtraContingencyLabel.place(relx=0, rely=0.6)
        ExtraContingencyEntry = Text(root, height=5, width=52)
        ExtraContingencyEntry.pack(side=RIGHT)
        ExtraContingencyEntry.place(relx=0.1, rely=0.6)
        # Check button for Tenant finish ?
        Checkbutton1 = BooleanVar()

        TenantFinishCheckbox = Checkbutton(root, text="Tenant Finish?",
                              variable=Checkbutton1,
                              onvalue=1,
                              offvalue=0,
                              height=2,
                              width=10)
        TenantFinishCheckbox.place(relx=0.082, rely=0.45)

        # Calendar for Commencement Days
        cal = Calendar(root, selectmode='day',
                       year=TenantData.getTodayYear(), month=TenantData.getTodayMonth(),
                       day=TenantData.getToday())
        cal.pack(pady=20)
        cal.place(relx=0.76, rely=0.5)

        # Calculates the difference from today to commencement
        def getDeltaDate():
            d0 = date(int(str(TenantData.getTodayYear())), TenantData.getTodayMonth(), TenantData.getToday())
            d1 = date(int('20'+cal.get_date()[5:7]), int(cal.get_date()[0:1]), int(cal.get_date()[2:4]))
            DeltaDate = str(d1 - d0)
            deltaDateIndex = DeltaDate.index(' ')
            return DeltaDate[0:deltaDateIndex]



        # Checks if there exists text in landlord work textbox
        def checkLandlordWork():
            if len(LandlordWorkEntry.get("1.0", 'end-1c')) >= 1:
                NewTenant.setLandlordWorkExist(True)

        # getter function for the Data required to make documents
        def getData():
            # Set data
            NewTenant.setTenant(TenantEntry.get())
            NewTenant.setFirstName(LeadFirstNameEntry.get())
            NewTenant.setSpaceAddress(SpaceLocationEntry.get())
            NewTenant.setLeaseTerm(TermLengthEntry.get())
            NewTenant.setSpaceLocation(PropertiesDropdown.get())
            NewTenant.setPossessionDate(cal.get_date())
            NewTenant.setDeltaDate(int(getDeltaDate()))
            NewTenant.setTenantWork(TenantWorkEntry.get("1.0",'end-1c'))
            NewTenant.setLandlordWork(LandlordWorkEntry.get("1.0",'end-1c'))
            NewTenant.setExtraConstingency(ExtraContingencyEntry.get("1.0",'end-1c'))
            NewTenant.setTenantFinishCheckbox(Checkbutton1.get())
            checkLandlordWork()


            # Initiate LOI and LA
            PopulateLOI.initDirectories()
            LeaseAnalysis.createTemplate(choices.index(PropertiesDropdown.get()))
            PopulateLOI.createTemplate()

        ExecuteButton = Button(self, text='Execute Automation', command=getData)
        ExecuteButton.place(x=1055,y=550)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("1200x600")
app = Window(root)
root.mainloop()
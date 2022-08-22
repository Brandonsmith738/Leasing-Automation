import tkinter
import tkcalendar
from datetime import date
from tkinter import *
from tkcalendar import Calendar
import PopulateLOI
import Populate_Lease_Info
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

    def client_exit(self):
        exit()

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
        TenantLabel = Label(root, text="Tenant Business Name", font=('Times', 12))
        TenantLabel.pack(side=LEFT)
        TenantLabel.place(relx=.05, rely=.01)
        TenantEntry = Entry(root, bd=5)
        TenantEntry.pack(side=RIGHT)
        TenantEntry.place(relx=.12, rely=.01)

        LeadFirstNameLabel = Label(root, text="Lead First Name", font=('Times', 12))
        LeadFirstNameLabel.pack(side=LEFT)
        LeadFirstNameLabel.place(relx=0.23, rely=.01)
        LeadFirstNameEntry = Entry(root, bd=5)
        LeadFirstNameEntry.pack(side=RIGHT)
        LeadFirstNameEntry.place(relx=0.28, rely=.01)

        SpaceLocationLabel = Label(root, text="Space Address", font=('Times', 12))
        SpaceLocationLabel.pack(side=LEFT)
        SpaceLocationLabel.place(relx=0.38, rely=.01)
        SpaceLocationEntry = Entry(root, bd=5)
        SpaceLocationEntry.pack(side=RIGHT)
        SpaceLocationEntry.place(relx=0.43, rely=.01)

        drop = OptionMenu(root, PropertiesDropdown, *choices)
        drop.pack()
        drop.place(relx=0.5, rely=.01)
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

        BaseRentLabel = Label(root, text="Yearly Base Rent", font=('Times', 12))
        BaseRentLabel.pack(side=LEFT)
        BaseRentLabel.place(relx=0.57, rely=.01)
        BaseRentEntry = Entry(root, bd=5)
        BaseRentEntry.pack(side=RIGHT)
        BaseRentEntry.place(relx=0.62, rely=.01)

        # PushBaseRent = Button(self, text='Add Base Rent', command=pushToBaseRentList)
        # PushBaseRent.place(x=1023, y=30)

        # Row 2
        TermLengthLabel = Label(root, text="Term Length (yrs)", font=('Times', 12))
        TermLengthLabel.pack(side=LEFT)
        TermLengthLabel.place(relx=.71, rely=.01)
        TermLengthEntry = Entry(root, bd=5)
        TermLengthEntry.pack(side=RIGHT)
        TermLengthEntry.place(relx=0.76, rely=.01)

        ROILabel = Label(root, text="ROI", font=('Times', 12))
        ROILabel.pack(side=LEFT)
        ROILabel.place(relx=.85, rely=.01)
        ROIEntry = Entry(root, bd=5)
        ROIEntry.pack(side=LEFT)
        ROIEntry.place(relx=.87, rely=.01)

        LandlordWorkLabel = Label(root, text="Landlord's Work: ", font=('Times', 12))
        LandlordWorkLabel.pack(side=LEFT)
        LandlordWorkLabel.place(relx=.05, rely=0.15)
        LandlordWorkEntry = Text(root, height=5, width=52)
        LandlordWorkEntry.pack(side=RIGHT)
        LandlordWorkEntry.place(relx=0.1, rely=0.15)

        TenantWorkLabel = Label(root, text="Tenant's Work: ", font=('Times', 12))
        TenantWorkLabel.pack(side=LEFT)
        TenantWorkLabel.place(relx=.05, rely=0.3)
        TenantWorkEntry = Text(root, height=5, width=52)
        TenantWorkEntry.pack(side=RIGHT)
        TenantWorkEntry.place(relx=0.1, rely=0.3)

        ExtraContingencyLabel = Label(root, text="Extra Contingencies: ", font=('Times', 12))
        ExtraContingencyLabel.pack(side=LEFT)
        ExtraContingencyLabel.place(relx=.40, rely=0.15)
        ExtraContingencyEntry = Text(root, height=5, width=52)
        ExtraContingencyEntry.pack(side=RIGHT)
        ExtraContingencyEntry.place(relx=0.46, rely=0.15)

        # Signage entry
        SignageLabel = Label(root, text="Signage: ")
        SignageLabel.pack(side=LEFT)

        SignageLabel.place(relx=.42, rely=0.3)
        SignageEntry = Text(root, height=5, width=52)
        SignageEntry.pack(side=RIGHT)
        SignageEntry.place(relx=0.46, rely=0.3)

        # Check button for Tenant finish ?
        Checkbutton1 = BooleanVar()

        TenantFinishCheckbox = Checkbutton(root, text="Tenant Finish?",
                                           variable=Checkbutton1,
                                           onvalue=1,
                                           offvalue=0,
                                           height=10,
                                           width=20, font=('Times', 12))
        TenantFinishCheckbox.place(relx=.75, rely=0.27)

        # Calendar for Commencement Days
        cal = Calendar(root, selectmode='day',
                       year=TenantData.getTodayYear(), month=TenantData.getTodayMonth(),
                       day=TenantData.getToday())
        cal.pack(padx=20)
        cal.place(relx=0.75, rely=.15)

        # Calculates the difference from today to commencement
        def getDeltaDate():
            try:
                d0 = date(int(str(TenantData.getTodayYear())), TenantData.getTodayMonth(), TenantData.getToday())
                d1 = date(int('20' + cal.get_date()[5:7]), int(cal.get_date()[0:1]), int(cal.get_date()[2:4]))
                DeltaDate = str(d1 - d0)
                deltaDateIndex = DeltaDate.index(' ')
                return DeltaDate[0:deltaDateIndex]
            except:
                print("Invalid Date Entered")



        # Checks if there exists text in landlord work textbox
        def checkIfExists():
            if len(LandlordWorkEntry.get("1.0", 'end-1c')) >= 1:
                NewTenant.setLandlordWorkExist(True)
            if len(SignageEntry.get("1.0", 'end-1c')) >= 1:
                NewTenant.setSignageExists(True)

        # getter function for the Data required to make documents
        def getData():
            # Set data
            
        try:
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
            NewTenant.setSignage(SignageEntry.get("1.0",'end-1c'))
            NewTenant.setTenantFinishCheckbox(Checkbutton1.get())
         except:
              print("(Entry Error)")

            checkIfExists()


            # Initiate LOI, LA, and LI
            PopulateLOI.initDirectories()
            LeaseAnalysis.createTemplate(choices.index(PropertiesDropdown.get()))
            PopulateLOI.createTemplate()
            Populate_Lease_Info.createTemplate()

        ExecuteButton = Button(self, text='Execute Automation', command=getData)
        ExecuteButton.place(x=1055,y=550)

def client_exit(self):
    exit()

root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
app = Window(root)

class MiniWindow(Frame):
    def openNewWindow():
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(root)

        newWindow.title("New Window")

        # sets the geometry of the new window
        newWindow.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        Label(newWindow,
              text="Solutions Go Here").pack()
        #Save button
        SaveButton = Button(newWindow, width= 400, height=30, bg='blue')
        SaveButton.place(relx=0, rely=.75)
        SaveLabel = Label(newWindow, text='Save All Solutions', font=('Arial, 100'), fg='white', bg='blue')
        SaveLabel.place(relx=.3, rely=.8)
    #Calculate button
    CalculateButton = Button(root, command=openNewWindow, width=400, height=30, bg='orange')
    CalculateButton.place(relx=0, rely=.75)
    CalculateLabel = Label(root, text='Calculate Solutions', font=('Arial', 100), fg='white', bg='orange')
    CalculateLabel.place(relx=.275, rely=.8)

root.mainloop()

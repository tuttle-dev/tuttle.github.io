"""Defines all text strings displayed in the app"""

APP_NAME = "Tuttle"
APP_DESCRIPTION = "Time and money management for freelancers"
APP_DESCRIPTION_LENGTHY = "Tuttle is a time and finance planning tool tailored for the requirements of freelancers."

"""splash screen strings"""
WELCOME_TITLE = "Hi, Welcome to Tuttle."
WELCOME_SUBTITLE = "Let's get you started"
GET_STARTED = "Get Started"
SPLASH_IMG_SEMANTIC_LBL = "Tuttle splash image"

PREFERENCES = "Preferences"
TOOLTIP_NEW = "New"
TOOLTIP_NOTIFICATIONS = "Notifications"
TOOLTIP_MY_PROFILE = "My Profile"

""" user info """
NAME_LBL = "Name"
EMAIL_LBL = "Email"
TITLE_LBL = "Title"
TITLE_HINT = "Your freelancor title e.g. data analyst"
NAME_HINT = "Enter your name"
EMAIL_HINT = "Enter your email"
PHONE_LBL = "Phone number"
PHONE_HINT = "Include country code e.g. +49"
ADDRESS_LBL = "Your address"
ADDRESS = "Address"
ADDRESS_HINT_OPTIONAL = "For your contracts & invoices. You can skip for now"
ID_LBL = "Id"
INVOICING_CONTACT_ID = "Invoicing Contact Id"

"""User info errors"""
MISSING_NAME_ERR = "Your name is required"
MISSING_EMAIL_ERR = "Your email is required"
MISSING_PHONE_ERR = "Your phone number is required"
TITLE_NOT_SET_ERR = (
    "You have not set your title.\nYou can use a generic one such as Freelancer"
)
PROFILE = "My Profile"

"""Side bar menu"""
PROJECTS = "Projects"
CLIENTS = "Clients"
CONTRACTS = "Contracts"
CONTACTS = "Contacts"

"""Settings"""
SETTINGS = "Settings"

"""My Projects View"""
MY_PROJECTS = "My Projects"
NO_PROJECTS_ADDED = "You have not added any projects yet."
ACTIVE = "Active"
COMPLETED = "Completed"
UPCOMING = "Upcoming"
ALL = "All"
VIEW_DETAILS = "View"
START_DATE = "Start Date"
END_DATE = "Deadline"
CLIENT_ID_LBL = "Client Id"
CONTRACT_ID_LBL = "Contract Id"
PROJECT_TAG = "#"
PROJECT_STATUS_LBL = "status"
SIDE_MENU_MAIN_GROUP_TITLE = "Work"
SIDE_MENU_SUB_GROUP_TITLE = "Generated"
PROJECT_LBL = "Project"
EDIT_PROJECT = "Edit Project"
MARK_AS_COMPLETE = "Mark as complete"
DELETE_PROJECT = "Delete project"
VIEW_CLIENT_LBL = "Client"
VIEW_CONTRACT_LBL = "Contract"
VIEW_CLIENT_HINT = "View client"
VIEW_CONTRACT_HINT = "view contract"
PROJECT_DESC_LBL = "Project Description"

"""DATE PICKER"""
DAY_LBL = "D"
MONTH_LBL = "M"
YEAR_LBL = "Y"


"""Create project / client / contracts"""
CREATE_PROJECT_FAILED = "Failed to create the project! Please retry"
CREATE_CLIENT_MISSING_TITLE_ERR = "The title is required"
CREATE_CLIENT_FAILED_ERR = "Saving client failed. Please retry"
CREATE_CONTRACT_MISSING_DESCRIPTION_ERR = "The contract description is required"
CREATE_CONTRACT_FAILED_ERR = "Saving contract failed. Please retry"
PROJECT_NOT_FOUND = "Looks like that project does not exist!"
CLIENT_NOT_FOUND = "Looks like that client does not exist!"
CONTRACT_NOT_FOUND = "Looks like that contract does not exist!"
CREATE_CONTACT_FAILED_ERR = "Saving contact failed. Please retry"
CONTACT_NOT_FOUND = "Looks like that contact does not exist!"
CREATE_ADDRESS_FAILED_ERR = "Saving address failed. Please retry"
ADDRESS_NOT_FOUND = "Looks like that address does not exist!"

"""Contracts List View"""
MY_CONTRACTS = "My Contracts"
NO_CONTRACTS_ADDED = "You currently have no contracts"

"""Clients List View"""
MY_CLIENTS = "My Clients"
NO_CLIENTS_ADDED = "You currently have no clients"
EDIT_CLIENT_TOOLTIP = "Edit client"

"""Contacts List View"""
MY_CONTACTS = "My Contacts"
NO_CONTACTS_ADDED = "You currentyl have no contacts"
COMPANY_LBL = "Company"
EDIT_CONTACT_TOOLTIP = "Edit contact"
NEW_CLIENT_ADDED_SUCCESS = "New client added"

"""TIME / CYCLE UNITS"""
HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"
HOUR = "hour"
MINUTE = "minute"
DAY = "day"
CONTRACT_BILLING_CYCLE = "Billing Cycle"
CONTRACT_TIME_UNIT = "Time Unit"

"""Contract Details screen"""
CONTRACT_STATUS_LBL = "status"
DELETE_CONTRACT = "Delete contract"
EDIT_CONTRACT = "Edit contract"
CONTRACT_LBL = "Contract"
CONTRACT_RATE = "Rate"
CONTRACT_CURRENCY = "Currency"
CONTRACT_VAT_RATE = "Vat Rate"
CONTRACT_UNITS_PER_WORKDAY = "Units Per Workday"
CONTRACT_VOLUME = "Volume"
CONTRACT_TERM_OF_PAYMENT = "Term of Payment"
CONTRACT_SIGNATURE_DATE = "Signed On"


"""Contact Details screen"""
DELETE_CONTACT = "Delete contact"
EDIT_CONTACT = "Edit contact"
CONTACT_LBL = "Contact"
UPDATING_ADDRESS_FAILED = "Failed to update the address! Please re-try"
UPDATING_CONTACT_FAILED = "Failed to update the address! Please re-try"
UPDATING_CONTACT_SUCCESS = "Contact updated successfully"
NEW_CONTACT_ADDED_SUCCESS = "New contact added"

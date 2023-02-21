from page.add_contact_page import AddContactPage
from page.contacts_index_page import ContactsIndexPage
from page.saved_contact_page import SavedContactPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def add_contact(self):
        return AddContactPage(self.driver)

    @property
    def contacts_index(self):
        return ContactsIndexPage(self.driver)

    @property
    def saved_contact(self):
        return SavedContactPage(self.driver)




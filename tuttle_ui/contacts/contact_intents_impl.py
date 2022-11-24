from typing import Mapping, Optional
from core.abstractions import LocalCache
from .abstractions import ContactsIntent
from .utils import ContactIntentsResult
from .contact_data_source_impl import ContactDataSourceImpl
from .contact_model import Contact
from res.strings import (
    CREATE_ADDRESS_FAILED_ERR,
    CREATE_CONTACT_FAILED_ERR,
    CONTACT_NOT_FOUND,
    ADDRESS_NOT_FOUND,
)


class ContactIntentImpl(ContactsIntent):
    def __init__(self, cache: LocalCache):
        super().__init__(cache=cache, dataSource=ContactDataSourceImpl())
        self.allContactsCache: Mapping[str, Contact] = None

    def get_all_contacts(self) -> Mapping[str, Contact]:
        if self.allContactsCache:
            # return cached results
            return self.allContactsCache

        # fetch from data source
        self._clear_cached_results()
        result = self.dataSource.get_all_contacts_as_map()
        if result.wasIntentSuccessful:
            self.allContactsCache = result.data
            return self.allContactsCache
        else:
            # TODO log error
            return {}

    def _clear_cached_results(self):
        self.allContactsCache = None

    def cache_contacts_data(self, key: str, data: any):
        self.cache.set_value(key, data)

    def create_or_update_contact(
        self,
        first_name: str,
        last_name: str,
        company: Optional[str],
        email: str,
        address_id: Optional[int],
        contact_id: Optional[str] = None,
    ) -> ContactIntentsResult:
        result = self.dataSource.save_contact(
            contact_id=contact_id,
            first_name=first_name,
            last_name=last_name,
            company=company,
            email=email,
            address_id=address_id,
        )
        if not result.wasIntentSuccessful:
            result.errorMsg = CREATE_CONTACT_FAILED_ERR
        return result

    def create_or_update_address(
        self,
        street: str,
        number: str,
        city: str,
        postal_code: str,
        country: str,
        address_id: Optional[str] = None,
    ) -> ContactIntentsResult:
        result = self.dataSource.save_address(
            address_id=address_id,
            street=street,
            number=number,
            city=city,
            postal_code=postal_code,
            country=country,
        )
        if not result.wasIntentSuccessful:
            result.errorMsg = CREATE_ADDRESS_FAILED_ERR
        return result

    def get_address_by_id(self, addressId) -> ContactIntentsResult:
        addressIfFound = self.dataSource.get_address_by_id(addressId=addressId)
        return ContactIntentsResult(
            wasIntentSuccessful=addressIfFound != None,
            data=addressIfFound,
            errorMsgIfAny=ADDRESS_NOT_FOUND if addressIfFound == None else "",
        )

    def get_contact_by_id(self, contactId) -> ContactIntentsResult:
        contactIfFound = self.dataSource.get_contact_by_id(contactId=contactId)
        return ContactIntentsResult(
            wasIntentSuccessful=contactIfFound != None,
            data=contactIfFound,
            errorMsgIfAny=CONTACT_NOT_FOUND if contactIfFound == None else "",
        )

    def set_contact_address_id(
        self, address_id: str, contact_id: str
    ) -> ContactIntentsResult:
        return self.dataSource.set_contact_address_id(
            address_id=address_id, contact_id=contact_id
        )

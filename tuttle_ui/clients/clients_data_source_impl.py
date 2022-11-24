from .abstractions import ClientDataSource
from .client_model import Client
from .utils import ClientIntentsResult
from typing import Mapping

# TODO
class ClientDataSourceImpl(ClientDataSource):
    def __init__(self):
        super().__init__()
        self.clients: Mapping[str, Client] = {}

    def get_all_clients_as_map(
        self,
    ) -> ClientIntentsResult:
        self._set_dummy_clients()
        return ClientIntentsResult(wasIntentSuccessful=True, data=self.clients)

    def save_client(self, title: str) -> ClientIntentsResult:
        return ClientIntentsResult(wasIntentSuccessful=False)

    def set_client_contact_id(
        self, invoicing_contact_id: str, client_id: str
    ) -> ClientIntentsResult:
        return ClientIntentsResult(wasIntentSuccessful=True)

    def get_client_by_id(self, clientId) -> ClientIntentsResult:
        i = int(clientId)
        c = Client(id=i, title=f"Client {i}")
        return ClientIntentsResult(wasIntentSuccessful=True, data=c)

    """DUMMY CONTENT BELOW ---  DELETE ALL"""

    def _set_dummy_clients(self):
        self.clients.clear()
        total = 50
        for i in range(total):
            c = Client(id=i, title=f"Client {i}", invoicing_contact_id=int(i * 3.142))
            self.clients[c.id] = c

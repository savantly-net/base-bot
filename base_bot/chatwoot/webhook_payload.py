from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Account:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Account':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        return Account(_id, _name)


@dataclass
class Browser:
    device_name: str
    browser_name: str
    platform_name: str
    browser_version: str
    platform_version: str

    @staticmethod
    def from_dict(obj: Any) -> 'Browser':
        _device_name = str(obj.get("device_name"))
        _browser_name = str(obj.get("browser_name"))
        _platform_name = str(obj.get("platform_name"))
        _browser_version = str(obj.get("browser_version"))
        _platform_version = str(obj.get("platform_version"))
        return Browser(_device_name, _browser_name, _platform_name, _browser_version, _platform_version)


@dataclass
class AdditionalAttributes:
    browser: Browser
    referer: str
    initiated_at: str

    @staticmethod
    def from_dict(obj: Any) -> 'AdditionalAttributes':
        _browser = Browser.from_dict(obj.get("browser"))
        _referer = str(obj.get("referer"))
        _initiated_at = str(obj.get("initiated_at"))
        return AdditionalAttributes(_browser, _referer, _initiated_at)

@dataclass
class Contact:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Contact':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        return Contact(_id, _name)

@dataclass
class Conversation:
    display_id: str
    additional_attributes: AdditionalAttributes

    @staticmethod
    def from_dict(obj: Any) -> 'Conversation':
        _display_id = str(obj.get("display_id"))
        _additional_attributes = AdditionalAttributes.from_dict(obj.get("additional_attributes"))
        return Conversation(_display_id, _additional_attributes)


@dataclass
class Sender:
    id: str
    name: str
    email: str

    @staticmethod
    def from_dict(obj: Any) -> 'Sender':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _email = str(obj.get("email"))
        return Sender(_id, _name, _email)

@dataclass
class Root:
    event: str
    id: str
    content: str
    created_at: str
    message_type: str
    content_type: str
    source_id: str
    sender: Sender
    contact: Contact
    conversation: Conversation
    account: Account

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _event = str(obj.get("event"))
        _id = str(obj.get("id"))
        _content = str(obj.get("content"))
        _created_at = str(obj.get("created_at"))
        _message_type = str(obj.get("message_type"))
        _content_type = str(obj.get("content_type"))
        _source_id = str(obj.get("source_id"))
        _sender = Sender.from_dict(obj.get("sender"))
        _contact = Contact.from_dict(obj.get("contact"))
        _conversation = Conversation.from_dict(obj.get("conversation"))
        _account = Account.from_dict(obj.get("account"))
        return Root(_event, _id, _content, _created_at, _message_type, _content_type, _source_id, _sender, _contact, _conversation, _account)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

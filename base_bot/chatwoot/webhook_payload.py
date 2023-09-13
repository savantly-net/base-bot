from typing import Optional
from pydantic import BaseModel

class Account(BaseModel):
    id: str
    name: str

    @classmethod
    def from_dict(cls, obj):
        return cls(id=str(obj.get("id")), name=str(obj.get("name")))


class Browser(BaseModel):
    device_name: str
    browser_name: str
    platform_name: str
    browser_version: str
    platform_version: str

    @classmethod
    def from_dict(cls, obj):
        return cls(
            device_name=str(obj.get("device_name")),
            browser_name=str(obj.get("browser_name")),
            platform_name=str(obj.get("platform_name")),
            browser_version=str(obj.get("browser_version")),
            platform_version=str(obj.get("platform_version")),
        )


class AdditionalAttributes(BaseModel):
    browser: Browser
    referer: str
    initiated_at: Optional[object] = None

    @classmethod
    def from_dict(cls, obj):
        return cls(
            browser=Browser.from_dict(obj.get("browser")),
            referer=str(obj.get("referer")),
            initiated_at=str(obj.get("initiated_at")),
        )


class Contact(BaseModel):
    id: str
    name: str

    @classmethod
    def from_dict(cls, obj):
        return cls(id=str(obj.get("id")), name=str(obj.get("name")))


class Conversation(BaseModel):
    id: str
    display_id: Optional[str] = None
    additional_attributes: Optional[AdditionalAttributes] = None

    @classmethod
    def from_dict(cls, obj):
        return cls(
            display_id=str(obj.get("display_id")),
            additional_attributes=AdditionalAttributes.from_dict(obj.get("additional_attributes")),
        )


class Sender(BaseModel):
    id: str
    name: str
    email: Optional[str] = None

    @classmethod
    def from_dict(cls, obj):
        return cls(
            id=str(obj.get("id")),
            name=str(obj.get("name")),
            email=str(obj.get("email")),
        )


class Root(BaseModel):
    event: str
    id: str
    content: str
    created_at: str
    message_type: str
    content_type: str
    source_id: Optional[str] = None
    sender: Sender
    contact: Optional[Contact] = None
    conversation: Conversation
    account: Account

    @classmethod
    def from_dict(cls, obj):
        return cls(
            event=str(obj.get("event")),
            id=str(obj.get("id")),
            content=str(obj.get("content")),
            created_at=str(obj.get("created_at")),
            message_type=str(obj.get("message_type")),
            content_type=str(obj.get("content_type")),
            source_id=str(obj.get("source_id")),
            sender=Sender.from_dict(obj.get("sender")),
            contact=Contact.from_dict(obj.get("contact")),
            conversation=Conversation.from_dict(obj.get("conversation")),
            account=Account.from_dict(obj.get("account")),
        )

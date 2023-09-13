from pydantic import BaseModel, Field
from typing import Any, List

class Browser(BaseModel):
    device_name: str
    browser_name: str
    platform_name: str
    browser_version: str
    platform_version: str

class AdditionalAttributes(BaseModel):
    browser: Browser
    referer: str
    initiated_at: dict

class ContactInbox(BaseModel):
    id: int
    contact_id: int
    inbox_id: int
    source_id: str
    created_at: str
    updated_at: str
    hmac_verified: bool
    pubsub_token: str

class Message(BaseModel):
    id: int
    content: str
    account_id: int
    inbox_id: int
    conversation_id: int
    message_type: int
    created_at: int
    updated_at: str
    private: bool
    status: str
    source_id: Any
    content_type: str
    content_attributes: dict
    sender_type: str
    sender_id: int
    external_source_ids: dict
    additional_attributes: dict
    label_list: Any
    conversation: dict
    sender: dict

class Conversation(BaseModel):
    additional_attributes: AdditionalAttributes
    can_reply: bool
    channel: str
    contact_inbox: ContactInbox
    id: int
    inbox_id: int
    messages: List[Message]
    labels: List[Any]
    meta: dict
    status: str
    custom_attributes: dict
    snoozed_until: Any
    unread_count: int
    first_reply_created_at: Any
    agent_last_seen_at: int
    contact_last_seen_at: int
    timestamp: int
    created_at: str

class Account(BaseModel):
    id: int
    name: str

class Sender(BaseModel):
    account: Account
    additional_attributes: dict
    avatar: str
    custom_attributes: dict
    email: Any
    id: int
    identifier: Any
    name: str
    phone_number: Any
    thumbnail: str

class Root(BaseModel):
    account: Account
    additional_attributes: dict
    content_attributes: dict
    content_type: str
    content: str
    conversation: Conversation
    created_at: str
    id: int
    inbox: dict
    message_type: str
    private: bool
    sender: Sender
    source_id: Any
    event: str

from . import config

class UIContext:
    page_title = config.UI_PAGE_TITLE
    page_description = config.UI_PAGE_DESCRIPTION
    page_favicon = config.UI_PAGE_FAVICON
    show_header = config.UI_SHOW_HEADER
    header_center = config.UI_HEADER_CENTER
    header_title = config.UI_HEADER_TITLE
    header_logo_src = config.UI_HEADER_LOGO_SRC
    header_logo_alt = config.UI_HEADER_LOGO_ALT
    header_logo_href = config.UI_HEADER_LOGO_HREF
    chat_bot_name = config.UI_CHAT_BOT_NAME

ui = UIContext()
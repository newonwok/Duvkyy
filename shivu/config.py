class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1853342928"
    sudo_users = "1853342928", "6327652067"
    GROUP_ID = -1001945562571
    TOKEN = "6657141119:AAE9He0fZ_EICUt6NTDZUavjoYIwrODfnfg"
    mongo_url = ""
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "lavda_lasan"
    UPDATE_CHAT = "lavda_lasan"
    BOT_USERNAME = "lavda_lasan"
    CHARA_CHANNEL_ID = "-1001945562571"
    api_id = 24726690
    api_hash = "1452fafefb8b331e1118a7363d364e16"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

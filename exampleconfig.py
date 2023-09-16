from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 21609328
    API_HASH = "a4b9bbdffa3b5602e0e940ba1fd653d9"
    # the name to display in your alive message
    ALIVE_NAME = "Koury"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://aarkaqfd:EHNLULcma1v0ox1UMPjuqxLQKMiNWKTk@surus.db.elephantsql.com/aarkaqfd"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzQBuzmdAHxyL8JG-7o0PDcVupNxe_Q-Kw3g5sF2EYdbVZQUTesZgfQCD2SiCRi84MzYg0U3zJZvSMfBYA6N_hDbJ3od9Vec0PW0jknMr3eFIgOOsoqXMP222fxYyHLm3MD22SD_qUUz867tMB_gFEgvUYh6Sv0Hjb9Dpr1E-Eu4kMCZtfR9FIHQUwKw5tbmbAW0_w5mSHdDOsELKzNudbfMmqeMRY_kFKWFyq2XHW6S6RK-_J2A9nz-UPJa96Fa8SOHD0emFeMOrnK91gHAZOJK0TVacW-zFJokUaelluLmfvCG0Vn8teYTVImuuLncRzn9zP2XwsoGCFAkWSIG7CddPoo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6653543487:AAH5HY5kTExotIXw6CmTXD4bjfnIX_890fc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001877478696
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"

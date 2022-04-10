import conf.config as config

class BotConfig:
    def __init__(self):
        pass

    def __Generate(self):
        self._data = dict(
            Version = config.VERSION_CFG_BOT,
            Testing = False,
            Token = None,
            Token_Testing = None,
            Bot = True,
            CommandPrefix = None,
            Intents = dict(
                all = False,
                none = False,
                default = False,
                Flags = dict(
                    guilds = False,
                    members = True,
                    bans = False,
                    emojis = False,
                    integrations = False,
                    webhooks = False,
                    invites = False,
                    voice_states = False,
                    presences = False,
                    messages = False,
                    guild_messages = False,
                    dm_messages = False,
                    reactions = True,
                    guild_reactions = False,
                    dm_reactions = False,
                    typing = False,
                    guild_typing = False,
                    dm_typing = False
                ),
            ),
            Modules = [],
        )
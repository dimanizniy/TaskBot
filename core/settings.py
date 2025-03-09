from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Setings:
    bots: Bots

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Setings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id = env.int("ADMINS")
        )
    )

settings = get_settings('.env')
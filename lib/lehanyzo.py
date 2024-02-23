import aiohttp
import asyncio
from dotenv import load_dotenv
import os
import random
from datetime import datetime

load_dotenv()

debug_mode = os.getenv("DEBUG_MODE") #itt hiaba alakitottam at bool-a valami oknal fogva nem tetszett neki.

# egy workaround megoldas xd
if debug_mode.lower() in ["true", "be", "bekapcsol", "i", "y", "porniți", "activați"]:
    debug_mode = True
else:
    debug_mode = False

class get:

    async def stream_allapot(client_id, username):
        url = "https://gql.twitch.tv/gql"
        query = "query {\n  user(login: \"" + username + "\") {\n    stream {\n      id\n    }\n  }\n}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json={"query": query, "variables": {}}, headers={"client-id": client_id}) as response:
                    data = await response.json()
                    if debug_mode:
                        print("debug valasz:", data)
                    stream_data = data.get("data", {}).get("user", {}).get("stream")
                    return stream_data and stream_data.get("id")
            except Exception as e:
                print(f"Hiba biba bibu bip bup bam bum: {e}")
                return False

    def env_var(key):
        return os.getenv(key)

    def debug_mode():
        debug_mode = os.getenv("DEBUG_MODE")
        if debug_mode.lower() in ["true", "be"]:
            debug_mode = True
        else:
            debug_mode = False
        return debug_mode


    def kranem_footer(footer, cmd=None):
        jelenlegi_ev = datetime.now().year
        jelenlegi_ido = datetime.now().strftime("%Y/%m/%d %H:%M")

        if random.random() < 0.25:
            footer = "Kranem Bots © " + str(jelenlegi_ev)
        else:
            if "[current_command]" in footer and cmd:
                footer = footer.replace("[current_command]", cmd)
            if "[year]" in footer:
                footer = footer.replace("[year]", str(jelenlegi_ev))
            if "[current_time]" in footer:
                footer = footer.replace("[current_time]", str(jelenlegi_ido))



        return footer
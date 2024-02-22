import aiohttp
import asyncio

async def checkIfUserIsStreaming(felhasznalonev):
    url = "https://gql.twitch.tv/gql"
    query = "query {\n  user(login: \""+felhasznalonev+"\") {\n    stream {\n      id\n    }\n  }\n}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"query": query, "variables": {}}, headers={"client-id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}) as valasz:
            data = await valasz.json()
            print("debug valasz:", data)  
            stream_data = data.get("data", {}).get("user", {}).get("stream")
            if stream_data and stream_data.get("id"):
                return True
            else:
                return False

async def main():
    is_streaming = await checkIfUserIsStreaming("lehanyzo")
    print("streamel?:", is_streaming)

if __name__ == "__main__":
    asyncio.run(main())

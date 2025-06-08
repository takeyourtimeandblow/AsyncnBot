import asyncio
import requests

sites: tuple = (
    'https://api.ipify.org?format=json',
    'http://ip-api.com/json/'
)

async def request_ip(site) -> str:
    await asyncio.sleep(0.05)
    js = requests.get(site).json()
    if 'query' in js:
        return js["query"]
    elif "ip" in js:
        return js["ip"]

    return ""

async def main():
    tasks = [request_ip(sites[0]), request_ip(sites[1])]

    for completed in asyncio.as_completed(tasks):
        res = await completed
        print(res)
        break

if __name__ == '__main__':
    asyncio.run(main())


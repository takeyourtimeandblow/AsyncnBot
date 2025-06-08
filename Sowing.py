import asyncio

from typing import Final

should_speed_up: bool = True

feeding: Final[int] = 3 if not should_speed_up else 0.003
pest_control: Final[int] = 5 if not should_speed_up else 0.005

async def feed_pest(name):
    print("7 Application of fertilizers for", name)
    await asyncio.sleep(feeding)
    print("7 Fertilizers for the", name, "have been introduced")

    print("8 Treatment of", name, "from pests")
    await asyncio.sleep(pest_control)
    print("8 The", name, "is treated from pests")

async def sowing(name, soak, shelter, plant):
    if should_speed_up:
        soak /= 1000
        shelter /= 1000
        plant /= 1000

    print("0 Beginning of sowing the", name, "plant")
    # ...
    print("1 Soaking of the", name, "started")
    await asyncio.sleep(soak)
    print("2 Soaking of the", name, "is finished")

    print("3 Shelter of the", name, "is supplied")
    await asyncio.sleep(shelter)
    print("4 Shelter of the", name, "is removed")

    print("5 The", name, "has been transplanted")
    await asyncio.sleep(plant)
    print("6 The", name, "has taken root")

    print("9 The seedlings of the", name, "are ready")

async def main():
    data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]

    tasks = [
        (asyncio.create_task(sowing(name, i, i1, i2)),
         asyncio.create_task(feed_pest(name)))
        for name, i, i1, i2 in data
    ]

    await asyncio.gather(*tasks[0])
    await asyncio.gather(*tasks[1])

if __name__ == '__main__':
    asyncio.run(main())

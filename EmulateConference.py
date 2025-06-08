import asyncio
import time


async def do_task(name, *args):
    coef = .01
    it = iter(args)

    for i, (a, b) in enumerate(zip(it, it), 1):
        print(f'{name} started the {i} task.')
        await asyncio.sleep(coef * a)
        print(f"{name} moved on to the defense of the {i} task.")
        await asyncio.sleep(coef * b)
        print(f"{name} completed the {i} task.")
        if i < 2:
            print(f"{name} is resting.")
            await asyncio.sleep(coef * 5)

async def main():
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()

    tasks = [
        asyncio.create_task(do_task(name, i, i1, i2, i3)) for name, i, i1, i2, i3 in data
    ]
    await asyncio.gather(*tasks)
    print(time.time() - t0)

if __name__ == "__main__":
    asyncio.run(main())
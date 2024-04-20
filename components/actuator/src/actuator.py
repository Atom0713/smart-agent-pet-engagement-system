import asyncio


async def main() -> None:
    while True:
        await asyncio.sleep(20)
        print("Hello!")


def run() -> None:
    asyncio.run(main())


run()

from models import Start, Category, Currency, Discont, Power, Promo, Coin, Application, Admin


async def main():

    coins = [ "bitcoin-cash", "litecoin", "ethereum-classic", "zcash", "dash"]
    for co in coins:
        co = Coin(
            name=co,
        )
        await co.save()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

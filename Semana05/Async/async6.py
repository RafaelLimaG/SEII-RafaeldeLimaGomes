import asyncio

async def main():
    print('Rafael')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(2)
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("finish task")
    
asyncio.run(main())

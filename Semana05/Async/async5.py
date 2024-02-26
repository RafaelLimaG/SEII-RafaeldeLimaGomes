import asyncio

async def main():
    print('Gabriel')
    task = asyncio.create_task(foo('text'))
    await task
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("finish task")
    
asyncio.run(main())

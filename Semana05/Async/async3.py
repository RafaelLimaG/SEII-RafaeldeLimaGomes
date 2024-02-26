import asyncio

async def main():
    print('Gabriel')
    await foo('text')
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(5)
    print("finish task")
    
asyncio.run(main())

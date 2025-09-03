"""
aiogram
"""
import asyncio
from  aiogram import Bot , Dispatcher , types , F
from handlers import router

TOKEN = "8227707236:AAFlQlr8OvklYp9v8hbOvOkQ3FaTimbpVhQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

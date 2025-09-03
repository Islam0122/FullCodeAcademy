from aiogram import Router , F
from aiogram.types import Message , CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db_list import db_list

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    kb = InlineKeyboardBuilder()
    for lesson in db_list:
        kb.button(text=f"📖 {lesson['title']}", callback_data=f"lesson_{lesson['id']}")
    await message.answer(
        "👋 Привет! Добро пожаловать в Учебный бот!\n\n"
        "Выбери урок ниже ⬇️",
        reply_markup=kb.as_markup()
    )

@router.callback_query(F.data.startswith("lesson_"))
async def show_lesson(callback: CallbackQuery):
    lesson_id = int(callback.data.split("_")[1])
    lesson = next((l for l in db_list if l["id"] == lesson_id), None)

    if lesson:
        kb = InlineKeyboardBuilder()
        kb.button(text="📝 Пройти задание", callback_data=f"quiz_{lesson_id}")
        await callback.message.answer(
            f"✨ Урок: {lesson['title']}\n\n{lesson['content']}",
            reply_markup=kb.as_markup()
        )
    await callback.answer()


@router.callback_query(F.data.startswith("quiz_"))
async def show_quiz(callback: CallbackQuery):
    lesson_id = int(callback.data.split("_")[1])
    lesson = next((l for l in db_list if l["id"] == lesson_id), None)

    if lesson:
        kb = InlineKeyboardBuilder()
        for idx, ans in enumerate(lesson["answers"]):
            kb.button(text=ans["text"], callback_data=f"answer_{lesson_id}_{idx}")
        await callback.message.answer(
            f"❓ {lesson['question']}",
            reply_markup=kb.as_markup()
        )
    await callback.answer()

# 🔹 проверка ответа
@router.callback_query(F.data.startswith("answer_"))
async def check_answer(callback: CallbackQuery):
    _, lesson_id, ans_idx = callback.data.split("_")
    lesson_id, ans_idx = int(lesson_id), int(ans_idx)

    lesson = next((l for l in db_list if l["id"] == lesson_id), None)
    if lesson:
        answer = lesson["answers"][ans_idx]
        if answer["is_correct"]:
            await callback.message.answer("🎉 Молодец! Это правильный ответ ✅")
        else:
            await callback.message.answer("❌ Неверно! Попробуй ещё раз 😉")

    await callback.answer()


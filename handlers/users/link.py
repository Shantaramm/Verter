from aiogram.dispatcher import FSMContext
import io
from loader import dp
from aiogram import types
import urllib3
from PIL import Image
from utils.elemental import qr_img_link

@dp.message_handler(text="🖼 Создать QR-код")
async def qr_link(message: types.Message, state: FSMContext):
    await message.answer(text="Вставте вашу ссылку:")
    await state.set_state("qr_link")

@dp.message_handler(state="qr_link")
async def short_link_run(message: types.Message, state: FSMContext):
    url = message.text
    logo = "logo7.png"
    try:
        byte_arr = io.BytesIO()
        if message.entities[0].type == "url" or message.entities[0].offset == 0:
            url = "https://clck.ru/--?url=" + url
            http = urllib3.PoolManager()
            response = http.request("GET", url)
            img_qr_link = qr_img_link.qr_picture(logo=logo, url=response.data.decode('utf-8'))
            img_qr_link.save(byte_arr, format="PNG")
            byte_arr = byte_arr.getvalue()
        await message.answer_photo(byte_arr)
    except :
        await message.answer("Проверьте правильность написания и вставте правельную ссылку (например: google.com):)")
    await state.finish()


@dp.message_handler(text="✂️ Скоратить ссылку️")
async def short_link(message: types.Message, state: FSMContext):
    await message.answer(text="Вставте вашу ссылку:")
    await state.set_state("short_link")

@dp.message_handler(state="short_link")
async def short_link_run(message: types.Message, state: FSMContext):
    try:
        if message.entities == [] or message.entities[0].offset > 0:
            await message.answer("Проверьте правильность написания ссылки и повторите запрос:)")
            await state.finish()
            return
        url = "https://clck.ru/--?url=" + message.text
        http = urllib3.PoolManager()
        response = http.request("GET", url)
        await message.answer(response.data.decode('utf-8'))
    except:
        await message.answer("Проверьте правильность написания ссылки и повторите запрос :)")
    await state.finish()



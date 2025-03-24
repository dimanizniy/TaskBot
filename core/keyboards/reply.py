from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Rockets"),
        KeyboardButton(text="Ships"),
        KeyboardButton(text="Atomic bombs")
    ],
    [
        KeyboardButton(text="Make a call"),
        KeyboardButton(text="Send a contact")
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Жмакай сюда", selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Send location",
            request_location=True
            )
    ],
    [
        KeyboardButton(
            text="Send contact",
            request_contact=True
            )
    ],
    [
        KeyboardButton(
            text="Create a poll",
            request_poll=KeyboardButtonPollType(type="quiz") # regular для обычного опроса
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder="Локация, контакт и опрос")

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="First")
    keyboard_builder.button(text="Second")
    keyboard_builder.button(text="Third")
    keyboard_builder.button(text="Send location", request_location=True)
    keyboard_builder.adjust(3, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Жмакай сюда")
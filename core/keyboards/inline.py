from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_notebook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text = "MSI Pro 2023",
            callback_data= "msi_pro_2023"
        )
    ],
    [
        InlineKeyboardButton(
            text = "MSI Gamer 2024",
            callback_data= "msi_gamer_2024"
        )
    ],
    [
        InlineKeyboardButton(
            text = "MSI ROG 2020",
            callback_data= "msi_rog_2020"
        )
    ]
])
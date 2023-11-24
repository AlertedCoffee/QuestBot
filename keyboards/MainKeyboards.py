from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать',
                                                                             callback_data='start_quest')]])

continue_rename_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Продолжить',
                                                                                       callback_data='continue_quest')],
                                                                 [InlineKeyboardButton(text='Переименоваться',
                                                                                       callback_data='start_quest')]])

branch_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ОИТ', callback_data='ОИТ'),
                                                         InlineKeyboardButton(text='ОЭС', callback_data='ОЭС'),
                                                         InlineKeyboardButton(text='ОМЭиКС', callback_data='ОМЭиКС')]])

continue_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Продолжить',
                                                                                callback_data='continue_quest')]])


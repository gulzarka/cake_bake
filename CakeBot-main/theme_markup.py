from telebot import types


def get_start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept_conditions = types.InlineKeyboardButton('Accept terms and conditions', callback_data='back_to_main')
    markup.add(accept_conditions)
    return markup


def get_main_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    see_menu = types.InlineKeyboardButton('Cake menu', callback_data='see_cake_menu')
    see_offers = types.InlineKeyboardButton('Special offers', callback_data='see_offers')
    custom_cake = types.InlineKeyboardButton('Custom cake', callback_data='custom_cake_about')
    see_last_order_delivery_status = types.InlineKeyboardButton('Check delivery status', callback_data='last_order_delivery_status')
    see_history = types.InlineKeyboardButton('Order history', callback_data='see_history')
    markup.add(see_offers, see_menu, custom_cake, see_last_order_delivery_status, see_history)
    return markup


def get_cake_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    position_1 = types.InlineKeyboardButton('1', callback_data='cake_menu_position_1')
    position_2 = types.InlineKeyboardButton('2', callback_data='cake_menu_position_2')
    position_3 = types.InlineKeyboardButton('3', callback_data='cake_menu_position_3')
    position_4 = types.InlineKeyboardButton('4', callback_data='cake_menu_position_4')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(position_1, position_2, position_3, position_4, back_to_main)
    return markup


def get_offers_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    position_1 = types.InlineKeyboardButton('1', callback_data='offer_menu_position_1')
    position_2 = types.InlineKeyboardButton('2', callback_data='offer_menu_position_2')
    position_3 = types.InlineKeyboardButton('3', callback_data='offer_menu_position_3')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(position_1, position_2, position_3, back_to_main)
    return markup


def get_custom_cake_about_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept = types.InlineKeyboardButton('Order a custom cake', callback_data='custom_cake_start')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(accept, back_to_main)
    return markup


def get_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    add_inscription = types.InlineKeyboardButton('Add', callback_data='add_inscription')
    no_inscription = types.InlineKeyboardButton('Skip', callback_data='no_inscription')
    back_to_custom_cake_decorations = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_decorations')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    markup.add(add_inscription, no_inscription, back_to_custom_cake_decorations, back_to_main)
    return markup


def get_writing_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    cancel_inscription = types.InlineKeyboardButton('Cancel', callback_data='cancel_inscription')
    markup.add(cancel_inscription)
    return markup


def get_last_order_delivery_status_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(back_to_main)
    return markup
    

def get_history_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    repeat_last_order = types.InlineKeyboardButton('Repeat last order', callback_data='repeat_last_order')
    repeat_select_order = types.InlineKeyboardButton('Repeat specific order', callback_data='repeat_specific_order')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(repeat_last_order, repeat_select_order, back_to_main)
    return markup

def get_repeat_last_order_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept_repeat_last_order = types.InlineKeyboardButton('Do you wish to repeat this order ?', callback_data='accept_repeat_last_order')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(accept_repeat_last_order, back_to_main)
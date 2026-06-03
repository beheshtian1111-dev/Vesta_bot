import telebot

TOKEN = "8521280831:AAFNrwcECqrwxHFty9FxIhyPAyPjVa27K-g"
bot = telebot.TeleBot(TOKEN)

CHANNEL = "https://t.me/Diivarpoosh"
CHANNEL_ID = "@Diivarpoosh"
ADMIN_SUPPORT = "@botSupport_vesta"
ADMIN_IDS = [7333037232]


# ===== CHECK MEMBERSHIP =====
def is_member(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ["member", "administrator", "creator"]
    except:
        return False


# ===== FILE ID CATCHER (فقط ادمین) =====
@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    if message.from_user.id in ADMIN_IDS:
        file_id = message.photo[-1].file_id
        bot.send_message(
            message.chat.id,
            f"📦 FILE ID:\n\n`{file_id}`",
            parse_mode="Markdown"
        )


# ===== MENUS =====
def show_main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🛍 محصولات", "🛒 ثبت سفارش")
    markup.row("💬 پشتیبانی", "📞 تماس با ما")
    markup.row("🌐 مشاهده سایت", "💰 لیست قیمت")
    bot.send_message(message.chat.id, "🏠 منوی اصلی 👇", reply_markup=markup)


def show_products_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🧱 دیوارپوش فومی پشت چسبدار")
    markup.row("🏠 دیوارپوش فومی رولی")
    markup.row("🪵 ترمووال")
    markup.row("⬜ کفپوش")
    markup.row("🔙 بازگشت")
    bot.send_message(message.chat.id, "دسته‌بندی محصولات 👇", reply_markup=markup)


# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📢 عضویت در کانال", "✅ عضو شدم")
    bot.send_message(message.chat.id, "برای ورود باید عضو کانال باشی 👇", reply_markup=markup)


# ===== JOIN =====
@bot.message_handler(func=lambda m: m.text == "📢 عضویت در کانال")
def join_channel(message):
    bot.send_message(message.chat.id, CHANNEL)


@bot.message_handler(func=lambda m: m.text == "✅ عضو شدم")
def enter_shop(message):
    if not is_member(message.from_user.id):
        bot.send_message(
            message.chat.id,
            "❌ هنوز عضو کانال نشدی!\nاول عضو بشو بعد دوباره امتحان کن 👇\n" + CHANNEL
        )
        return
    show_main_menu(message)


# ===== PRODUCTS =====
@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def products(message):
    show_products_menu(message)


# ===== FOAM STICKY =====
@bot.message_handler(func=lambda m: m.text == "🧱 دیوارپوش فومی پشت چسبدار")
def foam_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("آجر کلاسیک", "آجر بهمنی")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "زیرمجموعه فومی 👇", reply_markup=markup)


# ===== AJOR CLASSIC =====
@bot.message_handler(func=lambda m: m.text == "آجر کلاسیک")
def ajor_classic(message):
    caption = "🧱 آجر کلاسیک\n📐 ابعاد: ۷۰ × ۷۷ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIBr2ogSJiqIZkc6tHU9wRMd_T4ZOvBAAJ7DmsbM2wBUW9wP_Oqe1JMAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBsGogSJiH2R4v4ZhNOemqzY1hcA_DAAJ8DmsbM2wBUanhH2bOPDZ8AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBsmogSJiO2ZWQOP7eSbX92z-GDQd8AAJ-DmsbM2wBUSFB16W-suPKAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBsWogSJiDaw4mCm-JeZ6_G8-6p0diAAJ9DmsbM2wBUUBBaIPIvssqAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBs2ogSJjow1uupWDCE8bBQiECCtQCAAJ_DmsbM2wBUXVc_sM-eEdDAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBtGogSJiHUYsu0yR0GIJrVe8qZG0FAAKADmsbM2wBUTdcU8E_XivBAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBtWogSJixY7t3I8p1SnctiJ7RFriEAAKBDmsbM2wBUesIrjDd8uHYAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBtmogSJjOvRnZqVefXA_jzYZU-gGkAAKCDmsbM2wBUf8Rr2hV2XTqAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBt2ogSJh9QuvOnVimlpkePTbVzwpuAAKDDmsbM2wBUVxpI3_uLIExAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBuGogSJhpGn6xvis1n_lesIKXGFzEAAKEDmsbM2wBUU3hYCWybzGjAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIBuWogSJpl1wx8XzeJY3OojoZiSoiIAAKFDmsbM2wBUXBOmrY2OY_WAQADAgADeAADOwQ",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== AJOR BAHMANI =====
@bot.message_handler(func=lambda m: m.text == "آجر بهمنی")
def ajor_bahmani(message):
    caption = "🧱 آجر بهمنی\n📐 ابعاد: ۷۰ × ۷۷ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIB7mogUUx8tn_vBScy801IodcVMyeNAAKXDmsbM2wBUc-E1tThaYSoAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB72ogUUznNmsQDeWJKon1jjEWIjO0AAKYDmsbM2wBUW9LGrPNzPeWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8GogUUz5lVyAN4vR6BAiEiaMFOxRAAKZDmsbM2wBUa07ZTpGZxC8AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8WogUUxqhowl0jkNRxfe3P4sY5tbAAKaDmsbM2wBUUK0Zs-bq6tLAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8mogUUy0d-nhaXsc5gl6QcqUwp7lAAKbDmsbM2wBUTVCMbmdDSBMAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB82ogUUyy7CBivNp8gKmw7KExntVlAAKcDmsbM2wBUUqGz8i-PzuWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9GogUUxoekNmDTpL07BGMHcGCmmGAAKdDmsbM2wBUTve2EbWu3-2AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9WogUUxWYEPOMk0EoolZen5yez61AAKeDmsbM2wBUc2Tv5uQnSYUAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9mogUUwUtyRaIm0thnAqI2V-1ksgAAKfDmsbM2wBURRQeAiiSA-hAQADAgADeAADOwQ",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== FOAM ROLL =====
@bot.message_handler(func=lambda m: m.text == "🏠 دیوارپوش فومی رولی")
def foam_roll(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(
        message.chat.id,
        "🏠 دیوارپوش فومی رولی\nبرای اطلاعات بیشتر با پشتیبانی تماس بگیر.\n" + ADMIN_SUPPORT,
        reply_markup=markup
    )


# ===== TERMO =====
@bot.message_handler(func=lambda m: m.text == "🪵 ترمووال")
def termo_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("PVC 20cm", "MDF 50cm")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "ترمووال 👇", reply_markup=markup)


# ===== PVC 20 =====
@bot.message_handler(func=lambda m: m.text == "PVC 20cm")
def pvc20(message):
    caption = "🪵 ترمووال PVC 20cm\n📐 ابعاد: عرض ۲۰ سانت × ارتفاع ۲۸۰ سانت\n💰 قیمت: ۶۲۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAICiWogZJJLBIcNQHzywzhcHDsHwJeRAAKID2sbhIIAAVHIvM-HzTU_-AEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICiGogZJL0DIj2sGcFQfYwRjAiTdMwAAKHD2sbhIIAAVHN35yIQyZGXQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICimogZJJHBCvMigK9rnUz9eUdEgcAA4kPaxuEggABUTf3iZtOcHC6AQADAgADeQADOwQ",
        "AgACAgQAAxkBAAICi2ogZJKV7B-NxYW985jUyBiSiMcdAAKKD2sbhIIAAVE96ZIKscfG8QEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICjGogZJL0ekVq3P1u2non-_svi6gsAAKLD2sbhIIAAVHKwr5zKi21XwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICjWogZJLYZuM95fSXIkwWu3qRlZ8fAAKMD2sbhIIAAVGHtp7a0GfXZwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICjmogZJJomK4yZ_e85rztaodSNotyAAKND2sbhIIAAVExn2EdhefBLAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICj2ogZJJO8PCEZ79b8iSMw7cAAWAaewACjg9rG4SCAAFRWe_nDdRHS4gBAAMCAAN5AAM7BA",
        "AgACAgQAAxkBAAICkGogZJLIA25Yx2nVgCfKUvYPn-mOAAKPD2sbhIIAAVHx4uBSov0tfAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICkWogZJIG_HdGlOUAAfn6fXs8Der4JgACkA9rG4SCAAFRCAGBHbgPilcBAAMCAAN5AAM7BA",
        "AgACAgQAAxkBAAICkmogZJJzttqdxDCJyoIaMB6wynvjAAKRD2sbhIIAAVEdLBY8Sptx3QEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICk2ogZJIg2Ez3vNlbzHaLVjnooOK7AAKSD2sbhIIAAVHnDgh2yjUXwgEAAwIAA3kAAzsE",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== MDF 50 =====
@bot.message_handler(func=lambda m: m.text == "MDF 50cm")
def mdf50(message):
    caption = "🪵 ترمووال MDF 50cm\n📐 ابعاد: عرض ۵۰ سانت × ارتفاع ۲۸۰ سانت"
    file_ids = [
        "AgACAgQAAxkBAAIC5mogaFTSW8UK2EeWpwnBRAHCtgGmAAKTD2sbhIIAAVGN7kmS6YnH1AEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC52ogaFSp0tqhCHjgpwu9c8BCeWs3AAKUD2sbhIIAAVFrD_Aw4IWuCwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6GogaFQRJ8miFGUORpD2yoojuM6fAAKVD2sbhIIAAVH_hX7rRtb1vwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6WogaFTSpHQ4nIn3Gx6ICBrtwpinAAKWD2sbhIIAAVH9ecXCJ_v3NQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC62ogaFRIbLPlGLfMqI9dsZg3bT5JAAKYD2sbhIIAAVELSOIgyPgkhgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6mogaFQetEXGT-vDNAqwXi_5SSd4AAKXD2sbhIIAAVHKUmUEdxBwXAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC7GogaFR-jtE6yFCnq5pNIEzOaOsTAAKZD2sbhIIAAVFjiDY-LokqaQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC7WogaFQ8XyIodtWoOBmJcBlI-bK1AAKaD2sbhIIAAVF2XX-dWGMzBQEAAwIAA3kAAzsE",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== FLOOR =====
@bot.message_handler(func=lambda m: m.text == "⬜ کفپوش")
def floor_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("طرح سنگ", "طرح پارکت")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "کفپوش 👇", reply_markup=markup)


# ===== FLOOR STONE =====
@bot.message_handler(func=lambda m: m.text == "طرح سنگ")
def stone_floor(message):
    caption = "⬜ کفپوش طرح سنگ\n📐 ابعاد: ۶۰ × ۶۰ سانتی‌متر\n💰 قیمت ورقی: ۴۴۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAICNGogXS0XT11Bk3HRXuQ3Og4h65IiAAK9DmsbM2wBUVBEJjXiGQstAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICNWogXS2FZEU_oiMw6r462jHtK9lNAAK-DmsbM2wBUcekQ8nLtTVpAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICNmogXS0tbFjUfgU9xTUGaFndbQgWAAK_DmsbM2wBUd3VsMHNAWszAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICN2ogXS06z5EWjb9B8pfJaCobl71-AALADmsbM2wBURTyicohgq7MAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICOGogXS2uBhpYN_Wm6uT0Gzs3z6kkAALBDmsbM2wBUW3cs9nclhf0AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICOWogXS1fkqC_1Q6xruU-MRJID2MxAALCDmsbM2wBUcZcAAFx_Nej_wEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAICOmogXS36qpIo6o40uwhiCzPzYJlAAALDDmsbM2wBUQ5ORzadXCclAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICO2ogXS17N9DeYmWGs9yyxUKTUo-dAALEDmsbM2wBUc7BGQjwI9srAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICPGogXS1Xf2CJLny9_XQG9f1b_WuuAALFDmsbM2wBUcbLpFmo2vt8AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICPWogXS0J84_bE3MYOfcxkuTY7LiFAALGDmsbM2wBUcyQ36nIrRphAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICPmogXTL8ZGGK1hVRjfxSbAckP8w6AALHDmsbM2wBUdQkd7BIk-bYAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICP2ogXTKpo_hadsKGb-gR8jrHQneEAALIDmsbM2wBUSyORIDaCw2NAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAICQGogXTIBgaumDOP2i358PaxZWZktAALJDmsbM2wBUaJSGh46_eyDAQADAgADeAADOwQ",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== FLOOR PARQUET =====
@bot.message_handler(func=lambda m: m.text == "طرح پارکت")
def parquet_floor(message):
    caption = "⬜ کفپوش طرح پارکت\n📏 متراژ هر کارتن: ۳ متر و ۶۰ سانتی‌متر\n💰 قیمت هر کارتن: ۳.۹۶۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIDxWoggUahj0yf52hgF1CfGIadDBqeAALaD2sbhIIAAVHd9OGbpmFPhwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDx2oggUajZlo3WngSXFRFGGMOokQ7AALcD2sbhIIAAVGxKKgQIqadWAEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDyGoggUbKsUcajKbfeUJmTadcRAQCAALdD2sbhIIAAVGmdgzcP--eUwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDxmoggUbQjJ1FUq6wx5Pq2sbqfxyeAALbD2sbhIIAAVEzdwuo8C49DAEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDyWoggUaSVr-ZvEt_9j1iZ2yEL0HlAALeD2sbhIIAAVEHRZnmbh0TPwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDymoggUbXrck5CqYdLkICdf4RGcgMAALfD2sbhIIAAVFdZvOF9ypz2AEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDy2oggUajA6DAya7Tb6NN8CWFUUNdAALgD2sbhIIAAVG9ZLuKklmP1QEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDzGoggUa1ItAjkARNOWbXpCy_Wn_hAALhD2sbhIIAAVEAAYNltlWK8a8BAAMCAAN4AAM7BA",
        "AgACAgQAAxkBAAIDzmoggUasCt6D_sKG9m36bf2VNz-pAALjD2sbhIIAAVGsP9pcP1NLQQEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDzWoggUYygyvsKG5GjDD34iWlx6ZqAALiD2sbhIIAAVG2INX-onDUJAEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIDz2oggUbR5M0syN0xgREr3tm1MOhbAALkD2sbhIIAAVGEWtG9YsA2VQEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAID0GoggUbR3BiYCX2II_82nxTsYJARAALlD2sbhIIAAVH-YOnIP4QNJAEAAwIAA3gAAzsE",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid, caption=caption)


# ===== BACK =====
@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت")
def back(message):
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به محصولات")
def back_products(message):
    show_products_menu(message)


# ===== CONTACT =====
@bot.message_handler(func=lambda m: m.text == "📞 تماس با ما")
def contact(message):
    bot.send_message(message.chat.id, "📞 09120646909\n📞 09370072236")


# ===== SUPPORT =====
@bot.message_handler(func=lambda m: m.text == "💬 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id, ADMIN_SUPPORT)


# ===== SITE =====
@bot.message_handler(func=lambda m: m.text == "🌐 مشاهده سایت")
def site(message):
    bot.send_message(message.chat.id, "https://vestadeccor.com")


# ===== PRICE LIST =====
@bot.message_handler(func=lambda m: m.text == "💰 لیست قیمت")
def price_list(message):
    bot.send_message(
        message.chat.id,
        "💰 لیست قیمت محصولات:\n\n"
        "🧱 آجر کلاسیک — تایلی ۳۸۰ تومان\n"
        "🧱 آجر بهمنی — تایلی ۳۸۰ تومان\n"
        "🪵 ترمووال PVC 20cm — ۶۲۰ تومان\n"
        "🪵 ترمووال MDF 50cm — تماس بگیرید\n"
        "⬜ کفپوش طرح سنگ — ورقی ۴۴۰ تومان\n"
        "⬜ کفپوش طرح پارکت — کارتنی ۳.۹۶۰ تومان\n\n"
        "📞 09120646909\n📞 09370072236"
    )


# ===== ORDER =====
@bot.message_handler(func=lambda m: m.text == "🛒 ثبت سفارش")
def order(message):
    bot.send_message(
        message.chat.id,
        "🛒 برای ثبت سفارش با پشتیبانی در ارتباط باش:\n" + ADMIN_SUPPORT
    )


# ===== RUN =====
bot.infinity_polling()

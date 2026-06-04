import telebot
from telebot import types

TOKEN = "8521280831:AAFNrwcECqrwxHFty9FxIhyPAyPjVa27K-g"
bot = telebot.TeleBot(TOKEN)

CHANNEL = "https://t.me/Diivarpoosh"
CHANNEL_ID = "@Diivarpoosh"
ADMIN_SUPPORT = "@botSupport_vesta"
ADMIN_ID = 7333037232
ADMIN_IDS = [7333037232]

# ذخیره وضعیت استعلام کاربران
user_inquiry = {}


# ===== CHECK MEMBERSHIP =====
def is_member(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ["member", "administrator", "creator"]
    except:
        return False


# ===== FILE ID CATCHER =====
@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    if message.from_user.id in ADMIN_IDS:
        file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, f"📦 FILE ID:\n\n`{file_id}`", parse_mode="Markdown")


# ===== MENUS =====
def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🛍 محصولات", "🛒 ثبت سفارش")
    markup.row("💬 پشتیبانی", "📞 تماس با ما")
    markup.row("🌐 مشاهده سایت", "💰 لیست قیمت")
    bot.send_message(message.chat.id, "🏠 منوی اصلی 👇", reply_markup=markup)


def show_products_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🧱 دیوارپوش فومی پشت چسبدار")
    markup.row("🏠 دیوارپوش فومی رولی")
    markup.row("🪵 ترمووال")
    markup.row("⬜ کفپوش")
    markup.row("🔙 بازگشت")
    bot.send_message(message.chat.id, "دسته‌بندی محصولات 👇", reply_markup=markup)


def show_foam_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("آجر کلاسیک", "آجر بهمنی")
    markup.row("چهار پر", "آجر تخت")
    markup.row("آجر آنتیک", "طرح بتن")
    markup.row("ترمو فوم", "سنگ آنتیک")
    markup.row("لوزی")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "🧱 دیوارپوش فومی 👇", reply_markup=markup)


# ===== دکمه استعلام موجودی =====
def inquiry_button(product_name):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "📋 استعلام موجودی",
        callback_data=f"inquiry_{product_name}"
    ))
    return markup


# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📢 عضویت در کانال", "✅ عضو شدم")
    bot.send_message(message.chat.id, "برای ورود باید عضو کانال باشی 👇", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "📢 عضویت در کانال")
def join_channel(message):
    bot.send_message(message.chat.id, CHANNEL)


@bot.message_handler(func=lambda m: m.text == "✅ عضو شدم")
def enter_shop(message):
    if not is_member(message.from_user.id):
        bot.send_message(message.chat.id, "❌ هنوز عضو کانال نشدی!\nاول عضو بشو بعد دوباره امتحان کن 👇\n" + CHANNEL)
        return
    show_main_menu(message)


# ===== PRODUCTS =====
@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def products(message):
    show_products_menu(message)


@bot.message_handler(func=lambda m: m.text == "🧱 دیوارپوش فومی پشت چسبدار")
def foam_menu(message):
    show_foam_menu(message)


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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("آجر کلاسیک"))
        else:
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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("آجر بهمنی"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== چهار پر =====
@bot.message_handler(func=lambda m: m.text == "چهار پر")
def char_par(message):
    caption = "🧱 چهار پر\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIE12ohbjPXVgq00sQyRmqP618FXNk_AAI4Dmsb2rYQUavcHjeNytujAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE2GohbjPpEWTqtwhooUpDgzPkFsnqAAI5Dmsb2rYQUSsxNF1dCwABPgEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIE2WohbjM3-2B-YXpcKXKBK_bjc0JaAAI6Dmsb2rYQUYUMpuTFEvRoAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE2mohbjOdXPwwNa4WlvY1vIE1NJKGAAI7Dmsb2rYQUXsEsikrPYLHAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE22ohbjOm0jqjcrVBgW-DF2ZDrnhZAAI8Dmsb2rYQUfiCNAqyGTnXAQADAgADbQADOwQ",
        "AgACAgQAAxkBAAIE3GohbjP5tFkQLkUyz9zJyJLqpTRGAAI9Dmsb2rYQUSCBBvqqjwbxAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE3WohbjNexPlsJYGEum3XwKpgBbjHAAI-Dmsb2rYQUQJuPEPZqvO7AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE3mohbjMRR-cWeDGq-qkXc2YK_eL5AAI_Dmsb2rYQUXpWFeitNxkCAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE32ohbjO-yMM9dTglXWI1Ket1cuKWAAJADmsb2rYQUZttRzKqpvjNAQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("چهار پر"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== آجر تخت =====
@bot.message_handler(func=lambda m: m.text == "آجر تخت")
def ajor_takht(message):
    caption = "🧱 آجر تخت\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIE6mohcmfBazcg3607q5tDjoQBQA7bAAJHDmsb2rYQUWoXapgZoYFOAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE6Wohcmf6m5NheC1ysuOUAQFsf0b7AAJGDmsb2rYQUUwTNsuafSkiAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE62ohcmcxkjELMomCp-49EnXNnWXnAAJIDmsb2rYQUU9Y_pn_tOnWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE7GohcmdsGOhN2XVtdK2RmzgCbHgLAAJJDmsb2rYQUcyN1hfeZycUAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE7WohcmcElA9lRYV-F-GLwaXdmtdHAAJKDmsb2rYQUZB4ctjJjGQ4AQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("آجر تخت"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== آجر آنتیک =====
@bot.message_handler(func=lambda m: m.text == "آجر آنتیک")
def ajor_antique(message):
    caption = "🧱 آجر آنتیک\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIE9GohcozW62nAdfU50ISIwFDIhOgoAAJMDmsb2rYQUd_QFAQ0m02YAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE82ohcoyUuHUz8EpDNgLkG9za2hzJAAJLDmsb2rYQUQQ8rv-QD-G-AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE9Wohcoynx5pInTxsA-IRtjmN4LMRAAJNDmsb2rYQUaKqqTyXXgABcAEAAwIAA3gAAzsE",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("آجر آنتیک"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== طرح بتن =====
@bot.message_handler(func=lambda m: m.text == "طرح بتن")
def beton(message):
    caption = "🧱 طرح بتن\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIE-Wohcr38QB-sokNFECGLL0V9YYU3AAJODmsb2rYQUciRAYQ9fyMlAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE-mohcr2hqn5VUMPnqdGHxIPtIfJNAAJPDmsb2rYQUYbN9GKJo3vSAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE-2ohcr3mw-ptAAG8mMHSm9O-Z1lfNgACUA5rG9q2EFGJeDty70dZYwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIE_Gohcr3bkC0LhWMYqnHWJn2AI0WDAAJRDmsb2rYQUYAs3r_C9qpFAQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("طرح بتن"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== ترمو فوم =====
@bot.message_handler(func=lambda m: m.text == "ترمو فوم")
def termo_foam(message):
    caption = "🧱 ترمو فوم\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIFC2ohcv7ZtloacYVD-RqX9Dk7UrI_AAJTDmsb2rYQUdmvAmXlKX3zAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFCmohcv7KLHbOMuYS8lYNo7oQ-jGkAAJSDmsb2rYQUUaOrajgklhBAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDGohcv5LwEGDjziFtSdquJHvaSK4AAJUDmsb2rYQUfbPZscKxRA1AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDWohcv7WvBk3vAh0yjjrzSy41QpjAAJVDmsb2rYQUYDKAhh3WZS4AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDmohcv7Ic7cR1Fza_e1jJjXQLqioAAJWDmsb2rYQUVG-Uo8eL2WfAQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("ترمو فوم"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== سنگ آنتیک =====
@bot.message_handler(func=lambda m: m.text == "سنگ آنتیک")
def sang_antique(message):
    caption = "🧱 سنگ آنتیک\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIFFWohcxc5c2heSPLil6zSpH19VDZdAAJYDmsb2rYQUXuJ2MTE0HZAAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFFGohcxfqL3fTHqI2bDYmF2o6RMiRAAJXDmsb2rYQUXOLl--qclFWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFFmohcxcMaH4s7Hd00NVxghTZfE-XAAJZDmsb2rYQUb-9o7DzKrSTAQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("سنگ آنتیک"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== لوزی =====
@bot.message_handler(func=lambda m: m.text == "لوزی")
def lozi(message):
    caption = "🧱 لوزی\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان"
    file_ids = [
        "AgACAgQAAxkBAAIFHWohczGfsBtYh8wEZuGGheVB7lrwAAJaDmsb2rYQUXFk75-0ZeN5AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFHmohczEcFp9rzQMBunZ2bC5Czn6TAAJbDmsb2rYQUS9mimGJDu97AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFH2ohczGEVGW0zpYm_0xkgrM-wBlCAAJcDmsb2rYQUdlwf7banIKYAQADAgADeAADOwQ",
    ]
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("لوزی"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== FOAM ROLL =====
@bot.message_handler(func=lambda m: m.text == "🏠 دیوارپوش فومی رولی")
def foam_roll(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "🏠 دیوارپوش فومی رولی\nبرای اطلاعات بیشتر با پشتیبانی تماس بگیر.\n" + ADMIN_SUPPORT, reply_markup=markup)


# ===== TERMO =====
@bot.message_handler(func=lambda m: m.text == "🪵 ترمووال")
def termo_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("PVC 20cm", "MDF 50cm")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "ترمووال 👇", reply_markup=markup)


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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("ترمووال PVC 20cm"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("ترمووال MDF 50cm"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== FLOOR =====
@bot.message_handler(func=lambda m: m.text == "⬜ کفپوش")
def floor_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("طرح سنگ", "طرح پارکت")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "کفپوش 👇", reply_markup=markup)


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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("کفپوش طرح سنگ"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


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
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(message.chat.id, fid, caption=caption, reply_markup=inquiry_button("کفپوش طرح پارکت"))
        else:
            bot.send_photo(message.chat.id, fid, caption=caption)


# ===== استعلام موجودی =====
@bot.callback_query_handler(func=lambda call: call.data.startswith("inquiry_"))
def handle_inquiry(call):
    product = call.data.replace("inquiry_", "")
    user_inquiry[call.from_user.id] = {"product": product, "step": "color"}
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"📋 استعلام موجودی *{product}*\n\nچه رنگی مد نظر داری؟", parse_mode="Markdown")


@bot.message_handler(func=lambda m: m.from_user.id in user_inquiry and user_inquiry[m.from_user.id].get("step") == "color")
def get_color(message):
    user_inquiry[message.from_user.id]["color"] = message.text
    user_inquiry[message.from_user.id]["step"] = "count"
    bot.send_message(message.chat.id, "چه تعداد/متراژی نیاز داری؟")


@bot.message_handler(func=lambda m: m.from_user.id in user_inquiry and user_inquiry[m.from_user.id].get("step") == "count")
def get_count(message):
    data = user_inquiry[message.from_user.id]
    data["count"] = message.text
    product = data["product"]
    color = data["color"]
    count = data["count"]
    username = f"@{message.from_user.username}" if message.from_user.username else f"کاربر {message.from_user.id}"

    # ارسال به ادمین
    admin_text = (
        f"📋 *استعلام موجودی جدید*\n\n"
        f"🏷 محصول: {product}\n"
        f"🎨 رنگ: {color}\n"
        f"📦 تعداد: {count}\n"
        f"👤 از: {username}"
    )
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✅ موجود است", callback_data=f"available_{message.from_user.id}"),
        types.InlineKeyboardButton("❌ ناموجود است", callback_data=f"unavailable_{message.from_user.id}")
    )
    bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown", reply_markup=markup)

    # پاسخ به مشتری
    bot.send_message(message.chat.id, "✅ درخواست استعلام شما ثبت شد!\nبه زودی پاسخ دریافت میکنی.")
    del user_inquiry[message.from_user.id]


# ===== پاسخ ادمین به استعلام =====
@bot.callback_query_handler(func=lambda call: call.data.startswith("available_") or call.data.startswith("unavailable_"))
def handle_admin_response(call):
    user_id = int(call.data.split("_")[1])
    if call.data.startswith("available_"):
        bot.send_message(user_id, "✅ محصول مورد نظر شما *موجود* است!\nبرای ثبت سفارش با پشتیبانی تماس بگیرید:\n" + ADMIN_SUPPORT, parse_mode="Markdown")
        bot.answer_callback_query(call.id, "پاسخ موجود ارسال شد ✅")
    else:
        bot.send_message(user_id, "❌ متأسفانه محصول مورد نظر شما در حال حاضر *ناموجود* است.\nبرای اطلاعات بیشتر با پشتیبانی تماس بگیرید:\n" + ADMIN_SUPPORT, parse_mode="Markdown")
        bot.answer_callback_query(call.id, "پاسخ ناموجود ارسال شد ❌")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)


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


@bot.message_handler(func=lambda m: m.text == "💬 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id, ADMIN_SUPPORT)


@bot.message_handler(func=lambda m: m.text == "🌐 مشاهده سایت")
def site(message):
    bot.send_message(message.chat.id, "https://vestadeccor.com")


@bot.message_handler(func=lambda m: m.text == "💰 لیست قیمت")
def price_list(message):
    bot.send_message(message.chat.id,
        "💰 لیست قیمت محصولات:\n\n"
        "🧱 دیوارپوش فومی — تایلی ۳۸۰ تومان\n"
        "🪵 ترمووال PVC 20cm — ۶۲۰ تومان\n"
        "🪵 ترمووال MDF 50cm — تماس بگیرید\n"
        "⬜ کفپوش طرح سنگ — ورقی ۴۴۰ تومان\n"
        "⬜ کفپوش طرح پارکت — کارتنی ۳.۹۶۰ تومان\n\n"
        "📞 09120646909\n📞 09370072236")


@bot.message_handler(func=lambda m: m.text == "🛒 ثبت سفارش")
def order(message):
    bot.send_message(message.chat.id, "🛒 برای ثبت سفارش با پشتیبانی در ارتباط باش:\n" + ADMIN_SUPPORT)


bot.infinity_polling()
ENDOFFILE
echo "Done"

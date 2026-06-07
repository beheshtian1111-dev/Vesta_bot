import telebot
from telebot import types
import threading
from flask import Flask

TOKEN = "8521280831:AAGnbbW-ikeJPb8338w8cDO4SgSksS2TmzY"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def health():
    return 'OK'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask, daemon=True).start()

CHANNEL = "https://t.me/Diivarpoosh"
CHANNEL_ID = "@Diivarpoosh"
ADMIN_SUPPORT = "@botSupport_vesta"
ADMIN_ID = 7333037232
ADMIN_IDS = [7333037232]
WHATSAPP = "https://wa.me/989120646909"
INSTAGRAM = "https://www.instagram.com/divar.posh?igsh=b2ZlbmkycGU3M2Rj&utm_source=qr"


def is_member(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ["member", "administrator", "creator"]
    except:
        return False


@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    if message.from_user.id in ADMIN_IDS:
        file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, f"FILE ID:\n\n`{file_id}`", parse_mode="Markdown")



def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🛍 محصولات", "💬 پشتیبانی")
    markup.row("📞 تماس با ما", "📱 واتساپ")
    markup.row("📸 اینستاگرام", "🌐 سایت")
    bot.send_message(message.chat.id, "🏠 منوی اصلی 👇", reply_markup=markup)


def show_main_menu_by_id(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🛍 محصولات", "💬 پشتیبانی")
    markup.row("📞 تماس با ما", "📱 واتساپ")
    markup.row("📸 اینستاگرام", "🌐 سایت")
    bot.send_message(chat_id, "🏠 منوی اصلی 👇", reply_markup=markup)


def show_products_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🧱 دیوارپوش فومی پشت چسبدار")
    markup.row("🏠 دیوارپوش فومی رولی")
    markup.row("🪵 ترمووال")
    markup.row("⬜ کفپوش")
    markup.row("📐 قرنیز")
    markup.row("🖼 ابزار قاب بندی")
    markup.row("🪨 لمسه پشت چسبدار")
    markup.row("🔙 بازگشت")
    bot.send_message(message.chat.id, "دسته‌بندی محصولات 👇", reply_markup=markup)


def show_foam_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🧱 آجر کلاسیک", "🧱 آجر بهمنی")
    markup.row("🔶 چهار پر", "🟫 آجر تخت")
    markup.row("🏛 آجر آنتیک", "🩶 طرح بتن")
    markup.row("🌿 ترمو فوم", "🪨 سنگ آنتیک")
    markup.row("💠 لوزی", "🎋 بامبو")
    markup.row("💎 کریستال", "⬛ مربع")
    markup.row("✨ هشت پر")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "🧱 دیوارپوش فومی 👇", reply_markup=markup)



def inquiry_button(product_name):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📋 استعلام موجودی", callback_data=f"inquiry_{product_name}"),
        types.InlineKeyboardButton("🛒 ثبت سفارش", callback_data=f"order_{product_name}")
    )
    return markup


@bot.callback_query_handler(func=lambda call: call.data.startswith("inquiry_"))
def handle_inquiry(call):
    product = call.data.replace("inquiry_", "")
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_to_main"))
    bot.send_message(
        "📋 *استعلام موجودی — " + product + "*\n\nبرای دریافت اطلاعات موجودی این محصول\nبه پشتیبانی پیام بدید:\n\n👤 " + ADMIN_SUPPORT,
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
def handle_order(call):
    product = call.data.replace("order_", "")
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_to_main"))
    text = "🛒 *ثبت سفارش — " + product + "*\n\nبرای ثبت سفارش این محصول\nبه پشتیبانی پیام بدید:\n\n👤 " + ADMIN_SUPPORT
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main_callback(call):
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    show_main_menu_by_id(call.message.chat.id)


# ===== START =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📢 عضویت در کانال", "✅ عضو شدم")
    bot.send_message(
        message.chat.id,
        "✨ *به وستا دکور خوش اومدی!*\n\n"
        "🏠 ما در وستا دکور بهترین محصولات دیوارپوش، کفپوش و دکوراسیون رو با کیفیت بالا و قیمت مناسب ارائه میدیم.\n\n"
        "🎨 از طرح‌های متنوع آجر، بتن، چوب و سنگ گرفته تا ترمووال و کفپوش — همه چیز در یک جا!\n\n"
        "📲 برای ورود به فروشگاه، اول باید عضو کانال ما بشی 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.message_handler(func=lambda m: m.text == "📢 عضویت در کانال")
def join_channel(message):
    bot.send_message(message.chat.id, CHANNEL)


@bot.message_handler(func=lambda m: m.text == "✅ عضو شدم")
def enter_shop(message):
    if not is_member(message.from_user.id):
        bot.send_message(message.chat.id, "❌ هنوز عضو کانال نشدی!\nاول عضو بشو:\n" + CHANNEL)
        return
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def products(message):
    show_products_menu(message)


@bot.message_handler(func=lambda m: m.text == "🧱 دیوارپوش فومی پشت چسبدار")
def foam_menu(message):
    show_foam_menu(message)


@bot.message_handler(func=lambda m: m.text == "🧱 آجر کلاسیک")
def ajor_classic(message):
    send_photos(message.chat.id, [
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
    ], "🧱 آجر کلاسیک\n📐 ابعاد: ۷۰ × ۷۷ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "آجر کلاسیک")


@bot.message_handler(func=lambda m: m.text == "🧱 آجر بهمنی")
def ajor_bahmani(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIB7mogUUx8tn_vBScy801IodcVMyeNAAKXDmsbM2wBUc-E1tThaYSoAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB72ogUUznNmsQDeWJKon1jjEWIjO0AAKYDmsbM2wBUW9LGrPNzPeWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8GogUUz5lVyAN4vR6BAiEiaMFOxRAAKZDmsbM2wBUa07ZTpGZxC8AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8WogUUxqhowl0jkNRxfe3P4sY5tbAAKaDmsbM2wBUUK0Zs-bq6tLAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB8mogUUy0d-nhaXsc5gl6QcqUwp7lAAKbDmsbM2wBUTVCMbmdDSBMAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB82ogUUyy7CBivNp8gKmw7KExntVlAAKcDmsbM2wBUUqGz8i-PzuWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9GogUUxoekNmDTpL07BGMHcGCmmGAAKdDmsbM2wBUTve2EbWu3-2AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9WogUUxWYEPOMk0EoolZen5yez61AAKeDmsbM2wBUc2Tv5uQnSYUAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIB9mogUUwUtyRaIm0thnAqI2V-1ksgAAKfDmsbM2wBURRQeAiiSA-hAQADAgADeAADOwQ",
    ], "🧱 آجر بهمنی\n📐 ابعاد: ۷۰ × ۷۷ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "آجر بهمنی")


@bot.message_handler(func=lambda m: m.text == "🔶 چهار پر")
def char_par(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIE12ohbjPXVgq00sQyRmqP618FXNk_AAI4Dmsb2rYQUavcHjeNytujAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE2GohbjPpEWTqtwhooUpDgzPkFsnqAAI5Dmsb2rYQUSsxNF1dCwABPgEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIE2WohbjM3-2B-YXpcKXKBK_bjc0JaAAI6Dmsb2rYQUYUMpuTFEvRoAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE2mohbjOdXPwwNa4WlvY1vIE1NJKGAAI7Dmsb2rYQUXsEsikrPYLHAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE22ohbjOm0jqjcrVBgW-DF2ZDrnhZAAI8Dmsb2rYQUfiCNAqyGTnXAQADAgADbQADOwQ",
        "AgACAgQAAxkBAAIE3GohbjP5tFkQLkUyz9zJyJLqpTRGAAI9Dmsb2rYQUSCBBvqqjwbxAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE3WohbjNexPlsJYGEum3XwKpgBbjHAAI-Dmsb2rYQUQJuPEPZqvO7AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE3mohbjMRR-cWeDGq-qkXc2YK_eL5AAI_Dmsb2rYQUXpWFeitNxkCAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE32ohbjO-yMM9dTglXWI1Ket1cuKWAAJADmsb2rYQUZttRzKqpvjNAQADAgADeAADOwQ",
    ], "🔶 چهار پر\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "چهار پر")


@bot.message_handler(func=lambda m: m.text == "🟫 آجر تخت")
def ajor_takht(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIE6mohcmfBazcg3607q5tDjoQBQA7bAAJHDmsb2rYQUWoXapgZoYFOAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE6Wohcmf6m5NheC1ysuOUAQFsf0b7AAJGDmsb2rYQUUwTNsuafSkiAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE62ohcmcxkjELMomCp-49EnXNnWXnAAJIDmsb2rYQUU9Y_pn_tOnWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE7GohcmdsGOhN2XVtdK2RmzgCbHgLAAJJDmsb2rYQUcyN1hfeZycUAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE7WohcmcElA9lRYV-F-GLwaXdmtdHAAJKDmsb2rYQUZB4ctjJjGQ4AQADAgADeAADOwQ",
    ], "🟫 آجر تخت\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "آجر تخت")


@bot.message_handler(func=lambda m: m.text == "🏛 آجر آنتیک")
def ajor_antique(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIE9GohcozW62nAdfU50ISIwFDIhOgoAAJMDmsb2rYQUd_QFAQ0m02YAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE82ohcoyUuHUz8EpDNgLkG9za2hzJAAJLDmsb2rYQUQQ8rv-QD-G-AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE9Wohcoynx5pInTxsA-IRtjmN4LMRAAJNDmsb2rYQUaKqqTyXXgABcAEAAwIAA3gAAzsE",
    ], "🏛 آجر آنتیک\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "آجر آنتیک")


@bot.message_handler(func=lambda m: m.text == "🩶 طرح بتن")
def beton(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIE-Wohcr38QB-sokNFECGLL0V9YYU3AAJODmsb2rYQUciRAYQ9fyMlAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE-mohcr2hqn5VUMPnqdGHxIPtIfJNAAJPDmsb2rYQUYbN9GKJo3vSAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIE-2ohcr3mw-ptAAG8mMHSm9O-Z1lfNgACUA5rG9q2EFGJeDty70dZYwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIE_Gohcr3bkC0LhWMYqnHWJn2AI0WDAAJRDmsb2rYQUYAs3r_C9qpFAQADAgADeAADOwQ",
    ], "🩶 طرح بتن\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "طرح بتن")


@bot.message_handler(func=lambda m: m.text == "🌿 ترمو فوم")
def termo_foam(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIFC2ohcv7ZtloacYVD-RqX9Dk7UrI_AAJTDmsb2rYQUdmvAmXlKX3zAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFCmohcv7KLHbOMuYS8lYNo7oQ-jGkAAJSDmsb2rYQUUaOrajgklhBAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDGohcv5LwEGDjziFtSdquJHvaSK4AAJUDmsb2rYQUfbPZscKxRA1AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDWohcv7WvBk3vAh0yjjrzSy41QpjAAJVDmsb2rYQUYDKAhh3WZS4AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFDmohcv7Ic7cR1Fza_e1jJjXQLqioAAJWDmsb2rYQUVG-Uo8eL2WfAQADAgADeAADOwQ",
    ], "🌿 ترمو فوم\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "ترمو فوم")


@bot.message_handler(func=lambda m: m.text == "🪨 سنگ آنتیک")
def sang_antique(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIFFWohcxc5c2heSPLil6zSpH19VDZdAAJYDmsb2rYQUXuJ2MTE0HZAAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFFGohcxfqL3fTHqI2bDYmF2o6RMiRAAJXDmsb2rYQUXOLl--qclFWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFFmohcxcMaH4s7Hd00NVxghTZfE-XAAJZDmsb2rYQUb-9o7DzKrSTAQADAgADeAADOwQ",
    ], "🪨 سنگ آنتیک\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "سنگ آنتیک")


@bot.message_handler(func=lambda m: m.text == "💠 لوزی")
def lozi(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIFHWohczGfsBtYh8wEZuGGheVB7lrwAAJaDmsb2rYQUXFk75-0ZeN5AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFHmohczEcFp9rzQMBunZ2bC5Czn6TAAJbDmsb2rYQUS9mimGJDu97AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFH2ohczGEVGW0zpYm_0xkgrM-wBlCAAJcDmsb2rYQUdlwf7banIKYAQADAgADeAADOwQ",
    ], "💠 لوزی\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "لوزی")


@bot.message_handler(func=lambda m: m.text == "🎋 بامبو")
def bambo(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIHnmokG6bvEFshOt9TRuWREPBZ_0kkAAKDD2sb4dwgUepBTwraWApDAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHn2okG6ZDK16l-aglNabXL0JA2lW3AAKED2sb4dwgUU2YQ51nOBL0AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHoGokG6bgWKS5f1CTfU_flOmkwgZ1AAKFD2sb4dwgUSjFuQJ_jlkkAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHoWokG6YpY0IXBPSzkP45hdIQmK1bAAKGD2sb4dwgUQLzm6xVItRUAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHomokG6Yj-hPpqlCT9h25Gk5nENbyAAKHD2sb4dwgUQABwh1xbFyaIgEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIHo2okG6YBIVL3jzyqwk-mSXDghZzCAAKID2sb4dwgUW5jFj0OgLidAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHpGokG6aZtwwdkcXQ4LKN-rsAAQJ7iAACiQ9rG-HcIFEhPoXebtYTLwEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIHpWokG6Zu3ussijLqAQEIcSUDtlJzAAKKD2sb4dwgUVoK5m_sH4WYAQADAgADeAADOwQ",
    ], "🎋 بامبو\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "بامبو")


@bot.message_handler(func=lambda m: m.text == "💎 کریستال")
def crystal(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIHtWokHIEXBn6UJ99um1tlOihW5gOAAAKMD2sb4dwgUbn9uyrxxQ1XAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHtmokHIGOpjWJ01MxZvAbeSO1Aza_AAKND2sb4dwgUc9LR8BU10E-AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHt2okHIH5Z9IROPqIB6gHROxBRUhkAAKOD2sb4dwgUcx4bCXVZTGOAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHuGokHIEcAXth9Uy-a3zXPZZv-1-wAAKPD2sb4dwgUfpMRh6hpd-JAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHuWokHIFW1pexP6qebxYSFb0UT4V0AAKQD2sb4dwgUSnYsVyf8-PgAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHumokHIE-2Lhvj8sEzwABdCTkKc8vagACkQ9rG-HcIFGqmNBU7_f6iQEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIHu2okHIG4Oci-ho78civDRR5NekuBAAKSD2sb4dwgUStBzF7lusAnAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHvGokHIFVTiEwX2jptFCkRYVwuLOHAAKTD2sb4dwgUfsKcxVMMVLnAQADAgADeAADOwQ",
    ], "💎 کریستال\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "کریستال")


@bot.message_handler(func=lambda m: m.text == "⬛ مربع")
def moraba(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIHxmokHOXUxZmZ26ZE6gQmP5EQjhDEAAKVD2sb4dwgUdRybeQgkwABXAEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIHxWokHOVnHckEteDE39GP8SHaiIrBAAKUD2sb4dwgUTWGemVpep8VAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHx2okHOV-xIw5P_keyn-SzHUYiLWmAAKWD2sb4dwgUWtnTv7a09klAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHyGokHOWGdOV4F4dDSz1BeQzannfRAAKXD2sb4dwgUUqnIn6Bi8FHAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHyWokHOWGBTopcPwrXP0r_J9uFRwvAAKYD2sb4dwgUTwb95cvBuw-AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHymokHOWe5zYp92xOJyxThTaBsTSdAAKZD2sb4dwgUcmMUppD350BAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHy2okHOUub8kKKfWCnKGYL_Y3N5HpAAKaD2sb4dwgUUyddTOHF5glAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHzGokHOXgL4huP-l6ixE9BzbJPGQ8AAKbD2sb4dwgUf4eXiazL8fLAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHzWokHOWe-cgDtZeXnCfHhHIXuncsAAKcD2sb4dwgUTPtyjecrrMYAQADAgADeAADOwQ",
    ], "⬛ مربع\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "مربع")


@bot.message_handler(func=lambda m: m.text == "✨ هشت پر")
def hasht_par(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIH2mokHRu3A5cJXDa0FRzOJ_LEN3MKAAKeD2sb4dwgUfefoa_aLzGGAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH2WokHRtHqBke_lWL3AK3WlMxGN5rAAKdD2sb4dwgUTlKRG_OKvuQAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH22okHRvUu7HDSzE7mL-tXk_WtU6YAAKfD2sb4dwgUQiFZUABuTR5AQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH3GokHRvXTmvXIkgVW-eRBZnmT0cHAAKgD2sb4dwgUXoI5WppekmEAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH3WokHRt5n_ZEFH7mZ92ygPxLHhKrAAKhD2sb4dwgUaxfkWDoaXTDAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH3mokHRsvcbGoywtlhcWuAg6CzO5AAAKiD2sb4dwgUTFLoe5cwA5mAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH32okHRv9NId50NHkgsfWcmk0AAF55gACow9rG-HcIFH_TVDE3Ibj6wEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIH4GokHRuBnkkp3T6rwlxxmeTsLPHuAAKkD2sb4dwgUR4DZr95b5XuAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH4WokHRtVcjZ3Yk9GG70ORf7F_X7xAAKlD2sb4dwgUej8pouYdUUvAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH4mokHRtR2doYsc3invsDh_0wRh7hAAKmD2sb4dwgUfhYyCOzuvHWAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIH42okHRy29B_TaALWORgSkTlhChBxAAKnD2sb4dwgUTC0lzrR2KrrAQADAgADeAADOwQ",
    ], "✨ هشت پر\n📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت تایلی: ۳۸۰ تومان", "هشت پر")


@bot.message_handler(func=lambda m: m.text == "🏠 دیوارپوش فومی رولی")
def foam_roll(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "🏠 دیوارپوش فومی رولی\nبرای اطلاعات بیشتر با پشتیبانی تماس بگیر.\n" + ADMIN_SUPPORT, reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "🪵 ترمووال")
def termo_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("PVC 20cm", "MDF 50cm")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "ترمووال 👇", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "PVC 20cm")
def pvc20(message):
    send_photos(message.chat.id, [
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
    ], "🪵 ترمووال PVC 20cm\n📐 ابعاد: عرض ۲۰ سانت × ارتفاع ۲۸۰ سانت\n💰 قیمت: ۶۲۰ تومان", "ترمووال PVC 20cm")


@bot.message_handler(func=lambda m: m.text == "MDF 50cm")
def mdf50(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIC5mogaFTSW8UK2EeWpwnBRAHCtgGmAAKTD2sbhIIAAVGN7kmS6YnH1AEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC52ogaFSp0tqhCHjgpwu9c8BCeWs3AAKUD2sbhIIAAVFrD_Aw4IWuCwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6GogaFQRJ8miFGUORpD2yoojuM6fAAKVD2sbhIIAAVH_hX7rRtb1vwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6WogaFTSpHQ4nIn3Gx6ICBrtwpinAAKWD2sbhIIAAVH9ecXCJ_v3NQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC62ogaFRIbLPlGLfMqI9dsZg3bT5JAAKYD2sbhIIAAVELSOIgyPgkhgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC6mogaFQetEXGT-vDNAqwXi_5SSd4AAKXD2sbhIIAAVHKUmUEdxBwXAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC7GogaFR-jtE6yFCnq5pNIEzOaOsTAAKZD2sbhIIAAVFjiDY-LokqaQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC7WogaFQ8XyIodtWoOBmJcBlI-bK1AAKaD2sbhIIAAVF2XX-dWGMzBQEAAwIAA3kAAzsE",
    ], "🪵 ترمووال MDF 50cm\n📐 ابعاد: عرض ۵۰ سانت × ارتفاع ۲۸۰ سانت\n💰 قیمت پنلی: ۱.۶۰۰ تومان", "ترمووال MDF 50cm")


@bot.message_handler(func=lambda m: m.text == "⬜ کفپوش")
def floor_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("طرح سنگ", "طرح پارکت")
    markup.row("🔙 بازگشت به محصولات")
    bot.send_message(message.chat.id, "کفپوش 👇", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "طرح سنگ")
def stone_floor(message):
    send_photos(message.chat.id, [
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
    ], "⬜ کفپوش طرح سنگ\n📐 ابعاد: ۶۰ × ۶۰ سانتی‌متر\n💰 قیمت ورقی: ۴۴۰ تومان", "کفپوش طرح سنگ")


@bot.message_handler(func=lambda m: m.text == "طرح پارکت")
def parquet_floor(message):
    send_photos(message.chat.id, [
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
    ], "⬜ کفپوش طرح پارکت\n📏 متراژ هر کارتن: ۳ متر و ۶۰ سانتی‌متر\n💰 قیمت هر کارتن: ۳.۹۶۰ تومان", "کفپوش طرح پارکت")


@bot.message_handler(func=lambda m: m.text == "📐 قرنیز")
def qarniz(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIFI2ohejFtz_Nu3D6Qfn9vMetG6RCtAAJzDmsb2rYQUYfb1SEAAXJe6QEAAwIAA3gAAzsE",
        "AgACAgQAAxkBAAIFJGohejGh8aizhTs8OW3gWbvhYcfgAAJ0Dmsb2rYQUcyiWWKbn2QPAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFJWohejG2CxLJziQxyeUH0Qs4sv-jAAJ1Dmsb2rYQUY9DuNezvIurAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFJmohejECZlkm0c8KHb062BuE1K3WAAJ2Dmsb2rYQUQiSaku__kxoAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFJ2ohejEMUcWhX2W3_0zuE4xfze3XAAJ3Dmsb2rYQUUcG6jMT3NdEAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFKGohejHroYKiOiD7gok4sIzzS8ZdAAJ4Dmsb2rYQUdB71qyEVqsVAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIFKWohejFKGMbubnLi2m0gyWF2dqPiAAJ5Dmsb2rYQUaj1DcqRb94cAQADAgADeAADOwQ",
    ], "📐 قرنیز\n📐 ابعاد: ۹ سانت × ۲۸۰ سانت\n💰 قیمت: ۲۶۰ تومان", "قرنیز")


@bot.message_handler(func=lambda m: m.text == "🖼 ابزار قاب بندی")
def abzar_ghabbandi(message):
    file_ids = [
        "AgACAgQAAxkBAAIGeGoikNm8HnELftYwnuNqN2lgKq1HAAJWD2sbqCgZUVyYMkRApZ0QAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIGeWoikNldvo-pPBcIRLfkflr3VrlcAAJXD2sbqCgZUUILtVr6oeVLAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIGemoikNk_FgnoU8yVmcB4taew1M6QAAJYD2sbqCgZUe0UmolqO7WGAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIGe2oikNlAnQqIp1K2M1AwgBrOGHqhAAJZD2sbqCgZUc8slXbEF70wAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIGfGoikNk849zVNNhAHPnIC7iXkmgXAAJaD2sbqCgZUViZqGBWmMTCAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIGfWoikNkFKIha_5YyPxRyrykbQBx-AAJbD2sbqCgZUeMwjhdhjozRAQADAgADeQADOwQ",
    ]
    for fid in file_ids:
        bot.send_photo(message.chat.id, fid)


@bot.message_handler(func=lambda m: m.text == "🪨 لمسه پشت چسبدار")
def lamse(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIHc2oj844GN6B6Mqxqgm4cni_6aEJkAAJND2sb4dwgUSU0Ps9m3sstAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHdGoj8471VZUlm-1TgMNPIZ8so24GAAJOD2sb4dwgUX9jY97EOpbPAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHdWoj845x0VJPWS0EyMlx_LG_UnhOAAJPD2sb4dwgUWvnkm4Zr63fAQADAgADeAADOwQ",
        "AgACAgQAAxkBAAIHdmoj847rK2beFTtxfMFPuRRVPl4oAAJQD2sb4dwgUYRE8nr0EuvWAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHd2oj8473ASYFF_DUyYAuF6FHqO0CAAJRD2sb4dwgUdm6wzENmA_rAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHeGoj846u-2IF5g65LOvu4fbGuIfRAAJSD2sb4dwgUYgw8NepI5HmAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHeWoj8455m-xXCw0f8r16wapRHCIJAAJTD2sb4dwgUb-J1bv3zRN_AQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHemoj844kzHIIYM5wRQ_UXGwzydAfAAJUD2sb4dwgUcVP99BfX_5GAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHe2oj847_Um4TQDFUu7GkbcVsRVgBAAJVD2sb4dwgUUoS8cDyWJypAQADAgADeQADOwQ",
        "AgACAgQAAxkBAAIHfGoj847Pj4Viez9Cm-P_Isu8UqCOAAJWD2sb4dwgUf_VRcbUSyYMAQADAgADeQADOwQ",
    ], "🪨 لمسه پشت چسبدار\n📐 ابعاد: ۴۷ × ۴۷ سانتی‌متر\n💰 قیمت تایلی: ۲۷۰ تومان", "لمسه پشت چسبدار")


# ===== BACK =====
@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت")
def back(message):
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به منو")
def back_to_menu(message):
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به محصولات")
def back_products(message):
    show_products_menu(message)


@bot.message_handler(func=lambda m: m.text == "📞 تماس با ما")
def contact(message):
    bot.send_message(message.chat.id, "📞 09120646909\n📞 09370072236")


@bot.message_handler(func=lambda m: m.text == "💬 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id, ADMIN_SUPPORT)


@bot.message_handler(func=lambda m: m.text == "🌐 سایت")
def site(message):
    bot.send_message(message.chat.id, "🌐 https://vestadeccor.com")


@bot.message_handler(func=lambda m: m.text == "📱 واتساپ")
def whatsapp(message):
    bot.send_message(message.chat.id, f"📱 واتساپ:\n{WHATSAPP}")


@bot.message_handler(func=lambda m: m.text == "📸 اینستاگرام")
def instagram(message):
    bot.send_message(message.chat.id, f"📸 اینستاگرام:\n{INSTAGRAM}")


bot.remove_webhook()
bot.infinity_polling()

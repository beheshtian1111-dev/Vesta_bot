import telebot
from telebot import types
import threading
from flask import Flask

# ─── بات تلگرام ────────────────────────────────────────────
TOKEN = "8521280831:AAESd0hqkaoHazBV-9LC85z-69hxKDMBxDs"
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
    return None


def send_photos(chat_id, file_ids, caption, product_name):
    full_caption = caption + "\n\n📋 استعلام موجودی و ثبت سفارش:\n👤 " + ADMIN_SUPPORT
    for fid in file_ids:
        bot.send_photo(chat_id, fid, caption=full_caption)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔙 بازگشت به محصولات", "🏠 منوی اصلی")
    bot.send_message(chat_id, "👆 عکس‌های محصول", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    if message.from_user.id in ADMIN_IDS:
        file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, "FILE ID:\n\n`" + file_id + "`", parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data.startswith("inq_"))
def handle_inquiry(call):
    product = call.data[4:]
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_main"))
    bot.send_message(
        call.message.chat.id,
        "📋 *استعلام موجودی — " + product + "*\n\nبرای دریافت اطلاعات موجودی\nبه پشتیبانی پیام بدید:\n\n👤 " + ADMIN_SUPPORT,
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("ord_"))
def handle_order(call):
    product = call.data[4:]
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_main"))
    bot.send_message(
        call.message.chat.id,
        "🛒 *ثبت سفارش — " + product + "*\n\nبرای ثبت سفارش\nبه پشتیبانی پیام بدید:\n\n👤 " + ADMIN_SUPPORT,
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "back_main")
def back_main(call):
    try:
        bot.answer_callback_query(call.id)
    except:
        pass
    show_main_menu_by_id(call.message.chat.id)


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
    ], "🧱 آجر کلاسیک\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "آجر کلاسیک")


@bot.message_handler(func=lambda m: m.text == "🧱 آجر بهمنی")
def ajor_bahmani(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIClGogZNLqxczQGaMEi2nCpDl5roqkAAKbD2sbhIIAAVFaKNzsMiD3mwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIClWogZNIK0dQ3XQVP-PjJe8SdsFJbAAKcD2sbhIIAAVGVfSJIpQ2bUAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIClmogZNJJ_m7e8xTW0Z_jVRG5IrLuAAKdD2sbhIIAAVEzP5vlTlQNfAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICl2ogZNJFVWaJzYvfm-4IHmn0MmpNAAKeD2sbhIIAAVFlRi4xJ4VGnwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICmGogZNIfIBVCjRqRwgD6MiDUqUqAAAKfD2sbhIIAAVFkWi5dEXarVAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICmWogZNJuMW3mCiFb8tTPuM5MTCm_AAKgD2sbhIIAAVFZV4Gh8zF_HQEAAwIAA3kAAzsE",
    ], "🧱 آجر بهمنی\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "آجر بهمنی")


@bot.message_handler(func=lambda m: m.text == "🔶 چهار پر")
def chahar_par(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAICoGogZQ0KtWz_8hzTl_bVm2wkyL--AAKpD2sbhIIAAVGuBeSEcNkxiQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICo2ogZQ1BEyHuD1LCGONrAFU2IfroAAKqD2sbhIIAAVGJvWt_Y_FI4AEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIComogZQ0pVUPAeVb8z_pqJLkf4WY2AAKrD2sbhIIAAVFqxFrHH-8dswEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICpGogZQ3MNkgE9RqajaBBSGdh2Y0SAAKsD2sbhIIAAVFC0ADELFBfSwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICpWogZQ2e1oVZbGZm_HV_QLSZrLaeAAKtD2sbhIIAAVFdNMD27JTFdQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICpmogZQ2g1JnnK4QZp5Q1Y7LFPVvdAAKuD2sbhIIAAVFJzx6pBdKmpAEAAwIAA3kAAzsE",
    ], "🔶 چهار پر\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "چهار پر")


@bot.message_handler(func=lambda m: m.text == "🟫 آجر تخت")
def ajor_takht(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAICvWogZcWxHxHlE-P8bibyGWsGKkiOAAK-D2sbhIIAAVFJ2MnBK9C1TgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICvmogZcU4A6fQHFJ2SLlYqPxeXTAbAAK_D2sbhIIAAVE7vGEDn-k5HQEAAWIAAO8AAzsE",
        "AgACAgQAAxkBAAICv2ogZcVKYWJqN_nGLGNNRi5UbMvNAALAD2sbhIIAAVGEpLCz06TgVwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICwGogZcV8n5Wb5sGHs6heFhYt7FHeAALBD2sbhIIAAVGzBJQJg2o8TQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICwWogZcVaU4bHf9gPCcfz4V5TFTp1AALCD2sbhIIAAVHlj9iqBOmSqQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAICwmogZcVLx4o7YxiXpLbXjGBbBJJDAALDD2sbhIIAAVGCjJi9RkgLuQEAAwIAA3kAAzsE",
    ], "🟫 آجر تخت\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "آجر تخت")


@bot.message_handler(func=lambda m: m.text == "🏛 آجر آنتیک")
def ajor_antik(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIC2GogZmqwv8xERpXq2YcnqByaHkfXAALhD2sbhIIAAVFhE8tRBxjZKgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC2WogZmq6_EjK1xCrSREwO3JUjIVjAALiD2sbhIIAAVHR9B2g9Bpl2gEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC2mogZmqFJIiEpR2DpTN5txrGJ8PXAALL2sbhIIAAVFo3S5sCnMBbAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC22ogZmqu0GHfB9-nwGR6fJwUE03WAALN2sbhIIAAVELkbcMLJzhlgEAAwIAA3kAAzsE",
    ], "🏛 آجر آنتیک\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "آجر آنتیک")


@bot.message_handler(func=lambda m: m.text == "🩶 طرح بتن")
def beton(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIC5GogZpkCfqz0-fC_c4e2rY1f7y8XAALPD2sbhIIAAVFkMuUcGNRkBwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC5WogZpmpq62UOBVL6f1W0YVJ9V1BAALDQ2sbhIIAAVGlPM60H8k0dgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIC5mogZpkSz1v2aAXBH_GsKq-6XaxfAALRD2sbhIIAAVEmzaP5ykz3ngEAAwIAA3kAAzsE",
    ], "🩶 طرح بتن\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "طرح بتن")


@bot.message_handler(func=lambda m: m.text == "🌿 ترمو فوم")
def termo_foam(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDCGogZ4Y0O4DJthLm_V5mXXsZZijWAAIID2sbhIIAAVExTfxGisPmfgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDCWogZ4bnc-J0G6HHHtSHCHXQwLXJAAIJD2sbhIIAAVHbX_FiZAd5oAEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDCmogZ4bxH0_k6TK5MKUMWsxbGbLyAAIKD2sbhIIAAVH0uysPl8SFBwEAAwIAA3kAAzsE",
    ], "🌿 ترمو فوم\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "ترمو فوم")


@bot.message_handler(func=lambda m: m.text == "🪨 سنگ آنتیک")
def sang_antik(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDFGogZ8mKAZ2_6HB6MCpzYdVLkPD2AAIUD2sbhIIAAVHfuN1LlH5uagEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDFWogZ8kH5tHfVbXH5zz9Qkqge0PZAAIVD2sbhIIAAVGpvb8n2n6DOwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDFmogZ8lhAQ5SrkZh6m7oNxJqCe1LAAIWD2sbhIIAAVF5Caf79-NiKAEAAwIAA3kAAzsE",
    ], "🪨 سنگ آنتیک\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "سنگ آنتیک")


@bot.message_handler(func=lambda m: m.text == "💠 لوزی")
def lozi(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDImogaBz5vCfaJYqp5VjuJhHIkFi7AAIiD2sbhIIAAVE5iHVWxkpYpwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDI2ogaBze1w0hLfj7oIPHHBLdv7mFAAIjD2sbhIIAAVFiHNi0JCfVfgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDJGogaBysGYaJi73s4sn3MHoeTzFDAAIkD2sbhIIAAVHlJHGsI8KG_gEAAwIAA3kAAzsE",
    ], "💠 لوزی\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "لوزی")


@bot.message_handler(func=lambda m: m.text == "🎋 بامبو")
def bambo(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDMmogaEDPblNUagv8KTjTBIAfH9j0AAIyD2sbhIIAAVGjHaexcDrJVgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDM2ogaEARcYKFsXsslkLXzGPjcGMsAAIzD2sbhIIAAVH2VNrX1NhWGwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDNGogaEBkDAJf-MnbHUiCX3g9RfN_AAI0D2sbhIIAAVHQ72PEuJQVAAE7BA",
    ], "🎋 بامبو\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "بامبو")


@bot.message_handler(func=lambda m: m.text == "💎 کریستال")
def crystal(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDQGogaIGVSiJMRkVMGXnWmNzjuXN5AAJfD2sbhIIAAVGxKiPSB_MYjwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDQWogaIEaKc7K8NjJPpYdoiUE7R75AAJgD2sbhIIAAVEaRnb28r0_fgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDQmogaIGmxm6m5F4a1XDhFJMNcT_1AAJhD2sbhIIAAVGR1H6U9tpYPQEAAwIAA3kAAzsE",
    ], "💎 کریستال\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "کریستال")


@bot.message_handler(func=lambda m: m.text == "⬛ مربع")
def morabba(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDTmogaLBl-6rwR0BIMxjqRVLFbf8NAAJ8D2sbhIIAAVE0-XijW3q-TgEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDT2ogaLBiVe3gvMkJ_N1yKrNT7bBjAAJ9D2sbhIIAAVGE3tOv4ZikBQEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDUGogaLDJKIfR1T45QMl71IKOyEMCAAJ-D2sbhIIAAVFv01y7MZAA_AEAAwIAA3kAAzsE",
    ], "⬛ مربع\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "مربع")


@bot.message_handler(func=lambda m: m.text == "✨ هشت پر")
def hasht_par(message):
    send_photos(message.chat.id, [
        "AgACAgQAAxkBAAIDXGogaOLaJBG1hpEq6FZtEL4mMlaeAAKID2sbhIIAAVEDUXy13yl0TQEAAWIAAO8AAzsE",
        "AgACAgQAAxkBAAIDXWogaOKFOVhflMFrVdEh4LZ1WtUiAAKJD2sbhIIAAVHQiZ8w2bwUuwEAAwIAA3kAAzsE",
        "AgACAgQAAxkBAAIDXmogaOJf5C5M3LiGVBlLGJBaLWUMAAKKD2sbhIIAAVEZQ1hRgFBj4AEAAwIAA3kAAzsE",
    ], "✨ هشت پر\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n💰 قیمت تایلی: ۱۸۰ تومان", "هشت پر")


@bot.message_handler(func=lambda m: m.text == "🏠 دیوارپوش فومی رولی")
def roli(message):
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
def abzar(message):
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


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت")
def back(message):
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🏠 منوی اصلی")
def main_menu(message):
    show_main_menu(message)


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به محصولات")
def back_products(message):
    show_products_menu(message)


@bot.message_handler(func=lambda m: m.text == "💬 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id, "💬 پشتیبانی:\n" + ADMIN_SUPPORT)


@bot.message_handler(func=lambda m: m.text == "📞 تماس با ما")
def contact(message):
    bot.send_message(message.chat.id,
        "📞 *تماس با ما*\n\n"
        "📱 09120646909\n"
        "📱 09370072236\n"
        "☎️ 02155278487\n"
        "☎️ 02155278488\n\n"
        "📍 تهران، بزرگراه آیت الله سعیدی، چهاردانگه، خیابان کریمی، میدان شهدا، وستا دکور",
        parse_mode="Markdown"
    )


@bot.message_handler(func=lambda m: m.text == "📱 واتساپ")
def whatsapp(message):
    bot.send_message(message.chat.id, "📱 واتساپ:\n" + WHATSAPP)


@bot.message_handler(func=lambda m: m.text == "📸 اینستاگرام")
def instagram(message):
    bot.send_message(message.chat.id, "📸 اینستاگرام:\n" + INSTAGRAM)


@bot.message_handler(func=lambda m: m.text == "🌐 سایت")
def site(message):
    bot.send_message(message.chat.id, "🌐 https://vestadeccor.com")


# ─── بات بله ───────────────────────────────────────────────
import telebot as bale_lib
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

BALE_TOKEN   = "560660765:yORGFoVOwJN8qEk2iToVDdSRSXwEzOoO4FE"
BALE_MOBILE1 = "09120646909"
BALE_MOBILE2 = "09370072236"
BALE_LINE1   = "02155278487"
BALE_LINE2   = "02155278488"
BALE_ADDRESS = "تهران، بزرگراه آیت الله سعیدی، چهاردانگه، خیابان کریمی، میدان شهدا، وستا دکور"
BALE_IG      = "https://www.instagram.com/divar.posh?igsh=b2ZlbmkycGU3M2Rj&utm_source=qr"
BALE_WA      = "https://wa.me/989120646909"
BALE_SUPPORT = "@divar_posh"

bale_bot = bale_lib.TeleBot(BALE_TOKEN, custom_url="https://tapi.bale.ai/bot")

BALE_PRODUCTS = {
    "🧱 دیوارپوش فومی": f"🏷 *دیوارپوش فومی سه‌بعدی*\n\n✅ سبک، عایق صدا و حرارت\n📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
    "🏠 دیوارپوش فومی رولی": f"🏷 *دیوارپوش فومی رولی*\n\n✅ نرم و انعطاف‌پذیر\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
    "🪵 ترمووال": f"🏷 *پانل ترمووال*\n\n✅ عایق حرارتی و صوتی\n✅ مناسب دیوار و سقف\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
    "⬜ کفپوش": f"🏷 *کفپوش لمینت و وینیل*\n\n✅ طرح‌های متنوع\n✅ مقاوم در برابر رطوبت\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
    "📐 قرنیز": f"🏷 *قرنیز PVC و MDF*\n\n✅ رنگ‌بندی متنوع\n✅ مقاوم در برابر رطوبت\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
    "🪨 ماربل شیت": f"🏷 *ماربل شیت*\n\n✅ ظاهر لوکس، وزن سبک\n✅ مناسب آشپزخانه و سرویس\n\n📞 سفارش:\n{BALE_MOBILE1}\n{BALE_SUPPORT}",
}

def bale_main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(KeyboardButton("🛍 محصولات"), KeyboardButton("📍 آدرس و اطلاعات"))
    kb.add(KeyboardButton("🤝 پشتیبانی"), KeyboardButton("📸 اینستاگرام"))
    return kb

def bale_products_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for name in BALE_PRODUCTS:
        kb.add(KeyboardButton(name))
    kb.add(KeyboardButton("🔙 بازگشت به منوی اصلی"))
    return kb

@bale_bot.message_handler(commands=["start"])
def bale_start(message):
    name = message.from_user.first_name or "کاربر عزیز"
    bale_bot.send_message(message.chat.id,
        f"سلام {name} عزیز 👋\n\nبه بات رسمی 🏠 *وستا دکور* خوش آمدید!\n\n"
        "• دیوارپوش فومی و ترمووال\n• کفپوش لمینت و وینیل\n• قرنیز، ماربل شیت\n\n"
        "از منوی پایین انتخاب کنید 👇",
        parse_mode="Markdown", reply_markup=bale_main_kb())

@bale_bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def bale_products(message):
    bale_bot.send_message(message.chat.id, "📦 *محصولات وستا دکور*\n\nیک محصول انتخاب کنید:",
        parse_mode="Markdown", reply_markup=bale_products_kb())

@bale_bot.message_handler(func=lambda m: m.text in BALE_PRODUCTS)
def bale_product_detail(message):
    bale_bot.send_message(message.chat.id, BALE_PRODUCTS[message.text],
        parse_mode="Markdown", reply_markup=bale_products_kb())

@bale_bot.message_handler(func=lambda m: m.text == "📍 آدرس و اطلاعات")
def bale_address(message):
    bale_bot.send_message(message.chat.id,
        f"🏪 *وستا دکور*\n\n📍 *آدرس:*\n{BALE_ADDRESS}\n\n"
        f"☎️ *تلفن ثابت:*\n{BALE_LINE1}\n{BALE_LINE2}\n\n"
        f"📱 *موبایل:*\n{BALE_MOBILE1}\n{BALE_MOBILE2}\n\n"
        "🕐 *ساعت کاری:*\nشنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب",
        parse_mode="Markdown", reply_markup=bale_main_kb())

@bale_bot.message_handler(func=lambda m: m.text == "🤝 پشتیبانی")
def bale_support(message):
    bale_bot.send_message(message.chat.id,
        f"👨‍💼 *پشتیبانی وستا دکور*\n\n💬 بله: {BALE_SUPPORT}\n"
        f"📱 واتساپ: {BALE_WA}\n📞 تماس: {BALE_MOBILE1}\n\n"
        "⏰ شنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب",
        parse_mode="Markdown", reply_markup=bale_main_kb())

@bale_bot.message_handler(func=lambda m: m.text == "📸 اینستاگرام")
def bale_instagram(message):
    bale_bot.send_message(message.chat.id,
        f"📸 *اینستاگرام وستا دکور*\n\n{BALE_IG}\n\nآخرین طرح‌ها رو دنبال کنید! 🎨",
        parse_mode="Markdown", reply_markup=bale_main_kb())

@bale_bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به منوی اصلی")
def bale_back(message):
    bale_bot.send_message(message.chat.id, "منوی اصلی 🏠", reply_markup=bale_main_kb())

@bale_bot.message_handler(func=lambda m: True)
def bale_fallback(message):
    bale_bot.send_message(message.chat.id, "لطفاً از منوی پایین انتخاب کنید 👇",
        reply_markup=bale_main_kb())

def run_bale_bot():
    print("✅ بات وستا دکور (بله) شروع به کار کرد...")
    bale_bot.infinity_polling()

threading.Thread(target=run_bale_bot, daemon=True).start()

# ─── اجرای بات تلگرام ──────────────────────────────────────
bot.remove_webhook()
bot.infinity_polling()

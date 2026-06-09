import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ─── تنظیمات ───────────────────────────────────────────────
TOKEN        = "560660765:yORGFoVOwJN8qEk2iToVDdSRSXwEzOoO4FE"
MOBILE1      = "09120646909"
MOBILE2      = "09370072236"
LANDLINE1    = "02155278487"
LANDLINE2    = "02155278488"
ADDRESS      = "تهران، بزرگراه آیت الله سعیدی، چهاردانگه، خیابان کریمی، میدان شهدا، وستا دکور"
INSTAGRAM    = "https://www.instagram.com/divar.posh?igsh=b2ZlbmkycGU3M2Rj&utm_source=qr"
WHATSAPP     = "https://wa.me/989120646909"
SUPPORT_BALE = "@divar_posh"

# ─── ساخت بات با endpoint بله ──────────────────────────────
bot = telebot.TeleBot(
    TOKEN,
    custom_url="https://tapi.bale.ai/bot"
)

# ─── محصولات ────────────────────────────────────────────────
PRODUCTS = {
    "🟫 دیوارپوش فومی": {
        "desc": (
            "🏷 *دیوارپوش فومی سه‌بعدی*\n\n"
            "✅ سبک، عایق صدا و حرارت\n"
            "📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n"
            "🎨 طرح‌های متنوع\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": "photos/wall_foam.jpg",
    },
    "🟦 دیوارپوش فومی رولی": {
        "desc": (
            "🏷 *دیوارپوش فومی رولی*\n\n"
            "✅ نرم، انعطاف‌پذیر، مناسب فضاهای بزرگ\n"
            "📏 عرض استاندارد رول\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": None,
    },
    "🧱 ترموال": {
        "desc": (
            "🏷 *پانل ترموال*\n\n"
            "✅ عایق حرارتی و صوتی عالی\n"
            "✅ مناسب دیوار و سقف\n"
            "✅ اجرای سریع و آسان\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": "photos/thermowall.jpg",
    },
    "🪵 کفپوش": {
        "desc": (
            "🏷 *کفپوش لمینت و وینیل*\n\n"
            "✅ طرح‌های متنوع چوب و سنگ\n"
            "✅ مقاوم در برابر رطوبت\n"
            "✅ نصب آسان\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": "photos/flooring.jpg",
    },
    "📏 قرنیز": {
        "desc": (
            "🏷 *قرنیز PVC و MDF*\n\n"
            "✅ رنگ‌بندی متنوع\n"
            "✅ مقاوم در برابر رطوبت\n"
            "✅ ظاهر شیک و مرتب\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": "photos/qarniz.jpg",
    },
    "🪨 ماربل شیت": {
        "desc": (
            "🏷 *ماربل شیت (سنگ مصنوعی ورقه‌ای)*\n\n"
            "✅ ظاهر لوکس، وزن سبک\n"
            "✅ مقاوم و بادوام\n"
            "✅ مناسب آشپزخانه و سرویس بهداشتی\n\n"
            f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
        ),
        "photo": None,
    },
}

# ─── کیبوردها ───────────────────────────────────────────────
def main_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("🛍 محصولات"),
        KeyboardButton("📍 آدرس و اطلاعات"),
        KeyboardButton("🤝 پشتیبانی"),
        KeyboardButton("📸 اینستاگرام"),
    )
    return kb

def products_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for name in PRODUCTS:
        kb.add(KeyboardButton(name))
    kb.add(KeyboardButton("🔙 بازگشت به منوی اصلی"))
    return kb

# ─── هندلرها ────────────────────────────────────────────────

@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name or "کاربر عزیز"
    text = (
        f"سلام {name} عزیز 👋\n\n"
        "به بات رسمی 🏠 *وستا دکور* خوش آمدید!\n\n"
        "ما ارائه‌دهنده انواع پوشش‌های دیوار و کف:\n"
        "• دیوارپوش فومی و ترموال\n"
        "• کفپوش لمینت و وینیل\n"
        "• قرنیز، ماربل شیت و بیشتر...\n\n"
        "از منوی پایین گزینه مورد نظر را انتخاب کنید 👇"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def show_products(message):
    bot.send_message(
        message.chat.id,
        "📦 *محصولات وستا دکور*\n\nیک محصول انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=products_keyboard()
    )


@bot.message_handler(func=lambda m: m.text in PRODUCTS)
def show_product_detail(message):
    product = PRODUCTS[message.text]
    caption = product["desc"]

    if product["photo"]:
        try:
            with open(product["photo"], "rb") as photo:
                bot.send_photo(
                    message.chat.id, photo,
                    caption=caption,
                    parse_mode="Markdown",
                    reply_markup=products_keyboard()
                )
            return
        except FileNotFoundError:
            pass

    bot.send_message(message.chat.id, caption, parse_mode="Markdown", reply_markup=products_keyboard())


@bot.message_handler(func=lambda m: m.text == "📍 آدرس و اطلاعات")
def show_address(message):
    text = (
        "🏪 *وستا دکور*\n\n"
        f"📍 *آدرس:*\n{ADDRESS}\n\n"
        f"☎️ *تلفن ثابت:*\n{LANDLINE1}\n{LANDLINE2}\n\n"
        f"📱 *موبایل:*\n{MOBILE1}\n{MOBILE2}\n\n"
        "🕐 *ساعت کاری:*\nشنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "🤝 پشتیبانی")
def show_support(message):
    text = (
        "👨‍💼 *پشتیبانی وستا دکور*\n\n"
        f"💬 بله: {SUPPORT_BALE}\n"
        f"📱 واتساپ: {WHATSAPP}\n"
        f"📞 تماس: {MOBILE1}\n\n"
        "⏰ *پاسخگویی:*\nشنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "📸 اینستاگرام")
def show_instagram(message):
    text = (
        "📸 *اینستاگرام وستا دکور*\n\n"
        f"{INSTAGRAM}\n\n"
        "آخرین طرح‌ها و پروژه‌های اجرا شده را دنبال کنید! 🎨"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به منوی اصلی")
def go_back(message):
    bot.send_message(message.chat.id, "منوی اصلی 🏠", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(
        message.chat.id,
        "لطفاً از منوی پایین گزینه‌ای انتخاب کنید 👇",
        reply_markup=main_keyboard()
    )


# ─── اجرا ───────────────────────────────────────────────────
if __name__ == "__main__":
    print("✅ بات وستا دکور (بله) شروع به کار کرد...")
    bot.infinity_polling()

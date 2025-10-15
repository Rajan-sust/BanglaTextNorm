"""
__author__ = "Rajan Saha Raju"
__email__ = "rajan-ictc@sust.edu"
"""

from utility import (
    bn_num_to_words
)


def convert_bndigits_to_endigits(bangla_digits: str) -> str:
    mapping = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
    return bangla_digits.translate(mapping)


def process_abbreviation(abbreviation: str, tokens: list) -> str:
    """
    Process the given abbreviation and return its expanded form.
    """
    abbreviations_dict = {
        "ড.": "ডক্টর",
        "মোঃ": "মোহাম্মদ",
        "মো.": "মোহাম্মদ",
        "ডাঃ": "ডাক্তার",
        "ডা.": "ডাক্তার",
        "মোছাঃ": "মোছাম্মত",
        "খ্রিঃপূর্ব": "খ্রিষ্টপূর্বাব্দ",
        "খ্রিঃপূঃ": "খ্রিষ্টপূর্বাব্দ",
        "খ্রীঃপূঃ": "খ্রিষ্টপূর্বাব্দ",
        "খ্রি.পূ.": "খ্রিষ্টপূর্বাব্দ",
        "খ্রী.পূ.": "খ্রিষ্টপূর্বাব্দ",
        "খ্রিঃ": "খ্রিষ্টাব্দ",
        "খ্রীঃ": "খ্রিষ্টাব্দ",
        "খ্রী.": "খ্রিষ্টাব্দ",
        "খ্রি.": "খ্রিষ্টাব্দ",
        "৳": "টাকা",
        "মি.মি.": "মিলিমিটার",
        "মি. মি.": "মিলিমিটার",
        "সে.মি.": "সেন্টিমিটার",
        "সে. মি.": "সেন্টিমিটার",
        "সেমি.": "সেন্টিমিটার",
        "সেমি": "সেন্টিমিটার",
        "কি.মি.": "কিলোমিটার",
        "কি. মি.": "কিলোমিটার",
        "কিমি": "কিলোমিটার",
        "ব.মি.": "বর্গমিটার",
        "ব. মি.": "বর্গমিটার",
        "ঘ.মি.": "ঘনমিটার",
        "ঘ. মি.": "ঘনমিটার",
        "কে.জি.": "কিলোগ্রাম",
        "মি.লি.": "মিলিলিটার",
        "মি. লি.": "মিলিলিটার",
        "লি.": "লিটার",
        "মি.গ্রা.": "মিলিগ্রাম",
        "মি. গ্রা.": "মিলিগ্রাম",
        "মি.গ্রাম": "মিলিগ্রাম",
        "লে:": "লেফট্যানেন্ট",
        "লে.": "লেফট্যানেন্ট",
        "লেঃ": "লেফট্যানেন্ট",
        "লেফ.": "লেফট্যানেন্ট",
        "সা.": "সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম",
        "সাঃ": "সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম",
        "সা:": "সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম",
        "রা.": "রাদিআল্লাহু আনহু",
        "রা:": "রাদিআল্লাহু আনহু",
        "রাঃ": "রাদিআল্লাহু আনহু",
        "কি.ও.ঘ.": "কিলোওয়াট-ঘণ্টা"
    }
    
    if abbreviation in abbreviations_dict:
        return abbreviations_dict[abbreviation]
    
    contextual_abbreviations = {
        "মি.": [
            {
                "context": ["দৈর্ঘ্য", "দীর্ঘ", "প্রস্থ", "প্রশস্ত", "বিস্তার", "চওড়া", "উচ্চতা", "উঁচু", "গভীরতা", "পুরুত্ব", "লম্বা", "বাহু", "ক্ষেত্র", "বর্গ", "দূরত্ব", "ভূমি", "পরিসীমা", "জমি", "সীমানা", "আকার"],
                "replace": " মিটার "
            },
            {
                "context": ["সময়", "রাত", "ঘণ্টা", "অপেক্ষা", "সময়", "সময়কাল", "সময়কাল", "সময়সীমা", "সময়সীমা", "সময়কালীন", "মুহূর্ত", "ক্ষণ", "পর্যন্ত"],
                "replace": " মিনিট "
            },
            {
                "context": ["মহাশয়", "সাহেব", "স্যার", "শ্রী", "জনাব", "স্যার", "মহোদয়", "মহাশয়া", "শ্রীমান", "শ্রীমতি", "মহাশয়"],
                "replace": " মিস্টার "
            }
        ],
        "সে.": [
            {
                "context": ["সময়, ব্যাপ্তিকাল, ঘণ্টা, রাত, অপেক্ষা, সময়, সময়কাল, সময়সীমা, সময়কালীন, মুহূর্ত, ক্ষণ, পর্যন্ত"],
                "replace": " সেকেন্ড  "
            },
            {
                "context": ["ডিগ্রী", "তাপমাত্রা", "তাপ", "ঠান্ডা", "গরম", "আবহাওয়া", "জলবায়ু", "আবহাওয়া", "জলবায়ু"],
                "replace": " সেলসিয়াস  "
            }
        ],
        "N" : [
            {
                "context": ["নিউটন", "বল", "শক্তি", "ফোর্স", "মেকানিক্স", "গতি", "গতিবিদ্যা"],
                "replace": " নিউটন "
            },
            {
                "context": ["উত্তর", "দিক", "দিশা", "নির্দেশ", "অবস্থান", "স্থান"],
                "replace": " নর্থ "
            },
            {
                "context": ["চিহ্ন", "প্রতীক", "সংকেত"],
                "replace": " এন "
            }
        ]
    }
    # Implementation coorected: 15 Oct 2025
    if abbreviation in contextual_abbreviations:
        for obj in contextual_abbreviations[abbreviation]:
            if any(word in obj["context"] for word in tokens):
                return obj["replace"]
    print("No context match found for abbreviation:", abbreviation)
    return abbreviation


def process_ordinal(number):
    """
    Process the given ordinal number and return its word form.
    """
    ordinals_dict = {
    "১ ম": "প্রথম",
    "১ম": "প্রথম",
    "২ য়": "দ্বিতীয়",
    "২য়": "দ্বিতীয়",
    "৩ য়": "তৃতীয়",
    "৩য়": "তৃতীয়",
    "৪ র্থ": "চতুর্থ",
    "৪র্থ": "চতুর্থ",
    "৫ ম": "পঞ্চম",
    "৫ম": "পঞ্চম",
    "৬ ষ্ঠ": "ষষ্ঠ",
    "৬ষ্ঠ": "ষষ্ঠ",
    "৭ ম": "সপ্তম",
    "৭ম": "সপ্তম",
    "৮ ম": "অষ্টম",
    "৮ম": "অষ্টম",
    "৯ ম": "নবম",
    "৯ম": "নবম",
    "১০ ম": "দশম",
    "১০ম": "দশম",
    "১১ শ": "একাদশ",
    "১১শ": "একাদশ",
    "১২ শ": "দ্বাদশ",
    "১২শ": "দ্বাদশ",
    "১৩ শ": "ত্রয়োদশ",
    "১৩শ": "ত্রয়োদশ",
    "১৪ শ": "চতুর্দশ",
    "১৪শ": "চতুর্দশ",
    "১৫ শ": "পঞ্চদশ",
    "১৫শ": "পঞ্চদশ",
    "১৬ শ": "ষোড়শ",
    "১৬শ": "ষোড়শ",
    "১৭ শ": "সপ্তদশ",
    "১৭শ": "সপ্তদশ",
    "১৮ শ": "অষ্টাদশ",
    "১৮শ": "অষ্টাদশ",
    "১৯ শ": "ঊনবিংশ",
    "১৯শ": "ঊনবিংশ",
    "২০ শ": "বিংশ",
    "২০শ": "বিংশ",
    "২১ শ": "একবিংশ",
    "২১শ": "একবিংশ"
    }

    for key in ordinals_dict:
        if key in number:
            return number.replace(key, ordinals_dict[key])
    return number

def process_acronym(acronym):
    mapping = {
        "জি-২০": "জি টুয়েন্টি",
        "জি-৭": "জি সেভেন",
        "টি-২০": "টি টুয়েন্টি",
        "4G": "ফোর  জি",
        "5G": "ফাইভ  জি",
        "Wi-Fi": "ওয়াই  ফাই",
        "WiFi": "ওয়াই  ফাই",
        "USB": "ইউএসবি",
        "CPU": "সি  পি  ইউ",
        "GPU": "জি  পি  ইউ",
        "RAM": "র‍্যাম",
        "HTTP": "এইচ  টি  টিপি",
        "HTTPS": "এইচ  টি  টিটিপিএস",
        "URL": "ইউ  আরএল",
        "WWW": "ডাব্লিউ  ডাব্লিউ  ডাব্লিউ",
        "AI": "এ  আই",
        "ML": "এম  এল",
        "IoT": "আই  ও  টি",
        "NASA": "নাসা",
        "FBI": "এফ  বি  আই",
        "CIA": "সি  আই  এ",
        "UN": "ইউ  এন",
        "EU": "ই  ইউ",
        "NATO": "ন্যাটো",
        "OPEC": "ওপেক",
        "COVID-19": "কোভিড নাইনটিন",
        "COVID19": "কোভিড নাইনটিন",
        "SARS-CoV-2": "সার্স কোভ টু",
        "SARSCoV2": "সার্স কোভ টু",
        "ওমেগা–৩": "ওমেগা থ্রি",
        "UNDP": "ইউএনডিপি",
        "UNICEF": "ইউনিসেফ",
        "WHO": "ডব্লিউএইচও",
        "IMF": "আইএমএফ",
        "WB": "ডব্লিউবি",
        "GDP": "জিডিপি",
        "GNP": "জিএনপি",
        "NGO": "এনজিও",
        "NPO": "এনপিও",
        "BGB": "বিজিবি",
        "RAB": "র‍্যাব",
        "DB": "ডিবি",
        "BSF": "বিএসএফ",
        "BSFI": "বিএসএফআই",
        "ATM": "এটিএম",
        "CD": "সিডি",
        "DVD": "ডিভিডি",
        "HIV": "এইচআইভি",
        "AIDS": "এইডস",
        "GPS": "জিপিএস",
        "HSC": "এইচএসসি",
        "SSC": "এসএসসি",
        "PSC": "পিএসসি",
        "BSC": "বিএসসি",
        "MSc": "এমএসসি",
        "PhD": "পিএইচডি",
        "USA": "ইউএসএ",
        "UK": "ইউকে",
        "UAE": "ইউএই",
        "কপ-২৮": "কপ টুয়েন্টি এইট",
        "Gen-Z": "জেন-জি",
        "Zen-G": "জেন-জি"
    }
    return mapping.get(acronym, acronym)


def int_to_date_words(num: int, num_dict: dict) -> str:
    if num == 0:
        return ""

    if num < 100:
        return num_dict.get(num, "")

    if num < 1000:
        return num_dict.get(num // 100, "") + "শ " + int_to_date_words(num % 100, num_dict)

    if num % 1000 == 0:
        return num_dict.get(num // 1000, "") + " হাজার"

    if num % 1000 < 100:
        return num_dict.get(num // 1000, "") + " হাজার " + int_to_date_words(num % 100, num_dict)

    if num % 1000 >= 100:
        return num_dict.get(num // 100, "") + "শ " + int_to_date_words(num % 100, num_dict)

    return ""

    
def process_date(date_str):
    """
    Process the given date string and return it in a standardized format.
    """
    # This is a placeholder function. Implement date processing logic as needed.
    date_mappings = {
        "১লা ": "পহেলা ",
        "১ লা ": "পহেলা ",
        "২রা ": "দোসরা ",
        "২ রা ": "দোসরা ",
        "৩রা ": "তেসরা ",
        "৩ রা ": "তেসরা ",
        "৪ঠা ": "চৌঠা ",
        "৪ ঠা ": "চৌঠা ",
        "৫ই ": "পাঁচই ",
        "৫ ই ": "পাঁচই ",
        "৬ই ": "ছয়ই ",
        "৬ ই ": "ছয়ই ",
        "৭ই ": "সাতই ",
        "৭ ই ": "সাতই ",
        "৮ই ": "আটই ",
        "৮ ই ": "আটই ",
        "৯ই ": "নয়ই ",
        "৯ ই ": "নয়ই ",
        "১০ই ": "দশই ",
        "১০ ই ": "দশই ",
        "১১ই ": "এগারোই ",
        "১১ ই ": "এগারোই ",
        "১২ই ": "বারোই ",
        "১২ ই ": "বারোই ",
        "১৩ই ": "তেরোই ",
        "১৩ ই ": "তেরোই ",
        "১৪ই ": "চৌদ্দই ",
        "১৪ ই ": "চৌদ্দই ",
        "১৫ই ": "পনেরোই ",
        "১৫ ই ": "পনেরোই ",
        "১৬ই ": "ষোলোই ",
        "১৬ ই ": "ষোলোই ",
        "১৭ই ": "সতেরোই ",
        "১৭ ই ": "সতেরোই ",
        "১৮ই ": "আঠারোই ",
        "১৮ ই ": "আঠারোই ",
        "১৯শে ": "উনিশে ",
        "১৯ শে ": "উনিশে ",
        "২০শে ": "বিশে ",
        "২০ শে ": "বিশে ",
        "২১শে ": "একুশে ",
        "২১ শে ": "একুশে ",
        "২২শে ": "বাইশে ",
        "২২ শে ": "বাইশে ",
        "২৩শে ": "তেইশে ",
        "২৩ শে ": "তেইশে ",
        "২৪শে ": "চব্বিশে ",
        "২৪ শে ": "চব্বিশে ",
        "২৫শে ": "পঁচিশে ",
        "২৫ শে ": "পঁচিশে ",
        "২৬শে ": "ছাব্বিশে ",
        "২৬ শে ": "ছাব্বিশে ",
        "২৭শে ": "সাতাশে ",
        "২৭ শে ": "সাতাশে ",
        "২৮শে ": "আটাশে ",
        "২৮ শে ": "আটাশে ",
        "২৯শে ": "ঊনত্রিশে ",
        "২৯ শে ": "ঊনত্রিশে ",
        "৩০শে ": "ত্রিশে ",
        "৩০ শে ": "ত্রিশে ",
        "৩১শে ": "একত্রিশে ",
        "৩১ শে ": "একত্রিশে "
    }

    for key in date_mappings:
        if key in date_str:
            return date_str.replace(key, date_mappings[key])
    
    # now solve case like ১৯৭১ -> উনিশো একাত্তর
    bn_year_to_en_year = convert_bndigits_to_endigits(date_str)
    en_num = int(bn_year_to_en_year) if bn_year_to_en_year.isdigit() else None
    date_in_words = int_to_date_words(en_num, bn_num_to_words) if en_num else date_str
    return date_in_words if date_in_words else date_str


def int_to_bn_words(num: int, bn_num_to_words: dict) -> str:
    if num == 0:
        return ""

    if num < 100:
        return bn_num_to_words.get(num, "")

    if num < 1000:
        return bn_num_to_words.get(num // 100, "") + "শ " + int_to_bn_words(num % 100, bn_num_to_words)

    if num < 100000:
        return bn_num_to_words.get(num // 1000, "") + " হাজার " + int_to_bn_words(num % 1000, bn_num_to_words)

    if num < 10000000:
        return bn_num_to_words.get(num // 100000, "") + " লক্ষ " + int_to_bn_words(num % 100000, bn_num_to_words)

    return int_to_bn_words(num // 10000000, bn_num_to_words) + " কোটি " + int_to_bn_words(num % 10000000, bn_num_to_words)


def process_cardinal(number):
    """
    Process the given cardinal number and return its word form.
    """
    # First, convert Bangla digits to English digits if necessary
    # remove commas from the number
    temp = number
    print("Processing cardinal number:", number)
    number = number.replace(",", "").strip()
    print("After removing commas:", number)

    number = convert_bndigits_to_endigits(number)
    en_num = int(number) if number.isdigit() else None
    if en_num == 0:
        return "শূন্য"
    
    num_in_words = int_to_bn_words(en_num, bn_num_to_words) if en_num else temp
    

    return num_in_words


def process_decimal(number):
    """
    Process the given decimal number and return its word form.
    """
    # First, convert Bangla digits to English digits if necessary
    number = number.replace(",", "").strip()
    number = convert_bndigits_to_endigits(number)

    if '.' in number:
        integer_part, fractional_part = number.split('.')
        en_integer_part = int(integer_part) if integer_part.isdigit() else None
        if en_integer_part == 0:
            integer_in_words = "শূন্য"
        else:
            integer_in_words = int_to_bn_words(en_integer_part, bn_num_to_words) if en_integer_part is not None else integer_part

        fractional_in_words = ' '.join([bn_num_to_words.get(int(digit), digit) for digit in fractional_part if digit.isdigit()])

        return f"{integer_in_words} দশমিক {fractional_in_words}"
    else:
        en_num = int(number) if number.isdigit() else None
        num_in_words = int_to_bn_words(en_num, bn_num_to_words) if en_num else number
        return num_in_words

def process_symbol(symbol: str, tokens: list):
    """
    Process the given symbol and return its word form.
    """
    symbols_dict = {
        "%": "শতাংশ",
        "&": "এন্ড",
        "@": "অ্যাট",
        "#": "হ্যাশ",
        "*": "স্টার",
        "+": "প্লাস",
        "=": "সমান",
        "$": "ডলার",
        "₹": "রুপি",
        "€": "ইউরো",
        "£": "পাউন্ড",
        "°": "ডিগ্রী",
        "©": "কপিরাইট",
        "®": "রেজিস্টার্ড",
        "™": "ট্রেডমার্ক",
        "´": "মিনিট"
    }
    if symbol in symbols_dict:
        return symbols_dict[symbol]
    
    hypen = ["-", "–", "—", "―", "−"]
    if symbol in hypen:
        symbol = "-"
    
    contextual_symbols = {
        "-": [
            {
                "context": ["বছর", "অর্থবছর", "সাল", "হাজার", "লাখ", "লক্ষ", "কোটি", "টাকা", "টি", "কেজি", "জন", "পর্যন্ত", "মিটার", "ফুট", "শতাংশ", "কিলোমিটার", "দিন", "ঘণ্টা", "মিনিট", "ডিগ্রি", "মেগাওয়াট", "কিলোওয়াট", "মেগাহার্টজ", "কিলোহার্টজ", "মেগাবাইট", "কিলোবাইট", "গিগাবাইট", "টেরাবাইট", "পাউন্ড", "ডলার", "ইউরো", "রুপি"],
                "replace": " থেকে "
            }
        ],
        "/": [
            {
                "context": ["হেক্টর", "টন", "কেজি", "কিলোগ্রাম", "লিটার"],
                "replace": " প্রতি "
            }
        ],
        ":": [
            {
                "context": ["অনুপাত", "অনুপাতে"],
                "replace": " এর বিপরীতে "
            }
        ],
        "x": [
            {
                "context": ["বেশী", "কম", "বেড়েছে", "হ্রাস", "বৃদ্ধি", "কমেছে"],
                "replace": " গুণ "
            },
            {
                "context": ["আকার", "দৈর্ঘ্য", "প্রস্থ", "উচ্চতা", "গভীরতা", "পুরুত্ব", "সাইজ", "কাগজ", "পেপার", "বক্স", "বাক্স", "স্ক্রিন", "ডিসপ্লে", "টিভি", "টেলিভিশন"],
                "replace": " বাই"
            }
        ]
    }
    if symbol in contextual_symbols:
        for context in contextual_symbols[symbol]:
            if any(word in context["context"] for word in tokens):
                return context["replace"]
    return symbol

def process_money(number: str) -> str:
    """
    Process the given monetary value and return its word form.
    """
    # First, convert Bangla digits to English digits if necessary
    tk = number.replace(",", "").strip()
    tk = convert_bndigits_to_endigits(tk)

    if '.' in tk:
        money = float(tk)
        integer_part = int(money)
        fractional_part = round((money - integer_part) * 100)
        if integer_part == 0:
            integer_in_words = "শূন্য"
        else:
            integer_in_words = int_to_bn_words(integer_part, bn_num_to_words) if integer_part is not None else str(integer_part)

        return f'{integer_in_words} টাকা {bn_num_to_words.get(fractional_part, str(fractional_part))} পয়সা'
    else:
        money = int(tk) if tk.isdigit() else None
        if money == 0:
            return "শূন্য"
        return int_to_bn_words(money, bn_num_to_words) if money else number

   
if __name__ == "__main__":
    money_test_cases = ["১২৩৪.৫৬", "০.৭৫", "১০০০", "৫০০০.০০", "০", "১২৩৪৫৬৭৮৯", "১.০১"]
    for tk in money_test_cases:
        print(f"Input: {tk} -> Output: {process_money(tk)}")

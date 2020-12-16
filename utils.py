import re
from datetime import datetime, timedelta


def clean_name_url(url):
    url, _ = url.split("refid")
    permalink = url[:-1].replace("mbasic.face", "web.face")
    return f'=HYPERLINK("{permalink}", "View Profile")'


def clean_post_url(url):
    url, _ = url.split("refid")
    permalink = url[:-1].replace("m.face", "web.face")
    return f'=HYPERLINK("{permalink}", "View Post")'


def clean_title(title):
    return title.replace("(Sold)", "")


def parse_price(price):
    str_res = "".join(re.findall(r"\d+", price))
    if str_res:
        return int(str_res)
    return 0


def parse_date(date):
    today = datetime.today()
    if "hrs" in date:
        parsed_date = today
    elif "Yesterday" in date:
        parsed_date = today - timedelta(days=1)
    else:
        return date.split(" at")[0]
    return parsed_date.strftime("%B %d")


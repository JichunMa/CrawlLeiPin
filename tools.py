import re

detail_limit_number = 3


def remove_all_whitespace(source_str):
    p = re.compile('\s+')
    new_string = re.sub(p, '', source_str)
    return new_string


def clean_html(raw_html):
    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, '', raw_html)
    return clean_text


def safe_get_first_from_list(list_data, default_value=""):
    if len(list_data) > 0:
        return list_data[0]
    else:
        return default_value

# config.py

BASE_URL = "https://www.imdb.com/title/tt0471571/trivia/"
#CSS_SELECTOR = "[class^='sc-dfa2eb22-5 cpRasK']"
#CSS_SELECTOR = "[class^='div-col']"
CSS_SELECTOR = "[class^='ipc-html-content-inner-div']"

REQUIRED_KEYS = [
    "name",
    "question",
    "answer",
]

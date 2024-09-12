import api
import string
import random
import requests
import threading


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


targets = ["LH1VdSk21uq7iycquhdROQ", "96VtAp9bfBwQn73pP6TJvw", "jwWk2V6c74sVJJmI4ZkzUQ",
           "txfksbikhZ45ob8jb9OXHQ", "o0il98rsLcQPNb4tIzMV8g", "Qt7rHp3z5AIymWoHHdDilg",
           "DWI9fOQpI4TRXkYs7gxcyg", "iZ9qfxTdHictv2J01DMzwA", "tifTz0lX4aXMrkSXDbqCaQ",
           "WaFtc6yRpfqIJ1WTWqRtjg", "5XQxAW7LdakWJZwi3qYb8g", "eFn9iFj9gJRajUnFwXHwkw",
           "P6SCJ9YiAVBQOBhto4ur7g", "DzTEDVWIjrHRF8NDeApDFA", "x3GuGXiY49A63ZcD0x08Ww",
           "iQkxGo0U9CRZ0eH52FYiKQ", "0QFYlqu0foYtxwKIA7bAPQ", "foObMNCalVk67XliuCGlNQ",
           "qlukRGHxcgpr6maAW5KURQ", "msXjA7Di3Whyx7WkL4Vd9Q", "lBJaodZDgGpVjcPficOIcg",
           "1khkhhBPWbQkgxKmlORsQg", "8WMUhXNgRsPc0SIVUgbzrQ", "kgY9x9pHy2Bc9PtNwnksMw",
           "2xiV8IT9EPvF3u1dOSKmpg", "pFup2idcTqbgamTyeVnWmA", "r34Frnp1TMyaMCLCagBKDQ",
           "WnzxphsHjz2fhagEd3LsZg", "JxQnV8hYniHnV3Uhr3vakw", "UIAM8GT36KJVsdwJLeqbEw",
           "PUyYIRnd0i8qNCgKON652Q", "PheQypJKmQVsFsyN0Wqzug", "9U932pI8dnTG2MfIwrkhIg",
           "VRPcMS0rxdv1nw8F4FiaLg", "TWqUqFwB60ypQUd0Bw02Vg", "tav1Oj4Rc6SXMmwaf3VtZA",
           "nCU7XBq2R9nj5o4IHQM29A", "qdsTgU9iMJcocuZwsvGqCg", "Vk16frsrHa7iuR4jwWmq5w",
           "Y1IThNWcqa4LJyk3y5JtJw", "JWxGHyC7OtS024363OFZLA", "hpJQKNYWEfHJ5ZjFmsM1dg",
           "naxxDm232O7QQYHl691i7g", "1MOKL0lwFV5m6xm058gKyw", "jFOdSoLtar0zR9j0Jf9cGQ",
           "POEvK1prg5T1HlfznqFLhg", "wilZIV8V5fpuC6IZqaIZkA", "DToTYnLOs6811TicR65zSw",
           "r83F0f050az0ZmVu5pwzjg", "1J5cVsrzINcFPvtOEh5mOQ", "gHhOq4c2lQCx7FySC4fRJA",
           "y2BAJCbDBmlUgnQMB9n3aw", "L3Q61j0wxZncIVR9WEG9hA", "zIG3WHNN6NgsE3Ifbpu8Cg"]

def donate():
    while True:
        api.monster_sell("erI8knuTyoPt7WRRlVjIvg", targets=targets)

for i in range(6):
    thr = threading.Thread(target=donate)
    thr.start()
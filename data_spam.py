from requests import get

while True:
    a = get('https://user-verify-pearl.vercel.app/pwhls?link=Abhi data chor hai, sudhar jaa bhai, tere bhale ke liye kah rha hun')
    print(a.status_code)

from requests import get

proxies = {
    'http': 'http://gofw8axb8qtmdr:gdmfjuci61ip31n7oghrct6w1nq@proxy.quotaguard.com:9292',
    'https': 'http://gofw8axb8qtmdr:gdmfjuci61ip31n7oghrct6w1nq@proxy.quotaguard.com:9292'
}

while True:
    a = get(
        'https://user-verify-pearl.vercel.app/pwhls?link=Abhi data chor hai, sudhar jaa bhai, tere bhale ke liye kah rha hun', 
        proxies=proxies
        
        )
    
    print(a.status_code)

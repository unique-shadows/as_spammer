from requests import get

proxies = {
    'http': 'http://zhl4dg0w7a8h4s:4kgbdnzin4qb1cl86fzi82tn6olvgm@proxy.quotaguard.com:9292',
    'https': 'http://zhl4dg0w7a8h4s:4kgbdnzin4qb1cl86fzi82tn6olvgm@proxy.quotaguard.com:9292'
}

while True:
    a = get(
        'https://api.alphastudyofficial.live/alpha/pw-khazana/get/lectures?khazana_slug=11th-jee-khazana-607507&subject_slug=complete-mathematics---11th-845097&teacher_slug=complete-mathematics-by-253144&chapter_slug=62cc8cd39f43b7001293d1c0',
        proxies=proxies
        
        )
    
    print(a.status_code)

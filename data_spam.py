from requests import get

proxies = {
    'http': 'http://pz600g667zu7ad:9i21feayawlhh3rlbz6i9ea53vck79@proxy.quotaguard.com:9292',
    'https': 'http://pz600g667zu7ad:9i21feayawlhh3rlbz6i9ea53vck79@proxy.quotaguard.com:9292'
}

while True:
    a = get(
        'https://user-verify-pearl.vercel.app/pwhls?link=Abhi data chor hai, sudhar jaa bhai, tere bhale ke liye kah rha hun', 
        # proxies=proxies
        
        )
    
    print(a.status_code)

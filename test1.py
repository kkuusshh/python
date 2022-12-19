possible_domain = ['com', 'net', 'org']
uri = input('Address : ')

find_domain = uri.split('/')[2].split('.')[-1]

if find_domain in possible_domain:
    print("[  OK  ]", find_domain)
else:
    print("[ FAIL ] not found")
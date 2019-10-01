import socket

seeders = [
    'xcrcseed.mempool.pw',
    'xcrcseed1.cryptocrowd.city',
    'xcrcseed2.cryptocrowd.city',
    'xcrcseed3.cryptocrowd.city',
    'xcrcseed4.cryptocrowd.city',
    'xcrcseed5.cryptocrowd.city',
    'xcrcseed1.cryptocrowdcrypto.site',
    'xcrcseed2.cryptocrowdcrypto.site',
    'xcrcseed3.cryptocrowdcrypto.site',
    'xcrcseed4.cryptocrowdcrypto.site',
    'xcrcseed5.cryptocrowdcrypto.site'
]

for seeder in seeders:
    try:
        ais = socket.getaddrinfo(seeder, 0)
    except socket.gaierror:
        ais = []
    
    # Prevent duplicates, need to update to check
    # for ports, can have multiple nodes on 1 ip.
    addrs = []
    for a in ais:
        addr = a[4][0]
        if addrs.count(addr) == 0:
            addrs.append(addr)
    
    print(seeder + ' = ' + str(len(addrs)))

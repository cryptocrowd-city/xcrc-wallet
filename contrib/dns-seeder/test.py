import socket

seeders = [
    'xcrcseed.mempool.pw',
    'xcrcseed1.cryptocrowd.city',
    'xcrcseed2.cryptocrowd.city',
    'xcrcseed3.cryptocrowd.city',
    'xcrcseed4.cryptocrowd.city',
    'xcrcseed5.cryptocrowd.city',
    'xcrcseed1.bulwarkcrypto.site',
    'xcrcseed2.bulwarkcrypto.site',
    'xcrcseed3.bulwarkcrypto.site',
    'xcrcseed4.bulwarkcrypto.site',
    'xcrcseed5.bulwarkcrypto.site'
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

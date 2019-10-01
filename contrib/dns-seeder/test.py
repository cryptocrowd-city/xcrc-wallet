import socket

seeders = [
    'bwkseed.mempool.pw',
    'bwkseed1.cryptocrowd.city',
    'bwkseed2.cryptocrowd.city',
    'bwkseed3.cryptocrowd.city',
    'bwkseed4.cryptocrowd.city',
    'bwkseed5.cryptocrowd.city',
    'bwkseed1.bulwarkcrypto.site',
    'bwkseed2.bulwarkcrypto.site',
    'bwkseed3.bulwarkcrypto.site',
    'bwkseed4.bulwarkcrypto.site',
    'bwkseed5.bulwarkcrypto.site'
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

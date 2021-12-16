dict_hb = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111'}

f = open('input.txt')
x = f.readline()
r = ''
for i in x:
    r += dict_hb[i]
f.close()

dict_pack = []  # check ID=4

aux = r

versions_l = []


def search(string, prueba=False):
    if prueba:
        print(string)
    n = 0
    v = int(string[n:n + 3], 2)
    versions_l.append(v)
    n += 3
    type_id = int(string[n:n + 3], 2)
    n += 3
    packages = []
    if prueba:
        print('version: ', v)
        print('type: ', type_id)
    if type_id == 4:
        packet = ''
        while True:
            p = string[n:n + 5]
            packet += p[1:]
            n += 5
            if p[0] == '0':
                break
        packet = int(packet, 2)
        yet_not_read = string[n:]
        dict_pack.append((v, type_id, packet))
        return yet_not_read, packet
    else:
        length = string[n]
        n += 1
        if prueba:
            print('length ID: ', length)
        if length == '0':
            tam = 15
            length_sp = int(string[n:n + tam], 2)
            n += tam
            yet_not_read = string[n:]
            to_search = yet_not_read[:length_sp]
            while len(to_search) > 0:
                to_search, packet = search(to_search, prueba=prueba)
                packages.append(packet)
            yet_not_read = yet_not_read[length_sp:]

        else:
            tam = 11
            number_sp = int(string[n:n + tam], 2)
            n += tam
            yet_not_read = string[n:]
            for j in range(number_sp):
                yet_not_read, packet = search(yet_not_read, prueba=prueba)
                packages.append(packet)
                if prueba:
                    print('Len: ', len(yet_not_read))
    if type_id == 0:
        return yet_not_read, sum(packages)
    elif type_id == 1:
        p = 1
        for j in packages:
            p *= j
        return yet_not_read, p
    elif type_id == 2:
        return yet_not_read, min(packages)
    elif type_id == 3:
        return yet_not_read, max(packages)
    elif type_id == 5:
        if packages[0] > packages[1]:
            return yet_not_read, 1
        else:
            return yet_not_read, 0
    elif type_id == 6:
        if packages[0] < packages[1]:
            return yet_not_read, 1
        else:
            return yet_not_read, 0
    elif type_id == 7:
        if packages[0] == packages[1]:
            return yet_not_read, 1
        else:
            return yet_not_read, 0


_, result = search(aux, False)
print('Sum', sum(versions_l))
print('Expression: ', result)

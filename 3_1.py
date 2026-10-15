graf = {
    'u': {'x': 1, 'y': 4, 'w': 5},
    'x': {'u': 1, 'y': 2, 'z': 3, 'v': 6},
    'y': {'u': 4, 'x': 2, 'w': 1, 'z': 2},
    'z': {'x': 3, 'y': 2, 'w': 2, 'v': 3},
    'w': {'u': 5, 'y': 1, 'z': 2, 'v': 2},
    'v': {'x': 6, 'z': 3, 'w': 2}
}

print("Derajat setiap vertex:")
ganjil = []

for vertex in graf:
    derajat = len(graf[vertex])
    print(vertex, ":", derajat)

    if derajat % 2 != 0:
        ganjil.append(vertex)

print("\nVertex berderajat ganjil:", ganjil)

urutan = ['u', 'x', 'y', 'u', 'w', 'y',
          'z', 'w', 'v', 'z', 'x', 'v']

total_bobot = 0

print("\nLangkah Algoritma Fleury:")
for i in range(len(urutan) - 1):
    asal = urutan[i]
    tujuan = urutan[i + 1]
    bobot = graf[asal][tujuan]
    total_bobot += bobot

    print(asal, "->", tujuan, "| Bobot:", bobot)

print("\nRute Euler Trail:")
print(" -> ".join(urutan))
print("Jumlah edge:", len(urutan) - 1)
print("Total bobot:", total_bobot)
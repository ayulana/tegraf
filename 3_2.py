from itertools import permutations

bobot = {
    ('U', 'V'): 51, ('U', 'W'): 56, ('U', 'X'): 60, ('U', 'Y'): 2,  ('U', 'Z'): 35,
    ('V', 'W'): 78, ('V', 'X'): 13, ('V', 'Y'): 51, ('V', 'Z'): 68,
    ('W', 'X'): 70, ('W', 'Y'): 57, ('W', 'Z'): 21,
    ('X', 'Y'): 61, ('X', 'Z'): 68,
    ('Y', 'Z'): 36,
}

def cost(a, b):
    return bobot.get((a, b)) or bobot.get((b, a))

awal = 'U'
simpul_lain = ['V', 'W', 'X', 'Y', 'Z']

terbaik = None
cost_min = float('inf')

for urutan in permutations(simpul_lain):
    rute = [awal] + list(urutan) + [awal]

    total = 0
    for i in range(len(rute) - 1):
        total += cost(rute[i], rute[i + 1])

    if total < cost_min:
        cost_min = total
        terbaik = rute

print("Rute terbaik:", " -> ".join(terbaik))
print("Total bobot :", cost_min)
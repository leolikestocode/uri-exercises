n = int(input())
pokemons = []

for i in range(n):
  pokemons.append(input())

print(f"Falta(m) {151 - len(set(pokemons))} pomekon(s).")

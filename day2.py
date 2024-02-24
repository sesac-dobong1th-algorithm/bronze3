x = int(input())
dict = {
  "kg": "2.2046 lb",
  "l": "0.2642 g",
  "lb": "0.4536 kg",
  "g": "3.7854 l"
}

for _ in range(x):
  a, b = input().split()
  a, b = float(a), str(b)
  
  if b in dict:
    ra, rb = dict[b].split()
    ra, rb = float(ra), str(rb)
    if a == 0: 
      print(f"0.0000 {rb}")
      continue
    print(f"{ra * a:.4f} {rb}")

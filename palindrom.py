def palindrom(angka):
  if len(angka) < 2:
      return "Palindrom"
  elif angka[0] != angka[-1]:
      return "Bukan Palindrom"
  return palindrom(angka[1:-1])

print(palindrom([1,2,3,4,4,3,2,1]))





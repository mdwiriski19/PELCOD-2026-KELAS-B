
jarak_pergi = 100
konsumsi_bensin = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak_pergi * 2
total_bensin = total_jarak / konsumsi_bensin
bensin_dibeli = total_bensin - sisa_bensin
total_biaya = bensin_dibeli * harga_bensin

print ("\n==HASIL==")
print("Total jarak perjalanan =", total_jarak, "km")
print("Total kebutuhan bahan bakar =", total_bensin, "liter")
print("Bahan bakar yang harus dibeli =", bensin_dibeli, "liter")
print("Total biaya bahan bakar = Rp", total_biaya)


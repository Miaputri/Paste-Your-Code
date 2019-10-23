import random
angka=random.randrange(1,100)
tebakan=0
tebakan_saudara = int(input("tebak angka yang sudah dibangkitkan antara 1 sampai 100"))
while tebakan_saudara != angka:
    tebakan += 1
    if tebakan_saudara > angka:
        print(tebakan_saudara,"terlalu tinggi")
    elif tebakan_saudara < angka:
        print(tebakan_saudara,"terlalu tinggi")
    tebakan_saudara = int(input("tebak lagi"))
print("\nBagus ! saudara menebak dalam ", tebakan, "tebakkan")
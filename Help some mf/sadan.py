import sadan2 as s

n = int(input("Banyak data : ... "))
print()

for i in range(n):
    s.garis()
    print("Data ke - ", i+1)
    kode = input("Kode Tiket [eko/pre] : ... ")
    tiket = int(input("Jumlah Tiket : ... "))
    if (kode == "eko"):
        total = s.tiket(tiket, 5000)
        print("kelasnya: ekonomi\t\ttotal: ", total)
    elif (kode == "pre"):
        total = s.tiket(tiket, 1000)
        print("kelasnya: premium\t\ttotal: ", total)
    s.garis()
    print()
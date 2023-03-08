def ganti_kata(kalimat, cari, ganti):
    kalimat_baru = ""
    kata = ""
    for i in range(len(kalimat)):
        if kalimat[i] == " ":
            if kata == cari:
                kalimat_baru += ganti + " "
            else:
                kalimat_baru += kata + " "
            kata = ""
        elif i == len(kalimat) - 1:
            kata += kalimat[i]
            if kata == cari:
                kalimat_baru += ganti
            else:
                kalimat_baru += kata
        else:
            kata += kalimat[i]
    return kalimat_baru

kalimat = input("Masukkan kalimat : ")
cari = input("Kata yang dicari : ")
ganti = input("DIganti menjadi : ")
kalimat_baru = ganti_kata(kalimat, cari, ganti)
print("Kalimat baru:", kalimat_baru)

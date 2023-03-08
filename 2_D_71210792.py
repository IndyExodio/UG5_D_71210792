# def hitung_mobil():
#     jumlahSol = 0
#     jumlahSur = 0
#     jumlahJog = 0
#     jumlahMag = 0
    
#     while True:
#         mobil = input('masukkan asal mobil(ketik "done" untuk keluar) : ').lower()
#         if mobil == 'done':
#             break
#         elif mobil == 'solo':
#             jumlahSol += 1
#         elif mobil == 'surabaya':
#             jumlahSur += 1
#         elif mobil == 'jogja':
#             jumlahJog += 1
#         elif mobil == 'magelang':
#             jumlahMag += 1
#         else:
#             print("Input tidak valid.")
    

#     print("Jumlah mobil dari Solo:", jumlahSol)
#     print("Jumlah mobil dari Surabaya:", jumlahSur)
#     print("Jumlah mobil dari Jogja:", jumlahJog)
#     print("Jumlah mobil dari Magelang:", jumlahMag)
# hitung_mobil()

def hitung_mobil():
    mobil_dict = {'solo': 0, 'surabaya': 0, 'jogja': 0, 'magelang': 0}

    while True:
        mobil = input('Masukkan asal mobil (ketik "done" untuk keluar): ').lower()

        if mobil == 'done':
            break

        if mobil not in mobil_dict:
            print("Input tidak valid.")
            continue

        mobil_dict[mobil] += 1

    print("Jumlah mobil dari Solo:", mobil_dict['solo'])
    print("Jumlah mobil dari Surabaya:", mobil_dict['surabaya'])
    print("Jumlah mobil dari Jogja:", mobil_dict['jogja'])
    print("Jumlah mobil dari Magelang:", mobil_dict['magelang'])


hitung_mobil()

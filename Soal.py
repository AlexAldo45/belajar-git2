while True:
    simpan = []
    bil_n = int(input('Masukkan N: '))
    for x in range (bil_n):
        input_bil = int(input('Masukkan bilangan ke ' + str(x + 1) + ': '))
        if input_bil not in simpan:
            simpan.append(input_bil)
    if len(simpan) == bil_n:
        print("Berbeda semua")
    else:
        print("Tidak berbeda semua")

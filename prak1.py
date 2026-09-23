persentase = int(input("Masukkan persentase nilai siswa: "))

if persentase >= 90:
    print("Excellent Performance)")
elif persentase >= 80:
    print("Very Good Performance)")
elif persentase >= 70:
    print("Good Performance)")
elif persentase >= 60:
    print("Average Performance)")
else:
    print("Poor Performance")
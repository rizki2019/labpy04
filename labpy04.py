nama = []
nim = []
tugas = []
uts = []
uas = []

while True:
    nama_input = input("Nama  : ")
    nim_input = input("Nim   : ")
    tugas_input = int(input("Tugas : "))
    uts_input = int(input("UTS   : "))
    uas_input = int(input("UAS   : "))
    tanya = input("Tambah data(y/t)? ")
    nama.append(nama_input)
    nim.append(nim_input)
    tugas.append(tugas_input)
    uts.append(uts_input)
    uas.append(uas_input)
    if tanya == 't':
        break
print("""
=====================================================================
| No |     Nama      |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |
=====================================================================""")

for i in range(len(nama)):
    print("|",i+1,end="")
    if i < 9 :
        print("  |", end="")
    else:
        print(" |", end="")
        
    print(" "+nama[i],end="")
    for j in range(14-len(nama[i])):
        print(" ",end="")
        
    print("|  "+nim[i],end="")
    for k in range(9-len(nim[i])):
        print(" ",end="")
        
    print("|  "+str(tugas[i]),end="")
    for l in range(7-len(str(tugas[i]))):
        print(" ",end="")
        
    print("|  "+str(uts[i]),end="")
    for m in range(5-len(str(uts[i]))):
        print(" ",end="")
        
    print("|  "+str(uas[i]),end="")
    for n in range(5-len(str(uas[i]))):
        print(" ",end="")
        
    akhir = round((float(tugas[i]*0.3)+float(uts[i]*0.35)+float(uas[i]*0.35)),2)

    print("|  "+str(akhir),end="")
    for o in range(6-len(str(akhir))):
        print(" ",end="")
        
    print("|")
    
print("=====================================================================")
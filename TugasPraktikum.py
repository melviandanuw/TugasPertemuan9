from tabulate import tabulate;

data = [];
data2 = [];
listData = [];

while True:
    data.append(input("Masukan nama         : "));
    nilaiTugas = int(input("Masukan nilai Tugas  : "));
    data.append(nilaiTugas);
    nilaiUAS = int(input("Masukan nilai UAS    : "));
    data.append(nilaiUAS);
    nilaiUTS = int(input("Masukan nilai UTS    : "));
    data.append(nilaiUTS);
    data.append(nilaiTugas * 30/100 + nilaiUAS * 35/100 + nilaiUTS * 35/100);
    data2 = data.copy();
    listData.append(data2);
    del data[:];
    addDatas = input("\nTambah data? \n");
    
    if addDatas.lower() == 'y':
        print('\nSilahkan masukan inputan kembali.');
    elif addDatas.lower() == 'n':
        print('\n', tabulate(listData, headers=["Nama", "Tugas", "UAS", "UTS", "Nilai Akhir"]));
        print("\nProgram akan berhenti.");
        break;
    else:
        print('\n', tabulate(listData, headers=["Nama", "Tugas", "UAS", "UTS", "Nilai Akhir"]));
        print("\nInputan Salah, Program akan berhenti.");
        break;
    
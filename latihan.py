myList = [1, 3, 10, 12, 2];


#Akses List
#Akses List elemen ke 3
print('Elemen ke 3:', myList[2]);

#Ambil elemen 2 - 4
print('Ambil elemen 2 - 4:', myList[1:4]);
del myList[1:4];
print('Sisa elemen yang diambil:', myList);

#Ambil elemen terakhir
print('Sebelum elemen terakhir diambil:', myList);
myList.pop();
print('Sesudah elemen terakhir diambil:', myList);

#-----------------------------------------------------

myList = [1, 3, 10, 12, 2];


#Ubah Elemen
#Ubah Elemen List ke 4
print('Sebelum elemen ke 4 diubah:', myList[3]);
myList[3] = 150;

#Ubah Elemen List ke 4 - terakhir
print('Sebelum elemen ke 4 - terakhir diubah:', myList);
for i in range(3, len(myList)):
    myList[i] = myList[i] + 10;
print('Setelah elemen ke 4 - terakhir diubah:', myList);

#-----------------------------------------------------

#Tambah elemen list
myListA = [1, 3, 10, 12, 2];
myListB = [2, 4, 1, 10, 12];

#Ambil 2 bagian pertama list A dan jadikan list B
print('myListA:', myListA);
print('myListB:', myListB);
myListB[0:2] = myListA[0:2];
print('myListB setelah 2 bagian pertama list A ditambahkan:', myListB);

#Tambah list B dengan string
print('myListB sebelum ditambahkan String:', myListB);
myListB.append('iniString');
print('myListB sesudah ditambahkan String:', myListB);

#Tambah list B dengan 3 nilai
print('myListB sebelum ditambahkan 3 nilai:', myListB);
for i in range(0, 3):
    myListB.append(myListB[i] + 10);
print('myListB sesudah ditambahkan 3 nilai:', myListB);

#Gabungkan list A dengan list B
print('myListA:', myListA);
print('myListB:', myListB);
myListC = myListA + myListB;
print('myListC, hasil penambahan list A dengan list B:', myListC);
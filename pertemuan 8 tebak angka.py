import random

angka_rahasia = (random.randint(1, 100))
print('halo..namaku laptop, saya akan kasih angka antara 1-100. apakah kamu bisa menebaknya?')

      
while True :
    bil= int(input('masukan angka: '))

    if(bil > angka_rahasia):
        print('maaf jawaban anda terlalu besar')
    elif(bil < angka_rahasia):
        print ('maaf jawaban anda terlalu kecil')
    elif (bil == angka_rahasia):
          print ('selamat anda benar')
    

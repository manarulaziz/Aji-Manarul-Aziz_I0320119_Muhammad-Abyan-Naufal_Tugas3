list_teman = ['Rahmat Herpradipto',
            'Yukuri Hanjani Putri',
            'Zafira Chairunnisa',
            'Zedi Ikram El Fathi', 
            'Ahmad Rifqi Waskita', 
            'Alfina Diva Ramadhanty', 
            'Alica Ayu Fitriani', 
            'Alvin Anindra Putra',
            'Alya Ramadhani',
            'Dendy Halim Kusuma'
            ]

print("List teman pada indeks keempat adalah", list_teman[4])  
print("List teman pada indeks keenam adalah", list_teman[6])  
print("List teman pada indeks ketujuh adalah", list_teman[7])  

list_teman[3] = 'Yuki Rizkylawati'
list_teman[5] = 'Yolanda Diandari'
list_teman[9] = 'Yeario Endriano'

list_teman.append('William Anderson')
list_teman.append('Wanda Aulia Abrar')

for friend in list_teman:
    print(friend, "adalah teman saya")

panjang_list_teman = len(list_teman)
print("Jumlah teman saya adalah", panjang_list_teman)


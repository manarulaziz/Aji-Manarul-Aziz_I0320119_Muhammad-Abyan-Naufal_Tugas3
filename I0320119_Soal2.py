dict_aku = {'Nama': 'Aji Manarul Aziz',
            'Hobi': ['Membaca','Menulis'],
            'Sosial media': ['@manaaarul', '@manarulaziz_'],
            'Lagu kesukaan': ['Mantan Terindah by Raisa', 'Intentions by Pamungkas', 'Happiness by Rex Orange County'],
            'Makanan favorit': ['Ayam geprek kumlot', 'Bakso UPT', 'Ayam spicy McD', 'Capcay pinggir jalan']
            }

dict_aku['Hobi'][1] = 'Ngoding'
dict_aku['Sosial media'][0] = '@ajimanarul'

del dict_aku['Makanan favorit'][2:]

dict_aku['Hobi'].append('Futsal')

print("Halo nama saya", dict_aku['Nama'],
    "\nHobi saya di antaranya adalah", dict_aku['Hobi'],
    "\nSaya memiliki sosial media dengan username", dict_aku['Sosial media'],
    "\nSaya suka sekali mendengar lagu berjudul", dict_aku['Lagu kesukaan'],
    "\nMakanan yang menjadi favorit bagi saya adalah", dict_aku['Makanan favorit'])
    
partecipante1= partecipante1={'nome':'Viviana', 'cognome':'Tarantino','data_nascita':[5,1,1988]}
print(partecipante1)
#print(len(partecipante1))
partecipante2={'nome':'Viviana', 'cognome':'Tarantino','data_nascita':[5,3,1988]}
anno1=partecipante1['data_nascita'][2]
#print(anno1)
anno2=partecipante2['data_nascita'][2]
#print(anno2)
#print(anno1>anno2)

mese1=partecipante1['data_nascita'][1]
mese2=partecipante2['data_nascita'][1]

if anno1==anno2 and mese1==mese2:
	print('partecipante 1 e partecipante 2 sono coetanei')
else anno1==anno2 and mese1>mese2: 
	print('partecipante2 è più giovane di partcipante1')
elif:
	print('partecipante1 è più giovane di partecipante2')


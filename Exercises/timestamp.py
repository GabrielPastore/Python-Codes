import datetime

data = str(input("\nMe diga uma data específica e o programa retornará essa data em Timestamp. \n\nFavor seguir o modelo abaixo.\nFormato: 01/12/2011 12:45\n\nR: "))
spaces = []

for c in range(0, (len(data)-7)):
    if data[c] == " ":
        spaces.append(c)

for c in spaces:
    data = data[:c] + "/" + data[c+1:]
    
timestamp = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M").timestamp()
print(int(timestamp))
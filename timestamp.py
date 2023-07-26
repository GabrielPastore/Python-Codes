import datetime

data = str(input("\nMe diga uma data específica e o programa retornará essa data em Timestamp. \n\nFavor seguir o modelo abaixo.\nFormato: 01/12/2011 12:45\n\nR: "))

timestamp = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M").timestamp()
print(int(timestamp))
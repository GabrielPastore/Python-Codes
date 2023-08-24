#Criação das variáveis iniciais que serão a base do sistema
name = input("Digite seu nome: ")
student = {"Name": name}
student_subjects = []
student_grades = []
student_average_grade = []

#Pegar as matérias
for _ in range(3):
    student_subjects.append(input("Digite uma matéria: "))
student["Matérias"] = student_subjects

#Pegar as notas
for index, _ in enumerate(student["Matérias"]):
    for _ in range(2):
        student_grades.append(float(input(f"Digite sua nota em {student['Matérias'][index]}: ")))
    name = student_subjects[index]

    #Trocar as Matérias por um dicionário que possua o nome de cada matéria como chave e seu conjunto de notas em cada matéria como valor
    student["Matérias"][index] = dict(student_subjects = student_grades)
    student["Matérias"][index][name] = student["Matérias"][index].pop("student_subjects")
    student_grades = []

#Fazer a média das notas
for subject in student["Matérias"]:
    for _, grades in subject.items():
        average_grade = sum(grades) / len(grades)
    student_average_grade.append(average_grade)

#Tratamento das variáveis para poder facilitar o uso do print no final do programa
student_subjects = []
student_grades = []
for dictionary in student["Matérias"]:
    student_subjects.append(*dictionary.keys())
    student_grades.append(*dictionary.values())

#Print final exibindo todas as informações
print(f"O nome do aluno é {student['Name']}, as matérias que ele tem são {student_subjects}, suas notas em cada matéria são {student_grades} e, por fim, sua média em cada uma dessas matérias, respectivamente, é de {student_average_grade}")
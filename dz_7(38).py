# Напишите программу, удаляющую из текста все слова содержащие "абв".

my_text = "f,df вьывль львыа абв абвапро a,d абв фффабвсс"
my_text = my_text.split()
new_text = [i for i in my_text if "абв" in i]
new_text = [j for j in my_text if j not in new_text]
print(new_text)
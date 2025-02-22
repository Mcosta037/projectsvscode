
n1= input("se deseja criar um ficheiro pressione C,se não quer criar nada pressione h: ")
if n1 == "c":
    with open('file5.txt', 'w') as file5:
        file5.write("\n")
    
    user_choice = (input("se deseja adicionar alguma coisa e apagar o anterior pressione A, se deseja ler o que escreveu pressione r,se deseja escrever e apagar o que estava escrito antes pressione w:"))
    
    if user_choice == "a":
        
        n3 =input("o que deseja escrever:")

        with open('file 5.txt', 'a') as arquivo:
            
            with open('exemplo.txt','a') as arquivo:
               
                arquivo.write("linha 4\n")
    
    elif user_choice == "r":
        
        with open('file5.txt', 'r') as arquivo:
           print(arquivo.read())
   
    elif user_choice == "w":
        
        n4 = input("o que deseja escrever:")
        with open('file5.txt', 'w') as arquivo:
            arquivo.write(f"{n4}\n")
    
    elif n1 == "h":
        print("vá embora")
else:
    print("that is not an option")







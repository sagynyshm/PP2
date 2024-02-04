def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)
#vjyhvyvlvul
#dydy
#wtfgug

users_input=str(input("enter a string"))
get_permutation(users_input)
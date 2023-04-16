

import random 
# from words import word_list
word_list = ['wares','soup','mount','extend','brown','expert','tired',
             'humidity','backpack','crust','dent','market','knock','smite','windy','coin','throw',
    'silence']

hangman = [

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""]   

print("Let's play hangman")
chosen_word = random.choice(word_list)

#print("The solution is: ",chosen_word)

display = []
word_lenth = len(chosen_word)
for i in range(word_lenth):
    display.append("_")

print(display)
live = 8
y = 0
end_of_game = False
while not end_of_game :
    guess = input("Guess a letter ").lower() 

    for position in range(word_lenth):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        live -= 1
        y = 8-live
        if live == 0:
            end_of_game = True
            print("You Lose.")
           
    print(display)
        
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman[y])
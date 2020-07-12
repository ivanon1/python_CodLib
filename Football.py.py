

def tournament_scores (lst):
 
 #Join the list values together into one index 
 lst_concat = [' '.join(lst)]
 #Replace the dash (-) with blank spaces 
 lst_del_dash = [s.replace("-", "") for s in lst_concat]

 #Create two lists of digits and letters for the A team and split the values 
 digits = [int(i) for i in lst_del_dash[0].split() if i.isdigit()] 
 letters = [str(i) for i in lst_del_dash[0].split() if i.isalpha()] 
 #Create two lists of digits and letters for the B team and split the values 
 digits_b = [int(i) for i in lst_del_dash[0].split() if i.isdigit()] 
 letters_b = [str(i) for i in lst_del_dash[0].split() if i.isalpha()] 
 #Create two lists of digits and letters for the C team and split the values 
 digits_c = [int(i) for i in lst_del_dash[0].split() if i.isdigit()] 
 letters_c = [str(i) for i in lst_del_dash[0].split() if i.isalpha()] 
 #Create two lists of digits and letters for the D team and split the values 
 digits_d = [int(i) for i in lst_del_dash[0].split() if i.isdigit()] 
 letters_d = [str(i) for i in lst_del_dash[0].split() if i.isalpha()] 

 #create a list for the A team 
 a_lst = ["A",0,0,0]
 #create a list for the B team 
 b_lst = ["B",0,0,0]
 #create a list for the C team 
 c_lst = ["C",0,0,0]
 #create a list for the D team 
 d_lst = ["D",0,0,0]

 #Recursive Function to swap indexes of digits and letters based on letter and odd/even based index positioning 
 def swap_index(arg,arg1,arg2):
    
     for index in range(1,len(arg),2):
         if(arg[index] == arg2 and arg.index(arg2) %2 == 0 or  arg.index(arg2) %2 != 0):
           arg[index-1],arg[index] = arg[index],arg[index-1]
           arg1[index-1],arg1[index] = arg1[index],arg1[index-1]
        
     index+=1
     return arg,arg1

 #call the swap_index function for the A team to position the Values of the A team as the first index in a game 
 swap_a = swap_index(letters,digits,"A")
 #call the swap_index function for the B team to position the Values of the B team as the first index in a game 
 swap_b = swap_index(letters_b,digits_b,"B")
 #call the swap_index function for the C team to position the Values of the C team as the first index in a game 
 swap_c = swap_index(letters_c,digits_c,"C")
 #call the swap_index function for the D team to position the Values of the D team as the first index in a game 
 swap_d = swap_index(letters_d,digits_d,"D")

 #Add a list to hold the conceded goal scores for team A
 sum_a = [0]

 #Loop through the A team's list of numbers and digits to determine team scores based off wins and losses 
 #All values of A are evaluated from the first index and compared to the next when looping through the lists 
 for i,letter in enumerate(letters):

     if( letter == "A" and i < len(letters)-1):
          next = digits[i+1] 
          #Add conceded goal scores to the list for team A 
          sum_a[0]+= next
          if(digits[i] < next):
           a_lst[1]+=0  
          elif(digits[i] > next):
           a_lst[1]+=3
          elif(digits[i] == next):
           a_lst[1]+=1 
       
#Sum the overall scored goals in the games for team 
     if(letter == "A"):
        a_lst[2] += digits[i]
     if(letter == "B"):
       b_lst[2] += digits[i]
     if(letter == "C"):
       c_lst[2] += digits[i]
     if(letter == "D"):
       d_lst[2] += digits[i]

     # Add the (scored goals - conceded goals) integer score to the list for team A 
     a_lst[3] = a_lst[2] - sum_a[0]

 i+=0
 
 #Add a list to hold the conceded goal scores for team B
 sum_b = [0]
 
 #Loop through the B team's list of numbers and digits to determine team scores based off wins and losses 
 #All values of B are evaluated from the first index and compared to the next when looping through the lists 
 for i,letter in enumerate(letters_b):
     
     if( letter == "B" and i < len(letters_b)-1):
           next = digits_b[i+1]
           #Add conceded goal scores to the list for team B
           sum_b[0]+= next
           if(digits_b[i] < next):
            b_lst[1]+=0    
           elif(digits_b[i] > next):
            b_lst[1]+=3
           elif(digits_b[i] == next):
            b_lst[1]+=1 
    
           # Add the (scored goals - conceded goals) integer score to the list for team B
           b_lst[3] = b_lst[2] - sum_b[0]

 i+=0
 
 #Add a list to hold the conceded goal scores for team C
 sum_c = [0]
 
 #Loop through the C team's list of numbers and digits to determine team scores based off wins and losses 
 #All values of C are evaluated from the first index and compared to the next when looping through the lists 
 for i,letter in enumerate(letters_c):
     
     if( letter == "C" and i < len(letters_c)-1):
          next = digits_c[i+1] 
          # Add conceded goal scores to the list for team C
          sum_c[0]+=next
          if(digits_c[i] < next):
           c_lst[1]+=0    
          elif(digits_c[i] > next):
           c_lst[1]+=3
          elif(digits_c[i] == next):
           c_lst[1]+=1 

          # Add the (scored goals - conceded goals) integer score to the list for team C        
          c_lst[3] = c_lst[2] - sum_c[0]

 i+=0
 
 #Add a list to hold the conceded goal scores for team D
 sum_d =[0]
 
 #Loop through the D team's list of numbers and digits to determine team scores based off wins and losses 
 #All values of D are evaluated from the first index and compared to the next when looping through the lists 
 for i,letter in enumerate(letters_d):
     
     if( letter == "D" and i < len(letters_d)-1):
           next = digits_d[i+1] 
           # Add conceded goal scores to the list for team D
           sum_d[0]+=next
           if(digits_d[i] < next):
            d_lst[1]+=0    
           elif(digits_d[i] > next):
            d_lst[1]+=3
           elif(digits_d[i] == next):
            d_lst[1]+=1 

           # Add the (scored goals - conceded goals) integer score to the list for team D
           d_lst[3] = d_lst[2] - sum_d[0]

 i+=0

 # Combine the four lists into one named scores
 scores = [a_lst] + [b_lst] + [c_lst] + [d_lst]
 
 # Sort the list of scores for each team by descending order 
 sorted_list = sorted(scores, key = lambda z: z[1:], reverse = True)

 #return the list of lists named scores 
 return(sorted_list)


#Driver Code for tournament scores function 
#lst =["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]
#lst = ["A 4 - 0 B", "C 2 - 1 D", "B 1 - 0 C", "D 3 - 2 A", "A 1 - 3 C", "B 2 - 1 D"]
lst = ["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C", "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"]

#Call the function tournament_scores
print(tournament_scores(lst))









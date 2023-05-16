import csv
from random import shuffle

#Global initializations
rights = 0
questions_list = []
list_responses = []
wrong_questions = []

f = open ('Questions Bank.csv',encoding='UTF8')
csv_reader = csv.reader(f)
for line in csv_reader:
    questions_list.append(line[0])
f.close()

shuffle(questions_list)
newlist = questions_list[:39]
#print (newlist)

#print questions
questions_nums = 1
for qt in newlist:
    f = open ('Questions Bank.csv',"r", encoding='UTF8')
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if line[0]== qt :
            print ("\n"+str(questions_nums)+") "+line[1]+"\n   "+line[2]+"\n   "+line[3]+"\n   "+line[4]+"\n   "+line[5]+"\n   "+line[6]+"\n   ") 
            response = input("Enter response: ")
            if response.upper() == line[7]:
                rights = rights+1
            else:
                wrong_questions.append(questions_nums)
            list_responses.append(line[7])
            questions_nums = questions_nums+1
    f.close()
    
#Print response list and wrong answers
for i in range(len(list_responses)):
    print("Question "+str(i+1)+") "+list_responses[i])
          
if wrong_questions == []:
    print ("\nNo wrong answers! Congrats!")
else:
    print ("Wrong Questions:\n")
    for w in wrong_questions:
        print ("Question: "+str(w))
    
final_score = rights/len(list_responses)*100
print ("\nYour final score is: "+str(final_score)+"%")

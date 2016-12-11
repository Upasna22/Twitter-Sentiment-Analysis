
import sys
import csv
import string

def main():
    sent_file = open(sys.argv[1])
    csv_file = open(sys.argv[2])
    file_reader = csv.reader(csv_file)
    scores={}
    user_list=[]
    tweet_list=[]
    term=[]
    score=[]
    score_o=[]
    term_o=[]
    score_t=[]
    term_t=[]
    term_sp=[]



    for line in sent_file.readlines():
       term = line.split("\t")[0]
       score =line.split("\t")[1]
       scores[term]= float(score)

       if " " in term:
           term_sp = term.split(" ")

           if len(term_sp)==2 :
               term_o.append(term_sp)
               score_o.append(score)

           if len(term_sp)==3:
             term_t.append(term_sp)
             score_t.append(score)

    user_dict ={}
    firstline = True

    for row in file_reader:

        if firstline:
           firstline = False
           continue
        user_list=row[0]
        tweet_list=row[1]



        if row[0] in user_dict.keys():
        # append the new number to the existing array at this slot
            user_dict[row[0]].append(row[1])
        else:
        # create a new array in this slot
            user_dict[row[0]] = [row[1]]



    tweet_score={}
    sen=0.0

    count_list=[]
    keys_d = user_dict.keys()

    user_freqdict={}
    for key in keys_d:

        count=0
        sen=0
        for word in user_dict[key]:
            word = word.replace('\n',' ')

            exclude = set(string.punctuation)
            word = ''.join(ch for ch in word if ch not in exclude)
            senti=sentiment(word.lower(),scores,term_o,score_o,term_t,score_t)


            count+=1
            count_list.append(count)
            sen +=senti
    #    print(key,sen)
        avg =sen/count
#        print(key,avg)
        user_freqdict[key]=avg
#    print(user_freqdict)
    user_freqlist=[]
    for key, value in user_freqdict.items():
        temp = [key,value]
        user_freqlist.append(temp)
#    print(user_freqlist)

    sorted_list=[]
    def getKey(item):
        return item[1]
    print("The list of user names and average sentiment scores in decreasing order is :")
    sorted_list =sorted(user_freqlist, key=getKey,reverse = True)
    for c in (sorted_list):
        print(c)
    print("\n")
    print(" The happiest actor is")
    print(sorted_list[:1])



def sentiment(word,scores,term_o,score_o,term_t,score_t):
    split_list =[]

    split_list.append(word.split(" "))

    sent = 0.0
    for wrd in split_list:

        for c in wrd:

            try:
                sent += scores[c]
            except KeyError:
                sent +=0.0

    for wrd in split_list:

        for i in range(0,len(wrd)):

            for j in range(0,len(term_o)):

                if(wrd[i] == term_o[j][0]):
                    #print(wrd[i],"________",term_o[j][0])
                    if((i+1) < (len(wrd)) and wrd[i+1] == term_o[j][1]):
                        sent+= score_o[j]


    for wrd in split_list:
        for i in range(0,len(wrd)):
            for j in range(0,len(term_t)):
                if(wrd[i] == term_t[j][0]):
                    if((i+1) < (len(wrd)) and wrd[i+1] == term_t[j][1]):
                        if((i+2) < (len(wrd)) and wrd[i+2] == term_t[j][2]):
                           sent+= score_t[j]




    return(sent)



if __name__ == '__main__':
    main()

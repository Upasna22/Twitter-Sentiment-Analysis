import json
import sys
import string
from operator import itemgetter
sorted_score=[]
sent_score=[]
word_list=[]
text_list=[]
sent_list=[]
max_list={}
max_list2={}
max_val2={}
min_list={}
min_list2={}
text_fin_list=[]
val_list =[]
score_o=[]
term_o=[]
score_t=[]
term_t=[]
term_sp=[]
score_list=[]

def sentiment(sent_file,tweet_file):

    scores={}
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


    for line in tweet_file.readlines():
        l=json.loads(line)
        if l.get('text'):
            text_list.append(l.get("text"))


    for word in text_list:
        word = word.replace('\n',' ')
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude)
        word_list.append(word)
        text =(word).lower().split(" ")

        text_fin_list.append(text)

    sent =sentiment_an(text_fin_list,scores,term_o,score_o,term_t,score_t)





    for i in range(0,len(text_fin_list)):
        #print(text_fin_list[i])
        sent_score.append([sent[i],word_list[i]])

    sorted_score =sorted(sent_score, key=itemgetter(0),reverse = True)
#    print(sorted_score)

    print("The top ten highest sentiment tweets are:")
#    for c in sorted_score[:10]:
   # print(sorted_score[:10],end ="\n")
    for element in sorted_score[:10]:
        print(element)
    print("The bottom ten lowest sentiment tweets are:")
    for element in sorted_score[-10:]:
        print(element)



def sentiment_an(text_fin_list,scores,term_o,score_o,term_t,score_t):
#    print(text_fin_list)
    #sent = 0.0
    for line in text_fin_list:
     #  print(line)
       sent=0
       for wrd in line:
         #  print(wrd)
           try:
               sent += scores[wrd]
           except KeyError:
               sent +=0.0
#        print(wrd,sent)
       #s =0.0

       for i in range(0,len(line)):



           s=0
           for j in range(0,len(term_o)):
               #   print(term_o[j])
               if(line[i] == term_o[j][0]):
               # print(text[i],"______",term_o[j][0],"+",text[i+1],"_______",term_o[j][1])
                      #print(text[i+1])
                     # print(term_o[j][1])
                   if((i+1)<(len(line)) and line[i+1] == term_o[j][1]):
                          #print(text[i+1],"_______",term_o[j][1])
                       s+= float(score_o[j])
                   #    print(line[i])
           sent+= s
#    print(line,"___",sent)
       sent_list.append(sent)
#    print(sent_list)
    return sent_list


def main():
    sent_file =open(sys.argv[1])
    tweet_file =open(sys.argv[2])
    sentiment(sent_file,tweet_file)


if __name__ =='__main__':
    main()

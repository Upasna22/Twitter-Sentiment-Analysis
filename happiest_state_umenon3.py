import sys
import json
import string

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #TODO: Implement
    state_list=[]
    text_list =[]
    place_list=[]
    country_list=[]
    user_split=[]
    user_list=[]
    user_loc =[]
    term=[]
    score=[]
    score_o=[]
    term_o=[]
    score_t=[]
    term_t=[]
    term_sp=[]
    scores={}
    st_txt_dict={}
    state_dict={"AL":"Alabama",
                "AK":"Alaska",
                "AZ":"Arizona",
                "AR":"Arkansas",
                "CA":"California",
                "CO":"Colorado",
                "CT":"Connecticut",
                "DE":"Delaware",
                "DC":"District of Columbia",
                "FL":"Florida",
                "GA":"Georgia",
                "HI":"Hawaii",
                "ID":"Idaho",
                "IL":"Illinois",
                "IN":"Indiana",
                "IA":"Iowa",
                "KS":"Kansas",
                "KY":"Kentucky",
                "LA":"Louisiana",
                "ME":"Maine",
                "MT":"Montana",
                "NE":"Nebraska",
                "NV":"Nevada",
                "NH":"New Hampshire",
                "NJ":"New Jersey",
                "NM":"New Mexico",
                "NY":"New York",
                "NC":"North Carolina",
                "ND":"North Dakota",
                "OH":"Ohio",
                "OK":"Oklahoma",
                "OR":"Oregon",
                "MD":"Maryland",
                "MA":"Massachusetts",
                "MI":"Michigan",
                "MN":"Minnesota",
                "MS":"Mississippi",
                "MO":"Missouri",
                "PA":"Pennsylvania",
                "RI":"Rhode Island",
                "SC":"South Carolina",
                "SD":"South Dakota",
                "TN":"Tennessee",
                "TX":"Texas",
                "UT":"Utah",
                "VT":"Vermont",
                "VA":"Virginia",
                "WA":"Washington",
                "WV":"West Virginia",
                "WI":"Wisconsin",
                "WY":"Wyoming"}

    state_word_dict ={}
    for line in sent_file.readlines():
       term=line.split("\t")[0]
       score=line.split("\t")[1]
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
           if l.get('lang') == 'en':
               if l.get('place') is not None :

                   place_list.append(l.get("place"))

                   if 'full_name' in l['place'] is not None:
                       if 'country' in l['place'] is not None:

                           if l['place']['country'] == 'United States':
                  #  country_list.append(l['place']['country'])
                       # print(l['place']['country'])
                               state_full= l['place']['full_name']
                        #print(state_full)
                               if l['place'] is not None:
                                   place_type= l['place']['place_type']

                                   if place_type == 'admin':
                                       state_split =state_full.split(",")[0]
                                       for key in state_dict:
                                           if state_split == state_dict[key]:
                                               state_list.append(key)


                                   elif place_type == 'city':
                                       state_split = state_full.split(",")[1]
                                       state_list.append(state_split)



                               if(l['place']['place_type']=='admin' or l['place']['place_type']=='city'):
                                   text_list.append(l.get("text"))
                            #text =l.get("text")
                            #st_txt_dict[state_list] = text_list
               elif l.get('user') is not None:
                   user_list.append(l.get("user"))
            #print(user_list)
                   if 'location' in l['user'] is not None:
                       if l['user']['location'] is not None:
                           user_loc= l['user']['location']

                           if "," in user_loc:                #print(user_loc)
                               user_split = user_loc.split(",")[1]
                       # print(user_split)
                               if(user_split.strip() in state_dict):
                           # print(user_split)
                                   state_list.append(user_split)
                                   text_list.append(l.get("text"))
                        #    print(state_dict[user_split])



    for i in range(0,len(state_list)):

        if state_list[i] in st_txt_dict.keys():
            st_txt_dict[state_list[i].strip()].append(text_list[i])
        else:
            st_txt_dict[state_list[i].strip()] = [text_list[i]]


    tweet_score={}
    sen=0.0
    user_freqlist=[]
    count_list=[]
    keys_d = st_txt_dict.keys()
#    print(keys_d)
    user_freqdict={}
    for key in keys_d:
#        print(user_dict[key])
        count=0
        sen=0.0
        for word in st_txt_dict[key]:

#            print(key,word)
            exclude = set(string.punctuation)
            word = ''.join(ch for ch in word if ch not in exclude)
            senti=sentiment(word.lower(),scores,term_o,score_o,term_t,score_t)
            #print(key,word,senti)
           # print(key+"---------"+word,senti)
            count+=1
            count_list.append(count)
            sen +=senti
         #   print(key,count,word,sent)
        avg =float(sen/count)
#        print(key,sen)
#        print(key,avg,sen,count)
        user_freqdict[key]=avg
#    print(user_freqdict)
    for key, value in user_freqdict.items():
        temp = [key,value]
        user_freqlist.append(temp)


    sorted_list=[]
    def getKey(item):
        return item[1]
    print("The list of states and average sentiment scores in decreasing order is :")
    sorted_list =sorted(user_freqlist, key=getKey,reverse = True)
    #print(sorted_list)
    for c in (sorted_list):
        print(c)
    print("\n")
    print(" The happiest state is")
    print(sorted_list[:1])


    print("The 5 happiest states are ")
    for c in (sorted_list[:5]):
       print(c)

    print("The 5 unhappiest states are")
    for c in (sorted_list[-5:]):
       print(c)


def sentiment(word,scores,term_o,score_o,term_t,score_t):
    split_list =[]
    split_list.append(word.split(" "))
   # print(split_list)
    sent = 0.0
 #       print(split_list[i])
    for wrd in split_list:
        #print(wrd)
        for i in range(0,len(wrd)):
#           print(wrd[i])
            try:
                sent += scores[wrd[i]]
            except KeyError:
                sent +=0.0
    for wrd in split_list:
        for i in range(0,len(wrd)):
           # print(wrd[i])
            for j in range(0,len(term_o)):
               # print(wrd[i])
                if(wrd[i] == term_o[j][0]):
                    #print(wrd[i],"________",term_o[j][0])
                    if((i+1) < (len(wrd)) and wrd[i+1] == term_o[j][1]):
                        sent +=float( score_o[j])


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


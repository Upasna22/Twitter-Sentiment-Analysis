import sys
import json
import string


def main():

    text_list =[]
    split_list=[]
    stop_list=[]
    unique_list=[]
    total_count =0
    sum =0
    word_list=[]
    unique_words=[]
    word_freqlist=[]
    word_count=0
    tweet_file = open(sys.argv[2])
    stop_wordfile=open(sys.argv[1])
    for line in tweet_file.readlines():
       line.strip()

       t = json.loads(line)


       if t['lang']=="en":

           if t.get('text'):
               text_list.append(t.get("text"))
       for line in text_list:
           exclude = set(string.punctuation)
           line = ''.join(ch for ch in line if ch not in exclude)


    for line in stop_wordfile:
       line =line.strip()
       stop_list.append(line)


    for word in text_list:


        split_list.append(word.lower().split(" "))

    unique_list=[]
    for line in split_list:

        unique_words=[item for item in line if item not in stop_list]

        unique_list.append(unique_words)


    for word in unique_list:
        for c in word:
           total_count+=1

           word_list.append(c)


    unique_list=sorted(set(word_list))



    word_dict ={}
    for word in unique_list:
       #print(word)
       if (word.isalnum() == True):
           exclude = set(string.punctuation)
           word = ''.join(ch for ch in word if ch not in exclude)

           word_dict[word.lower()]=word_list.count(word)
    #print(word_dict)

    word_freq={}
    for key in word_dict:
       frequency = word_dict[key]/total_count
       word_freq[key]= frequency

    for key, value in word_freq.items():
        temp = [key,value]
        word_freqlist.append(temp)

    sorted_list=[]
    def getKey(item):
        return item[1]
    print("The terms and frequencies are :")
    sorted_list =sorted(word_freqlist, key=getKey,reverse = True)

    for c in (sorted_list):
        print(c)
    print("\n")
    print(" The 30 most frequent terms are:")
    for c in (sorted_list[:30]):
        print(c)





if __name__ == '__main__':
    main()


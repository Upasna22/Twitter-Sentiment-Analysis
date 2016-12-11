# Twitter-Sentiment-Analysis

Streaming API:
*In this section , we access the current Twitter stream.
*The program fetches a random sample of all public statuses and prints out each tweet in json format.
*The Streaming APIs give access to (usually a sample of) all tweets as they published on Twitter
We need to execute the following command to fetch a sample.
$ python3 fetch_tweets.py ‐c fetch_samples 

*****************************************************************************************************************************************************************
Search API:
*This library allows you to create a search through the Twitter API.
*It gives you the relevant tweets that match your search term.
$ python3 fetch_tweets.py ‐c fetch_by_terms ‐term "[your_chosen_term]" is the command to find tweets of a particular search term.

For example:
If we choose the search term as "Sanders" and run the command above , we get a set of tweets. Some tweets from the search_output_umenon3.txt is:

OUTPUT :
Sanders

RT @machineiv: If Clinton is afraid of Sanders\'s supposed negativity, how in the hell does she ever hope to handle Trump?\\n\\nhttps:\\/\\/t.co\\/sN4\\u2026
RT @CapTimes: Calling Clinton a \\"weak frontrunner,\\" Sanders campaign says they\'ll fight hard to win Wisconsin. https:\\/\\/t.co\\/DAwB8mMZ1L
RT @CitizensFedUp: Obama endorses Wasserman Schultz in primary over Sanders backed candidate https:\\/\\/t.co\\/EqD15Qf6Of\'\\n\\n#ByeByeBernie https:\\u2026
ByeByeBernie
RT @davidsirota: Wait, did Bernie Sanders just hack Hillary Clinton\'s twitter account? https:\\/\\/t.co\\/YVXPKgq5YE

*******************************************************************************************************************************************************************
User API:
*Here, we get the recent 100 tweets of all the users specified in user_names.txt.
*First , we define the parameters to extract
 parameters = [("screen_name", user),("count",100)]
 This specifies that we want to extract the 100 recent tweets of "user"
*The response parameter response = twitterreq(url, "GET" ,parameters) requests for the parameters using the GET request.
*Then we need to decode it and convert it to a json object as follows:
           str_response =response.read().decode('utf-8')
           json_load=json.loads(str_response)
* The extracted data is then put into a csv file.

********************************************************************************************************************************************************************
Compute term frequency:
Here, we have to find the frequency of each term that is not present in the stopword file.
Algorithm:
* Read each line from tweet file and extract the "text" of tweet and store it in a "text_list".
* Iterate over each line of text_list and append those that are not in the stopword file into a list (say unique_list).
* Find total word count in this unique_list.
* Store the words of unique_list into a word_list.
* Find the number of occurences of each word in the word_list and store the word and its respective count in a dictionary word_dict.
* Find the frequency of each word by dividing each key of word_dict by total count.
* Store each word and its respective frequency in a dictionary word_freq.
* Now we have the unique words as keys and the respective frequencies as values of the word_freq dict.
* Sort the dictionary by the value(frequency).We get the entire list of terms and their frequencies sorted in decreasing order of frequency.
* Retrieve the first 30 elements to get the 30 most frequent terms.

OUTPUT:

The output format will be in the following form:(only portion of output is shown)
 ('but', 0.002954384306310565),
 ('amp', 0.0028362089340581422),
 ('from', 0.0027180335618057195),
 ('all', 0.0024816828173008744),
 ('get', 0.0024816828173008744),
 
* The 5 most frequent terms along with frequencies is as follows.

The 5 most frequent terms are:
['rt', 0.05652759084791386]
['like', 0.0070659488559892325]
['love', 0.004542395693135935]
['get', 0.0035329744279946162]
['need', 0.00319650067294751]

###################################################################################################################################


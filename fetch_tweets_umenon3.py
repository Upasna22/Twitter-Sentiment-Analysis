import argparse
import oauth2 as oauth
import urllib.request as urllib
import json
import sys
import csv
import codecs
# See Assignment 1 instructions for how to get these credentials
access_token_key = "635142863-lvrE1s8c84YK3Wu5yXR6G6a6LrcgWiB4XBc90tL8"
access_token_secret = "ssNUVcWfkSexLFlHw5S7yEvRoUQGzHqOPwNlamuxIsIlw"

consumer_key = "1rGsmsAe6rT3pIaZ5e5lRAGIe"
consumer_secret = "P9CyHo0MZvf3E2Ims1Mb6e0bl9763BWFN7HCRpHeH6OaZnuYzA"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetch_samples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print (line.strip().decode('utf-8'))

def fetch_by_terms(term):
    url = "https://api.twitter.com/1.1/search/tweets.json?count=100"
    parameters = [("q", term)]
    response = twitterreq(url, "GET", parameters)
    print (response.readline())

def fetch_by_user_names(user_name_file):
    #TODO: Fetch the tweets by the list of usernames and write them to stdout in the CSV format
    sn_file = open(user_name_file)
    url ="https://api.twitter.com/1.1/statuses/user_timeline.json"
    with open('result.csv','w') as csvfile:
        n =['User','Tweet']
        print ("User , Tweet")
        w = csv.writer(csvfile)
        w.writerow(n)
        for line in sn_file:
            user = line.strip()
            parameters = [("screen_name", user),("count",100)]
            response = twitterreq(url, "GET" ,parameters)
     #   resp =response.read()
       # reader = codecs.getreader("utf-8")
        #obj =json.load(reader(response))
            str_response =response.read().decode('utf-8')
        #obj = json.loads(str_response)
            json_load=json.loads(str_response)
            for p in json_load :
                w.writerow((user,p['text']))
                print(user,",",p['text'])
            #w.writerow((p['text']))
        #texts =json_load['text']
        #coded =texts.encode('utf-8')
        #s =str(coded)
        #print(s[2:-1])
	        #for tweet in response
        #print(tweet['text'].encode('utf-8'))
        #print(user)
   # writer = csv.writer(sys.stdout)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Enter the command')
    parser.add_argument('-term', help='Enter the search term')
    parser.add_argument('-file', help='Enter the user name file')
    opts = parser.parse_args()
    if opts.c == "fetch_samples":
        fetch_samples()
    elif opts.c == "fetch_by_terms":
        term = opts.term
        print (term)
        fetch_by_terms(term)
    elif opts.c == "fetch_by_user_names":
        user_name_file = opts.file
        fetch_by_user_names(user_name_file)
    else:
        raise Exception("Unrecognized command")


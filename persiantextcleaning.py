#stop_words = ['یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه','ده','بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود','صد','یازده', 'دوازده']
import string
import re

def remove_emojis(data):
    emoj = re.compile("["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      u"\U00002500-\U00002BEF"  # chinese char
      u"\U00002702-\U000027B0"
      u"\U00002702-\U000027B0"
      u"\U000024C2-\U0001F251"
      u"\U0001f926-\U0001f937"
      u"\U00010000-\U0010ffff"
      u"\u2640-\u2642" 
      u"\u2600-\u2B55"
      u"\u200d"
      u"\u23cf"
      u"\u23e9"
      u"\u231a"
      u"\ufe0f"  # dingbats
      u"\u3030"
                    "]+", re.UNICODE)
    return re.sub(emoj, '', data)



def clean_persian_text(tweet,minimum_character_len=3,stop_words_path='stop_words.txt'):
    
    # list_hashtags = []
    # list_mentions = []
    tweet= tweet.replace("،"," ")
    new_tweet = ""
    
    with open(stop_words_path,'r',encoding='utf-8') as stop_words_file:
      stop_words_txt = stop_words_file.read()

    stop_words = [stop_word for stop_word in stop_words_txt.split()]
    
    # delete stop words
    
    new_tweet = tweet
    for word in tweet.split():
        if word in stop_words:
            continue 
    ####################################################    
    ####################################################    you can uncomment here to extract Hashtgs and mentions
    ####################################################
    #   elif "#" in word:
    #         list_hashtags.append(word)

    #     elif "@" in word:
    #         list_mentions.append(word)    
        
        else:
            new_tweet += " "+word


    # new_tweet = clean(new_tweet,to_ascii=0,no_emoji=1,no_digits=1,no_urls=1,no_punct=1,replace_with_url="<URL>",replace_with_punct=" ",replace_with_digit="")
    new_tweet = remove_emojis(new_tweet)
    # remove english alphabets
    new_tweet = re.sub(r'\s*[A-Za-z]+\b', '' , new_tweet)
    # removw all numerics
    new_tweet = new_tweet.translate(str.maketrans('', '', string.digits+'۰۱۲۳۴۵۶۷۸۹'))
    new_tweet = new_tweet.translate(str.maketrans('', '', string.digits+'0123456789'))
    # remove all links
    new_tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '<URL>', new_tweet, flags=re.MULTILINE,)
    # remove all punctuations
    new_tweet = new_tweet.translate(str.maketrans('', '', string.punctuation))
    # all lines in one
    new_tweet = new_tweet.replace("\n"," ")
    # delete extra spaces
    new_tweet = re.sub("  +"," ",new_tweet)

    if len(new_tweet) < minimum_character_len:
      return None

    return new_tweet#,list_hashtags,list_mentions









import re

def has_ip(url):
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

def chklength(url): 
 return(len(url)) 

def chkhttps(url):
     if url.startswith('https'):
         return 1 
     else:
         return 0 
     
def chkdot(url):
    return url.count('.')

def chkat(url):
    if '@' in url:
        return 1
    else:
        return 0

def chkhyphen(url):
    if '-' in url:
        return 1
    else:
        return 0
    
def chkslash(url):
    if '/' in url:
        return 1
    else:
        return 0
    
def chkbig(url):
    if(chklength(url) > 75):
        return 1
    else:
        return 0

def chkdigits(url):
    return sum(c.isdigit() for c in url)

def chkkeywords(url):
    keywords = ['login', 'secure', 'bank', 'account', 'verify', 'update', 'free', 'click', 'offer', 'password']
    return sum(word in url.lower() for word in keywords)

def special_chars(url):
    return sum(not c.isalnum() for c in url)
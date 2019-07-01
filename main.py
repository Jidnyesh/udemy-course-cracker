from requests import get
from pattern.web import plaintext
import sys
import webbrowser

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

with open('wordlist.txt','r') as wordl:
    wordlist = wordl.readlines()
    wordl.close()
wordlist = [x.strip() for x in wordlist]

course = input('Paste the url of course you want to crack\n')
price = input('What is the current price of the course\n')

compare = 'Current price: FreeOriginal price: ₹'+price+'Discount:100'

def attack(course):
    for word in wordlist:
        url = course+'?couponCode='+word
        print("Trying : "+word)
        htmlString = get(url,headers=headers).text
        webText = plaintext(htmlString)
        if compare in webText:
            print('\n' + word + ' is the coupon code for the course and it is free now')
            webbrowser.open_new_tab(url)
            sys.exit()  
attack(course=course)

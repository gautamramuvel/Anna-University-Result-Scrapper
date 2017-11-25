from bs4 import BeautifulSoup 
import requests

def solve():
    page = requests.get("http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl?regno="+str(roll))
    soup = BeautifulSoup(page.content, "html.parser")
    if page.status_code == 200:
        links = soup.find(text="Subject Code").find_parent("table")
        for link in links.find_all("strong"):
            print(link.text, end="\t")
            if link.text == "Result":
                print(end="\n\t")
    else:
        solve()

roll=str(input("Enter the roll number: "))
if len(roll) == 12:
    solve()
else:
    print("Enter correct roll number!")
    


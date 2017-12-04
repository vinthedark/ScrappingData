import google
import requests
import lxml.html as lh
from bs4 import BeautifulSoup

def get_galco_info(result):
    response = requests.post(result)
    trees = lh.document_fromstring(response.content).xpath('//*[@id="specs"]/div/div')
    try:
        print ("Im coming in galco")
        json_content = {}
        for tree in trees:
            galco_soup = BeautifulSoup(lh.tostring(tree, pretty_print=True), "lxml")
            row_divs = galco_soup.findAll("div", { "class" : "row" })
            for inside_div in row_divs:
                print inside_div.findAll("div", { "class" : "row" })
        print json_content
    except Exception as e:
        print e

search_results = google.search("1485D60", stop=2)
for result in search_results:
    print result
    url_link = result.split(".")
    if url_link[1] == "galco":
        get_galco_info(result)
    response = requests.post(result)
    trees = lh.document_fromstring(response.content).xpath('//*[@id="productPage"]/div[5]/div')
    for tree in trees:
        soup = BeautifulSoup(lh.tostring(tree, pretty_print=True), "lxml")
        json_content = {}
        uls = soup.find_all('ul')
        for ul in uls:
            for item in [li.text.strip() for li in ul.find_all('li')]:
                split_values = item.split('\n')
                print split_values
                #json_content[split_values[0]] = split_values[1]
        print json_content

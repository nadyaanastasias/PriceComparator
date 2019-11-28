from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import json

def scrap(keyword):
    page_url = "https://www.orami.co.id/c/" + keyword + "?page=1"


    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    containers_box = page_soup.findAll("div", {"class": "wrap-widget"})

    sumproducts = page_soup.find("div", {"class": "paging"})
    listsp = sumproducts.text.strip().split()
    json_dict = []

    for i in listsp:
        
        page_url = "https://www.orami.co.id/c/" + keyword + "?page="+ i
        uClient = uReq(page_url)

        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        containers_box = page_soup.findAll("div", {"class": "wrap-widget"})

        sumproducts = page_soup.find("div", {"class": "paging"})
        listsp = sumproducts.text.strip().split()
        
        for container_box in containers_box:
            container_name = container_box.find("div", {"class": "prod-name"})
            # print(container_name.text.strip())
            name = container_name.text.strip()

            container_price = container_box.find("div", {"class": "disc-price"})
            if (container_price is None):
                container_nprice = container_box.find("p", {"class": "price"})
                # print(container_nprice.find(text=True, recursive=False))
                price = container_nprice.find(text=True, recursive=False).strip()
            else:
                # print(container_price.find(text=True, recursive=False))
                price = container_price.find(text=True, recursive=False).strip()

            json_dict.append({'nama': name, 'harga': price})


    return(json.dumps(json_dict))





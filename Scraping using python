import requests
from bs4 import BeautifulSoup

#1:https://produto.mercadolivre.com.br/MLB-3318866513-camisa-fluminense-oficial-1-2324-umbro-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=d830f11f-cf22-4a8f-ba16-731906f38fac&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=ZGQ4MDBlNWUtZjRjOC00YTEzLWE4YzItNTgyZjdkMWRmYmNi


response  = requests.get("https://produto.mercadolivre.com.br/MLB-3318866513-camisa-fluminense-oficial-1-2324-umbro-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=d830f11f-cf22-4a8f-ba16-731906f38fac&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=ZGQ4MDBlNWUtZjRjOC00YTEzLWE4YzItNTgyZjdkMWRmYmNi")

text = BeautifulSoup(response.text, 'html.parser')

nome = text.find('h1',{'class':'ui-pdp-title'}).text
price_element = text.find('span', {'class': 'andes-money-amount__fraction'}).text
desc = text.find('p',{'class':'ui-pdp-description__content'}).text


print("O nome do produto: "+nome)
print("O preço: "+str(price_element))
print("Descrição: "+str(desc))







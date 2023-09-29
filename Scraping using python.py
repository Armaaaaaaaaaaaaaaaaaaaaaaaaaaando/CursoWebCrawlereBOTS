import requests
from bs4 import BeautifulSoup

#1: https://produto.mercadolivre.com.br/MLB-3318866513-camisa-fluminense-oficial-1-2324-umbro-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=d830f11f-cf22-4a8f-ba16-731906f38fac&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=ZGQ4MDBlNWUtZjRjOC00YTEzLWE4YzItNTgyZjdkMWRmYmNi
#2 https://www.retrogol.com.br/idolos-eternos/camisa-fluminense-bordo-2022-masculina?parceiro=4473&parceiro=4376&gad=1&gclid=CjwKCAjw69moBhBgEiwAUFCx2NhStOo7R49HvDmM5vpx7nYolRYH-w_dK0Xz2jWkvwm57YoUsvnM0RoCNbEQAvD_BwE&variant_id=9866


response  = requests.get("https://produto.mercadolivre.com.br/MLB-3318866513-camisa-fluminense-oficial-1-2324-umbro-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=d830f11f-cf22-4a8f-ba16-731906f38fac&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=ZGQ4MDBlNWUtZjRjOC00YTEzLWE4YzItNTgyZjdkMWRmYmNi")

text = BeautifulSoup(response.text, 'html.parser')

nome = text.find('h1',{'class':'ui-pdp-title'}).text
price_element = text.find('span', {'class': 'andes-money-amount__fraction'}).text
desc = text.find('p',{'class':'ui-pdp-description__content'}).text


print("O nome do produto: "+nome)
print("O preço: "+str(price_element))
print("Descrição: "+str(desc))


print()
print("Segundo produto")

response  = requests.get("https://www.retrogol.com.br/idolos-eternos/camisa-fluminense-bordo-2022-masculina?parceiro=4473&parceiro=4376&gad=1&gclid=CjwKCAjw69moBhBgEiwAUFCx2NhStOo7R49HvDmM5vpx7nYolRYH-w_dK0Xz2jWkvwm57YoUsvnM0RoCNbEQAvD_BwE&variant_id=9866")
text = BeautifulSoup(response.text, 'html.parser')
nome = text.find('h1',{'class':'product-name'}).text
price_element = text.find('span', {'class': 'data-app'}).text


print("Nome do produto: "+nome)
print("O preço: "+str(price_element))










import requests
from bs4 import BeautifulSoup


resposta = requests.get("https://posdigital.uninassau.edu.br/curso?type=pos&area1=business-intelligence&area2=e-commerce&area3=marketing-digital")     #Escolhemos um site especifico para verificar
print("Status code:", resposta.status_code)  

print(type(resposta.content))                               # Trás pra gente o tipo da váriavel em que o conteúdo está armazenado
conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')  
print(type(site))

area = site.find( 'div', attrs={'class': 'course-banner__text'})  
#print(area)

#     <h1>
       # Pós-graduação em Business Intelligence, E-commerce e Marketing Digital
      #</h1>
titulo = area.find('h1')
print(titulo.text)
   

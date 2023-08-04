import requests
from requests.models import Response
import bot

def api(address):
    url= "https://api.unmarshal.com/v1/bsc/address/"+address+"/assets?auth_key=your_key" 
    
    response = requests.get(url)
    bot.address_content = response.json()
    api.statuscode = response.status_code

import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")


body={"username":str(os.getenv("NAME")),"password":str(os.getenv("PASSWORD"))}

print(str(os.getenv("NAME")))
print(str(os.getenv("PASSWORD")))

x=requests.post("https://registre-national-entreprises-pprod.inpi.fr/api/sso/login",json=body)

print(x.text)

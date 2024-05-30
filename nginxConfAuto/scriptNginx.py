import jinja2
import os
from dotenv import load_dotenv

load_dotenv()

WEB_SECURITY = os.getenv('WEB_SECURITY')
WEB_SECURITY = WEB_SECURITY.upper()

if WEB_SECURITY == 'TRUE':
	
	templateElection = 'nginx_security.template'

else:

	templateElection = 'nginx_no_security.template'

template = open(templateElection, 'r+')
readTemplate = template.read()
template.close()

jtemplate = jinja2.Template(readTemplate)

renderJ2 = jtemplate.render(DOMAIN_SERVER=os.getenv('DOMAIN_SERVER'), IP_SERVER=os.getenv('IP_SERVER'))

config = open('nginx.conf', 'w')
config.write(renderJ2)
config.close
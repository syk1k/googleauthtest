from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
gauth.LoadClientConfigFile('media/credentials/client_secrets.json')
gauth.LocalWebserverAuth(host_name='localhost', port_numbers=[8080])
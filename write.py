import os
from requests_oauthlib import OAuth2Session
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Определение абсолютного пути к файлу credentials.json
file_path = os.path.expanduser('~/PycharmProjects/Skill_Requirements/key/credentials.json')

# Настройки авторизации Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)
client = gspread.authorize(credentials)

# Открытие таблицы по URL
sheet_url = "https://docs.google.com/spreadsheets/d/1F9x2Q9zUMF7XxOcIbS6747hmE95EWz8pBmIGjwF962E/edit?usp=sharing"
spreadsheet = client.open_by_url(sheet_url)

# Получение листа по имени
worksheet = spreadsheet.worksheet("Data_LinkedIn")




client_id = '77s31g2rysv70h'
client_secret = 'kwRU4UkX2CziWs8z'
redirect_uri = 'http://localhost:8080/callback'
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

linkedin = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Получаем ссылку для авторизации
authorization_url, state = linkedin.authorization_url(authorization_base_url)

print('Перейдите по следующей ссылке для авторизации:', authorization_url)

# Получаем код авторизации, который будет использоваться для получения токена доступа
authorization_response = input('Введите полный URL-адрес после перенаправления: ')
linkedin.fetch_token(token_url, client_secret=client_secret, authorization_response=authorization_response)

# Теперь у нас есть токен доступа и мы можем делать запросы к API
response = oauth2_session.get('https://api.linkedin.com/v1/job-search?keywords=data%20science&count=10')
print(response.json())



# # Пример записи данных в Google Sheets
# for result in search_results:
#     profile = linkedin.get_profile(result)
#     print(profile)
#     # worksheet.append_row(profile)

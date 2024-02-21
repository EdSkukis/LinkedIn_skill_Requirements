import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os


# Определение абсолютного пути к файлу credentials.json
file_path = os.path.expanduser('~/PycharmProjects/Skill_Requirements/key/credentials.json')

# Настройки авторизации
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)

# Авторизация и открытие таблицы
client = gspread.authorize(credentials)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1F9x2Q9zUMF7XxOcIbS6747hmE95EWz8pBmIGjwF962E/edit?usp=sharing").sheet1

# Получение данных из таблицы в виде списка списков
data = sheet.get_all_values()

# Создание DataFrame из данных
df = pd.DataFrame(data[1:], columns=data[0])

# Анализ данных
top_skills = df.iloc[:, 5:15].stack().value_counts().head(7)
top_requirements = df.iloc[:, 15:].stack().value_counts().head(7)

# Вывод результатов анализа
print("Топ 7 навыков:")
print(top_skills)
print("\nТоп 7 требований:")
print(top_requirements)

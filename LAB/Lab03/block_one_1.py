import pickle

# Данные: имя рабочего -> зарплаты по годам (2016-2020)
workers = {
    'Иванов': {2016: 50000, 2017: 52000, 2018: 51000, 2019: 53000, 2020: 55000},
    'Петров': {2016: 48000, 2017: 49000, 2018: 47000, 2019: 46000, 2020: 51000},
    'Сидоров': {2016: 55000, 2017: 56000, 2018: 57000, 2019: 58000, 2020: 59000},
    'Кузнецов': {2016: 45000, 2017: 46000, 2018: 45500, 2019: 44000, 2020: 47000},
    'Морозов': {2016: 53000, 2017: 54000, 2018: 52000, 2019: 51000, 2020: 53000},
    'Новиков': {2016: 47000, 2017: 48000, 2018: 46000, 2019: 45000, 2020: 49000},
    'Федоров': {2016: 51000, 2017: 51500, 2018: 50000, 2019: 49500, 2020: 52000},
}

# 1. Вывести список рабочих и их среднюю зарплату за 5 лет
print("Средняя зарплата работников за 2016-2020:")
for worker, salaries in workers.items():
    avg_salary = sum(salaries.values()) / len(salaries)
    print(f"{worker}: {avg_salary:.2f}")

print()

# 2. Для каждого рабочего найти год с минимальной зарплатой
print("Год с минимальной зарплатой для каждого рабочего:")
for worker, salaries in workers.items():
    min_year = min(salaries, key=salaries.get)
    min_salary = salaries[min_year]
    print(f"{worker}: {min_year} ({min_salary})")

print()

# 3. Рабочие с минимальной и максимальной зарплатой в 2019 году
salaries_2019 = {w: s[2019] for w, s in workers.items()}
min_2019_worker = min(salaries_2019, key=salaries_2019.get)
max_2019_worker = max(salaries_2019, key=salaries_2019.get)
print(f"Минимальная зарплата в 2019: {min_2019_worker} ({salaries_2019[min_2019_worker]})")
print(f"Максимальная зарплата в 2019: {max_2019_worker} ({salaries_2019[max_2019_worker]})")

print()

# 4. Рабочие, у которых зарплата в 2018 была меньше, чем в 2020 более чем на 10%
print("Рабочие, у которых зарплата в 2018 была более чем на 10% меньше, чем в 2020:")
for worker, salaries in workers.items():
    salary_2018 = salaries[2018]
    salary_2020 = salaries[2020]
    if salary_2018 < salary_2020 * 0.9:
        print(f"{worker}: 2018 = {salary_2018}, 2020 = {salary_2020}")

# Сохраняем словарь в бинарный файл
with open('data.pickle', 'wb') as f:
    pickle.dump(workers, f)

# Читаем обратно из файла и выводим для проверки
with open('data.pickle', 'rb') as f:
    loaded_workers = pickle.load(f)

print("\nДанные успешно загружены из файла:")
for w in loaded_workers:
    print(w, loaded_workers[w])

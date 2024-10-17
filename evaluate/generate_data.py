import matplotlib.pyplot as plt
import numpy as np

# Пример данных для графиков
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [120, 150, 100, 170, 200, 180]

brands = ['Хавалы', 'Фрицы', 'Пендосия', 'Буханочка']
sales_by_brand = [300, 200, 150, 350]

# График ежемесячных продаж
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('monthly_sales.png')
plt.close()

# График распределения продаж по брендам
plt.figure(figsize=(10, 6))
plt.bar(brands, sales_by_brand, color=['blue', 'green', 'red', 'purple'])
plt.title('Sales by Brand')
plt.xlabel('Brand')
plt.ylabel('Sales')
plt.savefig('brand_distribution.png')
plt.close()

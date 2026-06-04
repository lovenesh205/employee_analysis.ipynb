from sqlalchemy import create_engine

# Replace with your own MySQL username, password, and database name
engine = create_engine("mysql+pymysql://root:october2006@localhost/employee_db")



import pandas as pd

# Load all employees
df = pd.read_sql("SELECT * FROM employees", engine)
print(df.head(20))



# Employees hired after 2018
df_hired = pd.read_sql("SELECT * FROM employees WHERE hire_date > '2018-01-01'", engine)

# Average salary by department
avg_salary = pd.read_sql("""
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
""", engine)
print(avg_salary)



import matplotlib.pyplot as plt

# Example: Salary distribution
df['salary'].hist(bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()













# =====================================================================
#                          Section A only Answers
# =====================================================================
# 1. B
# 2. B
# 3. C
# 4. A
# 5. D
# 6. B
# 7. A
# 8. C
# 9. B
# 10.B
# =====================================================================
#                          Section B only Answers
# =====================================================================
#11.
#a.  Sara 80
#  Ali 65
#  John 90
#b.
# for name, marks in students.items():
#     average = calculate_average(marks)
#     if average >= 80:
#         print(name, average)
#C.
#It returns a view of the dictionary's key-value pairs.
#d.
#It raises a ZeroDivisionError because len([]) is 0, and division by zero is not allowed.

#12.
#a.
# SELECT c.Name, SUM(o.Amount) AS TotalAmount
# FROM Customers c
# JOIN Orders o ON c.CustomerID = o.CustomerID
# GROUP BY c.Name;
#b.
# HAVING SUM(o.Amount) > 3000;
#c.
#Sara: 2000 + 3000 = 5000
#d.
#LEFT JOIN

#13.
#a.65
#b.The condition keeps values ≥ 65, so selected = [65 80 95]
#c.selected.size returns the total number of elements in the NumPy array

#14.
#a. df.isnull().sum()
#b. df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
#c. The IT salaries are 50000, 43750 and 40000. The mean is 133,750/3 = 44,583.33
#d.Mean imputation can distort the data distribution and may introduce bias, especially when different departments have different salary patterns

# =====================================================================
#                          Section C only Answers
# =====================================================================
#15.B
#16.D
#17.C
#18.B
#19.B
#20.B
#21.C
#22.B
#23.B
#24.B
#25.B
#26.A
#27.B
#28.B
#29.C
# =====================================================================
#                          Section D only Answers
# =====================================================================
#30.
#a. 
# import pandas as pd
# df = pd.read_csv("retail_sales.csv")
# print(df.head())
# df.info()
# print(df.isnull().sum())
#b.
#df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
#c.
# df["Sales"] = df["Quantity"] * df["Unit_Price"]
# category_sales = df.groupby("Category")["Sales"].sum()
# category_sales = category_sales.sort_values(ascending=False)
# print(category_sales)

#31.
#a
# import pandas as pd
# df = pd.read_csv("student_performance.csv")
# print(df.head())
# print(df.isnull().sum())
# correlation = df["Study_Hours"].corr(df["Final_Score"])
# print("Correlation:", correlation)

#b.
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# df = pd.read_csv("student_performance.csv")
# df = df.dropna(subset=["Study_Hours", "Final_Score"])

# Define input feature and target
# X = df[["Study_Hours"]]
# y = df["Final_Score"]

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("Predicted Final Scores:", y_pred)
# print("Actual Final Scores:")
# print(y_test.tolist())
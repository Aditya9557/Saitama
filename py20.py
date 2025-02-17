import pandas as pd


data ={'Department':['HR','IT','IT','HR','Finance'],
      'Employee':['John','Jas','Karan','Preet','Eve'],
       'Salary':[50000,60000,55000,52000,70000]
       }
df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()

print(result)

df.to_csv("outpt.csv",index= True)

df.to_excel("ou.xlsx",index=True)

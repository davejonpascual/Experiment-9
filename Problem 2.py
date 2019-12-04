import pandas as pd
a1={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length', 'Width','Height','Length','Width','Height'],
    'Value':[6,4,2,5,3,4]}
Df=pd.DataFrame(a1,columns=['Box','Dimension','Value'])
tidy=Df.pivot_table(index=['Box'],columns='Dimension',values='Value')
Data=tidy.insert(3,'Volume',[48,60],True)
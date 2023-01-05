import pandas as pd

krx_list = pd.read_html('C:/Users/kk234/Desktop/python_for_money/sangjang.xls')
#print(krx_list[0])

krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
print(krx_list[0])



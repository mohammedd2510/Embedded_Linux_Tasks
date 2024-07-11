import csv
import pandas as pd
from bs4 import BeautifulSoup
fs = open("./build/doc_doxygen/html/classled.html","r")
html_content = fs.read()
fs.close()
soup = BeautifulSoup(html_content,'lxml')
contents = soup.find("div",class_="contents")
functions_section = contents.find_all("div",class_="memitem")
print(functions_section)
func_params_html=[]
func_breifs=[]
func_signature=[]
func_returns=[]
func_params=[]
for func in functions_section:
    func_signature.append(func.find("td",class_="memname").text)
    func_breifs.append(func.find("p").text)
    params=(func.find("table",class_="params").find_all("td",class_="paramname")) 
    param_list=[]
    for i in params:     
        param_list.append(i.text) 
    func_params.append(", ".join(param_list))   
    func_returns.append(func.find("dl",class_="section return").find("dd").text)
"""
using csv module

with open("output.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Signature","Breif",'Parameters','Return'])
    for i in range(len(functions_section)):
        writer.writerow([func_signature[i],func_breifs[i],func_params[i],func_returns[i]])
"""
"""
using Pandas module
"""
data = {
    "Signature":func_signature,
    "Breif":func_breifs,
    "Parameters":func_params,
    "Return":func_returns
}
df = pd.DataFrame(data)
df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)








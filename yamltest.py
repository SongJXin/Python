import yaml  
  
#读取文件  
f = open(r"C:\Users\songjl\Documents\GitHub\appiumnAuto\devices.yaml",encoding='utf-8')  
  
#导入  
x = yaml.load(f)  
  
print (x)  

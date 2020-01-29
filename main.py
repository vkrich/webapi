import requests as rq
numbers=[]

with open('dataset_24476_3.txt','r') as f:
  for i in f:
    numbers.append(int(i))
  f.close()

for i in numbers:
  api_url = 'http://numbersapi.com/' + str(i) + '/' + 'math'

  param = {
    'type': 'math', 
    'number': i,
    'json': 'application/json'
  }

  res = rq.get(api_url, params = param)

  data=res.json()
  with open('output.txt','a') as f1:
    if data['found']:
      f1.write('Interesting'+'\n')
    else:
      f1.write('Boring'+'\n')

f1.close()    
  
  
  
  



import os, pickle,  re, urllib
	
dat = 'st40/all_horses.dat'
URL = 'http://localhost:81/cgi-bin/lab3.py'

def read_from_file(name):
    with open(name, 'rb') as f:
        new_stable = pickle.load(f)
        f.close()
    print('Success! filee')
    return new_stable
	
def main():
 new_stable = read_from_file(dat)
 student_num = re.search(r'student=(\d+)\">\[' + str(40) + '\]', str(urllib.request.urlopen(URL).read())).group(1)
 #print('student =' + student_num)
 
 for horse in new_stable:
   data = horse.get_horse()
   print('2')
   #row = data[0] 
   type = data.get('type_of_sport')
   #print(type)   
 
   if type is None: 
      action = 'add_horse'
   else: 
      action = 'add_sport_horse'

   parameters = {**data, **{'student': student_num,'action': action }}

   _url = URL + '?' + urllib.parse.urlencode(parameters)
   print('Sent to url: ' + _url)
   urllib.request.urlopen(_url)	


	

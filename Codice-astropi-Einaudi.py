from sense_hat import SenseHat
from time import sleep
import time
sense = SenseHat()

def get_sense_data():
  sense_data=[]
  sense_data.append(sense.get_temperature())
  sense_data.append(sense.get_humidity())
  sense_data.append(sense.get_pressure())
  sense_data.append(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
  return sense_data
  
def log_data(sense_data):
  f=open('dati.txt','a')
  f.write(str(sense_data)+'\n')
  f.close()

def display(v=5,min=0,max=80):
  delta=(max-min)/8
  led=int((v-min)/delta)
  tone=int((v-min)/(max-min)*254)
  if led==8:
    led=7
         
  for i in range(7):
      for j in range(8):
        color=sense.get_pixel(i+1,j)
        sense.set_pixel(i,j,color)

  for j in range(8):
      if j<=led:
        sense.set_pixel(7,7-j,tone,128,255-tone)
      else:   
        sense.set_pixel(7,7-j,0,0,0)
        
def logomax():
  sense.clear()
  B=(255,0,0)
  N=(0,0,0)
  snow=[
  N,N,N,N,N,N,N,N,
  N,B,N,B,N,B,N,N,
  N,N,B,B,B,N,N,N,
  N,B,B,B,B,B,N,N,
  N,N,B,B,B,N,N,N,
  N,B,N,B,N,B,N,N,
  N,N,N,N,N,N,N,N,
  N,N,N,N,N,N,N,N,
  ]
  sense.set_pixels(snow)
  sleep(1)
  sense.clear()
  
def logomin():
  sense.clear()
  B=(0,0,255)
  N=(0,0,0)
  snow=[
  N,N,N,N,N,N,N,N,
  N,B,N,B,N,B,N,N,
  N,N,B,B,B,N,N,N,
  N,B,B,B,B,B,N,N,
  N,N,B,B,B,N,N,N,
  N,B,N,B,N,B,N,N,
  N,N,N,N,N,N,N,N,
  N,N,N,N,N,N,N,N,
  ]
  sense.set_pixels(snow)
  sleep(1)
  
sense.clear()
  
sense_data=["Temperature","Humidity","pressure","date-time"]
f=open('dati.txt','w')
f.write(str(sense_data)+'\n')
f.close()

t=sense.get_temperature()
sense.show_message('temp.')
min=t*0.99
max=t*1.01
count =0
datum=0

while 1:
  count=count+1
  if count == 30:
    datum=1
    sense.show_message('humid.')
    t=sense.get_humidity()
    sense.show_message(str(int(t)))
    min=t*0.99
    max=t*1.01
  if count== 60:
    datum=2
    t=sense.get_pressure()
    sense.show_message(str(int(t)))
    min=t*0.99
    max=t*1.01
    sense.show_message('press.')
  if count==90:
    sense.show_message('temp.')
    t=sense.get_temperature()
    sense.show_message(str(int(t)))
    min=t*0.99
    max=t*1.01    
    count=0
    datum=0
    
  sleep(1)
  sense_data = get_sense_data()
  log_data(sense_data)
  t=sense_data[datum]
  if t>=max:
    max=t*1.01
    logomax()
  if t <= min:
    min=t*0.99
    logomin()
  display(t,min,max)

from ast import Lambda
import csv
from dataclasses import replace
import pandas as pd

info = pd.read_csv('./final_df.csv')
planets = pd.DataFrame(info)

planets['Radius']=planets['Radius'].to_string()
planets['Radius']=planets['Radius'].apply(lambda  x: x.replace('$', '').replace(',', '')).astype('float')

radius = planets['Radius'].to_list()
mass = planets['Mass'].to_list()
gravity = []

def convert_to_si(radius,mass):
  for i in range(0,len(radius)-1):
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30

convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
  G = 6.674e-11
  for index in range(0,len(mass)):
    g = (mass[index]*G)/((radius[index])**2)
    gravity.append(g)

gravity_calculation(radius,mass)

planets['Gravity'] = gravity
print(planets['Gravity']) 
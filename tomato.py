# -*- coding: utf-8 -*-
"""
Tomato

Created on Thu Jun  4 14:08:36 2020

@author: ecwal
"""
import time

class Plant :
    
    def __init__(self, plant_type, status = 'healthy',
                 age_group = 'baby_plant', epoch_age = time.time(),
                 watered = True, last_watered = time.time(),
                 fed = True, last_fed = time.time(),
                 harvested = 0, last_harvested = time.time()) :
        self.plant_type = plant_type
        self.status = status
        self.age_group = age_group
        self.epoch_age = epoch_age
        self.watered = watered
        self.last_watered = last_watered
        self.fed = fed
        self.last_fed = last_fed
        self.harvested = harvested
        self.last_harvested = last_harvested
    
    def to_grow(self):
        if self.age_group == 'adult_plant' :
            pass
        elif time.time() - self.epoch_age > 120 :
            self.age_group = 'adult_plant'
        elif time.time() - self.epoch_age > 60 :
            self.age_group = 'young_plant'
        
    def needs_water(self) :
        water_freq = 15
        if self.last_watered < (time.time() - water_freq) :
            self.watered = False
            #return 'Your {} plant needs water.'.format(self.plant_type)
        #else :
            #return 'Your {} plant does not need water.'.format(self.plant_type)
        
    def water_me(self) :
        self.watered = True
        self.last_watered = time.time()
        return 'You just watered your {} plant.'.format(self.plant_type)
    
    def needs_feed(self) :
        feed_freq = 25
        if self.last_fed < (time.time() - feed_freq) :
            self.fed = False
            #return 'Your {} plant needs feed.'.format(self.plant_type)
        #else :
            #return 'Your {} plant does not need feed.'.format(self.plant_type)
    
    def feed_me(self) :
        self.fed = True
        self.last_fed = time.time()
        return 'You just fed your {} plant.'.format(self.plant_type)
    
    def harvest_me(self) :
        harvest_freq = 15
        if self.age_group != 'adult_plant' :
            return 'Your {} plant is too young to harvest.'.format(self.plant_type)
        elif self.status != 'healthy' :
            return 'Your {} plant not healthy enough to harvest.'.format(self.plant_type)
        elif self.last_harvested <  (time.time() - harvest_freq) :
            self.last_harvested = time.time()
            self.harvested += 1
            return 'You just harvested your {} plant.'.format(self.plant_type)
        else :
            return "There's nothing to harvest right now."
            
    def check_status(self) :
        feed_freq = 25
        water_freq = 15
        if self.age_group != 'adult_plant' :
            pass
        elif self.last_watered < (time.time() - water_freq*2) :
            if self.last_watered < (time.time() - water_freq*4) :
                self.status = 'dead'
            else :
                self.status = 'sick'
        elif self.last_fed < (time.time() - feed_freq*2) :
            if self.last_fed < (time.time() - feed_freq*4) :
                self.status = 'dead'
            else :
                self.status = 'sick'
        else :
            self.status = 'healthy'
        



def check_water_feed() :
    plant_one.needs_water()
    plant_one.needs_feed()
    if plant_one.watered == False :
        if plant_one.fed == False :
            label['text'] = 'Your {} plant needs water and feed.'.format(plant_one.plant_type)
        else :
            label['text'] = 'Your {} plant needs water.'.format(plant_one.plant_type)
    elif plant_one.fed == False :
        label['text'] = 'Your {} plant needs feed.'.format(plant_one.plant_type)
    else :
        label['text'] = 'Your {} plant has everything it needs!'.format(plant_one.plant_type)

def water_plant():
    plant_one.water_me()
    plant_one.check_status()
    label['text'] = 'You watered your {} plant.'.format(plant_one.plant_type)
    
def feed_plant():
    plant_one.feed_me()
    plant_one.check_status()
    label['text'] = 'You just fed your {} plant.'.format(plant_one.plant_type)

def check_age_group():
    plant_one.to_grow()
    if plant_one.age_group == 'adult_plant' :
        plant_one_photo = tk.PhotoImage(master = root, file='adult_tomato.png')
        label['text'] = 'Your {} plant is fully grown.'.format(plant_one.plant_type)
    elif plant_one.age_group == 'young_plant' :
        plant_one_photo = tk.PhotoImage(master = root, file='young_tomato.png')
        label['text'] = 'Your {} plant is growing up!'.format(plant_one.plant_type)
    else :
        plant_one_photo = tk.PhotoImage(master = root, file='baby_tomato.png')
        label['text'] = 'Your {} plant is still a baby'.format(plant_one.plant_type)
    plant_one_button.configure(image=plant_one_photo)
    plant_one_button.image = plant_one_photo
    
def harvest_plant():
    #plant_one.harvest_me()
    label['text'] = plant_one.harvest_me()
    harvest_label['text'] = 'Fruit harvested: {}.'.format(plant_one.harvested)

def check_plant_status():
    plant_one.check_status()
    if plant_one.status == 'sick' :
        label['text'] = 'Oh no! Your {} plant is sick.'.format(plant_one.plant_type)
    if plant_one.status == 'dead' :
        label['text'] = 'Your {} plant is dead! Game over.'.format(plant_one.plant_type)
        
"""Not currently in use:
def tick(interval, function, *args):
    root.after(interval - timer() % interval, tick, interval, function, *args)
    function(*args) # assume it doesn't block
"""

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

background_image = tk.PhotoImage(master = root, file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)


#Intantiate tomato plant and set picture
plant_one = Plant('tomato', epoch_age=time.time(), last_harvested=time.time())
plant_one.to_grow()
if plant_one.age_group == 'adult_plant' :
    plant_one_photo = tk.PhotoImage(master = root, file='adult_tomato.png')
elif plant_one.age_group == 'young_plant' :
    plant_one_photo = tk.PhotoImage(master = root, file='young_tomato.png')
else :
    plant_one_photo = tk.PhotoImage(master = root, file='baby_tomato.png')
    
root.after(60000, check_age_group)
root.after(120000, check_age_group)

#Check status
root.after(180000, check_plant_status)
root.after(210000, check_plant_status)
root.after(240000, check_plant_status)
root.after(270000, check_plant_status)
root.after(300000, check_plant_status)
root.after(330000, check_plant_status)
root.after(360000, check_plant_status)
root.after(390000, check_plant_status)
root.after(420000, check_plant_status)
root.after(450000, check_plant_status)
root.after(480000, check_plant_status)
root.after(510000, check_plant_status)

#Action buttons
plant_one_button = tk.Button(root, image = plant_one_photo,
                         command = check_water_feed)
plant_one_button.place(relx = 0.35, rely = 0.3)

water_button = tk.Button(root, bg = 'blue', text = 'Water', 
                               command = water_plant)
water_button.place(relx = 0, rely = 0)

feed_button = tk.Button(root, text='Feed', bg='brown',
                             command=feed_plant)
feed_button.place(relx=0.35, rely=0)

harvest_button = tk.Button(root, text='Harvest', bg='red',
                             command=harvest_plant)
harvest_button.place(relx=0.6, rely=0)

#Info & harvest labels
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, bg = 'white')
label.pack()

harvest_label = tk.Label(root, bg='white', text='Fruit harvested: 0')
harvest_label.pack(side='right')

root.mainloop()



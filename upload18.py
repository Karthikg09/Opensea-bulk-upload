import tkinter
import subprocess
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from turtle import width
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO
import os
import io
import sys
import pickle
import time
from decimal import *
import webbrowser
# from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import timedelta  
from dateutil.relativedelta import relativedelta
from datetime import timedelta, date
import locale
import json 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#check local date format
locale.setlocale(locale.LC_ALL, '')
lastdate = date(date.today().year, 12, 31)

root = Tk()
root.geometry('750x850')
root.resizable(False, False)
root.title("NFTs Upload to OpenSea v1.8")
  
input_save_list = ["NFTs folder :", 0, 0, 0, 0, 0, 0, 0, 0, 0]
main_directory = os.path.join(sys.path[0])


def supportURL():
    webbrowser.open_new("https://www.infotrex.net/opensea/support.asp?r=app")

def coffeeURL():
    webbrowser.open_new("https://github.com/infotrex/bulk-upload-to-opensea/#thanks")

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
# imageurl = "https://www.infotrex.net/opensea/header.png"
imageurl = "data:image/jpeg;base64,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"
img = WebImage(imageurl).get()
imagelab = tk.Label(root, image=img)
imagelab.grid(row=0, columnspan=2)
imagelab.bind("<Button-1>", lambda e:supportURL())

is_polygon = BooleanVar()
is_polygon.set(True)

is_listing = BooleanVar()
is_listing.set(True) 

is_numformat = BooleanVar()
is_numformat.set(False) 


def save_duration():
    duration_value.set(value=duration_value.get())
    # print(duration_value.get())

def open_chrome_profile():
    subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + main_directory + "/chrome_profile",
        ],
        shell=True,
    )


def save_file_path():
    #return os.path.join(sys.path[0], "Save_file.cloud") 
    return os.path.join(sys.path[0], "Save_gui.cloud") 


# ask for directory on clicking button, changes button name.
def upload_folder_input():
    global upload_path
    upload_path = filedialog.askdirectory()
    Name_change_img_folder_button(upload_path)

def Name_change_img_folder_button(upload_folder_input):
    upload_folder_input_button["text"] = upload_folder_input

def is_numeric(val):
	if str(val).isdigit():
		return True
	elif str(val).replace('.','',1).isdigit():
		return True
	else:
		return False


class InputField:
    def __init__(self, label, row_io, column_io, pos,  master=root):
        self.master = master
        self.input_field = Entry(self.master, width=60)
        self.input_field.grid(ipady=3)
        self.input_field.label = Label(master, text=label, anchor="w", width=20, height=1 )
        self.input_field.label.grid(row=row_io, column=column_io, padx=12, pady=2)
        self.input_field.grid(row=row_io, column=column_io + 1, padx=12, pady=2)
        
        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.insert_text(new_dict[pos])
        except FileNotFoundError:
            pass
        
    def insert_text(self, text):
        self.input_field.delete(0, "end")
        self.input_field.insert(0, text)

    def save_inputs(self, pos):
        #messagebox.showwarning("showwarning", "Warning")
        input_save_list.insert(pos, self.input_field.get())
        #print(self.input_field.get())
        with open(save_file_path(), "wb") as outfile:
            pickle.dump(input_save_list, outfile)
            
    def validate_inputs(self, maxlen, type, message):

        if type == 0 and (len(self.input_field.get()) == 0 or (self.input_field.get()).isdigit() != True or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
                
        elif type == 1 and (len(self.input_field.get()) == 0 or is_numeric(self.input_field.get()) == False or len(self.input_field.get()) >= maxlen):
            messagebox.showwarning("showwarning", message)       
                
        elif type == 2 and ( len(self.input_field.get()) == 0 or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
               
        else:
            return True     
        

###input objects###
collection_link_input = InputField("OpenSea Collection Link:", 2, 0, 1)
start_num_input = InputField("Start Number:", 3, 0, 2)
end_num_input = InputField("End Number:", 4, 0, 3)
price = InputField("Default Price:", 5, 0, 4)
title = InputField("Title:", 6, 0, 5)
description = InputField("Description:", 7, 0, 6)
file_format = InputField("NFT Image Format:", 8, 0, 7)
external_link = InputField("External link:", 9, 0, 8)


def save():

    if len(start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) == 0 or (int(end_num_input.input_field.get()) < int(start_num_input.input_field.get())):
        #messagebox.showwarning("showwarning", "End number should greater than start number!")
        print ("true")
    elif len( start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) > 5 :
        #messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        print ("true")
    else:
        collection_link_input.validate_inputs(200, 2, 'Collection link required')
        price.validate_inputs(100, 1, 'Price required')
        title.validate_inputs(100, 2, 'title required')
        description.validate_inputs(200, 2, 'description required')
        file_format.validate_inputs(100, 2, 'file format required - png, jpg, jpeg')
        external_link.validate_inputs(100, 3, '')
     

    input_save_list.insert(0, upload_path)
    collection_link_input.save_inputs(1)
    start_num_input.save_inputs(2)
    end_num_input.save_inputs(3)
    price.save_inputs(4)
    title.save_inputs(5)
    description.save_inputs(6)
    file_format.save_inputs(7)
    external_link.save_inputs(8)
    

    

def main_program_loop():

    if len(end_num_input.input_field.get()) > 5 :
        messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        sys.exit()

    project_path = main_directory
    file_path = upload_path
    collection_link = collection_link_input.input_field.get()
    start_num = int(start_num_input.input_field.get())
    end_num = int(end_num_input.input_field.get())
    loop_price = float(price.input_field.get())
    loop_title = title.input_field.get()
    loop_file_format = file_format.input_field.get()
    loop_external_link = str(external_link.input_field.get())
    loop_description = description.input_field.get()

    ##chromeoptions
    opt = Options()
    opt.add_argument('--headless')
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(
        executable_path=project_path + "/chromedriver.exe",
        chrome_options=opt,
    )
    wait = WebDriverWait(driver, 60)

    ###wait for methods
    def wait_css_selector(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )
        
    def wait_css_selectorTest(code):
        wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )    

    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))


    while end_num >= start_num:
        if is_numformat.get():
            start_numformat = f"{ start_num:04}"
        else:
             start_numformat = f"{ start_num:01}"

        print("Start creating NFT " +  loop_title + str(start_numformat))
        print('number ',  start_numformat)
        driver.get(collection_link)
        
        
        wait_xpath('//*[@id="media"]')
        imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
        imagePath = os.path.abspath(file_path + "\\images\\" + str(start_numformat) + "." + loop_file_format)  # change folder here
        imageUpload.send_keys(imagePath)
        time.sleep(0.8)

        name = driver.find_element_by_xpath('//*[@id="name"]')
        name.send_keys(loop_title + str(start_numformat))  # +1000 for other folders #change name before "#"
        time.sleep(0.8)

        ext_link = driver.find_element_by_xpath('//*[@id="external_link"]')
        ext_link.send_keys(loop_external_link)
        time.sleep(0.8)

        desc = driver.find_element_by_xpath('//*[@id="description"]')
        desc.send_keys(loop_description)
        time.sleep(0.8)

        jsonFile = file_path + "/json/"+ str(start_numformat) + ".json"
        if os.path.isfile(jsonFile) and os.access(jsonFile, os.R_OK):
           
            #print(str(jsonMetaData))
            wait_css_selector("button[aria-label='Add properties']")
            properties = driver.find_element_by_css_selector("button[aria-label='Add properties']")
            driver.execute_script("arguments[0].click();", properties)
            time.sleep(0.8)

            # checks if file exists
            jsonData = json.loads(open(file_path + "\\json\\"+ str(start_numformat) + ".json").read())
            jsonMetaData = jsonData['attributes']

            for key in jsonMetaData:
                input1 = driver.find_element_by_xpath('//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                input2 = driver.find_element_by_xpath('//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                #print(str(key['trait_type']))
                #print(str(key['value']))
                input1.send_keys(str(key['trait_type']))
                input2.send_keys(str(key['value']))
                # driver.find_element_by_xpath('//button[text()="Add more"]').click()
                addmore_button = driver.find_element_by_xpath('//button[text()="Add more"]')
                driver.execute_script("arguments[0].click();", addmore_button)
            time.sleep(0.9)

            driver.find_element_by_xpath('//button[text()="Save"]').click()
            time.sleep(0.8)



        # Select Polygon blockchain if applicable
        #if is_polygon.get():

        create = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button')
        driver.execute_script("arguments[0].click();", create)
        time.sleep(0.8)

        wait_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
        cross = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
        cross.click()
        time.sleep(0.8)

        main_page = driver.current_window_handle

        if is_listing.get():
            
            wait_xpath('//a[text()="Sell"]')
            sell = driver.find_element_by_xpath('//a[text()="Sell"]')
            driver.execute_script("arguments[0].click();", sell)
            
            wait_css_selector("input[placeholder='Amount']")
            amount = driver.find_element_by_css_selector("input[placeholder='Amount']")
            amount.send_keys(str(loop_price))
            time.sleep(1)

            #duration
            duration_date = duration_value.get()
            #print(duration_date)
            # time.sleep(60)
            if duration_date == 1 : 
                endday = (date.today() + timedelta(days=1)).day
                endmonth = (date.today() + timedelta(days=1)).month
                #print(endday, endmonth)
            if duration_date == 3 : 
                endday = (date.today() + timedelta(days=3)).day
                endmonth = (date.today() + timedelta(days=3)).month
                #print(endday, endmonth)
            if duration_date == 7 : 
                endday = (date.today() + timedelta(days=7)).day
                endmonth = (date.today() + timedelta(days=7)).month   
                #print(endday, endmonth)       
            if duration_date == 30:
                endday = (date.today() + relativedelta(months=+1)).day
                endmonth = (date.today() + relativedelta(months=+1)).month
                #print(endday, endmonth)
            if duration_date == 60:
                endday = (date.today() + relativedelta(months=+2)).day
                endmonth = (date.today() + relativedelta(months=+2)).month
                #print(endday, endmonth)
            if duration_date == 90:
                endday = (date.today() + relativedelta(months=+3)).day
                endmonth = (date.today() + relativedelta(months=+3)).month
                #print(endday, endmonth)
            if duration_date == 120:
                endday = (date.today() + relativedelta(months=+4)).day
                endmonth = (date.today() + relativedelta(months=+4)).month  
                #print(endday, endmonth) 
            if duration_date == 150:
                endday = (date.today() + relativedelta(months=+5)).day
                endmonth = (date.today() + relativedelta(months=+5)).month  
                #print(endday, endmonth)  
            if duration_date == 180:
                endday = (date.today() + relativedelta(months=+6)).day
                endmonth = (date.today() + relativedelta(months=+6)).month   
                #print(endday, endmonth)

            if duration_date != 30:
                amount.send_keys(Keys.TAB)
                time.sleep(0.8)
                # wait_xpath('//*[@id="duration"]')
                # driver.find_element_by_xpath('//*[@id="duration"]').click()
                
                wait_xpath('//*[@role="dialog"]/div[2]/div[2]/div/div[2]/input')
                select_durationday = driver.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[2]/div/div[2]/input')
                driver.execute_script("arguments[0].click();", select_durationday)
                time.sleep(0.8)
                
                if lastdate.strftime('%x')[:2] == "12":
                    #print("is month first")
                    select_durationday.send_keys(str(endmonth))
                    select_durationday.send_keys(str(endday))
                    select_durationday.send_keys(Keys.ENTER)
                    time.sleep(1)
                elif lastdate.strftime('%x')[:2] == "31":
                    #print("is day first")
                    select_durationday.send_keys(str(endday))
                    select_durationday.send_keys(str(endmonth))
                    select_durationday.send_keys(Keys.ENTER)
                    time.sleep(1)
                else:
                    print("invalid date format: change date format to MM/DD/YYYY or DD/MM/YYYY")

            wait_css_selector("button[type='submit']")
            listing = driver.find_element_by_css_selector("button[type='submit']")
            driver.execute_script("arguments[0].click();", listing)
            time.sleep(10)
            
            if is_polygon.get():
                driver.find_element_by_xpath('//button[text()="Sign"]').click()
                time.sleep(1)

            for handle in driver.window_handles:
                if handle != main_page:
                    login_page = handle
                    #break
            # change the control to signin page
            driver.switch_to.window(login_page)
            wait_css_selector("button[data-testid='request-signature__sign']")
            sign = driver.find_element_by_css_selector("button[data-testid='request-signature__sign']")
            driver.execute_script("arguments[0].click();", sign)
            time.sleep(1)

  
        #change control to main page
        driver.switch_to.window(main_page)
        time.sleep(0.7)

        start_num = start_num + 1
        print('NFT creation completed!')
    
    driver.get("https://www.opensea.io")
    


duration_value = IntVar()
duration_value.set(value=180)

duration_date = Frame(root, padx=0, pady=1)
duration_date.grid(row=10, column=1, sticky=(N, W, E, S))
tk.Radiobutton(duration_date, text='1 day', variable=duration_value, value=1, anchor="w", command=save_duration, width=8,).grid(row=0, column=1)
tk.Radiobutton(duration_date, text="3 days", variable=duration_value, value=3, anchor="w", command=save_duration, width=8, ).grid(row=0, column=2)
tk.Radiobutton(duration_date, text="7 days", variable=duration_value, value=7, anchor="w", command=save_duration, width=8,).grid(row=0, column=3)
tk.Radiobutton(duration_date, text="30 days", variable=duration_value, value=30, anchor="w", command=save_duration, width=8,).grid(row=0, column=4)
tk.Radiobutton(duration_date, text="60 days", variable=duration_value, value=60, anchor="w", command=save_duration, width=8,).grid(row=0,  column=5)
tk.Radiobutton(duration_date, text="90 days", variable=duration_value, value=90, anchor="w",command=save_duration,  width=8,).grid(row=1, columnspan=1, column=1)
tk.Radiobutton(duration_date, text="120 days", variable=duration_value, value=120, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=2)
tk.Radiobutton(duration_date, text="150 days", variable=duration_value, value=150, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=3)
tk.Radiobutton(duration_date, text="180 days", variable=duration_value, value=180, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=4)
duration_date.label = Label(root, text="Duration:", anchor="w", width=20, height=1 )
duration_date.label.grid(row=10, column=0, padx=12, pady=2)


# isnumFormat = tkinter.Checkbutton(root, text='Number format 0001 ~ 99999', var=is_numformat,   width=49, anchor="w")
# isnumFormat.grid(row=18, column=1)
isCreate = tkinter.Checkbutton(root, text='Complete Listing', var=is_listing, width=49, anchor="w")
isCreate.grid(row=19, column=1)
isPolygon = tkinter.Checkbutton(root, text='Polygon Blockchain',  var=is_polygon, width=49, anchor="w")
isPolygon.grid(row=20, column=1)
upload_folder_input_button = tkinter.Button(root, width=50, height=1,  text="Add NFTs Upload Folder", command=upload_folder_input)
upload_folder_input_button.grid(row=21, column=1, padx=2)
open_browser = tkinter.Button(root, width=50, height=1,  text="Open Chrome Browser", command=open_chrome_profile)
open_browser.grid(row=23, column=1, pady=2)
button_save = tkinter.Button(root, width=50, height=1,  text="Save This Form", command=save) 
button_save.grid(row=22, column=1, pady=2)
button_start = tkinter.Button(root, width=44, height=2, bg="green", fg="white", text="Start", command=main_program_loop)
button_start['font'] = font.Font(size=10, weight='bold')
button_start.grid(row=25, column=1, pady=2)
# footer = tkinter.Button(root, height=3, width=60, text='Do you you want to show support? \n Now you have the chance to buy me a coffee. Thank you.',  command=coffeeURL, relief=GROOVE  )
# footer.grid(row=31, columnspan=2, padx=31, pady=31)

try:
    with open(save_file_path(), "rb") as infile:
        new_dict = pickle.load(infile)
        global upload_path
        Name_change_img_folder_button(new_dict[0])
        upload_path = new_dict[0]
except FileNotFoundError:
    pass
#####BUTTON ZONE END#######
root.mainloop()
    
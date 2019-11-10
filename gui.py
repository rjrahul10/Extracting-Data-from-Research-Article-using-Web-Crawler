#!/usr/bin/env python
import time
import sys
from PyPDF2 import PdfFileReader
import re
import csv
from selenium import webdriver
import tkinter as tk
from tkinter import ttk
import os
import requests
#pdf global variable
serialnumber=1

#Adding first row in the data.csv file
#change path here---------->>>>>>>>>>where ur gui file save now goto line no. 246 and make changes there
path2='/home/kabir/Desktop/data.csv'
data=["S.No.","Title","Author","Pages","Email Address","Subject"]
with open(path2,'w') as writefile:
	writer=csv.writer(writefile)
	writer.writerow(data)
#from PIL import Image, ImageTk
from tkinter import messagebox
win = tk.Tk()
win.title("                                PDF Extractor")

#You can set the geometry attribute to change the root windows size
win.geometry("500x300") #You want the size of the app to be 500x500
win.resizable(0, 0) #Don't allow resizing in the x or y direction
#to create keyword column
label = ttk.Label(win, text='::Welcome::')
label.grid(row=0,column=3,sticky=tk.W)
#for blank space
ttk.Label(win, text='                      ').grid(row=1,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=2,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=3,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=4,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=5,column=0,sticky=tk.W)

keyword_label = ttk.Label(win, text='Keyword : ')
keyword_label.grid(row=7,column=2,sticky=tk.W)
#create entry box
keyword_var = tk.StringVar()
keyword_entrybox=ttk.Entry(win,width=16,textvariable= keyword_var)
keyword_entrybox.grid(row=7,column=3)
keyword_entrybox.focus()
ttk.Label(win, text='  ').grid(row=8,column=4,sticky=tk.W)
#links
	
ttk.Label(win, text='                      ').grid(row=9,column=0,sticky=tk.W)




#https://www.sciencedirect.com/search/advanced?qs=blockchain&accessTypes=openaccess&lastSelectedFacet=accessTypes
#science direct links crawl
def science():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ", "searching your "+key)	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url=("https://www.sciencedirect.com/search/advanced?qs="+key+"&accessTypes=openaccess&lastSelectedFacet=accessTypes")
	driver.get(G_url)
	print(G_url)
#link=driver.find_elements_by_xpath('//a[@class="download-link"]')
	link = driver.find_elements_by_css_selector("a.download-link")
	url = [lik.get_attribute("href") for lik in link]
	print(url)
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))
	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")

#for IEEE
def ieee():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ","Searching Your "+key+"error~403~")	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url= "https://ieeexplore.ieee.org/search/searchresult.jsp?queryText="+key+"&highlight=true&returnFacets=ALL&returnType=SEARCH&openAccess=true"
	driver.get(G_url)
	print(G_url)
#link=driver.find_elements_by_xpath('//*[@id="xplMainContent"]/div[2]/div[2]/xpl-results-list/div[3]/xpl-results-item/div[1]/div[2]/ul/li[3]/div/a')
#link = selenium.getAttribute("css=@href")
	link = driver.find_elements_by_css_selector("a.icon-pdf")
	url = [lik.get_attribute("href") for lik in link]
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))

	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")
	

#for google Schlor
def google():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ","Searching Your "+key)	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url ="https://scholar.google.co.in/scholar?hl=en&as_sdt=0%2C5&q="+key+"+filetype%3Apdf&btnG="
	driver.get(G_url)
	print(G_url)
	#url=driver.find_elements_by_xpath('//*[@id="gs_res_ccl_mid"]/div[6]/div[1]/div/div/a')
	link = driver.find_elements_by_css_selector("div.gs_or_ggsm a")
	url = [lik.get_attribute("href") for lik in link]
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))	

	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")

#for Dl.acm
def dlacm():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ","Searching Your "+key)	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url = "https://dl.acm.org/results.cfm?query="+key+"&Go.x=0&Go.y=0"
	driver.get(G_url)
	print(G_url)
	#url=driver.find_elements_by_xpath('//*[@id="gs_res_ccl_mid"]/div[6]/div[1]/div/div/a')
	link = driver.find_elements_by_xpath("//a[@name='FullTextPDF']")
	url = [lik.get_attribute("href") for lik in link]
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))

	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")
#for Springer
def springer():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ","Searching Your "+key)	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url = "https://link.springer.com/search?showAll=false&query="+key+"&facet-content-type=%22Article%22"
	driver.get(G_url)
	print(G_url)
#link=driver.find_elements_by_xpath('//a[@class="download-link"]')
	link = driver.find_elements_by_css_selector("a.pdf-link")
	url = [lik.get_attribute("href") for lik in link]
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))

	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")
#pdf downloading
def down(url):
	r = requests.get(url, allow_redirects=True)  # to get content after redirection
	pdf_url = r.url # 'https://media.readthedocs.org/pdf/django/latest/django.pdf'
	f_name = 'file_name.pdf'
	with open(f_name, 'wb') as f:
    		f.write(r.content)
	return f_name
#pdf deleting
def dele(f_name):
	os.remove(f_name)
#get_info function to extract info. from PDF

def listToString(mylist):  
	str = ""  
	for ele in mylist:  
		str += ele   
	return str  

def get_info(path):
	pages=0
	with open(path, 'rb') as f:
		xdf = PdfFileReader(f)
		info = xdf.getDocumentInfo()
		number_of_pages = xdf.getNumPages()
		pages=number_of_pages
		#print(number_of_pages)
		pageObj=xdf.getPage(0)
		mylist=pageObj.extractText()
    
    #print("Title::")
	title = info.title
    #print(title)

    #print("Author::")
	author=info.author
    #print(author)

    #print("Subject::")
	subject = info.subject
    #print(subject)

    #converting the list obtained above into concatenated string
	string=listToString(mylist)
    #print(str)

    #searching e-mail from string str
	emaillist=[]
	for i in range(0,len(string)):
		emaillist=re.findall(r'[\w\.-]+@[a-z0-9\.-]+', string)
	str1=""

    #converting emaillist list in string 
	for i in range(0,len(emaillist)):
		str1+=emaillist[i]
		if i!=len(emaillist)-1:
			str1+=','
    #we have to declare serial number globally and then increment it after every pdf execution
	global serialnumber

	data=[serialnumber,title,author,pages,str1,subject]
    
	with open(path2,'a') as writefile:
		writer=csv.writer(writefile)
		writer.writerow(data)

    #os.startfile(path2)
    #subprocess.call(path2)
	writefile.close()

	serialnumber+=1


def extract(f_name):
	#change path here---------->>>>>>>>>>where ur gui file save
	path="/home/kabir/Desktop/"+f_name
	get_info(path)
	return f_name


button1= ttk.Button(win, text='ScienceDirect',command=science ).grid(row=9,column=2)
button2= ttk.Button(win, text='IEEE', command=ieee).grid(row=9,column=3)
button3= ttk.Button(win, text='Google Scholar', command=google).grid(row=9,column=4)
button4= ttk.Button(win, text='Dl.acm', command=dlacm ).grid(row=10,column=2)
button5= ttk.Button(win, text='Springer', command=springer).grid(row=10,column=4)

#bas u hi
ttk.Label(win, text='').grid(row=11,column=4,sticky=tk.W)
ttk.Label(win, text='').grid(row=12,column=4,sticky=tk.W)
ttk.Label(win, text='').grid(row=14,column=4,sticky=tk.W)
ttk.Label(win, text='').grid(row=15,column=4,sticky=tk.W)

exit=ttk.Button(win,text='EXIT',command=win.destroy).grid(row=16,column=3)
#time.sleep(15)
def fin():
	os.system("open -f '/usr/lib/libreoffice/program/soffice.bin' '/home/kabir/Desktop/data.csv'")	
final= ttk.Button(win, text="Result",command=fin).grid(row=13,column=3)
win.mainloop()
print("\n********Thanks**For**Visiting*********")

# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:38:07 2018

@author: Ran_the_User
"""

mainPath = 'https://il.pycon.org/2018/schedule/'

def getListByBS4():
    """
    ######## option 1 #########
    #from https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
    get this link list mainly by using BeautifulSoup
    """
    from bs4 import BeautifulSoup
    import urllib2
    import re
    html_page = urllib2.urlopen(mainPath)
    soup = BeautifulSoup(html_page) # ,from_encoding=html_page.info())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    print links


    for link in soup.find_all('a', href=True):
        print(link['href'])
            
def importByUrllinb():
    """        
    ######## option 2 #########
    # https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
    """
    import urllib
    import lxml.html

    connection = urllib.urlopen(mainPath)
    webContent = connection.read()
    dom =  lxml.html.fromstring(webContent)
    
    linkList=[]
    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        linkList.append(link)
        
    linkList[10]    

#from bs4 import BeautifulSoup
#import re
#
#resp = urllib.urlopen(mainPath)
#soup = BeautifulSoup(resp)#, from_encoding=resp.info())

##################################################
def importByPD():
    """
    '''
    import by Pandas reader
    '''
    """
    import pandas as pd
    dfPage = pd.read_html(mainPath)

    return dfPage    

def doMainFunc():
    """
    do the import by this methos
    """    
    fL = lambda x : 'presentation' in x
    #    lnk =linkList[10]    
    #mainPath -'2018/schedule/' + lnk
    basePath = 'https://il.pycon.org/'
    
    contents=[]
    for lnk in linkList:
    #    print fL(lnk)
        if fL(lnk):
            print (lnk)
            ''' get content '''
            
            "content-body"
            
    #        dfNewPage = pd.read_html(basePath+lnk) # ValueError: No tables found
            
            connection = urllib.urlopen(basePath+lnk)
            webContent = connection.read()
            dom =  lxml.html.fromstring(webContent)
    
            title = dom.xpath('//h2')
    #https://stackoverflow.com/questions/17380869/get-list-items-inside-div-tag-using-xpath
    #        cont = dom.xpath('//div/@class') # select the url in href for all a tags(links)
    #        cont = dom.xpath('//div/@class="abstract"') 
            
    #        cont = dom.xpath('//div[@class="abstract"]//bdi')
            cont = dom.xpath('//div[@class="abstract"]')
    #        cont[0]
    #        print (title)
    #        print (cont)
            try:
                abst = cont[0].text_content().encode('utf-8').strip().encode('ascii', 'ignore').decode('ascii')
                head = title[0].text_content().encode('utf-8').strip().encode('ascii', 'ignore').decode('ascii')
            except:
                pass 
    #        .decode('UTF-8')
            #'abstract'
            contents.append((head,abst))
    #            content-body
    import pandas as pd
    schdlTbl = pd.DataFrame(contents)
    pd.set_option('max_colwidth',5440)
    
    schdlTbl.to_html(open('schdle.html', 'w'))
    
    ##########################################
def setAllOutputsToWord():
    """
    just put the generated list to .docx file
    """
    import win32com.client as win32
    word = win32.Dispatch("Word.Application")
    word.Visible = 1
    word.Documents.Open("MyDocument")
    doc = word.ActiveDocument


if __name__=='__main__':
     """
     this is the main function of this script!!
     """
     doMainFunc()
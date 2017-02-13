import requests
session=requests.session()
uk10="282"
url="https://api.endclothing.com/mobileconnect/cart/add"
headers={
	'Host':              'api.endclothing.com',                                                                                                              
	'Content-Type':      'application/x-www-form-urlencoded',                                                                                                
	'Cookie':            'mobapp_code=usapp2;',                                                                             
	'User-Agent':        'END/531 CFNetwork/758.5.3 Darwin/15.6.0',                                                                                          
	'Connection':        'keep-alive',                                                                                                                       
	'Proxy-Connection':  'keep-alive',                                                                                                                       
	'Accept':            'application/x-www-form-urlencoded',                                                                                               
	'Accept-Language':   'en-us',                                                                                                                            
	'Accept-Encoding':   'gzip, deflate',                                                                                                                    
	'x-distil-secure':   'Ii4e9obc1CcQBYz' #this will need to be obtained      
}
start=355600
end=420000
while(start<end):
	data={
		'product':              str(start),#'355604',#'418889', #this is the pid - need to scrape (black tubular doom pk)
		'super_attribute[173]': uk10,
		'qty':                  '1'
	}
	r=session.post(url,data=data,headers=headers)
	print str(start)+" :: "+r.content.split("<text>")[1].split("<")[0] #xm-like data - scrape <text> and <status> n <message>
	start+=1

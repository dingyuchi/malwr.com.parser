from IPy import IP
from BeautifulSoup import BeautifulSoup

# static
filename = ""
size = ""
type = ""
md5 = ""
sha256 = ""
sha512 = ""
crc32 = ""
ssdeep = ""
download = ""  
ips = []
domains = []
        
# read file
html = open("report/11112.html", 'r').read()

parsed_html = BeautifulSoup(html)
    
# file info
file_info = parsed_html.body.find('section', attrs={'id':'file'}).findChildren('table')
for row in file_info[0].findChildren(['tr']):
    cols = row.findChildren('th')
    contents = row.findChildren('td')
    
    for col in cols:
        if col.string == 'File Name': 
            filename = contents[0].string
        if col.string == 'File Size': 
            size = contents[0].string
        if col.string == 'File Type': 
            type = contents[0].string
        if col.string == 'MD5': 
            md5 = contents[0].string
        if col.string == 'SHA256': 
            sha256 = contents[0].string       
        if col.string == 'SHA512': 
            sha512 = contents[0].string       
        if col.string == 'CRC32': 
            crc32 = contents[0].string       
        if col.string == 'Ssdeep': 
            ssdeep = contents[0].string                              
        if col.string is None:
            download = "https://malwr.com" + contents[0].a.get('href')
    
# hosts
host_info = parsed_html.body.find('section', attrs={'id':'hosts'}).findChildren('table')
try:
    for row in host_info[0].findChildren(['tr']):  
        for col in row.findChildren('td'):
            ips.append(col.string)
except:
    pass
    
# domain, ip
domain_info = parsed_html.body.find('section', attrs={'id':'domains'}).findChildren('table')
try:
    for row in domain_info[0].findChildren(['tr']):  
        contents = row.findChildren('td')
        if len(contents) == 2:
            domains.append({contents[0].string: contents[1].string})
except:
    pass
    
# drops
drop_info = parsed_html.body.find('div', attrs={'id':'dropped'}).findChildren('table')         
for row in drop_info[0].findChildren(['tr']):    
    cols = row.findChildren('th')
    contents = row.findChildren('td')

    for col in contents:
        print col.string  
            
#print "filename = %s" % filename 
#print "size = %s" % size
#print "type = %s" % type
#print "md5 = %s" % md5
#print "sha256 = %s" % sha256
#print "sha512 = %s" % sha512
#print "crc32 = %s" % crc32
#print "ssdeep = %s" % ssdeep
#print "download = %s" % download            
#print "ips:" 
#print ips
#print "domains:"
#print domains    
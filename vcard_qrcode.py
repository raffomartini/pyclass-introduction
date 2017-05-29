'''
Making vCards for the brother-in-law.
w QRcode!
'''

import urllib

template = '''\
BEGIN:VCARD
VERSION:2.1
N:{last};{first}
FN:{fullname}
ORG:California Raisin Co.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK:;;100 Waters Edge;Baytown;CA;90210;United States of America
EMAIL;PREF;INTERNET:{email}
END:VCARD
'''

url_template = "https://chart.googleapis.com/chart?cht=qr&chl={text}&choe=UTF-8&chs=500x500"


with open('notes/raisin_team.csv') as contacts_file:
    for line in contacts_file:
        last, first, title, email, phone = line.rstrip().split(',')
        fullname = '%s %s' % (first, last)
        vcard_dic = {
            'last' : last,
            'first' : first,
            'fullname' : fullname,
            'title' : title,
            'phone' : phone,
            'email' : email
            }
        text = template.format(**vcard_dic)

        # uses the rest API to get the qrcode
        qr_file = urllib.urlopen(url_template.format(text=text))
        # grabs the qrcode image
        img = qr_file.read()

        filename = '%s.%s.vcf' % (last, first)
        filename_qr = '%s.%s.png' % (last, first)
        
        with open(filename, 'w') as vcard_file:
            vcard_file.write(text)
        with open(filename_qr, 'wb') as img_file:
            img_file.write(img)

            

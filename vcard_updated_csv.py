'''
Making vCards for the brother-in-law.
'''

import csv

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

with open('notes/raisin_team_update.csv') as contacts_file:
    for row in csv.reader(contacts_file):
        last, first, title, email, phone = row
        fullname = '%s %s' % (first, last)
        row.insert(2,fullname)
        vcard_dic = dict(zip(('last','first','fullname','title','phone','email'),row))
##        vcard_dic = {
##            'last' : last,
##            'first' : first,
##            'fullname' : fullname,
##            'title' : title,
##            'phone' : phone,
##            'email' : email
##            }
        text = template.format(**vcard_dic)

        filename = '%s.%s.vcf' % (last, first)
        with open(filename, 'w') as vcard_file:
            vcard_file.write(text)

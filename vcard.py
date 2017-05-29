'''
Making vCards for the brother-in-law.
'''

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

        filename = '%s.%s.vcf' % (last, first)
        with open(filename, 'w') as vcard_file:
            vcard_file.write(text)

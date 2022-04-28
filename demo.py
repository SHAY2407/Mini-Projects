"""

This is a module listing the various domains under RUDRA and its activities 

"""
def RudraPrint():
    print('\n\n\n\nRUDRA is the official team of SRM IST taking part in\n' 
	  'University Rover Challenge organised by Mars Society since 2013.\n'
	  'The annual competition is held at the Mars Desert Research Station (MDRS),\n' 
	  'Martian Analog Site, near Hanksville, Utah, USA.\n'
	  'The team has been successfully operational for the last 7 years \n'
          'and has maintained its consistency in the competition.\n'
	  'Our Team consists of 25-30 undergraduate students of every year \n'
	  'from various engineering streams, working in different domains.\n' 
	  'The fun part - R&D, is the soul and essence of Team Rudra.\n '
	  'Brainstorming discussions are always welcome for giving birth to new ideas.\n')

RudraPrint()

class Domains:
    def __init__(self):
        self.domains = ['coding','electrical','mechanical','corporate']
    
    def outDomains(self):
        print('These are the available domains in the club')
        for domain in self.domains:
            print('\t%s ' % domain)
    def coding(self):
        print('abc')
    def electrical(self):
    	print("xyz")

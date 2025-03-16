from faker.providers import BaseProvider
import random


# Custom provider to populate the custom fields 

class commonCustomProvider(BaseProvider):
    def num(self, min, max):
        return random.randrange(min, max)

    def placementStatus(self):
        return random.choice(['Ready','Not Ready','Placed'])

    def companyName(self):
        return random.choice(['Infosys','CTS','TCS','Microsoft','Tesla','Oracle','Adobe'])

    def placedDate(self, fake):        
        placeddate = fake.date_between(start_date="-1y", end_date="-1d")        
        return placeddate.strftime('%Y-%m-%d')

    def language(self):
        return random.choice(['AI/ML','DataScience','Full Stack Development','Angular JS','BlockChain','Quantum Computing'])

    def age(self):
        return random.randrange(20, 50)

    def gender(self):
        return random.choice(['Male','Female'])

    def year(self, min, max):
        return random.randrange(min, max)

    def course(self):
        return random.choice(['AE-WBD01','AE-WBD02','AE-WBD03','AE-WBD04','AE-WBD05','AE-WBD06'])
import json

# Create a class that looks like our data
# Create method that load the data from json
    # parse it into instances of our Class


class Rates_Parser:
    def __init__(self, rate_file):
       #I want to get access to the json file
       #To do this I need to open it
            #I could then save it in a variable that is a dictionary

        rates_info_dict = self.__open_json_file() #this becomes the dictionary of the json file

        self.base = rates_info_dict['base']
        self.date = rates_info_dict['date']
        self.rates = rates_info_dict['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def __open_json_file(self, file_name_path):
        with open(file_name_path) as rates:
            return json.load(rates) #this returns a dictionary
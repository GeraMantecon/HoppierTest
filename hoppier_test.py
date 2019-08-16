import sys
import json

#Method to transform and clean string with snacks to list of snacks.
def to_SnackList(snack_string):
    snacks = [snack.encode('utf-8').strip() for snack in snack_string.replace(' and ',',').split(',')]
    return snacks

def main():
    #Load JSONS with snackers data and product data
    with open('MOCK_SNACKER_DATA.json','r') as data_reader:
        snackersData = json.load(data_reader)
    with open('product.json','r') as data_reader:
        productsData = json.load(data_reader)

    #Obtain list of all emails and their fave snacks.
    emailsSnacks = [(snacker['email'], to_SnackList(snacker['fave_snack'])) for snacker in snackersData if 'fave_snack' in snacker]
    #Obtaine dictionary of snacks in stock (assuming they are all in stock) with their price. 
    #using dictionary becuases we are going to look the price by product.
    products = dict([(product['title'].encode('utf-8'),product['variants'][0]['price']) for product in productsData['products']])
    #Find all snacker's fave snacks that we have
    snackerSnack = [(snacker[0], snack) for snacker in emailsSnacks for snack in snacker[1] if snack in products.keys()]
    
    #A)
    print('List the real stocked snacks you found under the snacker\'s \'fave_snack\'?')
    for snack in list(set(zip(*snackerSnack)[1])):
        print(snack)
    #B)
    print('\n'+'What\'re the emails of the snackers who listed those as a \'fave_snack\'?')
    for email in zip(*snackerSnack)[0]:
        print(email.encode('utf-8'))
    #C)
    print('\n'+'If all those snackers we\'re to pay for their \'fave_snack\' what\'s the total price?')
    print(sum(float(products[snack]) for snacker,snack in snackerSnack))

if __name__ == "__main__":
    main()
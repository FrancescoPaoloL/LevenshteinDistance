'''
In the example usage section, a database of three legitimate applications is defined, and a new application with a higher income than the previous one is tested. Since the Levenshtein distance between the name, address, and employment information  is above the default threshold of 5, the is_fraudulent function returns True, indicating that the new
'''

from levenshtein_distance import levenshtein_distance

def is_fraudulent(application, database, threshold=5):
    """
    Determines whether a credit card application is potentially fraudulent by comparing it to a database of
    legitimate applications using the Levenshtein distance. If the distance is above a certain threshold,
    the application is flagged as potentially fraudulent.
    """
    for app in database:
        name_dist = levenshtein_distance(application['name'], app['name'])
        address_dist = levenshtein_distance(application['address'], app['address'])
        employment_dist = levenshtein_distance(application['employment'], app['employment'])
        if (name_dist + address_dist + employment_dist) / 3 <= threshold:           
            return False
    return True

database = [    {'name': 'John Doe', 
                 'address': '123 Main St, Anytown USA', 
                 'income': 50000, 
                 'employment': 'Full-time'},

                {'name': 'Jane Smith', 
                 'address': '456 Oak St, Othertown USA',
                 'income': 75000, 
                 'employment': 'Full-time'},

                {'name': 'Bob Johnson', 
                 'address': '789 Elm St, Somewhere USA', 
                 'income': 60000, 
                 'employment': 'Part-time'}]


'''
Suppose a bank has received a credit card application from someone claiming to be "Jon Smith" with an address of 
"456 Oak St, Anytown USA' and employment status of "Self-employed". The bank suspects that this application may be fraudulent 
and decides to use the fraud detection script to compare it to a database of previously approved applications.
'''
new_application = {'name': 'Jon Smith', 
                   'address': '456 Oak St, Anytown USA', 
                   'income': 10000, 
                   'employment': 'Self-employed'}


if __name__ == '__main__':
    if is_fraudulent(new_application, database):
        print("This application may be fraudulent and should be investigated.")
    else:
        print("This application is legitimate.")

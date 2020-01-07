from fuzzywuzzy import process
import csv
districts = ['Bhojpur',
             'Dhankuta',
             'Ilam',
             'Jhapa',
             'Khotang',
             'Morang',
             'Okhaldhunga',
             'Panchthar',
             'Sankhuwasabha',
             'Solukhumbu',
             'Sunsari',
             'Taplejung',
             'Terhathum',
             'Udayapur',
             'Saptari',
             'Siraha',
             'Dhanusa',
             'Mahottari',
             'Sarlahi',
             'Bara',
             'Parsa',
             'Rautahat',
             'Sindhuli',
             'Ramechhap',
             'Dolakha',
             'Bhaktapur',
             'Dhading',
             'Kathmandu',
             'Kavrepalanchok',
             'Lalitpur',
             'Nuwakot',
             'Rasuwa',
             'Sindhupalchok',
             'Chitwan',
             'Makwanpur',
             'Baglung',
             'Gorkha',
             'Kaski',
             'Lamjung',
             'Manang',
             'Mustang',
             'Myagdi',
             'Nawalpur',
             'Parbat',
             'Syangja',
             'Tanahun',
             'Kapilvastu',
             'Parasi',
             'Rupandehi',
             'Arghakhanchi',
             'Gulmi',
             'Palpa',
             'Dang',
             'Pyuthan',
             'Rolpa',
             'Eastern Rukum',
             'Banke',
             'Bardiya',
             'Western Rukum',
             'Salyan',
             'Dolpa',
             'Humla',
             'Jumla',
             'Kalikot',
             'Mugu',
             'Surkhet',
             'Dailekh',
             'Jajarkot',
             'Kailali',
             'Achham',
             'Doti',
             'Bajhang',
             'Bajura',
             'Kanchanpur',
             'Dadeldhura',
             'Baitadi',
             'Darchula']


def read_csv(file_name):
    """Reads the csv files"""
    data = open('CSV_files/' + file_name, 'r').read().strip("\n").split("\n")
    return data


def create_csv_districts(file_name, l):
    """Creates a csv file and writes on it"""
    with open("CSV_files/" + file_name, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for items in l:
            writer.writerow([items])


def add_mistake_spelling_to_files():
    """For adding 10 values with incorrect spelling of the district to a file"""
    file_name = input('Enter the filename ')
    values = []
    for item in range(10):
        value = input('enter the mistake names ')
        values.append(value)
        create_csv_districts(file_name, values)


if __name__ == '__main__':
    create_csv_districts('new.csv', districts)  # this file is also present in csv_files
    result = read_csv('new.csv')
    filename = input('Enter the name of the csv_file whose spellings you want to check \n'
                     'Write in <filename>.csv format ')
    to_read = read_csv(filename)
    print("\nThe values with spelling error are:\n", to_read, '\n')
    for i in to_read:  # extract the nearest value of i from result list
        output = process.extract(i, result)
        print(output)

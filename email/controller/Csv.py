import csv

from model.model import Model


class Csv:
    def sendCsv():
        profile = Model.getAllUsers()

        f = open('files/data.csv', 'w')
        w = csv.writer(f)
        w.writerow(('id', 'Username', 'Full Name'))

        # writes to file csv
        print ("Writing CSV ...")
        for p in profile:
            w.writerow(p)

        # close file csv
        f.close()

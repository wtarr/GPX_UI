__author__ = 'William'
from bs4 import BeautifulSoup

class Trkpt:
    pass


class GPXparser:

    def load(self, filename):
        file = open(filename)
        data = file.read()
        file.close()
        return data

    def mapXMLElementToObject(self, item):
        trkpt = Trkpt()
        trkpt.time = item.find('time').text
        trkpt.elevation = item.find('ele').text
        return trkpt

    def createCollectionOfTrackPoints(self, data):
        allTrackPoints = []
        soup = BeautifulSoup(data)
        trkptsxml = soup.find_all('trkpt')
        for trkPt in trkptsxml:
            allTrackPoints.append(self.mapXMLElementToObject(trkPt))
        return allTrackPoints








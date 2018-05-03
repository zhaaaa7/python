
import urllib.request, urllib.parse, urllib.error

#https://www.michigandaily.com/section/student-life
fhand = urllib.request.urlopen('https://www.michigandaily.com')

for line in fhand:
        print(line.decode().strip())
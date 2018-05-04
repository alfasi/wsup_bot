from datetime import datetime
import calendar

today = datetime.today()
dest = datetime.strptime('3/3/2019', '%d/%m/%Y')

days_left = hex((dest - today).days)

url = "https://dummyimage.com/600x600/000/fff.jpg&text=" + days_left

print(url)

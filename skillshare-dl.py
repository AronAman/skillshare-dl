import sys
from skillshare import Skillshare

cookie = open('cookie.txt').read().replace('\n', '')

url=sys.argv[1]

dl = Skillshare(cookie=cookie)

dl.download_course_by_url(url, True, True)
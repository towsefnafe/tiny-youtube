import sys
import re
try:
	import requests
	from bs4 import BeautifulSoup
except Exception as e:
	print(e)
	sys.exit()

class Channel:
	def __init__(self, channel_id):
		self.channel_id = channel_id

	def __go_to_page(self, url):
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup.text

	def get_channel_name(self):
		soup = self.__go_to_page('https://www.youtube.com/channel/' + self.channel_id + '/about')
		pat = re.compile(r'", "name": "(.*?)"}}]}')
		results = pat.findall(soup)[0]
		return results

	def get_subscribers(self):
		soup = self.__go_to_page('https://www.youtube.com/channel/' + self.channel_id + '/about')
		pat = re.compile(r'"subscriberCountText":{"simpleText":"(.*?)"},"tvBanner"')
		results = pat.findall(soup)[0]
		return results

	def get_total_view(self):
		soup = self.__go_to_page('https://www.youtube.com/channel/' + self.channel_id + '/about')
		pat = re.compile(r'{"viewCountText":{"simpleText":"(.*?)"},"joinedDateText":')
		results = pat.findall(soup)[0]
		return results

	def get_joining_date(self):
		soup = self.__go_to_page('https://www.youtube.com/channel/' + self.channel_id + '/about')
		pat = re.compile(r' "},{"text":"(.*?)"}]},"canonicalChannelUrl"')
		results = pat.findall(soup)[0]
		return results

class Video:
	def __init__(self, video_id):
		self.video_id = video_id

	def __go_to_page(self, url):
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup.text

	def get_title(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id + '/about')
		pat = re.compile(r',"title":"(.*?)","lengt')
		results = pat.findall(soup)[0]
		return results

	def get_views(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id)
		pat = re.compile(r':{"videoViewCountRenderer":{"viewCount":{"simpleText":"(.*?)"},"shortViewCo')
		results = pat.findall(soup)[0]
		return results

	def get_description(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id)
		pat = re.compile(r'"},"description":{"simpleText":"(.*?)"},"lengthSeconds":"')
		results = pat.findall(soup)[0]
		return results

	def get_length(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id)
		pat = re.compile(r'"},"lengthSeconds":"(.*?)","ownerProfileUrl"')
		results = pat.findall(soup)[0]
		return results

	def get_owner_channel_id(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id)
		pat = re.compile(r'"externalChannelId":"(.*?)","isFamilySafe"')
		results = pat.findall(soup)[0]
		return results

	def get_publish_date(self):
		soup = self.__go_to_page('https://www.youtube.com/watch?v=' + self.video_id)
		pat = re.compile(r'"publishDate":"(.*?)","ownerChan')
		results = pat.findall(soup)[0]
		return results


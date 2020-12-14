# What is tiny-youtube?

**Tiny-Youtube** is a python module which helps to extract data from youtube. You can extract data of video and youtube channel. 

# Install tiny-youtube
To install it you must have [request](https://pypi.org/project/requests/) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

    pip install tinyyoutube

# Features

 - For YouTube Channel
-Get Channel Name
-Get total subscribers
-Get total views
-Get joining date
 - Fro YouTube Video
 -Get video title
 -Get views
 -Get description
 -Get video length
 -Get ower channel id
 -Get publish data

# Example
For YouTube channel:

    from tinyyoutube import Channel
    channel = Channel('UCEbcl1A3vxWgZm6QOOFfrLg') #channel id
    channel.get_channel_name() #Channel Name
    channel.get_subscribers() #Number of subscribers
    channel.get_total_view() #Total views
    channel.get_joining_date() #Joining Date
For YouTube Video:

    from tinyyoutube import Video
    video = Video('ndrMmO8g-X8') #video id
    video.get_title() #video title
	video.get_views() #number of views
	video.get_description() #video description
	video.get_length() #video length
	video.get_owner_channel_id() #author channel id
	video.get_publish_date() #publishing date

You can also find more in our YouTube channel [Tiny Programmer Ltd](https://www.youtube.com/channel/UCEbcl1A3vxWgZm6QOOFfrLg).
import pytube

url = input("enter video url: ")

path = "E:"
pytube.YouTube(url).streams.get_highest_resolution().download()



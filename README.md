# LinkCheck
Originally conceived as a notifier so I could watch TV shows the moment they're out without manually refreshing the website every minute, LinkCheck is your go-to script when you want something straight away without compromising on time.
## Application
- Booking movie tickets just as when booking starts and getting the best seats.
- Setting it up to be notified when a new torrent is out.
- Idk, use it however you wanna.
## How It Works
It fetches all the links from a user-specified website and scans them for a user-specified pattern, if it finds a match, it plays some user-specified music to notify the person else it just scans again after a minute.
## How To Use
1. The music file needs to be specified as an argument in the command prompt when you execute the file.
2. So, after navigating to the LinkCheck folder, input 
``` python
py LinkCheck.py -f FileName
```
>Here, FileName is the path to the Music file of your choice.
If you omit the filename, LinkCheck will search for .mp3, .ogg and .wav files in the current directory. If no music files are found, it will exit. If more than one are found, the first one will be used. 
3. Next, input the website you want to scrape.
4. Input the pattern you want to find, using regular expressions if you want.
5. If the pattern is found, the music starts playing. Else it searches again after a minute.
6. Come running to the music and marvel that the script worked :)
## Example Usage
Assume I want to be notified when the torrent of the next The Flash episode is out on `shaanig.org`.
Now, the part of the website that displays TV shows is ```shaanig.org/f67``` so that forms our website input.
I've already added the music file *OngoingThing.mp3* to the same folder as the script, so I don't need to input the whole filename and path.
I start the script with-
``` python
py LinkCheck.py OngoingThing.mp3
```
Next I input the website-
```
https://shaanig.org/f67
```
Then I check how the regular Flash link looks like. Checking the site, I see it looks like
```
https://www.shaanig.org/f67/flash-s03e18-720p-hdtv-x265-hevc-225mb-shaanig-5137509/
```
We can assume the link for Episode 19 would be similar so we change the e18 to e19, but we cannot predict the random number at the end of the link nor can we predict the file size. Hence, we use regular expressions and the pattern becomes
```
https://www.shaanig.org/f67/flash-s03e19-720p-hdtv-x265-hevc-...mb-shaanig-......./
```
This becomes our input for the pattern.
Then we wait..and wait and do unimportant everyday work so that our moms don't yell at us until it matches and we hear the sweet, sweet sound of music and download the episode and watch it in complete bliss :D

Ideally, I would check out the time when the previous episodes were released on the site and run the script somewhere around that time.
## Important Stuff
- This requires Python 3.x installed on your system along with the BeautifulSoup library.
- VLC media player is required to run the audio file.
- Don't forget to specify the audio file path as a command line argument.
- It cuts down on typing time if you place the audio file in the same folder.
- Piracy isn't cool, I don't recommend pirating TV shows, the [Example Usage](https://github.com/TheClashster/LinkCheck/blob/master/README.md#example-usage) part is hypothetical ~~maybe~~
- Try to specify the pattern as much as you can for more accuracy

Thanks for putting up with this ~~slightly~~ *detailed* document and/or using LinkCheck

**Feedback appreciated.**
###### Thanks a lot to [Aniket Bhattacharyea](https://github.com/BrokenMutant) for his help.

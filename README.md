# imginvid.py
Takes a clinical video as input. Looks for first frame which matches bars.png (a photo of colour bars) and then trims the video to remove everything past the first instance of a matching frame. In other words, the script finds color bars in a video and removes them. 

# Findings
The script works as intended on videos which exactly match bars.png. Further testing reveals the existence of additional color bars in certain videos. Image shown below.

![photo of secondary colour bars](secondary_bars.png)

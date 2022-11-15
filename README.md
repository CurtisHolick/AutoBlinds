# AutoBlinds
This is a small python based webserver I made to allow me to control my blinds from my phone across a local network not connected to the internet. 
I created a system to open and close the blinds using a small stepper motor, 3d printed brackets and a spool that I designed in Fusion 360, and some string.
The code was run on a raspberry pi 3b, which was connected to the motor.

## Technical Details
### Software Used:
- RPi.GPIO - Python package for raspberry pi gpio pin control
- Flask - Python package to run backend
- Jinja2 - Used with flask as template language for html files
- APscheduler - Python package for scheudling events

- Fusion 360 - CAD software I used to create parts

### Hardware:
- Raspberry Pi 3B
- Small generic stepper motor
- 3d printed parts

## Images
### Landing Page
The homepage where the user would land.
The toggle icon bounces up and down and the settings gear spins when hovering the buttons!

![BlindsHomePage](https://user-images.githubusercontent.com/38133364/201731430-bcdf8408-5346-4ae7-b47b-e12ee5c5af38.gif)

Backup image if gif doesn't load

<img src="https://user-images.githubusercontent.com/38133364/201730252-27e24f9a-0c54-40f6-b72b-b99c98e22234.png" width=40% height=40%>


### Schedule Editing Page
This is the page I am most pleased with, I feel that the bars with 2 sliders are a nice way to set a daily schedule. Could possibly be improved with a setting to change multiple at once.
![image](https://user-images.githubusercontent.com/38133364/201731722-65e97ea3-a3f8-4cfe-b9b9-f2d0b8a9bf5a.png)


### Settings Page
![image](https://user-images.githubusercontent.com/38133364/201731578-56551f0e-6d51-4f51-bb5b-129222b0b91f.png)

### Model Assembly
![Auto Blinds Mechanism Assembly](https://user-images.githubusercontent.com/38133364/201802248-b2736dcf-68eb-4f03-b871-a6fc5a6997fd.gif)


## Disclaimer
This project is still in early stages, so is still rough around the edges.

This was never intended to be run in an enviroment where it could be connected to the internet, and is not nearly secure enough. 
I had to include a setting to reset the system time on the raspberry pi, as it was unable to update itself. This runs a sudo command on the pi, which is obviously terrible security practice.

This exact code is from my computer where I ran and wrote the code, the actual code deployed to the raspberry pi is slightly different in some places.

I currently only use a preset number of rotations I manually determined to open/close the blinds, and while the stepper motor is fairly accurate, I would like to upgrade to some form of limit switches.

I am currently working on modifying this system to be much more secure and robust, especially now that I have an internet connected network which I am in control of.

I also have plans to make new versions of the 3d printed parts to work better and be more streamlined/visually pleasing. 


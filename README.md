## Disable Auto-Off

I haven't tested this with other headset brands but I imagine it would work with other brands that use the same method of turning off based on audio being sent through to the headphones.

I know a lot of people have complained about the auto-off feature on the Cloud Flight headset (myself included).  I personally use my headset throughout the entire day and take quite a few breaks in-between.  I walk away for 20 minutes, come back, and then attempt to play some music and get nothing but silence due to the headset being off.

Their dev team has already made it clear that they don't plan on developing anything to prevent it, but maybe the hardware in the headset causing it physically can't be disabled.  This app I built just simply plays an extremely quiet, in-audible sound that makes the headset think audio is being sent through.

This seems like something HyperX could fairly simply implement into their own software with an on/off toggle.  If it is a hardware limitation stopping them from disabling the auto-off feature then this is a super simple workaround to implement for the people that do want a choice of having their headset always on.

I only complied this for Windows but if interest is shown for the MacOS community I can get that setup as well. Just create an issue report if so.

I used Python to build this very simple app with the help of the PlaySound plugin for playing the sound (https://github.com/TaylorSMarks/playsound)

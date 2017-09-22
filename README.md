# AstroPi
European Astro Pi Challenge 2016 - 2017
Astro Pi Team: Juvara/Einaudi Siracusa, **IIS L. Einaudi**, Italia. 
Web: http://www.istitutoeinaudi.gov.it/



Mission | Contents
------------ | -------------
Primary mission | Detect crew presence in the Columbus module using the ISS Astro Pi and its sensors
Secondary  mission | The main goal of the secondary mission is to show  in real time the pattern of  the trend of all acquired measurements by using the 8x8 display and avoiding that astronauts touch the device.

## Primary mission : Detect crew presence in the Columbus module using the ISS Astro Pi and its sensors

* The Astro Pi device will record the environmental data and will save it in a file log useful for further analysis.
* The file log will have a collection of data for each line. 
* The survey will be accomplished every second and the temperature, humidity and pressure values will be saved by reporting  time of the collection of data, too. 


## Secondary  mission : Show  in real time the pattern of  the trend of all acquired measurements by using the 8x8 display

By collecting the data,  astro pi device define automatically the minimum and maximum values to show in the 8x8 display and determine in every moment the right amount of pixels to turn on related to the read parameter value, by showing it in the 8x8 pixel display. The code allows automatically to switch from a parameter to another after a certain time range. The astro pi device shows the parameter name through a sliding text and plot a pattern able to show the measured values.
* The measured values are shown through the number of pixels turn on and turn off. 
* The extreme values (minimum and maximum values) update dynamically and if the measured value reach the extreme values the astro pi device report the extreme values update by showing an icon in the display.  
* The device will show different icons by depending on minimum or maximum value reached in that instant. 

In order to have more information, the pixels will acquire a different chromatic effect. In fact, the measured value will determine the amount of pixels turn on and off and colours of the pixels.  The colour (defined inside a red/green scale) will change automatically and continuously according with the measured value. Therefore, the colour will be able to give a fine detailed information compared to the number of available pixel. 
Each light pixel represents a 1/8 of the difference between the maximum and the minimum. 

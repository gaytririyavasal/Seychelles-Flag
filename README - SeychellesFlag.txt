
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Using Turtle Graphics, draw the flag of Panama. (You have to actually draw it; you can't just include an image of the flag downloaded from the web.) I chose that flag because it's fairly simple to draw, consisting of several simple shapes. And it's pretty.

The flag has a ratio 2 to 3. For example, you might make your drawing 800 (height) by 1200 (width) pixels (or 400 by 600). Notice that the design is just several filled rectangles, and two filled star.

You must do this assignment in a modular fashion. That means defining functions to build a drawing toolkit, including at least a function to draw a rectangle and another function to draw a star. For example, you might define the drawRectangle function with parameters of the coordinates of the top left corner, width, height, and color. The star is a bit more complicated, but not too hard; see the hint below. Once you find the coordinates of locations on the flag, it's all pretty easy. It's another great example of functional abstraction.

Hint: You can't draw the star with 5 lines, as you probably would on a piece of paper. If you do that, it won't give you a properly enclosed area for filling. Instead, you have to draw the outline of the star with 10 line segments, all of equal length. This requires figuring out the appropriate angles to turn to walk around the perimeter. Each point of the star is 36 degrees. You can figure out the other angles from that. One way to think about it is as follows: imagine you were walking around a gigantic Panama flag painted on the ground. As you walk down each line segment that makes up one of the two stars, as you reach the end of that line segment, you'll need to turn some number of degrees right or left. How many degrees? Is it more than 90 degrees or not? Think it through and you should be able to work it out.

Note that you can specify Turtle colors as a triple representing a encoding the percentages of red, green, and blue in the color. Here are the three colors of the Panamanian flag, which are similar to those of the U.S. flag.

myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)

Anywhere you need to refer to that color, just use the name, like myBlue. Make sure you're in the right color mode. Assuming you're using the standard white background, you shouldn't have to color anything white. Be sure to draw a thin border for the entire flag.

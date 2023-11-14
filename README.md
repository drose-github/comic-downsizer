# comic-downsizer
~~This script was written to do 2 things, resize and chew bubble...gum...~~
This script was written to do 2 things.  Resize the images in a comicbook archive to something 'reasonable' and to make a list of which archives contain webp images.
It has the added bonus of converting cbr files to cbz because, while awesome, sucks.

## What is Reasonable
I have a lot of archives that have images encoded at, what I consider, needlessly high resolution.  For example, 1988x3057.  Since I do not read my comics on a Jumbotron, I don't find all those extra pixels to be useful.  I read mine on a 13" screen which is slightly more portable.
At the moment, my sweet spot is (width)x1440.  I define the height because comicbook pages always have the same height but double page spreads can alter the width, so I leave it variable.  Anyway, the size difference of my example jpeg, 1988x3057 (AR 0.65) is ~3.75MB.  The size of my 936x1440 jpeg (AR 0.65) is 244KB.  When you take the entire archive into consideration the difference is, in the parlance of our times, huge.  147MB vs 9MB huge.

## Don't worry people with suspiciously amazing eyes.  I've got you covered.
How can I have possibly achieved such an amazing feat?  By throwing away data, of course!  And not only did I throw away data, the person who originally created this behemoth of a JPEG also threw away data, but probably not as much as me.  At this point there's barely any data left.  In fact, in my example, I threw away practically all the data, 93% for those of you who like numbers.
Clearly, I am an idiot and I turned a beautiful work of art into a child's fingerpaint smears.  What kind of a madman would do such a thing?!

## If this wrong, I don't want to be right
I'm going to attempt to drop 2 images here.  I'm sure everyone else but me will think the smaller one is, literally, unreadable but it works for me.

Here's 1988x3057 (3.65MB)
![bigger](https://github.com/drose-github/comic-downsizer/assets/49666906/4901b4ed-86cc-482e-88da-b5af41050ec2)

Here's 936x1440 (280KB)
![smaller](https://github.com/drose-github/comic-downsizer/assets/49666906/2cabbc89-913b-4733-8bc2-2fc940ab2a22)



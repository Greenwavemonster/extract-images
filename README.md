## Python Script to extract images from a Dir to a diffrent Dir (Windows)

I had a Directory full of  diffrent folders which contained images, txt-files, and more... I wanted all the images copied out into a diffrent directory but still keep the initial folder order.

Somewhat like this:

* Dir A
   * Folder A                       
       * Image A                         
       * Text A
       * Script A
       * Image A2

   * Folder B                      
       * Image B                         
       * Script B


The Script will then do this:


* Dir B
   * Folder A                       
       * Image A 
       * Image A2                        

   * Folder B                      
       * Image B                         

Im a beginner so its coded bit weirdly... but hey it works.

## What you need to do
In order to run the Script you **will need to** open and edit the Paths since (start Dir, end Dir etc.) are Hardcoded... 

Currently its set to look for .jpg images, if you want you can change that by replacing "\*.jpg" (line 11 i believe) with png or whatever.

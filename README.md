## Python Script to extract images from a Dir to a diffrent Dir (Windows)

I had a Directory full of  diffrent folders which contained images, txt-files, and more... I wanted all the images copied out into a diffrent directory but still keep the initial folder order.

Explanation for dummys (like me):

* Dir A <-- **If you enter this Path and choose .jpg the Script will: ** 
   * Folder A                       
       * Image.jpg  <-- Copy this                         
       * Text.txt   <-- Ignore this
       * Script.py  <-- Ignore this
       * Image.png  <-- Ignore this
       * Folder AA  <-- Ignore this
       * Image2.jpg <-- Copy this

   * Folder B                      
       * Image.jpg <-- Copy this                        
       * Script2.py <-- Ignore this


It will Result in:


* Dir B <-- **The destination Path you choose**
   * Folder A                       
       * Image.jpg
       * Image2.jpg                       

   * Folder B                      
       * Image.jpg                       

Im a beginner so its coded bit weirdly... but hey it works.

## What you need to do
In order to run the Script you **will need to** open and edit the Paths since (start Dir, end Dir etc.) are Hardcoded... 

Currently its set to look for .jpg images, if you want you can change that by replacing "\*.jpg" (line 11 i believe) with png or whatever.

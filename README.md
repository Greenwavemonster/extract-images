## Python Script to extract images from a Dir to a diffrent Dir (Windows)

I had a Directory full of  diffrent folders which contained images, txt-files, and more... I wanted all the images copied out into a diffrent directory but still keep the initial folder order.
It is only capable to scan one childfolder. Going deeper doesn't work (yet?).

Explanation for dummys (like me):

* Dir A <-- **If you enter this Path and choose ".jpg" the Script will:** 
   * Image1.jpg <-- Ignore this
   * Folder A                       
       * Image.jpg  <-- Copy this                         
       * Text.txt   <-- Ignore this
       * Script.py  <-- Ignore this
       * Image.png  <-- Ignore this
       * Folder AA  <-- ***! Ignore this !***
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
Run the Script. It will ask you for the Start and Destination Path as well as the file extention you wish find and copy.

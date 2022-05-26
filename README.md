## Python Script to extract files from a Dir to a diffrent Dir (Windows)

I had a Directory full of  diffrent folders which contained images, txt-files, and more... I wanted all the images copied out into a diffrent directory but still keep the initial folder order.
It is only capable to scan one childfolder. Going deeper doesn't work (yet?), see explanation below.

Explanation for dummys (like me):
The Script will ask you for three things:
1. The full start Path: This is the directory from which you want to extract files from childdirectorys
2. The full destination Path: This is where the files shoud go. **Has to exist allready**
3. File extention: Here you can tipe what kind of file you want to extract. (.png, .jpg, .py ...)

### This is what the Script will do:

If you enter
1. C:\User\Greenwave\myfiles\DirA
2. C:\User\Greenwave\myfiles\DirB
3. .jpg 

The Script will do this:

* Dir A  
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


And will Result in:

* Dir B 
   * Folder A  <-- Created by Script                     
       * Image.jpg
       * Image2.jpg                       

   * Folder B <-- Created by Script                      
       * Image.jpg                       

You can type in any file extention and it should work.

Im a beginner so its coded bit weirdly... but hey it works. (back then i didnt know try:exept was a thing)


#### Conclusion
I hope its useful to someone :) Sorry bout that massive explanation

# example directory setup

this is an organized directory setup made primarily for use with latex and python, derived from [Genzkow and Shapiro's "Code and Data for Social Sciences: A Practitioner’s Guide."](https://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf) the only directories useres should directly change and edit are the input and code folder.

the code folder includes 2 useful utilities: `cleanDirectory.py` gets rid of garbage files in the code folder that latex produces and places the resulting .pdf into the output folder.

`runDirectory.py` will run the code `sample_chart.py` to produce a chart (all produced charts and figure go to the img folder), run the main tex file, and then run `cleanDirectory.py` to clean up the regeneratable files and place the output in the output folder. it is probably best to use this to make sure you are using the most up to date verison and, if you have other code, you can add it to `runDirectory.py`.

basically `runDirectory.py` is a roadmap of all the code needed to produce your file, and in what order. you should be able to delete everything except the files in the code and input folder, run `runDirectory.py` and be all good to go.

the current form of this repository would be what is expected after running `runDirectory.py`.

## setup with latexmk

in order to run [latexmk](http://users.phys.psu.edu/~collins/software/latexmk-jcc/) and have a pdf viewer updated in (near) real-time do the following (this works best with [skim pdf viewer](http://skim-app.sourceforge.net/) and [this](http://jon.smajda.com/2008/03/08/latexmk/) is where i found this process)

1.  cd to code folder.
2.  `touch .latexmkrc`
2. `open -a TextEdit.app .latexmkrc`
3. copy and paste this in (check the quotations as being straight and not curvy)

    ``$pdf_previewer = “open -a /Applications/Skim.app”; $clean_ext = “paux lox pdfsync out”;``

4. save and close it
5.  `latexmk Math_Notes.tex`
6.  now you can make changes to your .tex file and leave the program running in the background. latexmk will update the pdf with each change you make (after each save).
8. note: after you update and save the file once it will ask to auto update the pdf viewer. select auto and then it'll be good to go.

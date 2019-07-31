WTF
===

Do you like Joe "Joe Rogan" Rogan's youtube channel but always wonder who the guest is? Like who the fuck is $NAME? Is it someone interesting or yet another MMA turd? 

Well, I got a treat for you: This little thingy here combs through Joe "Joe Rogan" Rogan's youtube channel and extracts all the info about each episodes guest. And everything is then nicely packed into a single HTML file in a nice table with nice youtube links. W00t


INSTALLATION
============

install the dependencies:
youtube-dl
jq
gnu parallel 


RUNNING
=======
execute the scripts in the following order:

1. `mkvideolist.sh`
2. `mkdescs.sh`
3. `genhtml.py`
4. open `chimperium.html` in your favorite browsing apparatus (that's what app stands for) 

alternatively just execute `./run.sh`


EXAMPLE
=======

take a look at [http://cyber.vodka/chimps/](http://cyber.vodka/chimps/) 


LICENSE
=======

CPL 3.0 (Chimp Public License) - it's like the GPL only with chimps. 

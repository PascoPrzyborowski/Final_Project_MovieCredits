import pygame
from pygame.locals import *
from pygame import mixer

mixer.init()

mixer.music.load('music/Song10.mp3') # change Music Song (1 -10) for different styles
mixer.music.play()                  # without music comment this line out
    #mixer.music.set_pos(170)



pygame.init()
screen=pygame.display.set_mode([1000,800])

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#closing credits or end credits are a list of the movie cast or crew
movie_credits = '''


 At first their was nothing but darkness ...

 for a long time ...

 

 then there was a little spark of light ...

 brighter and brighter ...


 and than there was the P22_E02 Python class ...

 and the World was at Hope, Peace and Harmony ...



 That's our Journey ...


 We are a colorful, enthusiastic and very talented ...
 bunch of people  from all over the World ...
 that came here to Germany to find a good new life.
 

 From Afghanistan, Africa, Brazil, Syria, Iran(Persia), 
 Great Britain, Italy, Poland, Ukraine, 
 Kosovo, ...


 and a lot of other Countries else on the World.


 some times fleeing under difficult situations ...
 from war and/or dictatorship ...
 
 sometimes going through ...
 hell and back again in Germany before ...


 We entered the DCI Python Backend Developer Course ...
 for many reasons ...
 
 For make a change in our Career, 
 to get a good Job in the IT - Industry,
 to give our Families a good life,
 to make The World a better place,
 
 because we are the next Generation ...
 of Guardians of free Information for all of the World,


 Freedom and Peace made possible by using IT ...
 for a good reason and in a wise way !



 This Journey at DCI was a 1 year long ...


 Rodeo ride of ups and downs with many
 problems, difficulties, difficult decisions,
 sadness, madness but also a lot of happiness.


 After all ...
 we all made it finally to this point, now today ...


 So a big Thank you to all members of the Class ...

 it was a great pleasure to work with you all ...
 and find new great friends in the class ...


 Thank you also to DCI in a kind of way ...


 And a big Thank you to our Teacher Victor ...

 for being a lot patient with us all, ...
 making us all strong enough for the hard World outside, ...


 Thank you for giving us so much knowledge and Information ...
 
 about Python, Developer's World and Life in general ...
 and working with us, so we could grow beyond ourself!



 We all have a lot knowledge with 
 different working and social backgrounds, ...


 some of us are Captains or have PH.D.'s ...
 some of us have Kids and Families ...
 some of us are much life experienced ...


 various Nations, Backgrounds and Personalities ...
 mixed in this class ...


 We all are hard working, experienced, ...
 curious, eager to learn and enthusiastic Python Geeks ...
 all we want and need is a good IT - Job ... 


 So if you have a Job opportunity, ...
 get us the chance to show our work ability ...


     We all are worth it, ...
       and worth a try !

        (  \/   )
        \      /
        \     /
        \    /
        \   /
        \  /
        \ /
         /


    Thanks for wathching!
     Class P22_E02
 
'''


centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaY = centery + 50  # adjust so it goes below screen start


running =True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    screen.fill(0)
    deltaY-= 0.1996
    i=0
    msg_list=[]
    pos_list=[]
     
    font = pygame.font.SysFont('Courier', 26)

    #msg = font.render('Hello there, how are you?', True, red)
    for line in movie_credits.split('\n'):
        msg=font.render(line, True, red)
        msg_list.append(msg)
        pos= msg.get_rect(center=(centerx, centery+deltaY+30*i))
        pos_list.append(pos)
        i=i+1
   
    #pos = msg.get_rect(center=(centerx, centery+deltaY))
    

    #if (centery + deltaY < 0):
    #   running = False         # no repetition - once text scrolls up past screen, over 
        
    #screen.blit(msg, pos)
    for j in range(i):
        screen.blit(msg_list[j], pos_list[j])
        
    pygame.display.update()


pygame.quit()

    
    

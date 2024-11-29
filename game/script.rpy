# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jody")
define mc = Character('Max')   
define duf = Character('Duf', color="#ff0000")
define lee = Character('Lee', color="#ff0000")


# The game starts here.

label start:
    jump chapter3

label chapter3:
    scene dirt_road1
    
    show duf driving:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,100,0)        
    duf "The GPS tracker show the car turned down this dirt road!"
    lee "I am still confused why he killed her on his own and did not take her to us as ordered!"
    duf "I know, he made a deal with her husband and cut us out of our share!"
    lee "But we have our half the share in the tunk!"
    show duf driving1:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(-100,0,0)        
    lee "Lets get out and find the body and get the pictures!"
    show duf driving2
    lee "What the fuck Duf, you expecting a war?"
    lee "You think that drugged out girl is going to attack us?"
    duf "I am ready for anything!"
    "<Bang>"
    show duf driving3:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,100,0)
    lee "What the fuck did you just shoot?"
    lee "Oh my god, you have been shot"
    "<bang ... bang ... bang>"
    
    hide duf
    show mc driving1:
        matrixtransform ScaleMatrix(.6,.6,.6)*OffsetMatrix(1200,-600,0)
    show duf driving6:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(-100,100,0)
    mc "<thinking> Oh my god, how did they find her! I am a dead man!"
    mc "<thinking> Where are they, maybe hiding for an ambush!"
    show mc driving2:
        matrixtransform ScaleMatrix(.6,.6,.6)*OffsetMatrix(700,-600,0)
    mc "I really hope she is ok!"
    e "I am over here in the car! ... was getting cold sitting out there!"
    hide mc
    hide duf
    show jody girlrescue        
    mc "I am so happy you are alive!"
    e "I did exactly what you told me, see someone, shoot!"
    mc "I thought you did not know how to shoot!"
    e "I aimed and pulled the trigger like you said."
    e "I hurt my wrist from the gun firing!"
    mc "That is called the kick, you did great, I will look at in a few!"
    show jody girlrescue1
    mc "We need to get rid of these bodies!"
    hide jody
    show mc driving3:
        matrixtransform ScaleMatrix(.6,.6,.6)*OffsetMatrix(700,-700,0)
    show duf driving6
    mc "Let me look to see if there is anything in the trunk. I would expect they wanted to burn your body after the killed you!"
    mc "The trunk is full of gas cans and a bag of money!"
    e "We are keeping the money right?"
    mc "I don't think we have a choice!"
    hide mc
    hide duf
    show jody girlrescue1
    mc "Let's get you in my car and roll up the windows. If you get cold, start the car."
    show jody girlrescue2
    e "I can make it to the car, but I will take you up on the help later!"
    mc "I am going put everything in the car and burn it!"
    scene dirt_road1:
        matrixtransform ScaleMatrix(1.5,1.5,1.5)*OffsetMatrix(0,100,0)    
    show mc driving4:
        matrixtransform ScaleMatrix(.4,.4,.4)*OffsetMatrix(700,-700,0)
    show duf ablaze:
        matrixtransform ScaleMatrix(2,2,2)*OffsetMatrix(0,200,0)
    
    mc "Let'g get out of here!"

    scene pch_scene_5
    show mc riding1
    e "How are you involved in all of this?"
    mc "I was in the army under special intelligence until about a year ago."
    mc "One of my very closed friends told me about a girl who was under a conservatorship."
    e "Me?"
    mc "Yes."
    e "He told me that you parents passed away when you were nine and after that you never recovered."
    mc "He tired to visit you but was rejected as he was not part of you family!"
    e "Billy! How is he doing?"
    mc "He died in Afghanistan, I am sorry!"
    mc "He made me a promise that if something happed to him, I would investigate what really happend to you!"

    mc "I have hacked into your pharmacy records and found out that you have been taking anti-psychotic medication for the last 20 years."
    mc "You have had only two psychiatrists, both seem to get extra money from your trust fund!"
    mc "Your so called husband, I am not even sure you are legally married to!"


    mc "I tapped your husband phone to try to get more information, but he is very careful!"
    mc "I found there were two people he kept talking to in Pataluma and went up there to investigate."
    mc "I begreined the two gentlemen you just killed and told them I was strapped for cash!"
    mc "After a few weeks, they let me in on their plot to kill you!."
    mc "I offered to pick you up and drive you to the rondevue point!"
    mc "They agreed!"
    e "So you were going to help me!"
    mc "Until you tried to overdose on pills!"
    mc "And before you tell me, I know there have been numerous attempts.                        "







label chapter2:
    scene pch_scene_2
    show jody drivingfront
    mc "You are just staring at me, did you want to say something!"
    e "Can I get something from the bag?"
    mc "It't in the trunk area."
    show jody gettingdrugs
    mc "No funny business, I am watching you!"
    show jody drivingfront
    e "Thanks, got what I needed."
    mc "Go to sleep!" 
    show jody druggedout
    with fade
    mc "Something is wrong!"
    mc "Hey, sit up!"
    
    scene pch_scene_split:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,  0,0)
    show mc car:
        matrixtransform ScaleMatrix(.5,.5,.5)*OffsetMatrix(1400,800,0)
    mc "There is a turn off, I need to get off main road!"
    mc "I need to get off the main road!"
    scene pch_scene_4:
        matrixtransform ScaleMatrix(1.5,1.5,1.5)*OffsetMatrix(100,0,0)        
    show jody backsetout
    mc "Oh fuck!"
    show jody backsetout1:
        matrixtransform ScaleMatrix(1.4,1.4,1.4)*OffsetMatrix(0,200,0)        
    mc "Thow up!"
    e "<vomit>"
    show jody backsetout2:
        matrixtransform ScaleMatrix(1.4,1.4,1.4)*OffsetMatrix(0,200,0)        
    mc "Again!"
    show jody backsetout3:
        matrixtransform ScaleMatrix(1.4,1.4,1.4)*OffsetMatrix(0,200,0)        
    e "Your hurting me, get those fingers out of my mouth!"
    scene dirt_road2
    show jody backsetout4:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,200,0)
    e "Make it quick please!"
    mc "Fuck, Fuck ... fuck!"
    scene dirt_road2
    show jody backsetout5:
            matrixtransform ScaleMatrix(1.4,1.4,1.4)*OffsetMatrix(0,200,0)        
    mc "Here put my shirt and pants on!"
    mc "Hurry!"
    # show jody backsetout6:
    #     matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,200,0)
    # e "I am not feeling well!"
    show jody backsetout7:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,200,0)    
    e "Please make it quick!"
    mc "Here take the gun!"
    show jody backsetout8:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(0,300,0)    


    mc "I have to take car back to your house!"
    mc "If anyone comes near, you shot them!  Have you ever fired a gun!"
    e "No!"
    mc "I want you to promise me you will still be alive when I get back!"
    e "Fuck you!"
    mc "Promise me!"
    e "Fine, I promise."
    





label chapter1:
    scene house2
    mc "<think> There she is, just like the picture."
    mc "<think> Client told me she is very compliant and very passive, should be a simple job!"
    scene house3
    e "Wow, you don't fuck around, mask and everything!"    
    scene house3
    mc "Let's get you to the car and get this over with!"
    scene house4
    e "I need to grab a bag in my bedroom!"
    mc "No."
    e "Fuck you, I am getting my bag."
    mc "I said no! I will fucken shoot you right here!"
    scene house5
    e "If you don't let me get my bag, you will shoot me right here!"
    mc "Back up, I am warning you!"
    scene house6
    e "Fuck you, you can't kill me here!"
    mc "You point to the bag and let me inspect it!"
    e "Fuck you, I promise you there is no weapon in there!"
    mc "Here a towel, dry yourself off!"
    scene entrance_to_house
    show jody towel:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(800,200,0)
    mc "Where is your bag!"
    e "Upstairs."
    scene house_upstairs
    show jody towelback:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(800,200,0)
    e "I will be right back!"
    
    show jody towelback1:
        matrixtransform ScaleMatrix(.8,.8,.8)*OffsetMatrix(1000,0,0)
    mc "I am going with you!"
    scene house_upstairs_bedroom1
    show jody towelback:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(800,200,0)
    e "It's here!"
    scene house_upstairs_bedroom1:
        matrixtransform ScaleMatrix(1.5,1.5,1.5)*OffsetMatrix(100,-100,0)
    show jody towelback2:
        matrixtransform ScaleMatrix(.7,.7,.7)*OffsetMatrix(100,200,0)
    mc "Back away, I will grab the bag!"
    show jody towelback3:
        matrixtransform ScaleMatrix(1,1,1)*OffsetMatrix(800,200,0)
    mc "Lets get going!"
    e "Also lose the towel, you are dry!"
    show jody front
    mc "We are going to leave in your husbands car!"
    e "You might want to take my anti-psychotic medication with us!"
    show jody front1
    mc "You will not need them!"

    



    









    
    

   
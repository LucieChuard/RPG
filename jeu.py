import pygame 

def main():
     
    # initialisation module Pygame
    pygame.init()
    # logo de la fenetre et nom
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Jeu test")
     
    # Définir taille de l'écran et si l'écran est peut etre resize (voir http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)
    screen = pygame.display.set_mode((1820,980), pygame.RESIZABLE)
      
       #affichage d'une image
    image2=pygame.image.load("Sharwimote.PNG")
    screen.blit(image2, (50,50))
    pygame.display.flip() 
    # Variable pour la boucle
    running = True

    
     
     #boucle fonctionnement
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

 
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()


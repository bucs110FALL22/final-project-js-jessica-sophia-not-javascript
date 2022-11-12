:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### << Semester, Year >>
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

<< [https://replit.com/join/itrkusqryz-jchen753](#) >>

<< [link to demo presentation slides](#) >>

### Team: << Team JS >>
#### << Jessica Chen, Sophia Lee >>

***

## Project Description

<< This is a multiplayer game where each individual user tries to catch the other user. Throughout the chase, the users come across obstacles or powerups, which can change the players' speeds and sizes. >>

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - <<  >>

***        

## Program Design

* Non-Standard libraries
    * << Random >>
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << PlayerOne - The player will be able to move left and right, and jump, using wasd
         PlayerTwo - The player will be able to move left and right, and jump, using arrow keys
         Projectile - A powerup that boosts the player speed. It will travel across the screen and change the             player's speed when they get it
         Flag - A flag will be randomly given to a player. This flag will visually travel with whichever player
         gets it >>

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << Flag: change_players(),change_color(), despawn_on_time() >>
    * << PlayerOne: move()>>
    *  << PlayerTwo: move()>>
    * << projectile: change_speed(), slow_player_on_hit(), change_size()>>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

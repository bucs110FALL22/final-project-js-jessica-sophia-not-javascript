:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# JS' DiningHalleria
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[repl link](https://replit.com/join/itrkusqryz-jchen753)

[demo presentation slides](https://docs.google.com/presentation/d/1FM5DYylx94i1ZqEHgAuYoRv2kLpDqNlbks5mNqKFjkI/edit#slide=id.g10b651380e3_0_1544)

### Team: Team JS
#### Jessica Chen, Sophia Lee

***

## Project Description

Papa's cooking game series is a childhood favorite of many. JS' DiningHalleria is heavily inspired by said cooking game series, but with Jessica's and Sophia's own twist. As residents of the Hinman community, the starting page of the game's background is the Hinman dining hall. Click the start button to play a game of receiving and creating orders with the goal of receiving as many tips as possible.

***    

## User Interface Design

- **Initial Concept**
 ![Untitled-1](etc/Untitled-1.png)
    
- **Final GUI**
  - 

***        

## Program Design

* Non-Standard libraries
    
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * BaseComponent
    * Button
    * Image
    * InvisibleBUtton
    * TextBox
    * BaseScene
    * CreditsScene
    * DiningCustomerScene
    * DiningEmptyScene
    * EndingScene
    * KitchenOrderScene
    * KitchenScene
    * OrderingScene
    * ResultsScene
    * WelcomeScene

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * components
      * __init__.py
      * base_component.py
      * button.py
      * image.py
      * invisible_button.py 
      * textbox.py 
    * scenes
      * __init__.py
      * base_scene.py
      * credits_scene.py
      * dining_customer_scene.py
      * dining_empty_scene.py
      * ending_scene.py
      * kitchen_order_scene.py
      * kitchen_scene.py
      * ordering_scene.py
      * results_scene.py
      * welcome_scene.py
    * services
      * controller.py
  
      
* assets
    * chicken.png
    * pork.png
    * beef.png
    * broccoli.png
    * carrots.png
    * pepper.png
    * noodles.png
    * rice.png
    * orderBackground.png
    * dining_hall.jpg
    * customer.png
    * playerboy.png

***

## Tasks and Responsibilities 

   * Back End: Jessica, Sophia
   * Front End: Jessica, Sophia
   * We had multiple sessions where we sat down together and coded side by side. After finalizing our idea with the use of Figma, we were able to get a better understanding of each other's ideas and come to a consensus on what we want the game to look like.

## Testing

* Because there are multiple scenes throughout this game, when we implemented a new function, we ran through each scene individually to made sure that the output ran the way that it was intended. After each run, we would debug and did not move on to the coding more until the bug was fixed.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

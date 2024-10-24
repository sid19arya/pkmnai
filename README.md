# pkmnai

The goal of this project is to make use of reinforcement learning in order to make an agent that can play competitive pokemon. I have seen 3 major places this has been done before, each of which have led to some inspiration:
1) https://www.youtube.com/watch?v=rhvj7CmTRkg&t=862s 
2) https://cs230.stanford.edu/projects_fall_2018/reports/12447633.pdf
3) https://cs230.stanford.edu/projects_spring_2022/reports/127608668.pdf

However my approach to the problem will differ considerable from these methods.

This is currently a work in progress, but incremental reports will be made documentating both the software engienering as well as reinformcement learning parts of this process. 

The current explanatinos assume basic knowledge of both pokemon and machine learning. I will think about creating resources for thopse who don't have this knowledge if this project goes far.

Episode 1: Setup 
- In this episode I have four main goals
(i) Create a databse: Get ALL required infromation on the agents environemnt (pokemon info and other important aspects of the battle) that can serve helpful
(ii) Set up entities: Translate
(iii) Embed the enviornment: There are two reasons some sort of embedding needs to be create dof all the components at play. 1) I want learning to generalize between pokemons, moves, environemtns that are similar (an infernape and a blaziken should accomplish very similar things), 2) There is information that is not easy quantizable that I want the agent to pay attention to, for exmpale abilities, whose effects are understood by their text descriptions ("may poison target"), whch require embedding of some sort. 
(iv) Set up (integrate) an environemtn in which pokemon battles can be simulated. 

Additional Embedding Notes:
1) The information about pokemon and the environemt can exist in differnt modality (text/numerical/categorical etc) therefore finding an appropriate embedding that the model can work with is one of the most important parts - for this we use pre-trained, and fintetuned transformers.
2) Might consider retraining the embeddings a little more in the future, however, for now, the text descriptions can just be ommited and not considered.

Episode 2: Supervised Learning Model
(i) Grab Pokemon Showdown battle data - organize it in a way where all enviornemnt, and pokemon data is easy to make
(ii) Create a method to embedd ev/iv information too (look at the pokemon showdown command line API and see how it stores the data compactly) - and mimic that style to create an embedding of all infromation that pertains to a battle
(iii) Train a supervised model to predict what the next move will be (binary switch or move) / (predict out of the move options) / etc
(iv) Train a transformer model to learn the entire battle, evaluate the decoder to see if it can make reasonable moves (qualitative test)

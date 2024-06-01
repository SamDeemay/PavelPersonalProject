# PavelPersonalProject
Pavel is a mental health assistent

Step by step instructions for PPP, Pavel Personal Project:
Brief summary of what we will do here:
	-Setup LMstudio with a model and start a server locally where we can access the AI
	-Start a local server with FLASK, a python library, to make python able to access LMstudio's server and communicate the prompts and answers to javascript.
	-Open the html file containing the UI
	-Chat with Pavel with whatever llmoodel you want to use (Mistral, tiny Llama, gptq, etc.)

First of all unzip this file.

Downloading of LMstudio:
	-Follow the process of installation after the opening of the setup.exe (or download the latest setup from their website).
	-Download any model you want from the vast library.
	-Go to the local server tab on the left menu.
	-Insert your downloaded model clicking the "Select a model to load" button.
	-Click on the green "Start Server" button.

This should be it for the LMstudio setup, if you need more instructions or you want to explore it more you can see some tutorials or just play with the option. Should be a safe interface for interacting with AIs, it shouldn't mess up your computer (I am no expert though).

Python setup:
!Important!
Install python and all the basic libraries on you pc. There are plenty of resources for that, there is no need for me to write everything here as there are recent and in depth video of how to install python on your machine that are WAY better than anything I could ever write.

After installing python:
The python code is made to interact with LM studio once runned. If it doesnt work either LMstudio has changed, something in the python as been changed or the FLASK python library has been changed or updated (very probable).
To run this python file (which will create a server that javascript can interact with) you have to use the terminal. There are plenty of resources on how to use python and therefore run a python file, I have windows I do the following:
	-Open terminal
	-Go to the folder that contains all the files, in my case Documents/Pavel (assuming we are already on "PS C:\Users\Name_User>" which should be on default. Therefore writing (very important not to mess up the key words in the terminal): cd Documents/Pavel.
The terminal will give me back "PS C:\Users\Utente\Documents\Pavel>" (you might have somehìthing like "PS C:\Users\[Name user]\Desktop\PPP>"). If you digit the wrong directory digit "cd .." to go back one directory.
	-We are now accessing the folder Pavel, in documents. To run the code write "python Untitled-1.py". In our case Untitled-1.py is the name of our python file (very creative I know). You are allowed to change the name of the python file in the folder if you want, It shouldnt matter, the javascript is accessing the server the python file is creating and not the python file itself.
	-it should give back a few lines that start with asterisks and end with this line "Press CTRL+C to quit", self-explanatory, press ctrl and c to stop the server from running.

This should be all for the FLASK python server. Things to notice:
-Python is a ever changing language that changes with every new library.
-The base model for this python code was given by LMstudio, it's original purpouse was to access llms models with python using as a model a OpenAI script to access chatgpt API. It has been repurposed to create a local server (using FLASK) and communicate with javascript. Also it has been changed to show one word at a time (a lot chatgpt-like) instead of one big text once it has finished generating. This function is called "stream" (sending chunks of informations one at a time) and it communicates in a direct way with javascript. 
-You can actually change Pavel personality! It doesnt even need to be called pavel anymore! It can be a depressed 30 years old unenployed or a Loving partner. You only have to change what the lines from 43 to 48 say (notice that the more the sentences the longer it will take to answer, conciseness is key).

Lastly, html:
Html, CSS and javascript are already set up in a way that allows you to open the index.html file and start chatting. If something went wrong in either html or css, it usually pretty easy to spot if somethig is missing or not-well positioned. 
If the problem is javascript you can try solving the problem, but I would suggest seeking help to an AI to fix your AI (ironic, isn't it?). 

!Important!
If you are unsure if the model is working or not because it is taking to long go back to LMstudio and check the server log. The last lines should say something along the lines of "streaming response" which means that the llm is cooking. If a red sentence appears (like "missing gateway 200" or something simmilar), something went wrong. Try to start the process of activating the two server again and if it doesnt work have fun figuring out what went wrong.









# video-poker-tutor

<h1>Project Idea</h1>
<h2>Video Poker Tutor</h1>
	<p>A project that I have done for some beginning programming classes in the past has been a simple video poker machine. Its design is rather simple on paper and easy to explain to other people, though a bit difficult to code properly. The basic concept is that each round, a user can bet a set number of tokens, and is then dealt five cards. The user can choose any, all, or none of these five cards to keep, and the rest are discarded and replaced with new cards. After this, the hand is evaluated to see if it contains any of the standard poker hands, including flushes, straights, 3 or 4 in a row, and the like. If it does, the user wins that amount, though as there is no compensation for “high card” or one pair (unless it is a jack or higher), the player will likely lose.</p>
	<p>As a gambling game, video poker will have a select market, mostly older clients, though unlike some games like slots or poker, there is a small element of skill, as the player has some control over which cards they keep or discard. However, as no actual money is being used to gamble here, it could also be used to teach newer players how to play at no risk, or simply teach people poker hands, as most of them are similar between the two.</p>
	<p>Unlike a standard video poker machine, this machine will have a few additional tools that can be used to help teach newer players video poker should they choose to enable them. One tool can simply be used to automatically suggest which cards to hold and why. A second can calculate the probability of any hand with the given cards.<p>
<h2>Sampled Libraries</h2>
<h3>Terminal</h3> - https://github.com/thehomebrewnerd/python-video-poker
<p>To start off with, it is usually easier to explain a concept through a terminal interface if it is at all possible to do so, as less time needs to be spent on making card designs or a layout, especially if you can simply return “ace of hearts” instead of a reference to an image of said card. This code will likely be referenced when starting out the project.</p>
<h3>GUI</h3> - http://www.paulgriffiths.net/program/python/tkvideopoker.php 
<p>The GUI here can be used to help compile the GUI portion of the software, as it is closer to my previous project in how the card system was handled. The GUI from the screenshots is rather rudimentary, so it will have to be a base for the final project, not a template for.</p>
<h3>Simulator</h3> - https://github.com/nickweinberg/Python-Video-Poker-Sim
<p>This simulator can possibly be used to figure out the “optimal” scenario for the training tools, though the readme states that it may be slow, so I should look for a replacement library.</p>

# Poem_Slam: Orwell Inspired Thoughtcrime

## General Description

This is a poem that builds upon itself. 

Phase 1: Emotional Poetry

By making use of NLTK features and the NRC Lexicon, it is able to generate a line
  of poetry based on the genre of your choice. If you later on enjoy the 
  resulting poem, you can re-enter your genre to re-perform the poem.
Genres have been pre-selected through the categories of the Brown corpora via
  NLTK that align with the genre of George Orwell's dystopian sci-fi "1984."
Once you've helped create this line, the system then uses tagging to analyze the
  emotional scoring of included nouns, adjectives, and superlatives. This 
  emotional scoring through the aid of the Lexicon is my evaluation metric; from
  here the system can go onto the second part of the poem. 
  
Phase 2: Newspeak Poetry

By using the evaluated emotions that correlate with the nouns, adjectives, and 
  superlatives in the first line, Orwell can now look through a hand-crafted list
  of Newspeak words that connect to the basic emotions the Lexicon tags for. 
The next line that is generated then removes emotional words and replaces them
  with a few Newspeak words. 
These words are then printed out for your final poem and read aloud. By reading
  the lines altogether, the reading experience is made more seamless!


## Running

Running is simple! All you have to do is run the poem_generator.py file. 
Of course, this is assuming you've installed the included imports. 

You will be prompted for a genre, once you type it as shown to you, 
  rest assured that Orwell is hard at work!
  
Unfortunately, not every run results in a poem. Because of the randomized 
  nature of the line generation, it is possible that a line will not have
  any emotional words! Because the poem relies on having emotional words
  to later strip, Orwell requires a re-run from time to time. 
  Hence, a KeyError or IndexError is nothing to be afraid of! Please, try again!
  
  
## Challenges

I really kept in mind what you said last time about breaking tasks up! 
For this reason, I really tried to keep functions simple. With this, however, 
  it was definitely tricky making sure all my inputs and outputs were feeding
  in correctly. 
  
Also, it was disheartening to run into Errors that I knew weren't an indicator
  of a broken program, but I'd certainly like to learn more about how to handle 
  these going forward. 
  
I googled so much–not that that's abnormal. I forget how finnicky list 
  manipulation can be. It was fairly frustrating knowing I was so 
  close to the information I needed but having to write out multiple 
  functions to actualize that!
  
Using n-grams to make my initial line was fairly simple, as I found a helpful 
  tutorial on it, but making the phase 1 and phase 2 happen in conjunction 
  required a lot of motivation! I'm pretty proud I was able to code something
  related to my favorite book though!
  
  
## Sources

Scholarly Sources:

https://core.ac.uk/download/pdf/230921789.pdf
https://aclanthology.org/P06-4018.pdf
https://link.springer.com/chapter/10.1007/978-981-13-9187-3_53


Helpful but less fancy:

https://bookanalysis.com/1984/newspeak/
https://www.visualthesaurus.com/wordlists/24117
https://www.nltk.org/howto/corpus.html#categorized-corpora
https://www.youtube.com/watch?v=pEYfD5aVrRl
https://www.washingtonpost.com/archive/lifestyle/1984/01/02/words-newspeaking-your-way-through-1984/e20fde82-9b37-42e7-9df6-f8108f907188/
 

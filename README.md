# miniGPT-Mateo-Erkin
This repo contains the code for the assignment 2 of Machine Learning, a Bayesian Perspective for Mateo Miguelez and Erkin Özgür

The code is heavily inspired from "https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1149s" Andrej Karpathy. 

We  designed our own tokenizer (called Erkinizer). 
This algorithm analyzes the text. It expects a text encoded in UTF-8 ascii format. It creates pairs of tokens by performing many iterations. On every iteration it goes through the whole text and finds the most popular pair (pair that comes up the most). It creates a new token by assigning this pair a number and adding it to a dictionary. It then goes through the text and replaces the pair with the new token. This operation is repeated for N times. N is a design parameter

After encoding a dictionary is created with the string of characters corresponding to each token. This dictionary can then be used to decode during the generation.

Because now the alphabet is bigger than in the original code, where tokenization was just done by assigning a token to each individual character, the embedded space dimension should be increased. 

The training is done with the TinyShakeaspeare and for the generation, 1 random character from the dataset is chosen and the model generates from there. For error validation 10% of the dataset is used.

To run the code, you must create a visrtual enviroment and install packages like tiktoken, torch and numpy. There are two files, one has the erkinizer, our own tokenizer implementation, and the other uses gpt2 tokenizer from tiktoken library just for comparison. The recommended dictionary size for the erkinizer is about 1000.

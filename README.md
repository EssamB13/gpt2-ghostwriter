# gpt2-ghostwriter
GPT2 fined tuned on a large hip hop lyrics database to generate novel hip hop lyrics 

See the presentation slides to get an overview of the entire project, including my motivations and outcomes. 

train_eval_notebook.ipynb is the notebook that goes through a more "modern" training processing using Trainer and Datasets from HuggingFace

train_eval_notebook_orig.ipynb is the notebook that trains the GPT2 model in a more explicit manual fashion, where every step of the training process can be seen. The best results were achieved using the train_eval_notebook_orig.ipynb version of the training process. Both versions of the notebook generate text in the same way, and can use any model.

lyricsscraper.py contains all the lyrics scraping tools and the artist list.

Raplyzer is Malmi et al (2016)'s tool to analyze rhyme density and unique word count. Unzip lyrics_en.zip as a folder called "lyrics_en" and then you can run "python raplyzer.py" to generate rap metrics for all the text files inside lyrics_en.

<<<<<<< HEAD
=======
# Vibe Killer

## RAG:

* What is a RAG framework? 
> RAG (Retrieval-Augmented Generation) is a framework used to make AI models more task-specific and accurate. Basically lays out a definition for an AI framework to work more efficiently for a task. This is obtained by multi-layered prompt and result checking. Custom databases and pipelines are defined for the task.
  * Retrieval: When an AI receives a prompt, it searches a database or retrieves the most relevant information and context to the prompt
  * Augmentation: Appends or morphs the input prompt with this information to give the prompt more context
  * Generation: a model reads the prompt and produces a more accurate output
* Why use RAG?
  * Reduces Halucinations and allows for more precision, forcing ai to respond from real data
  * Fine-tuned to a specific user set
  * Allows for a more task-specific model without any retraining
 
## Project Overview
  This Project is aimed at reducing Vibe coding and bringing back engineers to writing code while maintaining the speed and effeciency of vibe coding while keeping the reliability of real human beings. This will be done by providing coders with the documentation and relevant implementation knowledge needed to write the code. No searching through long pages of documentation. No, implementing deprecated features only to find out the 50-line function you wrote is useless and needs refactoring. Just ask this agentic model how to implement X library into my project, and it will find the relevant up-to-date documentation and project context to allow you to do this in minutes while still understanding what youre implementing.


## How Do We Achieve This?
This is achieved using a multi-agentic pipeline to parse prompts, retrieve relevant project information, and retrieve relevant and up-to-date library and dependency documentation. Multi-layer agent filtering of integration and documentation to reduce unnecessary complexities and keep code simple but effective.

## Stack
Every project needs a stack to make components work together, this project is mostly in python but python has thousands of different options to connect a user to an agent, store data. So what do we use?

* Prompt Ingestion
  * In order to get the prompt to our agentic pipelines, you must use API calls between the “client” and the backend. To achieve this, we use FastAPI, a quick, lightweight way to implement our REST API calls. This is how our main stack communicates with the client.
* Internal Pipeline
  * We use pythons asynchronous queuing to allow agents to pass relavent information to each other and access proper tooling.
* Vector Database
  * Need a way to store similarity embeddings of context and documentation. The obvious option is ChromaDB.
* Embedding
  * Need a way to generate embeddings of project context and documentation. Pass through sentence transformers with a local model to generate basic embedding information.
* Reranking
  * Once you retrieve information from semantic search, you need a secondary filter, and you achieve this using the sentence transformers cross-encoder
* Scraping/Info Ingestion
  * Provide agent tooling with trafilatura, httpx, and beautifulsoup4, to search the web for relevant documentation.
* Caching
  * Redis for a more persistent storage solution
* Scheduling
  * APScheduler for re-ingestion jobs
* Environment
  * UV for dependencies
  * .env and python-dotenv for secrets and api keys

## Pipeline
General Program Pipeline
Client Prompt &rarr; Redis have we already ingested this information &rarr; If already have info skip ingestation &rarr; scrape docs for relavent info chunk into sections store as embeddings &rarr; Embed the query &rarr; semantic search of embeddings &rarr; return top candidates &rarr; reranking to find best candidate &rarr; Agent filtering pipeline &rarr; cache results in redis &rarr; build response &rarr; fastapi call back to client 
>>>>>>> 7478e1f80a658b912291e91e49af0cbf17b103ad

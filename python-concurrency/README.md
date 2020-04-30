# Concurrency

### Parallel Programming
Involves taking an computation task and spliter
in into smaller subtasks that are then assigned
to multiple threads or processes to be executed on
multiple  processor cores simultaneously.
With single-thread code, if you have multiple processor
cores on your system one core will be charged with execunting
your task, while the other cores sit idle.
With parallel programming all your processor cores
can be engaged.


### Asynchronous Programming

Asynchronous programming's concurrency model works
by delegating a subtask to another actor such as another
thread or deviced, and then continuing to do other work
instead wait for response. When the subtask is completed,
the actor then notifies the main thread, which calls a function
to handling results, this is usually known as a calback functions.


## Concurrency in Python

concurrent.futures = [
  threading, (python 1.5+)
  multiprocessing (python 2.6+)
]

asyncio (python 3.4+)





[Projec code nonconcurrency](./thumbnail-nonconcurrency)
[Projec code threading](./thumbnail-threading)


## IO-bound Operation Performance Test

### Intro

It is a well known fact that Python can only run one thread per process due to the GIL (Global
Interpreter Lock). Although, this can be a problem for CPU-bound operations, Python thread
work well for IO-bound operation. This is because while waiting for the IO resource, the thread
can release the GIL, and some other thread can acquire it to start its computation.

In Python 3.4, the language has introduced a module called *asyncio* that helps programmers to
write concurrent code in an asynchronous manner. This module has evolved and since Python
3.7 its api became pretty straightforward. This style of concurrent programming is refereed in
many languages as [coroutines]([https://github.com/pypa/pipenv](https://github.com/pypa/pipenv)).

The advantage of coroutines over thread are the fact that coroutines are generally more lightweight,
because they do not depended on OS system call to switch context and shared memory locking,
since all coroutines run in the same thread. That, along side other implementation details, make
coroutines highly scalable. 
 

### Project Purpose

This project has the purpose of give some insight in the performance speed up in IO-bound
operations using threads and asyncio. It has several scripts, as described below, but all of
them make 100 get requests to a fake api:

- sync_single: synchronous and single threaded
- sync_multi: synchronous and multi threaded
- async_single: asynchronous and single threaded

If want to test it know and get your results, you need to have Python 3.7+, but it is highly
recommended using a virtual environment to run it. The requirement is having [pipenv]([https://github.com/pypa/pipenv](https://github.com/pypa/pipenv)) installed,
and then run:

```bash
pipenv install --dev
pipenv shell
```
To execute the scripts run:

```bash
python <choosen_script>
```
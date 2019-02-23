About 
======
Trying to make the setup for headless chrome on AWS lambda a little easier.

You can clone the repo, run ```make``` in the root directory to collect
the binaries and then ``sls deploy`` to put the service up.

After you deploy the service with node via ```sls deploy```, you can invoke
it in the cloud with ```sls invoke -f process```; it should
return the first ten links from a google search (see
the handler for details).

You'll have to install the ```serverless-python-requirements``` dependency
for packaging up everything.

Extending the functionality
===========================

The base class ```Head``` in the chromehead directory can be used
to make whatever crawler you want. 

Tests
=====

I just have a basic test that isn't headless (chromium doesn't
like going headless on the mac).

And if you're going to run this test locally you should have Chrome installed.

You can run local test from the root directory:
```python -m pytest tests/. --fulltrace -s -v```


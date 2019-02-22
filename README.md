About 
======
Trying to make the setup for headless chrome on AWS lambda a little easier.

If you're going to test it locally you should have Chrome installed.

Note, I'm still debugging the deployment so if you see this it might now
work right now (I have a version of this but not installed from git
so that's the small hurdle).

Installing Locally
===================

You install the repo and binaries from git with the command below:   

``` python
pip install git+https://git@github.com/bibsian/chromehead#egg=chromehead
```

Serverless Config
==================
When you deploy your headless crawler as a lambda you have to install from
this repo by adding it to ``requirements.txt``:

``git+https://git@github.com/bibsian/chromehead#egg=chromehead``


You'll also have to add the following to your ``serverless.yml``.
The commands are used for installing from pip and making sure the binaries for
chromium are in the dockers path.

```yml
plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: true

environment:
  PATH: '/var/task/bin'

package:
  include:
    - bin/**

```

Tests
=====

I just have a basic test that isn't headless (chromium doesn't
like going headless on the mac).

You can run it from the root directory:
```python -m pytest tests/. --fulltrace -s -v```

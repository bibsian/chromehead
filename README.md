About 
======
Trying to make the setup for headless chrome on AWS lambda a little easier  

Installing Locally
===================

You install the repo and binaries from git with the command below:   

``` python
pip install git+ssh://git@github.com/bibsian/chromehead#egg=chromehead
```

Serverless Config
==================
When you deploy your headless crawler as a lambda you have to install from
this repo by adding it to ``requirements.txt``:

``git://git@github.com/bibsian/chromehead#egg=chromehead``


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

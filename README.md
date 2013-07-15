Githook
=======

This is a simple server that listens for a service hook POST from github and automatically updates your git repository.
It currently supports django and just running a git pull. We will be adding other server types later.

Requirements
=======

Linux, Python 2.7, bottle, and an ssh-key added to github for the server this is running on.
To install bottle simply do this:

    pip install bottle

To generate your own SSH key follow these steps (This example uses Ubuntu and the root ssh key. You can replace root
with your username.)

    ssh-keygen
    cat /root/.ssh/id_rsa.pub

Edit your repository settings on github and add the ssh key. This script should now work.

Configuration
=======
Edit main.py to your liking. It is pretty straight forward.

Usage
=======
    screen python ./main.py
That's it the server should run and listen for a POST request from github.
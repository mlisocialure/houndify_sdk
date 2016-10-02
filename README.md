# houndify_sdk
Houndify is a really cool platform that allows anyone to add smart, voice enabled, conversational interfaces to anything with an internet connection.
For more information on it see here:https://www.houndify.com/docs
The platform is still in beta. This little project is aimed at automating the maintenance and upgrade of the deployment instances of a houndify SDK.

Here I use a customized houndify SDK example, using the javascript SDK from Houndify as a template
added some unit tests via mocha,  set up continuous integration and deployment via travis 
and automated the basic admin side functions of upgrading and deploying instances of the app deployment via scripts written
in fabric.py. 

These allows the Houndify API user to easily push all changes onto production, along with all updated tests, and git commit, all by running a python script from the command line.


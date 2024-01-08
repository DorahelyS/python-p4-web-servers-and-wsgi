'''

http.server is a module in Python's standard library that creates a simple webpage that can respond to clients 
through an open URL and port. Run from the command line, it creates a navigable directory structure with URLs 
mimicking the path for each resource. Clicking on a directory shows its contents, and clicking on a file downloads 
it to your computer.

Ports
Notice the "8000" after your hostname when you run http.server? This is the port that allows you to access the 
resources that your server is serving. Ports are a networking concept that you won't use a whole lot in full-stack 
web development, but you'll see them whenever you run a server.

You can think of ports like extensions on phone numbers. If you call your doctor's office, you're accessing the 
practice with the phone number itself (this is like the URL), but you're reaching the specific doctor through the 
extension.

Some ports are explicit and specific- you can't access your http.server resource without including :8000 at the 
end of your URL. Others are implied by the protocol used to connect to the resource. HTTP is always :80, HTTPS is 
always :443, FTP (File Transfer Protocol) uses :20 and :21, etc.

Running your own server, you can choose any port between 1024 and 65,535 to make your application accessible in 
the browser. http.server defaults to 8000 as seen above, and Flask applications default to port 5000. 
We're typically going to change this to 5555 because of another application running on port 5000: Apple's Airplay!

Web Server Gateway Interface (WSGI):
The Web Server Gateway Interface (usually called WSGI) is a specification that tells our Python code on a client 
or server how to communicate effectively over HTTP (or HTTPS, of course). WSGIs were introduced by PEP 333 
(updated to PEP 3333 after the release of Python 3) because the web frameworks that existed at the time were not 
able to work with many popular servers without writing custom code. Developers usually have strong preferences 
about the frameworks and libraries that they implement applications with, so this limitation prevented many from 
making the switch from Java to Python.

Werkzeug:
Werkzeug is the WSGI library that we will be using in Phase 4. Werkzeug was developed by the Armin Ronacher 
(the author of Flask!) and is maintained by the Pallets Projects team. It includes a number of features that will 
come in handy as we start to build our first Python web applications:
An in-browser debugger.
Robust classes for requests and responses.
Routing, auto-generation and management of URLs.
A development server.
A testing framework that does not require a running server.

A Simple Werkzeug Application
Run pipenv install && pipenv shell to generate and enter your virtual environment. This will install Werkzeug, 
alongside our usual testing and debugging libraries.


The implementation of WSGI eliminated this concern. Because WSGIs could be configured to work with Python on one side to process requests and web servers on the other side to process responses, developers no longer had to worry about designing whole applications around their choice of server. WSGIs today are configured to work with most popular servers out of the box, and many even include development servers for you to work with as you build your application!


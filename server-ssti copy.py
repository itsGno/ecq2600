from http import cookies
from flask import Flask, abort, request, render_template_string, render_template,make_response
import jinja2
import re
import hashlib
from urllib.parse import unquote

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'


@app.route("/")
def home():
    user = request.args.get('user') or None
    template = '''
    <html><head>
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <title>Catch Me If You Can</title>
    <style>
    body { 
        width: 100%;
        height: auto;
        background-repeat: no-repeat;
        background-image: url('{{url_for('static', filename='bg-ecq.png')}}');
        background-color: black;
        background-size: cover;
        }

    input { 
        width: 65%; padding: .5em 1em; 
        height: 10%;
        text-align: center;
        margin-right: auto;
        margin-left: auto;
        
        }

    h1 { font-family: Consolas, monaco, monospace; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; color:#8B0000;} 
    h3 { font-family: Consolas, monaco, monospace; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15.4px; } 
    p { font-family: Consolas, monaco, monospace; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; } 
    blockquote { font-family: Consolas, monaco, monospace; font-size: 21px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 30px; } 
    pre { font-family: Consolas, monaco, monospace; font-size: 13px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 18.5714px; }
    a { font-family: Consolas, monaco, monospace; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; text-decoration: none;color:#8B0000;}

    .center-block {
    display: block;
    margin-right: auto;
    margin-left: auto;
    }
    </style>
    </head><body>
    '''

    footer = '''
    <br>
    <p style="margin-top: -1px;text-align: right;color: red;position: fixed; bottom: 0; width:100%; text-align: center;font-size:3vw;">
    <a href="https://e-cq.net/"  target="_blank" >Website</a>&nbsp;<a href="https://www.linkedin.com/company/ecq-official/" target="_blank" >/ LinkedIn /</a>&nbsp;<a href="https://www.facebook.com/ecqnet"  target="_blank" >Facebook</a>
     
   
    '''

    if user == None:
        template = template + '''
        
        
        <h1 style="margin-left:10px;margin-top: 50px;font-size:8vw;text-align: left;">Hello World'_#&;</h1>
      
        <form>

        <input  name="user" style="text-transform:uppercase;margin-left:10px;border: 2px solid #8B0000; padding: 20px; border-radius: 10px; margin-bottom: 25px;font-size:5vw;bottom: 0;" value="" placeholder="Who Are You?" autocomplete="off">
        <br>

        
        </form>
        '''.format(user) + footer
    else:
        template = template + '''
        <h1 >Hi {}</h1>
        Welcome to the vulnerable app.<br>
        Have fun with Server-Side Template Injection (SSTI).

        

        '''.format(unquote(user)) + footer
    
    return render_template_string(template)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False)
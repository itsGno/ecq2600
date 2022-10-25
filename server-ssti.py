from http import cookies
from urllib import response
from xxlimited import foo
from flask import Flask, abort, request, render_template_string, render_template,session,redirect

import jinja2
import re
import hashlib
from urllib.parse import unquote

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")

def home():
    session['hint']='D6fxq6+anbP/w8fV38xMvoP/nxNMX8P/v8LGqrleDuNxvgkb+OPdq=fVn8FMn8wsvuJtn8VVErV7+Zxb+miGJK7rwmlFw8z5'
    
    name = request.args.get('name') or None
    blacklist =["config","self","_",'"']
    
    hint='''<!--...O5FoQ5Au9mxkPr7oQrRdNqRZQWtiNLEjRqJW9LBZMrJmOLFt9rBZQbNZQWpnOKFZ9LFZPL/gMLFZ9KZiOaJXR4ZjPU...-->'''
    template = hint+'''
    <html><head>
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <title>Catch Me If You Can</title>
    <style>
        @keyframes example {from {background-color: red;}to {background-color: yellow;}}div {width: 100px;height: 100px;background-color: red;animation-name: example;animation-duration: 4s;}body {width: 100%;height: auto;background-repeat: no-repeat;background-image: url('{{url_for('static', filename='bg-ecq.png')}}');background-color: black;background-size: cover;}input {width: 65%;padding: .5em 1em;height: 10%;text-align: center;margin-right: auto;margin-left: auto;}h1 {font-family: Consolas, monaco, monospace;font-size: 24px;font-style: normal;font-variant: normal;font-weight: 700;line-height: 26.4px;color:#8B0000;}h3 {font-family: Consolas, monaco, monospace;font-size: 14px;font-style: normal;font-variant: normal;font-weight: 700;line-height: 15.4px;}p {font-family: Consolas, monaco, monospace;font-size: 14px;font-style: normal;font-variant: normal;font-weight: 400;line-height: 20px;}blockquote {font-family: Consolas, monaco, monospace;font-size: 21px;font-style: normal;font-variant: normal;font-weight: 400;line-height: 30px;}pre {font-family: Consolas, monaco, monospace;font-size: 13px;font-style: normal;font-variant: normal;font-weight: 400;line-height: 18.5714px;}a {font-family: Consolas, monaco, monospace;font-size: 20px;font-style: normal;font-variant: normal;font-weight: 700;line-height: 26.4px;text-decoration: none;color:#8B0000;}.center-block {display: block;margin-right: auto;margin-left: auto;}
    </style>
    </head><body>
    '''

    footer = '''
    <br>
    <p style="margin-top: -1px;text-align: right;color: red;position: fixed; bottom: 0; width:100%; text-align: center;font-size:3vw;">
    <a href="https://e-cq.net/"  target="_blank" >Website</a>&nbsp;<a href="https://www.linkedin.com/company/ecq-official/" target="_blank" >/ LinkedIn /</a>&nbsp;<a href="https://www.facebook.com/ecqnet"  target="_blank" >Facebook</a>
     
   
    '''
    try:
        for x in blacklist:
            if x in name.lower():
                template = template + '''
                <h1 style="margin-top: 50px;margin-left:10px;font-size:15vw;text-align: left;color:white">You</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:red">Are</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:white">Hacker!</h1>
                ''' + footer
                return render_template_string(template), 400

    except:
        pass

    try:
        if name == None:
            template = template + '''
            
            <br>
            <h1 style="margin-top: 70px;font-size:12vw;text-align: center;">Hello <font color="white">World</font></h1>
            
            <form style="text-align: center;">

            <input  name="name" style="border: 2px solid #8B0000; padding: 30px; border-radius: 10px; margin-bottom: 25px;font-size:7vw;bottom: 0;text-align: center;" value="" placeholder="Who Are You?" autocomplete="off">
            
            
            
            </form>
            '''.format(name) + footer + hint
        else:
            template = template + '''
            <h1 style="margin-left:10px;margin-top: 100px;font-size:8vw;text-align: left;">Hi</h1>
            <h1 style="margin-left:10px;font-size:20vw;text-align: left;color:white">{}!</h1>
            <br><h6>Have fun <br>with <br>Server-Side Template Injection (SSTI).<h6>

            '''.format(unquote(name).capitalize()) + footer 
    except:
        pass
    
    return render_template_string(template)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    
    # note that we set the 404 status explicitly
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False)
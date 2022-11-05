import base64
from http import cookies
from urllib import response
from xxlimited import foo
from flask import Flask, abort, request, render_template_string, render_template,session,redirect,url_for
import os
import jinja2
import re
import hashlib
from urllib.parse import unquote
import string
# import base64
import base62
import base58

import base64
from Crypto.Cipher import AES
# from Crypto import Random
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__(self):
        # self.iv = base64.b64decode('kfJMm0MpQMwDhS03yPkgsFrw5sqY3+CaxSVdrYJNAKQ=')  # key
        self.key = base64.b64decode('kfJMm0MpQMwDhS03yPkgsFrw5sqY3+CaxSVdrYJNAKQ=')  # key
        # 0zHDs5aMIW5s2RCIzLc1Wg==
        self.iv =  base64.b64decode('MDAwMDAwMDAwMDAwMDAwMA==')  # offset
        # print('IV:',base64.b64encode(self.iv),'\nKEY:',base64.b64encode(self.key))
        # print('==============================\nIV :',base64.b64encode(self.iv),'\nKey :',base64.b64encode(self.key))

    def encrypt(self, text,key):
        """
        Encryption: first add bits, then AES encryption, then base64 encoding
        :param text: the plain text to be encrypted
        :return:
        """ 
        key = hashlib.sha256(key.encode()).digest()
        iv = key[0:16]
        # text = pad(text) The wording of package pycrypto, the encryption function can accept str or bytes
        text = pad(text).encode()  # The encryption function of package pycryptodome does not accept str
        cipher = AES.new(key, mode=AES.MODE_CBC, IV=iv)
        # cipher = AES.new(key=self.key, mode=AES.MODE_CBC, IV=self.iv)
        encrypted_text = cipher.encrypt(text)
        # Perform 64-bit encoding, return the encrypted bytes, decode into a string 
        return base64.b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        """
        Decryption: the offset is key[0:16]; first base64 decryption, then AES decryption, and then cancel the bit supplement
        :param encrypted_text: encrypted ciphertext
        :return:
        """
        encrypted_text = base64.b64decode(encrypted_text)
        cipher = AES.new(key=self.key, mode=AES.MODE_CBC, IV=self.iv)
        decrypted_text = cipher.decrypt(encrypted_text)
        return unpad(decrypted_text)




app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/",methods= ['POST','GET'])


def home():

    session['cookie'] = 'NoAuth'

    if request.method == 'POST':
        username = request.form['username'] or None
        password = request.form['password'] or None
      
    else:
        username = request.args.get('username') or None
        password = request.args.get('password') or None


    blacklist =string.punctuation
    # app.logger.info(session["password"])
    
    # hint='''<!--...O5FoQ5Au9mxkPr7oQrRdNqRZQWtiNLEjRqJW9LBZMrJmOLFt9rBZQbNZQWpnOKFZ9LFZPL/gMLFZ9KZiOaJXR4ZjPU...-->'''
    template = 'hint'+'''
    <html><head>
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <title>The Things Between us!</title>
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
            if x in username.lower():
                template = template + '''
                <h1 style="margin-top: 50px;margin-left:10px;font-size:15vw;text-align: left;color:white">You</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:red">Are</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:white">Hacker!</h1>
                ''' + footer
                return render_template_string(template), 400

    except:
        pass

    try:
            # app.logger.info("out if")

   
            if username != None and password !=None and username.lower()   != 'admin' :
                # Generate file
                name = username.lower() 
                # mkdir = '''mkdir ./notes/{} 2>/dev/null'''.format(username)
                # echo some hint
                # filename = str(base64.urlsafe_b64encode(('Initial-Note-'+name).encode()),'utf-8')
                filename = 'Initial-Note-'+name
                # base32
                filename = base64.b32encode((filename).encode())
                # base62
                filename = base62.encodebytes((filename))
                # base58                
                filename = base58.b58encode(filename).decode("utf-8")
                ciphertext = AESCipher().encrypt(filename,name)
                # ciphertext, tag = cipher.encrypt(filename)
                ciphertext = base64.urlsafe_b64encode(ciphertext.encode()).decode("utf-8")
                cmd = '''
                echo "To {0},"> ./notes/{1}.txt 2>/dev/null
                '''.format(name,ciphertext)
                os.system(cmd)
                cmd = '''
                cat ./notes/temp >> ./notes/{0}.txt 2>/dev/null
                '''.format(ciphertext)
                os.system(cmd)

                # read file 
                template = template + '''
                <h1 style="margin-top: 50px;margin-left:10px;font-size:15vw;text-align: left;color:white">Welcome  </h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:red">New</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:white">Challenger</h1>
                <h1 style="margin-left:10px;font-size:15vw;text-align: left;color:red">{0}</h1>
                <a href="/notes/{1}">Read The Document</a>
                '''.format(name,ciphertext) + footer
                return render_template_string(template), 400

            else:
                template = template + '''
                <br>
                <h1 style="margin-top: 70px;font-size:12vw;text-align: center;">Hello <font color="white">World</font></h1>
                '''
                if username != None:
                    if username.lower() == 'admin':
                        template = template + '''
                        <h2 style="margin-top: 7px;font-size:2vw;text-align: center;color:white">User admin exist!</h1>
                        '''

                template = template + '''
               <form method="post" style="text-align: center;" id="form1">

                <input  name="username" style="border: 2px solid #8B0000; padding: 30px; border-radius: 10px; margin-bottom: 25px;font-size:7vw;bottom: 0;text-align: center;" value="" placeholder="Username" autocomplete="off"/>
                <input  name="password" type="password" style="border: 2px solid #8B0000; padding: 30px; border-radius: 10px; margin-bottom: 25px;font-size:7vw;bottom: 0;text-align: center;" value="" placeholder="Password" autocomplete="off"/>
        
                <br><button type="submit" form="form1" value="Submit" style="border: 2px solid #8B0000; padding: 10px; border-radius: 10px; margin-bottom: 5px;font-size:7vw;bottom: 0;text-align: center;">Sign in</button>
                    
                
                </form>'''.format(username) + footer 

         
    except ValueError:
        app.logger.info(ValueError)

    
    return render_template_string(template)




# @app.route("/success",methods= ['POST','GET'])
import process
do_work = process.FILE_HANDELING()
@app.route('/notes/<filename>',methods=['GET'])
def readFile(filename):
    app.logger.info("in readfile")
    start = request.args.get('startline', default=0, type=int)
    end = request.args.get('endline', default=0, type=int)
    # data = do_work._valid_file(filename)
    data = True
    app.logger.info("in data")
    app.logger.info(filename)
    if data is True:
        app.logger.info("in data2")
        temp = do_work._read_file(filename,start,end)
        app.logger.info(temp)
        if(temp == True):
            return render_template('output.html')
        else:
            return render_template('404.html', error=temp)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    
    # note that we set the 404 status explicitly
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31337, debug=True)
#!/usr/bin/python
import json
import re
import codecs
from flask import Flask, abort, request, render_template_string, render_template,session,redirect,url_for
app = Flask(__name__)

class FILE_HANDELING(object):
    def __init__(self):
        self.files = ["file1", "file2", "file3", "file4"]

    def _read_file(self, filename, start, end):
        try:
            startline = 0
            endline = 0
            app.logger.error("xxxxx")
            filename = filename+'.txt'
            f = codecs.open(r"./notes/"+filename,"r+", encoding="utf-8", errors='ignore')
            app.logger.error(f)
            f1 = open(r'templates/output.html', 'w')
            f1.write(r'{% extends "index.html" %}')
            f1.write(r'{% block content %}')
            total_lines = f.readlines()
            length = len(total_lines)    
            app.logger.info(total_lines)
            if(start >= 0 and start < length and end >= 0 and  end < length and end > start):
                startline = start
                endline = end - 1
            else:
                endline = length - 1
            for i, x in enumerate(total_lines):
                if i >= startline:
                    f1.write(x)
                    f1.write("<br>")
                    if i > endline:
                        break
            f1.write(r'{% endblock %}')
            f.close()
            f1.close()
            return True
        except Exception:
            # return str(ex)
            pass

    def _valid_file(self, name):
        app.logger.info("in _valid_file")

        file_name = re.split(r'\s',name)
        valid = False
        for file in self.files:
            if(re.search(file,file_name[0])):
                valid = True
        return valid
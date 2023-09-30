#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 07:12:42 2023

@author: dexter
"""

from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template('index2.html')


@views.route("/blog")
def blog():
    return render_template('blog2.html')


@views.route("/blog1")
def blog1():
    return render_template('blog_content1.html')

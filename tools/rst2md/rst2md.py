#!/usr/bin/env python
import html2text
import urllib
import lxml.html
import subprocess
import os
import sys

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def clone_repo(repo_url):
    git("clone", repo_url)

def update_repo(repo_url):
    git("add", "README.md")
    git("commit", "-am 'updated README to Markdown'")
#    git("push")

def convert(repo_url):
    cwd = os.getcwd()
    try:
        os.stat("tmp")
    except:
        os.mkdir("tmp")
    os.chdir("tmp")

    repo_url = repo_url.split("\n")[0]
    clone_repo(repo_url)
    resp = urllib.urlopen(repo_url)
    full_html = resp.read()
    html = lxml.html.fromstring(full_html)
    body = html.find_class("markdown-body")[0]
    body_text = lxml.html.tostring(body, 'utf-8')
    markdown = html2text.html2text(body_text)
    repo_name = repo_url.split("/")[-1]
    os.chdir(repo_name)
    f = open("README.md", 'w')
    f.write(markdown)
    f.close()
    readmes = [f for f in os.listdir(".") if os.path.isfile(f) and (f.lower() == 'readme.txt' or f.lower() == 'readme.rst')]
    for f in readmes:
        os.remove(f)
    update_repo(repo_url)
    os.chdir(cwd)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        convert(arg)

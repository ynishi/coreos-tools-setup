#!/usr/local/env python
# -*- coding: utf-8 -*-
'''
install docker-compose for coreos
'''
from github import Github
import os
import requests
import shutil
import subprocess

URL_tmpl = 'https://github.com/docker/compose/releases/download/{}/{}'
dc_tmpl = 'docker-compose-{}-{}'

g = Github(os.environ['GITHUB_TOKEN'])
r = g.get_user('docker').get_repo('compose')
gr = r.get_latest_release()

p = '/out/bin'
if not os.path.isdir(p):
    os.mkdir(p)

if 'DC_OS' in os.environ and 'DC_MACHINE' in os.environ:
    dc = dc_tmpl.format(os.environ['DC_OS'], os.environ['DC_MACHINE'])
    url = URL_tmpl.format(gr.title, dc)
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        dc_fullpath = os.path.join(p, 'docker-compose')
        with open(dc_fullpath, 'wb') as file:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, file)
        os.chmod(dc_fullpath, 755)
        subprocess.run([dc_fullpath, "--version"])

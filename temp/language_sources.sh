# -*- coding: utf-8 -*-
# 2013-05-23

# Some language source code

# WARNING: do not blindly run this.

# ────────── ────────── ────────── ────────── ──────────
# C

# emacs
# wget http://ftp.gnu.org/gnu/emacs/emacs-24.3.tar.xz
git clone https://github.com/emacsmirror/emacs.git

# linux kernel
# 1.6G
git clone https://github.com/torvalds/linux.git

# git
# 70M
git clone https://github.com/git/git.git

# node.js
# 190M
git clone https://github.com/joyent/node.git

# ────────── ────────── ────────── ────────── ──────────
# Java

# Google web toolkit
# 291M
svn checkout http://google-web-toolkit.googlecode.com/svn/trunk/ google-web-toolkit-read-only

# ────────── ────────── ────────── ────────── ──────────
# JavaScript

# Yahoo web framework
# 226M
git clone https://github.com/yui/yui3.git

# angular.js Google web framework
# git clone https://github.com/angular/angular.js.git # 60M
wget https://ajax.googleapis.com/ajax/libs/angularjs/1.0.7/angular.js # 493k

# prototype (frontend lib)
# 13M
git clone https://github.com/sstephenson/prototype.git

# JQuery (frontend lib)
wget http://code.jquery.com/jquery-1.9.1.js # 268k
#git clone https://github.com/jquery/jquery.git # 18M


# backbone (backend lib)
wget http://backbonejs.org/backbone.js # 59k
# git clone https://github.com/documentcloud/backbone.git # 26M

# dojo
# 23M
git clone https://github.com/dojo/dojo.git
# 25M
git clone https://github.com/dojo/dijit.git

# ────────── ────────── ────────── ────────── ──────────
# Python

# python base libs
# /usr/lib/python3.2/

# DJango web framework
# 126M
git clone https://github.com/django/django.git

# ────────── ────────── ────────── ────────── ──────────
# Perl

# perl base libs
 # "/usr/lib/perl5",
 # "/usr/lib/perl/5.14",
 # "/usr/share/perl5",
 # "/usr/share/perl/5.14",

# ────────── ────────── ────────── ────────── ──────────
# ruby

# ruby base libs
# "/usr/lib/ruby/1.9.1/"

# ruby on rails
# 91M
git clone https://github.com/rails/rails.git

# ────────── ────────── ────────── ────────── ──────────
# PHP

# Symfony (web framework)
# 41M
# http://symfony.com/

# ────────── ────────── ────────── ────────── ──────────
# shell scripts

# linux init scripts
cp -r --dereference --no-clobber --copy-contents /etc/init.d/ ~/Downloads/lang-source-code/linux-shell-scripts/

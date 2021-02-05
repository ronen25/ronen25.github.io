---
title: "Moving to Static Site Generation"
date: 2021-02-05T14:20:06+02:00
draft: false
---

Welcome to my new personal website!

First, I would like to explain the rationale for recreating my site from scratch, as a statically-generated website, after having my own custom-made site (hosted on a VPS) for more than two years...

<!--more-->

Initial attempts
---------------------------
I've always been interested in creating a personal blog and portfolio site, but being a Systems programmer, webdev has never been my forte. Because of this, I was always searching for quick and easy ways to create (and host) a website.

The first thing I remember trying ts something called <code>880mb.com</code>, which offered you 880 MB of free hosting in exchange for showing Google Ads at the top and bottom of your page.
The website itself was just some SharePoint thing from a template (and yes, it looked bad even for the late 2000's).

Last time I checked, the domain is up for sale, and any traces of this hosting site ever existing are long gone. It makes sense, because I recall clearly that it just stopped working suddenly, which is why I abandoned the idea of a website for a very, very long time (although I did toy around with Wordpress for some time).

First Static Site on Github Pages
-----------------------------------
The first "real" portfolio site I had was something I generated with [Pelican](https://blog.getpelican.com/). I found out about it by looking at someone else's personal site and thinking, "hey, this static generation thing isn't actually bad", so I used it myself.

The result was pretty good and I stuck with it for two years or so.

Custom Website
----------------
During the summer of 2019 I became more and more interested in Web development, so I wanted to finally create my own website from scratch.

Since I only had about a month to learn everything, I decided not to do the CSS myself, but to rather use an existing CSS framework. I looked around any decided to use [Bootstrap](https://getbootstrap.com/), which I knew about since my Army days.

For the website itself, I used [vue.js](https://vuejs.org/) since it was the hottest new thing around (at least, that I knew). I also wanted some backend "microservice" that will fetch repository info from Github and display it, so I went with Golang because I wanted to learn it.

The whole thing was to be hosted on a [Linode](https://linode.com) instance using Docker Compose for managing the website and the backend "microservice".

I was **in love** with the end result (despite it looking a bit 2012). For the first time in my life, I had a real custom website, hosted on an actual server. It was absolutely incredible.

The thing is, though, the whole thing was a **ridiculous overkill** for such a small site. Maintaining it was a pain in the you-know-what too.

New Static Website
-------------------
This site now uses [Hugo](https://gohugo.io/) and a nice theme I found. It no longer requires maintenance (since it's hosted on Github Pages and there's no VPS involved anymore), and I've set up some Github Actions to automate the generation every time I push to the source repo.

----------

Conclusions
------------
The current site suites me perfectly well, and I am hoping to use it for a very long time.
Hugo itself is incredibly easy to use, and I will happily recommend it for everyone wanting to create a simple website.

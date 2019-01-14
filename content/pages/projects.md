Title: Projects (Portfolio)
Date: 2018-01-14 21:40
Category: About
Tags: aboutme, projects, about, email
Slug: projects

# Portfolio (Projects)

## Panorama
![Panorama]({static}/screenshots/screenshot_panorama.png)

### What?
Panorama is a lightweight system monitor for Linux, with code separation to include cross-platform support
in the future (with a Windows port currently being in development).

### Why?
I wanted to create a cross-platform system monitor with uniform look and feel across all the
platforms I use on a day-to-day basis.

### Features
* Written in C++14

* Uses the ImGui immediate mode GUI framework

* Exteremly lightweight

* 700+ downloads on the Snap store

### Technologies
C++, C++14, GUI, Multithreading, ImGUI, Immediate Mode, Cross-Platform

### Download / Clone
[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/panorama)

----

## libcmdf
![libcmdf]({static}/screenshots/screenshot_libcmdf.png)

### What?
libcmdf is a C library for writing command line interfaces. It is heavily inspired by the Python <code>cmd</code> module.

### Why?
As part of my job, I had to write some little debugging utilites.

These utilities needed to be written in C/C++, so I unfortunately did not have the neat <code>cmd</code> module
in Python, so I decided to write one in C :-)

### Features
1. 100% ANSI C

2. Single header - No need to pass complicated commands to link it, just drop it into the project folder!

3. Easy to use

### Technlogoies
C, C89, ANSI C, Library, Header, Single Header

--------

## rpiweatherd / rpiweatherd-qtclient
![rpiweatherd and its frontend, rpiweatherd-qtclient]({static}/screenshots/screenshot_rpiweatherd.png)

### What?
<sup>(Read: R - Pi - Weather - D)</sup>

This project basically has two separate components:

**rpiweatherd** - A daemon that is installed on the Raspberry Pi, and monitors temperature and humidity data with
a connected sensor, storing this data in an internal on-disk database.

The daemon exposes the data with a RESTful API via a built-in HTTP server, returning portions of the data
as JSON.

**rpiweatherd-qtclient** - A very simple demo frontend that connects to an rpiweatherd server and displays the
current temperature and humidity.

It also calculates HUMIDEX and real feeling on-the-fly.

The background is a nice gradient that changes throughout the day :-)

### Technologies
*For rpiweatherd*: C99, pthreads, HTTP, JSON, INI Parsing, SQLite

*For rpiweatherd-qtclient*: C++11, Qt5, HTTP

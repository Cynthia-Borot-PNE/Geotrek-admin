============
INSTALLATION
============

These instructions will install *Geotrek* on a dedicated server for production.
For a developer instance, please follow  :ref:`the dedicated procedure <development-section>`.

Requirements
------------

* Ubuntu Server 16.04 Xenial Xerus (http://releases.ubuntu.com/16.04/) or
  Ubuntu Server 14.04 Trusty Tahr (http://releases.ubuntu.com/14.04/)


A first estimation of minimal required system resources are :

* 2 cores
* 4 Go RAM
* 20 Go disk space

For big instances required system resources are :

* 4 cores
* 8 Go RAM or more
* 50 Go disk space or more (20 Go + estimated size of attached files like photos, including elements imported from SIT)


Installation
------------

Once the OS is installed (basic installation, with OpenSSH server), log in with your linux user (not root). 
You will also need unzip and wget (``sudo apt-get install unzip wget``).

Make sure you are in the user folder :

::

    cd /home/mylinuxuser

Download the latest version of Geotrek-admin with the following commands (X.Y.Z to replace 
with the latest stable version number : https://github.com/GeotrekCE/Geotrek-admin/releases) :

::

    wget https://github.com/GeotrekCE/Geotrek-admin/archive/X.Y.Z.zip

Unzip the archive of Geotrek-admin

::

    unzip Geotrek-admin-X.Y.Z.zip
    
You can rename Geotrek-admin-X.Y.Z folder to Geotrek-admin

Go into Geotrek-admin folder and launch its installation

::

    cd Geotrek-admin
    ./install.sh

You will be prompt for editing the base configuration file (``settings.ini``),
using the default editor.

:notes:

    If you leave *localhost* for the database host (``dbhost`` value), a
    Postgresql with PostGis will be installed locally.

    In order to use a remote server (*recommended*), set the appropriate values
    for the connection.
    The connection must be operational (it will be tested during install).


To make sure the application runs well after a reboot, try now : ``sudo reboot``.
And access the application ``http://yourserver/``.

You will be prompted for login, jump to :ref:`loading data section <loading data>`,
to create the admin user and fill the database with your data!

Tips and Tricks
---------------

* Use symlinks for uploaded files and cached tiles to avoid duplicating them on disk:

::

    mv var/tiles ~/tiles
    ln -s ~/tiles `pwd`/var/tiles

    mv var/media ~/media
    ln -s ~/media `pwd`/var/media


* Speed-up upgrades by caching downloads :

::

    mkdir ~/downloads
    mkdir  ~/.buildout

Create ``/home/sentiers/.buildout/default.cfg`` with ::

    [buildout]
    download-cache = /home/sentiers/downloads

Secure your server
------------------

* Use fail2ban:

::

    sudo apt-get install fail2ban

* Documentation : https://www.fail2ban.org/wiki/index.php/MANUAL_0_8
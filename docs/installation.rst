============
INSTALLATION
============

These instructions will install *Geotrek* on a dedicated server for production.
For a developer instance, please follow  :ref:`the dedicated procedure <development-section>`.

Requirements
------------

* Ubuntu Server 12.04 Precise Pangolin (http://releases.ubuntu.com/12.04/)


A first estimation on system resources is :

* 1 Go RAM
* 10 Go disk space


Installation
------------

Once the OS is installed (basic installation, with OpenSSH server), install
the last version with the following commands :

::

    curl https://raw.githubusercontent.com/makinacorpus/Geotrek/master/install.sh > install.sh
    chmod +x install.sh
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

See information below for configuration and loading initial demonstration data.


Software update
---------------

All versions are published on `the Github forge <https://github.com/makinacorpus/Geotrek/releases>`_.
Download and extract the new version in a separate folder (**recommended**).

.. code-block:: bash

    wget https://github.com/makinacorpus/Geotrek/archive/vX.Y.Z.zip
    unzip vX.Y.Z.zip
    cd Geotrek-X.Y.Z/

Before upgrading, **READ CAREFULLY** the release notes, either from the ``docs/changelog.rst``
files `or online <https://github.com/makinacorpus/Geotrek/releases>`_.

Shutdown previous running version :

::

    # Shutdown previous version
    sudo stop geotrek


Copy your old configuration and uploaded files to your new folder.

::

    # Configuration files
    cp -aR ../previous-version/etc/ .

    # Uploaded files
    cp -aR ../previous-version/var/ .

    # If you have advanced settings
    cp ../previous-version/geotrek/settings/custom.py geotrek/settings/custom.py


Deploy the new version :

::

    # Re-run install
    ./install.sh

    # Empty cache
    sudo service memcached restart


Check the version on the login page !


:note:

    Shutting down the current instance may not be necessary. But this allows us to
    keep a generic software update procedure.

    If you don't want to interrupt the service, skip the ``stop`` step, at your own risk.


Check out the :ref:`troubleshooting page<troubleshooting-section>` for common problems.


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

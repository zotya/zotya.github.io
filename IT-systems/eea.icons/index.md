---
eea.icons
---

#  EEA Icons

[![http://ci.eionet.europa.eu/job/eea.icons-
www/badge/icon](https://camo.githubusercontent.com/c54e963efbc933a064673471b2c8d2fb903b67f3/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e69636f6e732d7777772f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.icons-www/lastBuild) [![http://ci.eionet.europa.eu/job/eea.icons-
plone4/badge/icon](https://camo.githubusercontent.com/c75f2febfb0501e6517e10ac1d3ae3e224f8a31b/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e69636f6e732d706c6f6e65342f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.icons-plone4/lastBuild)

##  Introduction

Font Awesome icons for Plone and EEA packages

Note

This add-on doesn't do anything by itself. It needs to be integrated by a
developer within your own products. For reference you can check the
[eea.progressbar](http://eea.github.com/docs/eea.progressbar) package.

Contents

  * Introduction
  * Main features
  * Install
  * Getting started
  * Source code
  * Copyright and license
  * Funding

##  Main features

  1. Register [Font Awesome icons](http://fontawesome.io/icons/) into Plone CSS registry
  2. Register [Font Awesome Animation](http://l-lin.github.io/font-awesome-animation/) into Plone CSS registry

##  Install

  * Add eea.icons to your eggs section in your buildout and re-run buildout. You can download a sample buildout from <https://github.com/eea/eea.icons/tree/master/buildouts/plone4>
  * Install eea.icons within Site Setup &gt; Add-ons

##  Getting started

Simply use the &lt;span&gt; tag with specific classes as following:

    
    
    <span class="eea-icon eea-icon-camera-retro"></span>
    

And for animated icons:

    
    
    <span class="eea-icon eea-icon-heart eea-icon-anim-burst animated"></span>
    

You can use the entire set of [Font Awesome
icons](http://fontawesome.io/icons/) . Font Awesome gives you scalable vector
icons that can instantly be customized - size, color, drop shadow, and
anything that can be done with the power of CSS.

There are many ways to customise the icons display. See the [practical
examples](http://fontawesome.io/examples/) and just replace the generic
**fa-** classname with our **eea-icon-** class prefix and for font awesome
animated icons replace **faa-** classname with our **eea-icon-anim-** class
prefix.

##  Source code

  * Latest source code (Plone 4 compatible): <https://github.com/eea/eea.icons>

##  Copyright and license

The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Progress Bar (the Original Code) is free software; you can
redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

More details under docs/License.txt

##  Funding

[EEA](http://www.eea.europa.eu/) \- European Environment Agency (EU)


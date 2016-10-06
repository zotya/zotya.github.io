---
title: EEA Alchemy
---
#  EEA Alchemy

Auto-discover geographical coverage, temporal coverage, related items and
keywords from documents common metadata (title, description, body, etc), auto
highlight keywords within a page content based on selected tags and auto-
update related items based on internal links found within object's metadata.

##  Contents

Contents

  * Contents
  * Introduction
  * Main features
  * Planed features
  * Install
  * Getting started
    * Auto discover keywords, location, related items or temporal coverage
    * Auto tagging
    * Auto relations
  * Source code
  * Copyright and license
  * Funding

##  Introduction

This tool allows Plone managers to auto-discover and fix subject keywords,
location and temporal coverage using <http://www.alchemyapi.com/> web service.

##  Main features

  * Auto-discover keywords, locations and temporal coverage;
  * Auto highlight keywords within a page content based on selected tags and link them to a custom search page;
  * Auto update related items based on internal links found within object's metadata.

##  Planed features

  * Add a wizard icon near Subject, Location, etc fields in edit form to auto-discover and suggest tags based on text in other fields (Title, Description)

##  Install

  * Add eea.alchemy to your eggs section in your buildout and re-run buildout. You can download a sample buildout from <https://github.com/collective/eea.alchemy/tree/master/buildouts/plone4>
  * Install eea.alchemy within Site Setup &gt; Add-ons

##  Getting started

###  Auto discover keywords, location, related items or temporal coverage

  1. Get your alchemy key here: <http://www.alchemyapi.com/api/register.html>
  2. Update your alchemy API key within Site Setup &gt; Alchemy Settings
  3. Within Plone Control panel go to Alchemy Discoverer.

###  Auto tagging

  1. _Enable auto-tagging_ within **Site Setup &gt; Alchemy Settings**
  2. Edit your document and add some tags for it within **/edit &gt; Categorization.** For example, if you're writing a news article about _water pollution_ go to **/edit &gt; Categorization** and add _water pollution_ within tags field (also known as _keywords_, _subjects_, _topics_). Now when you navigate to the **View** page of this article, you'll notice that all occurrences of _water pollution_ within your news article body are links to a custom search page which is also configurable within **Alchemy Settings ControlPanel**

###  Auto relations

  1. _Enable auto-relations_ within **Site Setup &gt; Alchemy Settings**
  2. Edit your document and add some internal links for it within **/edit &gt; Body Text.** For example, if you're writing an article about an event add a internal link to this event within **Body Text** field. Now Save your article and you should see a notification message on top of the page saying something like: **Automatically detected and added one relation since it is linked in content.** If you check the related content section for your article you'll notice that the Event object was automatically added there.

##  Source code

  * Latest source code (Plone 4 compatible): <https://github.com/collective/eea.alchemy>
  * Plone 2 and 3 compatible: <https://github.com/collective/eea.alchemy/tree/plone25>

##  Copyright and license

The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Alchemy (the Original Code) is free software; you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

More details under docs/License.txt

##  Funding

[EEA](http://www.eea.europa.eu/) \- European Environment Agency (EU)


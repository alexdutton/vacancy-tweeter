Vacancy tweeter
===============

.. note::
   This is very experimental at this stage!

Playing around with tweeting University of Oxford vacancies.

Expected features:

* Watch vacancy information as provided by data.ox, and tweet the new ones
* Use geolocated tweets to point at where the job is based
* Use Twitter screenname details from OxPoints to reference the owning department(s)
* Provide job title, salary and link
* Links should have some sort of analytics
* Use multiple vacancy feeds according to the type of role (e.g. one for developers, another for researchers)
* Be able to tweet as departments if we have OAuth powers for their accounts

Current work
------------

Most of it shouldn't be too difficult, but there are some benefits to be had in
tweeting about particular types of jobs differently. Postdoctoral research
assistent posts (PDRAs) generally all have the same job title, so it wouldn't
be helpful to produce a feed of just the job titles and department names.

So, before I do the easy bits, I want to be able to pull the following kinds of
things out of the plain text descriptions of roles:

* name of research group
* area of study
* name of the research group lead

The current code is a start on this using ntlk. Help welcome!

Running
-------

In this directory, use::

    $ python -m vacancy_tweeter

This will download a list of vacancies, and start trying to do named entity
recognition. Matches will be highlighted in the terminal output.


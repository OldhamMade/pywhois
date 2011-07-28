pywhois
=======

A Python module for retrieving WHOIS information of domains.

This project has been cloned from http://code.google.com/p/pywhois/

Goal
----

- Create a simple importable Python module which will produce parsed WHOIS data for a given domain.
- Able to extract data for all the popular TLDs (com, org, net, ...)
- Query a WHOIS server directly instead of going through an intermediate web service like many others do.
- Works with Python 2.4+ and no external dependencies

Example
-------

::
    >>> import pywhois
    >>> w = pywhois.whois('google.com')
    >>> w.expiration_date
    ['14-sep-2011']
    >>> w.emails
    ['contact-admin@google.com',
     'dns-admin@google.com',
     'dns-admin@google.com',
     'dns-admin@google.com']
    >>> print w
    ...


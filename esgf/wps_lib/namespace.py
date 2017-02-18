#! /usr/bin/env python

WPS = 'wps'
OWS = 'ows'
XLINK = 'xlink'
XSI = 'xsi'

NSMAP = {
        WPS: 'http://www.opengis.net/wps/1.0.0',
        OWS: 'http://www.opengis.net/ows/1.1',
        XLINK: 'http://www.w3.org/1999/xlink',
        XSI: 'http://www.w3.org/2001/XMLSchema-instance',
        }

def tag(tag, namespace):
    return '{%s}%s' % (NSMAP[namespace], tag)

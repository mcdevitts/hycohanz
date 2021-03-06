# -*- coding: utf-8 -*-
"""
Functions in this module correspond more or less to the functions described 
in the HFSS Scripting Guide, Section "Ansoft Application Object Script 
Commands".

At last count there were 1 functions implemented out of 15.
"""
from __future__ import division, print_function, unicode_literals, absolute_import

import pywintypes
import win32com.client

def setup_interface():
    """
    Set up the COM interface to the running HFSS process.
    
    Returns
    -------
    oAnsoftApp : pywin32 COMObject
        Handle to the HFSS application interface
    oDesktop : pywin32 COMObject
        Handle to the HFSS desktop interface
    
    Examples
    --------
    >>> import hycohanz as hfss
    >>> [oAnsoftApp, oDesktop] = hfss.setup_interface()
    
    """
    # I'm still looking for a better way to do this.  This attaches to an 
    # existing HFSS process instead of creating a new one.  I would highly 
    # prefer that a new process is created.  Apparently 
    # win32com.client.DispatchEx() doesn't work here either.

    # Point win32com at the proper install of HFSS if there are multiple on the computer!

    try:
        oAnsoftApp = win32com.client.Dispatch('AnsoftHfss.HfssScriptInterface')
    except pywintypes.com_error:
        oAnsoftApp = win32com.client.Dispatch('AnsoftHfss.HfssScriptInterface.13.0')

    oDesktop = oAnsoftApp.GetAppDesktop()

    return [oAnsoftApp, oDesktop]

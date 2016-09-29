# -*- coding: utf-8 -*-
"""
Functions in this module correspond more or less to the functions described 
in the HFSS Scripting Guide, Section "Reporter Editor Script Commands"

At last count there were 5 functions implemented out of 28.
"""
from __future__ import division, print_function, unicode_literals, absolute_import

from hycohanz.design import get_module
from hycohanz.analysis_setup import get_setups, get_sweeps


def create_report(design,
                  report_name,
                  report_type,
                  display_type,
                  setup_name,
                  sweep_name,
                  context_array,
                  families_array,
                  report_data_array):
    """
    Creates a new report with a single trace and adds it to the Results branch in the project tree.

    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    ReportName : string
        The name of the report.
    ReportType : string
        The type of report. Possible values are:
        "Modal S Parameters" - Only for Driven Modal solution-type problems with ports.
        "Terminal S Parameters" - Only for Driven Terminal solution-type problems with ports.
        "Eigenmode Parameters" - Only for Eigenmode solution-type problems.
        "Fields"
        "Far Fields" - Only for problems with radiation or PML boundaries.
        "Near Fields" - Only for problems with radiation or PML boundaries.
        “Emission Test”
    DisplayType : string
        If ReportType is "Modal S Parameters", "Terminal S Parameters", or "Eigenmode Parameters",
        then set to one of the following:
            "Rectangular Plot", "Polar Plot", "Radiation Pattern", "Smith Chart", "Data Table",
            "3D Rectangular Plot", or "3D Polar Plot".
        If ReportType is "Fields", then set to one of the following:
            "Rectangular Plot", "Polar Plot", "Radiation Pattern", "Data Table", or "3D Rectangular Plot".
        If ReportType is "Far Fields" or "Near Fields", then set to one of the following:
            "Rectangular Plot", "Radiation Pattern", "Data Table", "3D Rectangular Plot", or "3D Polar Plot"
        If ReportType is “Emission Test”, then set to one of the following:
            “Rectangular Plot” or “Data Table”
    SetupName : str
        Name of HFSS setup to use, for example "Setup1"
    SweepName : str
        Name of HFSS sweep to use, for example "LastAdaptive"
    ContextArray : list of strings
        Context for which the expression is being evaluated. This can be an empty string if there is no context.
        Must be passed in as a pair, for example
            ["Domain:=", "Sweep"]
            ["Domain:=", "Time"]
            ["Context:=", "Infinite Sphere"]
    FamiliesArray : list of strings
        Contains sweep definitions for the report.
        Must be passed in as a pair, for example
            ["VariableName:=", "Value"]
            ["Theta:=", "All")
    ReportDataArray : list of strings
        This array contains the report quantity and X, Y, and (Z) axis definitions.
        ["X Component:=", VariableName, "Y Component:=", VariableName]

    Returns
    -------
    None
    """

    #  TODO: Is there a way to improve the way these lists are input? (contextarray, familiesarray, reportdataarray)
    #  TODO: Provide some error checking on reporttype and displaytype

    check_setup(design, setup_name)
    check_sweep(design, setup_name, sweep_name)
    solution_name = setup_name + " : " + sweep_name

    module = get_module(design, "ReportSetup")
    module.CreateReport(report_name,
                        report_type,
                        display_type,
                        solution_name,
                        context_array,
                        families_array,
                        report_data_array,
                        [])


def export_to_file(design, report_name, filename):
    """
    From a data table or plot, generates text format, comma delimited, tab delimited, or .dat type output files.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    reportName : string
        The name of the report.
    filename : string
        Path and file name. The extension determines the type of file exported.
        - .txt : Post processor format file
        - .csv : Comma-delimited data file
        - .tab : Tab-separated file
        - .dat : Ansoft plot data file

    Returns
    -------
    None
    """
    module = get_module(design, "ReportSetup")
    module.ExportToFile(report_name, filename)


def get_all_report_names(design):
    """
    Gets the names of existing reports in a design.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.

    Returns
    -------
    reportnames : list of str
        A list with the names of all the reports in the Design
    """
    module = get_module(design, "ReportSetup")
    report_list = list(module.GetAllReportNames())
    return map(str, report_list)


def add_traces(design,
               report_name,
               setup_name,
               sweep_name,
               context_array,
               families_array,
               report_data_array):
    """
    Creates a new trace and adds it to the specified report.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    reportName : string
        The name of the report.
    SetupName : string
        Name of HFSS setup to use, for example "Setup1"
    SweepName : string
        Name of HFSS sweep to use, for example "LastAdaptive"
    ContextArray : list of strings
        Context for which the expression is being evaluated. This can be an empty string if there is no context.
        Must be passed in as a pair, for example
            ["Domain:=", "Sweep"]
            ["Domain:=", "Time"]
            ["Context:=", "Infinite Sphere"]
    FamiliesArray : list of strings
        Contains sweep definitions for the report.
        Must be passed in as a pair, for example
            ["VariableName:=", "Value"]
            ["Theta:=", "All")
    ReportDataArray : list of strings
        This array contains the report quantity and X, Y, and (Z) axis definitions.
        ["X Component:=", VariableName, "Y Component:=", VariableName]

    """
    check_setup(design, setup_name)
    check_sweep(design, setup_name, sweep_name)
    solution_name = setup_name + " : " + sweep_name

    module = get_module(design, "ReportSetup")
    module.AddTraces(report_name, solution_name, context_array, families_array, report_data_array, [])


def rename_trace(design, report_name, trace_name, new_name):
    """
    Rename a trace in a plot.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    reportName : string
        The name of the report.
    traceName : string
        The name of the trace to be renamed.
    newName : string
        The new name of the trace.
    Returns
    -------
    None
    """
    module = get_module(design, "ReportSetup")
    module.RenameTrace(report_name, trace_name, new_name)


def check_setup(design, setup_name):
    """
    Check that SetupName is in the current design. If not raise an exception.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    SetupName : str
        Name of HFSS setup to use, for example "Setup1"

    Returns
    -------
    None
    """
    # Get all of the setups in the design and test the name
    setups = get_setups(design)
    if setup_name not in setups:
        raise Exception("SetupName not in design.")


def check_sweep(design, setup_name, sweepname):
    """
    Check that SweepName is in the SetupName. If not raise an exception.

    Parameters
    ----------
    oDesign : pywin32 COMObject
        The HFSS design object upon which to operate.
    SetupName : str
        Name of HFSS setup to use, for example "Setup1"
    SweepName : str
        Name of HFSS sweep to use, for example "LastAdaptive"

    Returns
    -------
    None
    """
    # Get all of the sweeps in the setup and test the name
    sweeps = get_sweeps(design, setup_name)
    if sweepname not in sweeps:
        raise Exception("SweepName not in the Setup.")

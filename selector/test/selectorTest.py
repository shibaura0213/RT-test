﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file selectorTest.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import selector

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
selectortest_spec = ["implementation_id", "selectorTest", 
         "type_name",         "selectorTest", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.a_list", "0",
         "conf.default.m_list", "0",
         "conf.default.t_list", "0",
         "conf.default.sound", "0",

         "conf.__widget__.a_list", "text",
         "conf.__widget__.m_list", "text",
         "conf.__widget__.t_list", "text",
         "conf.__widget__.sound", "text",

         "conf.__type__.a_list", "int",
         "conf.__type__.m_list", "int",
         "conf.__type__.t_list", "int",
         "conf.__type__.sound", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class selectorTest
# @brief ModuleDescription
# 
# 
# </rtc-template>
class selectorTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_footage_drink_type = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._footage_drink_typeIn = OpenRTM_aist.InPort("footage_drink_type", self._d_footage_drink_type)
        self._d_footage_drink_weight = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._footage_drink_weightIn = OpenRTM_aist.InPort("footage_drink_weight", self._d_footage_drink_weight)
        self._d_sound = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._soundIn = OpenRTM_aist.InPort("sound", self._d_sound)
        self._d_result_a = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._result_aOut = OpenRTM_aist.OutPort("result_a", self._d_result_a)
        self._d_result_m = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._result_mOut = OpenRTM_aist.OutPort("result_m", self._d_result_m)
        self._d_result_t = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._result_tOut = OpenRTM_aist.OutPort("result_t", self._d_result_t)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  a_list
         - DefaultValue: 0
        """
        self._a_list = [0]
        """
        
         - Name:  m_list
         - DefaultValue: 0
        """
        self._m_list = [0]
        """
        
         - Name:  t_list
         - DefaultValue: 0
        """
        self._t_list = [0]
        """
        
         - Name:  sound
         - DefaultValue: 0
        """
        self._sound = ['0']
        
        # </rtc-template>


         
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("a_list", self._a_list, "0")
        self.bindParameter("m_list", self._m_list, "0")
        self.bindParameter("t_list", self._t_list, "0")
        self.bindParameter("sound", self._sound, "0")
        
        # Set InPort buffers
        self.addInPort("footage_drink_type",self._footage_drink_typeIn)
        self.addInPort("footage_drink_weight",self._footage_drink_weightIn)
        self.addInPort("sound",self._soundIn)
        
        # Set OutPort buffers
        self.addOutPort("result_a",self._result_aOut)
        self.addOutPort("result_m",self._result_mOut)
        self.addOutPort("result_t",self._result_tOut)
        
        # Set service provider to Ports
        
        # Set service consumers to Ports
        
        # Set CORBA Service Ports
        
        return RTC.RTC_OK
    
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #
    #    return RTC.RTC_OK
    
    #    ##
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
    
        ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
    
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("selectorTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def selectorTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=selectortest_spec)
    manager.registerFactory(profile,
                            selectorTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    selectorTestInit(manager)
    selector.selectorInit(manager)

    # Create a component
    comp = manager.createComponent("selectorTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()


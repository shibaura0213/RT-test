#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file footage.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import cv2
from screeninfo import get_monitors


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
footage_spec = ["implementation_id", "footage", 
         "type_name",         "footage", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.footage_type", "1",
         "conf.default.height", "1",

         "conf.__widget__.footage_type", "text",
         "conf.__widget__.height", "text",

         "conf.__type__.footage_type", "string",
         "conf.__type__.height", "int",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class footage
# @brief ModuleDescription
# 
# 
# </rtc-template>
class footage(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_drink_type = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._drink_typeIn = OpenRTM_aist.InPort("drink_type", self._d_drink_type)
        self._d_drink_weight = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._drink_weightIn = OpenRTM_aist.InPort("drink_weight", self._d_drink_weight)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  footage_type
         - DefaultValue: 1
        """
        self._footage_type = ['1']
        """
        
         - Name:  height
         - DefaultValue: 1
        """
        self._height = [1]
		
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
        self.bindParameter("footage_type", self._footage_type, "1")
        self.bindParameter("height", self._height, "1")
		
        # Set InPort buffers
        self.addInPort("drink_type",self._drink_typeIn)
        self.addInPort("drink_weight",self._drink_weightIn)
		
        # Set OutPort buffers
		
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
	
    ###
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
        print("This is footage")
        # モニター情報を取得
        for monitor in get_monitors():
            m_w = monitor.width
            m_h = monitor.height
            print(f"Width: {monitor.width}, Height: {monitor.height}")


        #背景画像を用意
        footage_0 = cv2.imread("back.png")

        cv2.namedWindow("back",cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("back", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.resizeWindow("back",monitor.width,monitor.height)

        cv2.imshow("back",footage_0)
        cv2.waitKey(1)


    
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
        self._footage_type.clear()
        self._footage_type.append("1")
        cv2.destroyAllWindows()
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if self._drink_typeIn.isNew():
            self._d_drink_type = self._drink_typeIn.read()  
            self._footage_type.append(self._d_drink_type.data)
            #"1"はコンフィギュレーション値
            if not self._footage_type[-2] == self._footage_type[-1] and not self._footage_type[-2] == "1":
                cv2.destroyWindow(self._footage_type[-2])

        if self._drink_weightIn.isNew():
            self._d_drink_weight = self._drink_weightIn.read()
        
        if self._d_drink_weight.data < 1:
            self._d_drink_weight.data = 1
        
        #モニター情報を取得
        for monitor in get_monitors():
            m_w = monitor.width
            m_h = monitor.height

        water_level = self._d_drink_weight.data / 100
        water_height = int(m_h*water_level)
        
        footage_1 = self._footage_type[-1]
        image = cv2.imread(footage_1)

        print(water_level)
        print(footage_1)
        print("==============")

        #水位とモニター情報をもとに映像の大きさを設定
        cv2.namedWindow(footage_1, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(footage_1, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.resizeWindow(footage_1,m_w,m_h)

        #映像を流す
        cv2.moveWindow(footage_1, 0, m_h - water_height)
        cv2.imshow(footage_1,image)
        cv2.waitKey(1)

        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
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
	



def footageInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=footage_spec)
    manager.registerFactory(profile,
                            footage,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    footageInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("footage" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()


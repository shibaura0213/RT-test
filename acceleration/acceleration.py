#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file acceleration.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
import smbus
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
acceleration_spec = ["implementation_id", "acceleration", 
         "type_name",         "acceleration", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class acceleration
# @brief ModuleDescription
# 
# 
# </rtc-template>
class acceleration(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_acceleration = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
        """
        """
        self._accelerationOut = OpenRTM_aist.OutPort("acceleration", self._d_acceleration)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
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
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("acceleration",self._accelerationOut)
		
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
        print("This is acce")
        #I2C設定
        i2c = smbus.SMBus(1)
        dev_addr = 0x68

        #MPU-6050設定
        #CONFIGレジスタ
        i2c.write_byte_data(dev_addr, 0x1a, 0x00)

        #GYRO_CONFIGレジスタ
        i2c.write_byte_data(dev_addr, 0x1b, 0x00)

        #ACCEL_CONFIGレジスタ
        i2c.write_byte_data(dev_addr, 0x1c, 0x00)

        #PWR_MGMT_1レジスタ
        i2c.write_byte_data(dev_addr, 0x6b, 0x00)
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

        #加速度データ読み込み
        acc_x = i2c.read_word_data(dev_addr, 0x3b)
        acc_y = i2c.read_word_data(dev_addr, 0x3d)

        #加速度データ変換
        acc_x = (acc_x << 8) & 0xFF00 | (acc_x >> 8)
        acc_y = (acc_y << 8) & 0xFF00 | (acc_y >> 8)

        if acc_x >= 32768:
            acc_x -= 65536
    
        if acc_y >= 32768:
            acc_y -= 65536
    


        #重力加速度（G）に変換
        acc_x = acc_x / 16384.0
        acc_y = acc_y / 16384.0

        #標準値に（m/s^2）に変換
        acc_x = acc_x / 9.8
        acc_y = acc_y / 9.8

        #合計値
        X = acc_x**2
        Y = acc_y**2
        Acc = (X + Y)**0.5

        self._d_acceleration.data = Acc
        self._accelerationOut.write()
        time.sleep(0.1)
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
	



def accelerationInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=acceleration_spec)
    manager.registerFactory(profile,
                            acceleration,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    accelerationInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("acceleration" + args)

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


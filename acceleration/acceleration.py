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

        self._d_acceleration_x = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
        """
        """
        self._acceleration_xOut = OpenRTM_aist.OutPort("acceleration_x", self._d_acceleration_x)
        self._d_acceleration_y = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
        """
        """
        self._acceleration_yOut = OpenRTM_aist.OutPort("acceleration_y", self._d_acceleration_y)
        self._d_acceleration_z = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
        """
        """
        self._acceleration_zOut = OpenRTM_aist.OutPort("acceleration_z", self._d_acceleration_z)


		


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
        self.addOutPort("acceleration_x",self._acceleration_xOut)
        self.addOutPort("acceleration_y",self._acceleration_yOut)
        self.addOutPort("acceleration_z",self._acceleration_zOut)
		
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
        acc_z = i2c.read_word_data(dev_addr, 0x3f)
        
     #角速度データ読み込み
        gyr_x = i2c.read_word_data(dev_addr, 0x43)
        gyr_y = i2c.read_word_data(dev_addr, 0x45)
        gyr_z = i2c.read_word_data(dev_addr, 0x47)

        #加速度データ変換
        acc_x = (acc_x << 8) & 0xFF00 | (acc_x >> 8)
        acc_y = (acc_y << 8) & 0xFF00 | (acc_y >> 8)
        acc_z = (acc_z << 8) & 0xFF00 | (acc_z >> 8)
    
        #角速度データ変換
        gyr_x = (gyr_x << 8) & 0xFF00 | (gyr_x >> 8)
        gyr_y = (gyr_y << 8) & 0xFF00 | (gyr_y >> 8)
        gyr_z = (gyr_z << 8) & 0xFF00 | (gyr_z >> 8)

        #加速度極性判断
        if acc_x >= 32768:
            acc_x -= 65536
    
        if acc_y >= 32768:
            acc_y -= 65536
    
        if acc_z >= 32768:
            acc_z -= 65536
    
        #角速度極性判断
        if gyr_x >= 32768:
            gyr_x -= 65536
    
        if gyr_y >= 32768:
            gyr_y -= 65536
    
        if gyr_z >= 32768:
            gyr_z -= 65536

        #加速度を物理量に変換
        acc_x = acc_x / 16384.0
        acc_y = acc_y / 16384.0
        acc_z = acc_z / 16384.0
    
        #角速度を物理量に変換
        gyr_x = gyr_x / 131.0
        gyr_y = gyr_y / 131.0 
        gyr_z = gyr_z / 131.0

        m_<acceleration_x> = acc_x
        m_<acceleration_y> = acc_y
        m_<acceleration_z> = acc_z
 
        #加速度送る
        m_<acceleration_x>Out.wire()
        m_<acceleration_y>Out.wire()
        m_<acceleration_z>Out.wire()
        #角速度送る


    
        time.sleep(0.5)

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


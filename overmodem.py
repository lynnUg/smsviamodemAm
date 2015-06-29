from pygsm import GsmModem
import logging
class overmodem:
    def __init__(self,port,in_verbose = True):
        self.port=port
        self.verbose=in_verbose
        self.debug=logging.debug
        self.working_modem=self.start_modem()
    def statusmsg( self, input_string ):
        if self.verbose:
            print "[ STATUS ] " + input_string
    def errormsg( self, input_string ):
        if self.verbose:
            print "[ ERROR ] " + input_string
                    
    def sms(self , phone_number,text):
        self.modem.wait_for_network()
        was_sent = self.modem.send_sms(
            		phone_number,
            		text)
        return was_sent
    def gsm_log(self, modem, str, level):
        self.debug("%s: %s" % (level, str))
   
    def start_modem(self):
        self.statusmsg("Connecting and booting via pyGSM...")
    	result=False
    	try:
    		result=True
    		
    		self.modem = GsmModem(logger=self.gsm_log, port=self.port)
    		self.modem.boot()
    	except Exception as e:
            result=False
            self.statusmsg(e.message)
    	return result

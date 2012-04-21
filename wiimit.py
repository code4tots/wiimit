#!/usr/bin/python
# 4.20-21.2012
# import everything I need
import threading
import time
import cwiid

# Global stuff
GL = {}
GL['running'] = True
# Cursor stuff
GL['lastMove'] = time.time()
GL['cx'] , GL['cy'] = 130 , 130
GL['cursorSpeed'] = 0.1
#
GL['lastPrint'] = time.time()
# Buttons
GL['b'] = {}
GL['b']['C'] = False
GL['b']['Z'] = False
GL['b']['A'] = False
GL['b']['B'] = False
GL['b']['up'] = False
GL['b']['down'] = False
GL['b']['left'] = False
GL['b']['right'] = False
GL['b']['1'] = False
GL['b']['2'] = False
GL['b']['+'] = False
GL['b']['-'] = False
GL['b']['home'] = False

GL['rep'] = time.time()

# Set up wiimote
wm = cwiid.Wiimote()
time.sleep(0.5)
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK
# wm.state = { 'acc': (x,y,z), 'led': , 'rpt_mode': , 'ext_type': , 'buttons': xx, 'rumble': 0, 'error': 0, 'nunchuk': {'acc':(x,y,z), 'buttons': xx, 'stick': (x,y)}, 'battery': }

# Set up Xlib stuff
from Xlib import X, display, ext
disp = display.Display()


# helper methods
def buttonState():
	b = {}
	# C button (on nunchuk)
	# if ( wm.state['nunchuk']['buttons'] / 2 ) % 2 == 1:
	b['C'] = ( wm.state['nunchuk']['buttons'] / 2 ) % 2 == 1
	# Z button (on nunchuk)
	# if ( wm.state['nunchuk']['buttons'] / 1 ) % 2 == 1:
	b['Z'] = ( wm.state['nunchuk']['buttons'] / 1 ) % 2 == 1
	# 1 button
	b['1'] = ( wm.state['buttons'] / 2 ) % 2 == 1
	# 2 button (yes it's weird that 2 --> 1 and 1 --> 2)
	b['2'] = ( wm.state['buttons'] / 1 ) % 2 == 1
	# A button 8
	b['A'] = ( wm.state['buttons'] / 8 ) % 2 == 1
	# B button 4
	b['B'] = ( wm.state['buttons'] / 4 ) % 2 == 1
	# minus button 16
	b['-'] = ( wm.state['buttons'] / 16 ) % 2 == 1
	# plus button 4096
	b['+'] = ( wm.state['buttons'] / 4096 ) % 2 == 1
	# home button 128
	b['home'] = ( wm.state['buttons'] / 128 ) % 2 == 1
	# Up button 2048
	b['up'] = ( wm.state['buttons'] / 2048 ) % 2 == 1
	# Down button 1024
	b['down'] = ( wm.state['buttons'] / 1024 ) % 2 == 1
	# Left button 256
	b['left'] = ( wm.state['buttons'] / 256 ) % 2 == 1
	# Right button 512
	b['right'] = ( wm.state['buttons'] / 512 ) % 2 == 1



while GL['running']:
	now = time.time()
	
	# Keep track of buttons pressed
	b = {}
	
	# Move cursor if enough time has passed
	if now - GL['lastMove'] > 0.005:
		# print now ,  now - GL['lastMove']
		
		x , y = wm.state['nunchuk']['stick']
		dx , dy = x - GL['cx'] , y - GL['cy']
		dx *= GL['cursorSpeed']
		dy *= GL['cursorSpeed']
		disp.warp_pointer(dx,-dy)
		
		disp.sync()
		GL['lastMove'] = now
		
	# Check for button clicks
	# C button (on nunchuk)
	# if ( wm.state['nunchuk']['buttons'] / 2 ) % 2 == 1:
	b['C'] = ( wm.state['nunchuk']['buttons'] / 2 ) % 2 == 1
	# Z button (on nunchuk)
	# if ( wm.state['nunchuk']['buttons'] / 1 ) % 2 == 1:
	b['Z'] = ( wm.state['nunchuk']['buttons'] / 1 ) % 2 == 1
	# 1 button
	b['1'] = ( wm.state['buttons'] / 2 ) % 2 == 1
	# 2 button (yes it's weird that 2 --> 1 and 1 --> 2)
	b['2'] = ( wm.state['buttons'] / 1 ) % 2 == 1
	# A button 8
	b['A'] = ( wm.state['buttons'] / 8 ) % 2 == 1
	# B button 4
	b['B'] = ( wm.state['buttons'] / 4 ) % 2 == 1
	# minus button 16
	b['-'] = ( wm.state['buttons'] / 16 ) % 2 == 1
	# plus button 4096
	b['+'] = ( wm.state['buttons'] / 4096 ) % 2 == 1
	# home button 128
	b['home'] = ( wm.state['buttons'] / 128 ) % 2 == 1
	# Up button 2048
	b['up'] = ( wm.state['buttons'] / 2048 ) % 2 == 1
	# Down button 1024
	b['down'] = ( wm.state['buttons'] / 1024 ) % 2 == 1
	# Left button 256
	b['left'] = ( wm.state['buttons'] / 256 ) % 2 == 1
	# Right button 512
	b['right'] = ( wm.state['buttons'] / 512 ) % 2 == 1
	
	# Now process the buttons presses
	#if now - GL['lastPrint'] > 0.3 and (wm.state['buttons'] != 0 or wm.state['nunchuk']['buttons'] != 0):
	#	for key in b:
	#		if b[key]:
	#			print key + ' was pressed.'
	#			
	#	GL['lastPrint'] = now
	
	if GL['b']['A'] != b['A']:
		#if b['A'] and b['C']:
		#	ext.xtest.fake_input(disp,X.ButtonPress,37) # ctrl
			#ext.xtest.fake_input(disp,X.ButtonPress,int('2e',16)) # c (2e)
			#ext.xtest.fake_input(disp,X.ButtonRelease,int('2e',16)) # c
		#	ext.xtest.fake_input(disp,X.ButtonRelease,37) # ctrl
		if b['A']:
			print 'A was pressed'
			# 1 left ; 2 middle ; 3 right
			ext.xtest.fake_input(disp,X.ButtonPress,1)
		else:
			ext.xtest.fake_input(disp,X.ButtonRelease,1)
			print 'A was released'
			
	if GL['b']['B'] != b['B']:
		#if b['B'] and b['C']:
			#ext.xtest.fake_input(disp,X.ButtonPress,37) # ctrl
		#	ext.xtest.fake_input(disp,X.ButtonPress,int('2f',16)) # v
		#	ext.xtest.fake_input(disp,X.ButtonRelease,int('2f',16)) # v (2f)
			#ext.xtest.fake_input(disp,X.ButtonRelease,37) # ctrl
		if b['B']:
			print 'B was pressed'
			ext.xtest.fake_input(disp,X.ButtonPress,3)
		else:
			ext.xtest.fake_input(disp,X.ButtonRelease,3)
			print 'B was released'
			
	if GL['b']['C'] != b['C']:
		if b['C']:
			print 'C was pressed'
		else:
			print 'C was released'
			
	if GL['b']['up'] != b['up']:
		#if b['up'] and b['C']:
			#ext.xtest.fake_input(disp,X.KeyPress,(10*16) + (15))
			#ext.xtest.fake_input(disp,X.KeyRelease,(10*16) + (15))
		#elif b['up']:
		if b['up']:
			print 'up was pressed'
			ext.xtest.fake_input(disp,X.ButtonPress,4)
		else:
			ext.xtest.fake_input(disp,X.ButtonRelease,4)
			print 'up was released'
	elif time.time() - GL['rep'] > 0.05:
		if b['up']:
			ext.xtest.fake_input(disp,X.ButtonPress,4)
			ext.xtest.fake_input(disp,X.ButtonRelease,4)
			GL['rep'] = time.time()

	if GL['b']['down'] != b['down']:
		#if b['down'] and b['C']:
			#ext.xtest.fake_input(disp,X.KeyPress,(10*16) + (14))
			#ext.xtest.fake_input(disp,X.KeyRelease,(10*16) + (14))
		#elif b['down']:
		if b['down']:
			print 'down was pressed'
			ext.xtest.fake_input(disp,X.ButtonPress,5)
		else:
			ext.xtest.fake_input(disp,X.ButtonRelease,5)
			print 'down was released'
	elif time.time() - GL['rep'] > 0.05:
		if b['down']:
			ext.xtest.fake_input(disp,X.ButtonPress,5)
			ext.xtest.fake_input(disp,X.ButtonRelease,5)
			GL['rep'] = time.time()
			


	# Now save the current button configurations
	for key in b:
		GL['b'][key] = b[key]

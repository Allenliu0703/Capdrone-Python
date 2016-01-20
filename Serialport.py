import serial
import time
import sys
import glob
global xList
global yList
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
#List all serial port on Computer
def serial_Ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            # s = serial.Serial(port)
            # s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def serial_Setup(port):
	baudrate = 9600
	timeout = 3
	# port = "/dev/tty.usbserial-A50285BI"
	return serial.Serial (str(port), baudrate, timeout = timeout)

def serial_Listen(ser):
	try:
		line = ser.readline()
	except ser.SerialTimeoutException:
		print('Timeout! Data could not be read!')
	# print (line.decode("utf-8"))
	return line.decode("utf-8")

def serial_Decoder(line_received):
	data_array = line_received.split()
	if not data_array:
		print('Data not received :( Data array is empty')

	# else:
	# 	if any(c.isalpha() for c in data_array[0][2:]) or any(c.isalpha() for c in data_array[1][2:]):
	# 		print (data_array)
	# 		data_array = None
	# 		pass
	# 	else:
	# 		data_x = int(data_array[0][2:])
	# 		data_y = int(data_array[1][2:])
	# 		data_array = [data_x,data_y]
	# 	print(data_array)
	# return data_array
	if len(data_array) == 3:
		pass
	else:
		data_x = int(data_array[0][2:])
		data_y = int(data_array[1][2:])
		data_array = [data_x,data_y]
	return data_array

def serial_Start(serial,xList,yList):
	data = serial_Listen (serial)
	# for i in range (0, len(data)):
	#     if (data[i] is 'X')and (data[i+1] is ':'):
	#         a = i+2
	#         i= a
	#         while(RepresentsInt(data[i])):
	#             i= i +1
	#         x = int (data[a:i])
	#     if (data[i] is 'Y') and(data[i+1] is ':'):
	#         a = i+2
	#         i = a
	#         while(RepresentsInt(data[i])):
	#             i= i+1
	#             if i >= len(data):
	#                 break 
	#         y = int (data[a:i])
	#         if x in range (0,1001) and y in range (0,1001):
	#             floatx = float(x)/100
	#             floaty = float(y)/100
	#             xList.append(floatx)
	#             yList.append(floaty)
	#         else:
	#             # print (str(x) + " ;" + str(y))
	#             pass
	data_array = data.split()
	if len(data_array) >= 3:
		print(data_array)
		pass
	elif (len(data_array) == 2):
		if hasNumbers(data_array[0][2:]) and hasNumbers(data_array[1][2:]):
			data_x = int(data_array[0][2:])
			data_y = int(data_array[1][2:])
			if data_x in range (0,1001) and data_y in range (0,1001):
		            floatx = float(data_x)/100
		            floaty = float(data_y)/100
		            xList.append(floatx)
		            yList.append(floaty)
			else:
		            print (str(data_x) + " ;" + str(data_y))
		            pass
		else:
			print(data_array)
	else:
		print(data_array)



# def main():
# 	ser = serial_Setup ()
# 	while 1:
# 		data = serial_Listen (ser)
# 		# print(data)
# 		location_data = serial_Decoder(data)
# 		# print(location_data)
# 		if not location_data:
# 			print('Data not received :( Data array is empty')
# 		else:
# 			# ser.write("X value is received as " + (str)(location_data[0]) + " Y value is received as " + (str)(location_data[1]))
# 			print ("X value is received as " + (str)(location_data[0]) + " Y value is received as " + (str)(location_data[1]))



if __name__ == '__main__':
    print(serial_Ports())

# ser = serial.Serial('/dev/tty.usbmodem1421', 9600, timeout= 1)
 
# while 1:
#  try:
#   x = ser.readline()
#   #time.sleep(1)
#   print (x)
#   time.sleep(0.01)
#  except ser.SerialTimeoutException:
#   print('Data could not be read')

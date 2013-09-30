# -*- coding: utf-8 -*-

# Python + PyQt4 By Skylar 
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
# Por favor si modificas algo haz referencia al autor.
from PyQt4 import QtCore, QtGui
import sys
from login import Ui_Form
from principal import Ui_Form1
import socket
global usuario 
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import re
import pyodbc
import hashlib
import checa


usuario = 'jsandoval'
class v_login(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.vlogin = Ui_Form()
		self.vlogin.setupUi(self)

		self.connect(self.vlogin.btn_aceptar, QtCore.SIGNAL('clicked()'),self.validaUsuario)

	def conectaPosMaster_Valida(self,sentencia):
			return False
			"""
			#QMessageBox.about(self, "Error Acceso Denegado", 'entre a consulta')
			conn = pyodbc.connect("DRIVER={SQL Server};SERVER=192.168.1.1;UID=usuario;PWD=password;")
			curs = conn.cursor()
			curs.execute(sentencia)
			rows = curs.fetchall()
			  
			  
			if rows != "[]":

				for row in rows:
				   global usuario
				   usuario = row.emp_nombre
				   return True

			else:

				return False		
			  
			curs.close ()
			conn.close () #"""

	def validaUsuario(self):
		usuario = self.vlogin.t_usuario.text()
		passwd = self.vlogin.t_password.text()


		passwd = passwd.encode('utf-8')
		passwd_md5 = hashlib.md5(passwd).hexdigest()
		#QMessageBox.about(self, "Error Acceso Denegado", passwd_md5)

		tienda_var = "select emp_nombre, emp_id, app_permiso\
		              from soporte..cat_empleado, soporte..cat_empleado_app\
		              where app_emp = emp_id\
		                    and emp_login = '%s'\
		                    and emp_password = '%s' and app_desc = 'DHCP'" % (usuario,passwd_md5)

		        
		if self.conectaPosMaster_Valida(tienda_var) == True:
			
			self.ventana()
		    
		else:
			QMessageBox.about(self, "Error Acceso Denegado", str('Acceso Denegado, Verifica Password '))
			self.vlogin.t_password.clear() 



		

	def ventana(self):
		#global usuario
		global ip
		self.hide()
		
		#usuario = self.vlogin.t_usuario.text()
		ip = socket.gethostbyname(socket.gethostname())

		self.w = v_principal()
		self.w.show()
		

class v_principal(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.vprincipal = Ui_Form1()
		self.vprincipal.setupUi(self)
		self.vprincipal.label.setText(usuario)
		self.vprincipal.label_2.setText(ip)
		d = date.today()
		self.vprincipal.label_3.setText(str(d.year)+ '-' + str(d.month) + '-'+ str(d.day))
		self.connect(self.vprincipal.lineEdit_14, QtCore.SIGNAL('textChanged(QString)'), self.cambio)
		self.connect(self.vprincipal.pushButton_7, QtCore.SIGNAL('clicked()'),self.comandos)
		self.vprincipal.label_9.hide()
		self.vprincipal.label_10.hide()
		self.vprincipal.label_11.hide()
		self.vprincipal.pushButton_6.hide()
		self.vprincipal.pushButton_7.hide()
		self.connect(self.vprincipal.lineEdit_2, QtCore.SIGNAL('textChanged(QString)'), self.rango)
		self.connect(self.vprincipal.lineEdit_3, QtCore.SIGNAL('textChanged(QString)'), self.rango1)
		self.vprincipal.tabWidget.setEnabled(False)
		self.connect(self.vprincipal.pushButton_6, QtCore.SIGNAL('clicked()'),self.reserva)
		self.vprincipal.lineEdit_14.setFocus()
		#self.vprincipal.lineEdit_14.setInputMask('000.000.000.000;_')
		self.connect(self.vprincipal.pushButton_2, QtCore.SIGNAL('clicked()'),self.ver_ipreservada)
		self.connect(self.vprincipal.pushButton, QtCore.SIGNAL('clicked()'),self.ver_scope)
		self.connect(self.vprincipal.pushButton_9, QtCore.SIGNAL('clicked()'),self.ver_clientes)
		self.connect(self.vprincipal.pushButton_5, QtCore.SIGNAL('clicked()'),self.Elimina_Ip)
		self.connect(self.vprincipal.pushButton_4, QtCore.SIGNAL('clicked()'),self.Elimina_Ip_Reservada)
		self.connect(self.vprincipal.pushButton_3, QtCore.SIGNAL('clicked()'),self.Elimina_scope)
		self.connect(self.vprincipal.lineEdit_11, QtCore.SIGNAL('textChanged(QString)'), self.rangoMC)


	def limpia_campos(self,objeto):
		if objeto == 'L_ip':
			self.vprincipal.lineEdit_9.clear()
		elif objeto == 'L_ip_R':
			self.vprincipal.lineEdit_10.setText(str(self.vprincipal.label_17.text()))
			self.vprincipal.lineEdit_15.clear()
		elif objeto == 'L_mc':
			self.vprincipal.lineEdit_11.clear()
			self.vprincipal.lineEdit_12.clear()
			self.vprincipal.lineEdit_13.clear()



	def Elimina_scope(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')

		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server delete scope %(oct1)s.%(oct2)s.0.0 DHCPFULLFORCE'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1])
			else:
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server delete scope %(oct1)s.%(oct2)s.%(oct3)s.0 DHCPFULLFORCE'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])

			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_10,"<b>Eliminando Scope  .. </b>")

			inserta = "insert soporte..sop_bitacora_app values ('DHCP', '%s', '%s', getdate(), '%s', '%s')" \
			% (servidor,socket.gethostbyname(socket.gethostname()),usuario,"Elimino Scope: %(srv)s")\
	 				% dict (srv=servidor)
			#QMessageBox.about(self, "My message box", str(inserta))
			self.conectaPosMaster_log(inserta)


	def Elimina_Ip_Reservada(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')	
		macadress = self.vprincipal.lineEdit_15.text()
		macadress = macadress.replace(':', '')

		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.0.0 delete reservedip %(eliminaIp)s  %(mc)s'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1],eliminaIp=str(self.vprincipal.lineEdit_10.text()),mc=macadress)
			else:
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.%(oct3)s.0 delete reservedip %(eliminaIp)s  %(mc)s'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2],eliminaIp=str(self.vprincipal.lineEdit_10.text()),mc=macadress)
			
			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_10,"<b>Eliminando IP Reservada  .. </b>")

			inserta = "insert soporte..sop_bitacora_app values ('DHCP', '%s', '%s', getdate(), '%s', '%s')" \
			% (servidor,socket.gethostbyname(socket.gethostname()),usuario,"Elimino IP Reservada: %(ip)s")\
	 				% dict (ip=self.vprincipal.lineEdit_10.text())
			#QMessageBox.about(self, "My message box", str(inserta))
			self.conectaPosMaster_log(inserta)

			self.limpia_campos('L_ip_R')


	def Elimina_Ip(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')

		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.0.0 delete lease %(eliminaIp)s'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1],eliminaIp=str(self.vprincipal.label_17.text()) + str(self.vprincipal.lineEdit_9.text()))
			else:
				sentencia_dhcp_10 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.%(oct3)s.0 delete lease %(eliminaIp)s'" \
			                        % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2],eliminaIp=str(self.vprincipal.label_17.text()) + str(self.vprincipal.lineEdit_9.text()))
			
			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_10,"<b>Eliminando IP  .. </b>")

			inserta = "insert soporte..sop_bitacora_app values ('DHCP', '%s', '%s', getdate(), '%s', '%s')" \
					% (servidor,socket.gethostbyname(socket.gethostname()),usuario,"Elimino IP: %(ip)s")\
			 				% dict (ip=self.vprincipal.label_17.text() + self.vprincipal.lineEdit_9.text())
			#QMessageBox.about(self, "My message box", str(inserta))
			self.conectaPosMaster_log(inserta)

			self.limpia_campos('L_ip')
		


	def ver_clientes(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')	
		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:

			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':	
				sentencia_dhcp_9 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.0.0 show clients'" % dict(oct1=octeto[0],oct2=octeto[1])
			else:
				sentencia_dhcp_9 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.%(oct3)s.0 show clients'" % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])

			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_9,"<b>Listando Clientes Conectados  .. </b>")

	def ver_scope(self):
		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			sentencia_dhcp_8 = "xp_cmdshell'netsh dhcp server show scope'"
			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_8,"<b>Listando Scope  .. </b>")

	def ver_ipreservada(self):
		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			texto = self.vprincipal.lineEdit_14.text()
			octeto = texto.split('.')

			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':	
				sentencia_dhcp_4 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.0.0 show reservedip'" \
			                    % dict(oct1=octeto[0],oct2=octeto[1],srv=servidor)
			else:
				sentencia_dhcp_4 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.%(oct3)s.0 show reservedip'" \
			                    % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2],srv=servidor)

			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_4,"<b>Listando Ip Reservadas  .. </b>")		


	def comandos(self):

		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:

			rinicio = self.vprincipal.lineEdit_2.text()
			rfinal = self.vprincipal.lineEdit_3.text()
			texto = self.vprincipal.lineEdit_14.text()
			octeto = texto.split('.')


			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				sentencia_dhcp_1 = "xp_cmdshell'netsh dhcp server add scope %(oct1)s.%(oct2)s.0.0 255.255.0.0 Inventario DHCP_Inventarios'" % dict(oct1=octeto[0],oct2=octeto[1])
				sentencia_dhcp_2 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.0.0 set state 0'"  % dict(srv =servidor,oct1=octeto[0],oct2=octeto[1])


				sentencia_dhcp_3 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.0.0 add iprange %(rango)s%(rango_inicio)s %(rango)s%(rango_final)s'" \
				% dict(srv =servidor,oct1=octeto[0],oct2=octeto[1],rango_inicio=rinicio,rango_final=rfinal,rango=self.vprincipal.label_6.text())


				sentencia_dhcp_5 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.0.0 set state 1'" % dict(srv =servidor,oct1=octeto[0],oct2=octeto[1])

				sentencia_dhcp_7 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.0.0 set optionvalue 003 IPADDRESS %(oct1)s.%(oct2)s.254.254'" % dict(oct1=octeto[0],oct2=octeto[1])


			else:
				sentencia_dhcp_1 = "xp_cmdshell'netsh dhcp server add scope %(oct1)s.%(oct2)s.%(oct3)s.0 255.255.255.0 Inventario DHCP_Inventarios'" % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])



				sentencia_dhcp_2 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.%(oct3)s.0 set state 0'"  % dict(srv =servidor,oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])


				sentencia_dhcp_3 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.%(oct3)s.0 add iprange %(rango)s%(rango_inicio)s %(rango)s%(rango_final)s'" \
				% dict(srv =servidor,oct1=octeto[0],oct2=octeto[1],oct3=octeto[2],rango_inicio=rinicio,rango_final=rfinal,rango=self.vprincipal.label_6.text())


				sentencia_dhcp_5 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.%(oct3)s.0 set state 1'" % dict(srv =servidor,oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])

				sentencia_dhcp_7 = "xp_cmdshell'netsh dhcp server scope %(oct1)s.%(oct2)s.%(oct3)s.0 set optionvalue 003 IPADDRESS %(oct1)s.%(oct2)s.%(oct3)s.254'" % dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2])

			

			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_1,"<b>Creando Scope  .. </b>")
			self.Conecta(servidor,sentencia_dhcp_2,"<b>Detener Scope  .. </b>")
			self.Conecta(servidor,sentencia_dhcp_3,"<b>Crear Rangos   .. </b>")
			self.Conecta(servidor,sentencia_dhcp_7,"<b>Asignar Gateway   .. </b>")
			self.Conecta(servidor,sentencia_dhcp_5,"<b>Iniciar Scope .. </b>")
			self.vprincipal.textEdit.append(str('<b>Proceso DHCP Terminado ... </b> '))

			inserta = "insert soporte..sop_bitacora_app values ('DHCP', '%s', '%s', getdate(), '%s', '%s')" \
					% (servidor,socket.gethostbyname(socket.gethostname()),usuario,"Creo Scope: %(srv)s")\
			 				% dict (srv=servidor)
			#QMessageBox.about(self, "My message box", str(inserta))
			self.conectaPosMaster_log(inserta)
			

	def cambio(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')
		
		#QMessageBox.about(self, "My message box", str(len(octeto)))

		if len(octeto) >= 4:
			if self.ValidarIP(texto) == True:
				self.vprincipal.label_6.setStyleSheet("color:green;")
				self.vprincipal.label_7.setStyleSheet("color:green;")
				self.vprincipal.label_17.setStyleSheet("color:green;")
				self.vprincipal.label_20.setStyleSheet("color:green;")	
				self.vprincipal.tabWidget.setEnabled(True)
			else:
				self.vprincipal.label_6.setStyleSheet("color:red;")
				self.vprincipal.label_7.setStyleSheet("color:red;")	
				self.vprincipal.label_17.setStyleSheet("color:red;")	
				self.vprincipal.label_20.setStyleSheet("color:red;")
				self.vprincipal.tabWidget.setEnabled(False)	
	

		if len(octeto) >= 4:
			
			if octeto[0] == '190' or octeto[0] == '191':
				self.vprincipal.lineEdit_2.setText('0')
				self.vprincipal.lineEdit_3.setText('0')
				self.vprincipal.lineEdit_11.setText('0')
				octeto_OK = octeto[0] + '.' + octeto[1] + '.5.'
				
			
			elif octeto[0] == '10':
				self.vprincipal.lineEdit_2.setText('0')
				self.vprincipal.lineEdit_3.setText('0')
				self.vprincipal.lineEdit_11.setText('0')
				octeto_OK = octeto[0] + '.' + octeto[1] + '.' + octeto[2] + '.'

			elif octeto[0] == '192':
				self.vprincipal.lineEdit_2.setText('0')
				self.vprincipal.lineEdit_3.setText('0')
				self.vprincipal.lineEdit_11.setText('0')
				octeto_OK = octeto[0] + '.' + octeto[1] + '.' + octeto[2] + '.'
				
			else:
				octeto_OK = ('Octeto Error')
				self.vprincipal.tabWidget.setEnabled(False)	

		else:

			octeto_OK = texto



		global servidor
		servidor = self.vprincipal.lineEdit_14.text()
		self.vprincipal.label_6.setText(octeto_OK)
		self.vprincipal.label_7.setText(octeto_OK)
		self.vprincipal.label_17.setText(octeto_OK)
		self.vprincipal.label_20.setText(octeto_OK)
		self.vprincipal.lineEdit_10.setText(octeto_OK)



	def reserva(self):
		texto = self.vprincipal.lineEdit_14.text()
		octeto = texto.split('.')
		macadress = self.vprincipal.lineEdit_12.text()
		macadress = macadress.replace(':', '')

		if checa.enLinea(servidor) == False:
			QMessageBox.about(self, str('Validando Servidor'), str('Servidor Fuera de Linea, Favor de Verificar la  IP --> %(srv)s <-- ' % dict (srv=str(servidor)) ))
		else:
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				sentencia_dhcp_4 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.0.0 add reservedip %(rango)s%(rs)s  \"%(macc_adr)s\" \"%(nom)s\" \"\" BOTH'"\
						% dict(oct1=octeto[0],oct2=octeto[1],rango=self.vprincipal.label_6.text(), rs=self.vprincipal.lineEdit_11.text(), macc_adr=macadress, \
							nom=self.vprincipal.lineEdit_13.text(),srv =servidor)
			else:
				sentencia_dhcp_4 = "xp_cmdshell'netsh dhcp server %(srv)s scope %(oct1)s.%(oct2)s.%(oct3)s.0 add reservedip %(rango)s%(rs)s  \"%(macc_adr)s\" \"%(nom)s\" \"\" BOTH'"\
						% dict(oct1=octeto[0],oct2=octeto[1],oct3=octeto[2],rango=self.vprincipal.label_6.text(), rs=self.vprincipal.lineEdit_11.text(), macc_adr=macadress, \
							nom=self.vprincipal.lineEdit_13.text(),srv =servidor)

			#QMessageBox.about(self, "My message box", str(sentencia_dhcp_4))
			self.vprincipal.textEdit.clear()
			self.Conecta(servidor,sentencia_dhcp_4,"<b>Reservando IP </b> ")
			inserta = "insert soporte..sop_bitacora_app values ('DHCP', '%s', '%s', getdate(), '%s', '%s')" \
					% (servidor,socket.gethostbyname(socket.gethostname()),usuario,"Borro IP Reservada: %(ip)s")\
			 				% dict (ip=self.vprincipal.label_20.text() + self.vprincipal.lineEdit_11.text())
			#QMessageBox.about(self, "My message box", str(inserta))
			self.conectaPosMaster_log(inserta)
			  
			self.limpia_campos('L_mc')

	def ValidarIP(self,ip_valida):
		pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
		if re.match(pattern, ip_valida):
						return True
		else:
						return False


	def rangoMC(self):
		texto = self.vprincipal.lineEdit_14.text()
		rangomc_t = self.vprincipal.lineEdit_11.text()

		octeto = texto.split('.')
		if rangomc_t != "":
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				rango_inicio = 100
				rango_final = 190
				
			
			elif octeto[0] == '10':
				rango_inicio = 145
				rango_final = 200
				
			else:
				rango_inicio = 0
				

			if int(rangomc_t) >= rango_inicio and int(rangomc_t) <= rango_final:
				self.vprincipal.label_11.show()
				self.vprincipal.label_11.setStyleSheet("color:green;")
				self.vprincipal.label_11.setText('OK!')
				self.vprincipal.pushButton_6.show()
			else:
				self.vprincipal.label_11.show()
				self.vprincipal.label_11.setStyleSheet("color:red;")
				self.vprincipal.label_11.setText('Rango Invalido')
				self.vprincipal.pushButton_6.hide()
		else:

			pass




	def rango(self):
		texto = self.vprincipal.lineEdit_14.text()
		rinicio = self.vprincipal.lineEdit_2.text()
		rfinal = self.vprincipal.lineEdit_3.text()

		octeto = texto.split('.')
		if rinicio != "":
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				rango_inicio = 100
				rango_final = 190
				
			
			elif octeto[0] == '10':
				rango_inicio = 145
				rango_final = 200
				
			else:
				rango_inicio = 0
				rango_final = 0

			if int(rinicio) >= rango_inicio and int(rinicio) <= rango_final and int(rinicio) != int(rfinal):
				self.vprincipal.label_9.show()
				self.vprincipal.label_9.setStyleSheet("color:green;")
				self.vprincipal.label_9.setText('OK!')
				self.vprincipal.lineEdit_3.show()
			else:
				self.vprincipal.label_9.show()
				self.vprincipal.label_9.setStyleSheet("color:red;")
				self.vprincipal.label_9.setText('Rango Invalido')
				self.vprincipal.lineEdit_3.hide()
		else:
			self.vprincipal.lineEdit_2.clear()


	def rango1(self):
		texto = self.vprincipal.lineEdit_14.text()
		rinicio = self.vprincipal.lineEdit_2.text()
		rfinal = self.vprincipal.lineEdit_3.text()

		octeto = texto.split('.')

		if rfinal != "":
			if octeto[0] == '190' or octeto[0] == '191' or octeto[0] == '192':
				rango_inicio = 100
				rango_final = 190
				
			
			elif octeto[0] == '10':
				rango_inicio = 145
				rango_final = 200
				
			else:
				rango_inicio = 0
				rango_final = 0

			if int(rfinal) >= rango_inicio and int(rfinal) <= rango_final and int(rinicio) < int(rfinal):
				self.vprincipal.label_10.show()
				self.vprincipal.label_10.setStyleSheet("color:green;")
				self.vprincipal.label_10.setText('OK!')
				self.vprincipal.pushButton_7.show()
			else:
				self.vprincipal.label_10.show()
				self.vprincipal.label_10.setStyleSheet("color:red;")
				self.vprincipal.label_10.setText('Rango Invalido')
				self.vprincipal.pushButton_7.hide()

		else:
			self.vprincipal.lineEdit_3.clear()
		

	def Conecta(self,dhcp_1,sentencia,valor):
		conn = pyodbc.connect("DRIVER={SQL Server};SERVER=%s;UID=usuario;PWD=password;" % (dhcp_1))
		curs = conn.cursor()
		curs.execute(sentencia)

		rows = curs.fetchall()
		
		self.vprincipal.textEdit.append(str(valor))
		QCoreApplication.processEvents()
		
		for row in rows:

			tabla = str(row)
			tabla = tabla.replace("None", " ")
			tabla = tabla.replace("( , )", " ")
			tabla = tabla.replace("('", " ")
			tabla = tabla.replace("', )", " ")


			self.vprincipal.textEdit.append(str(tabla))
			QCoreApplication.processEvents()

		curs.close ()
		conn.close ()

	def conectaPosMaster_log(self,inserta):
	    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=192.168.1.1;UID=usuario;PWD=password;")
	    curs = conn.cursor()
	    curs.execute(inserta)
	    curs.commit()
	    curs.close ()
	    conn.close ()


			
def main():
	app = QtGui.QApplication(sys.argv)
	vlogin = v_login()
	vlogin.show()
	sys.exit(app.exec_())




if __name__ == '__main__':
	main()
		
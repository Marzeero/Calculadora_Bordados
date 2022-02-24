from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="universo_gp" 
)

def funcao_principal():
  linha1 = float(formulario.lineEdit.text())
  linha2 = float(formulario.lineEdit_2.text())
  linha3 = float(formulario.lineEdit_3.text())
  linha4 = float(formulario.lineEdit_4.text())
  linha5 = float(formulario.lineEdit_5.text())
  linha6 = float(formulario.lineEdit_6.text())
  linha7 = float(formulario.lineEdit_7.text())
  linha8 = float(formulario.lineEdit_8.text())
  cliente = str(formulario.lineEdit_9.text())

  formulario.lineEdit.setText("")
  formulario.lineEdit_2.setText("")
  formulario.lineEdit_3.setText("")
  formulario.lineEdit_4.setText("")
  formulario.lineEdit_5.setText("")
  formulario.lineEdit_6.setText("")
  formulario.lineEdit_7.setText("")
  formulario.lineEdit_8.setText("")
  formulario.lineEdit_9.setText("")
  #print(f"Valor pontos: {linha1}")
  #print(f"Valor hora: {linha2}")
  #print(f"Quantidade de Pontos: {linha3}")
  #print(f"Quantidade de Horas: {linha4}")
  #print(f"Energia: {linha5}")
  #print(f"Material: {linha6}")
  #print(f"Frete: {linha7}")
  #print(f"Adicional: {linha8}")


  v1 = linha1*linha3
  v2 = linha2*linha4
  v3 = linha5+linha6+linha7+linha8
  v4 = v1+v2+v3

  
  cursor = banco.cursor()
  comando_SQL = "INSERT INTO geral (cliente,vtotal,taxas,vponto,vtemp) VALUES (%s,%s,%s,%s,%s)"
  dados = (str(cliente),v4, v3, v1, v2)
  cursor.execute(comando_SQL,dados)
  banco.commit() 

  formulario.label_17.setText(f"V. Ponto: {v1}")
  formulario.label_16.setText(f"V. Tempo: {v2}")
  formulario.label_15.setText(f"Taxas: {v3}")
  formulario.label_13.setText(f"VALOR TOTAL: {v4}")
  formulario.label_18.setText(f"CLIENTE: {cliente}")
  
  
  


  


app=QtWidgets.QApplication([])
formulario=uic.loadUi("INTERFACE.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

from flask import Flask, request, jsonify
from flask_cors import CORS  # Importamos CORS
import openpyxl

app = Flask(__name__)
CORS(app)  # Habilitamos CORS para todas las rutas

@app.route("/update_excel", methods=["POST"])
def update_excel():

    print("ESTOY ENTRANDO BRO")
    data = request.json
    precio = float(data.get("precio", 0))
    gastos = float(data.get("gastos", 0))
    impuestos = float()
    cantidad = float(data.get("cantidad",0))
    print("GASTOS: ",gastos,"Ingresos: ",precio, "cantidad", cantidad),
    archivo = "contabilidad.xlsx"
    wb = openpyxl.load_workbook(archivo)
    hoja = wb.active

    hoja["A1"] = "Ingresos"
    hoja["B1"] = "Gastos"
    hoja["C1"] = "cantidad"
    precio*= cantidad
    hoja["A2"] = precio
    
    hoja["B2"] = gastos
    
    hoja["C2"] = cantidad
    wb.save(archivo)

    rentable = precio > gastos
    print("rentabilidad", rentable)
    return jsonify({"rentable": rentable})

if __name__ == "__main__":
    app.run(debug=True)

# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    data_path = "files/input/shipping-data.csv"
    df = pd.read_csv(data_path)

    plt.figure(figsize=(8, 6))
    df["Warehouse_block"].value_counts().plot(kind="bar", color="skyblue")
    plt.title("Cantidad de Envíos por Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Cantidad de Envíos")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(os.path.join(output_dir, "shipping_per_warehouse.png"))
    plt.close()

    plt.figure(figsize=(8, 6))
    df["Mode_of_Shipment"].value_counts().plot(kind="bar", color="lightcoral")
    plt.title("Modo de Envío")
    plt.xlabel("Modo")
    plt.ylabel("Cantidad")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(os.path.join(output_dir, "mode_of_shipment.png"))
    plt.close()

    plt.figure(figsize=(8, 6))
    df.groupby("Warehouse_block")["Customer_rating"].mean().plot(kind="bar", color="seagreen")
    plt.title("Promedio de Calificación del Cliente por Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Calificación Promedio")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(os.path.join(output_dir, "average_customer_rating.png"))
    plt.close()


    plt.figure(figsize=(8, 6))
    df["Weight_in_gms"].plot(kind="hist", bins=20, color="gold", edgecolor="black")
    plt.title("Distribución del Peso de los Productos")
    plt.xlabel("Peso (gramos)")
    plt.ylabel("Frecuencia")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(os.path.join(output_dir, "weight_distribution.png"))
    plt.close()

    html_content = f"""
    <html>
    <head>
        <title>Dashboard de Envíos</title>
    </head>
    <body>
        <h1>Dashboard de Envíos</h1>
        <h2>Cantidad de Envíos por Warehouse</h2>
        <img src="shipping_per_warehouse.png" width="600">
        <h2>Modo de Envío</h2>
        <img src="mode_of_shipment.png" width="600">
        <h2>Promedio de Calificación del Cliente</h2>
        <img src="average_customer_rating.png" width="600">
        <h2>Distribución del Peso</h2>
        <img src="weight_distribution.png" width="600">
    </body>
    </html>
    """

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Dashboard generado en: {output_dir}/index.html")
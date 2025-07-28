from argparse import ArgumentParser
import mlflow
import pandas
mlflow.set_tracking_uri("http://localhost:5000")

def main():
    parser = ArgumentParser(
            prog="Social Media Addiction Classifier",
            description="CLI para modelo de prediccion de adiccion a redes sociales"
            )
    parser.add_argument("-p", "--filepath", type=str, required=True, help="Ruta al archivo csv que contiene la serie de python")
    args = parser.parse_args()

    if args.filepath:
      try:
        data = pandas.read_csv(args.filepath, header=0).iloc[:,1:]
      except Exception as e:
        print(e)

    model = mlflow.pyfunc.load_model("models:/Prediction_addicted/1")
    prediction = model.predict(data)
    print(f"El puntaje predicho de adicción es: {prediction}")

if __name__ == "__main__":
    main()
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

model = joblib.load("app/model.pkl") 

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(
    request: Request,
    Age: int = Form(...),
    Avg_Daily_Usage_Hours: float = Form(...),
    Sleep_Hours_Per_Night: float = Form(...),
    Mental_Health_Score: float = Form(...),
    Academic_Level: str = Form(...),
    Gender: str = Form(...),
    Country: str = Form(...),
    Most_Used_Platform: str = Form(...),
    Affects_Academic_Performance: str = Form(...),
    Relationship_Status: str = Form(...),
    Conflicts_Over_Social_Media: str = Form(...)
):
    try:
        # Crear el DataFrame con los datos del usuario
        input_data = pd.DataFrame([{
            "Age": Age,
            "Avg_Daily_Usage_Hours": Avg_Daily_Usage_Hours,
            "Sleep_Hours_Per_Night": Sleep_Hours_Per_Night,
            "Mental_Health_Score": Mental_Health_Score,
            "Academic_Level": Academic_Level,
            "Gender": Gender,
            "Country": Country,
            "Most_Used_Platform": Most_Used_Platform,
            "Affects_Academic_Performance": Affects_Academic_Performance,
            "Relationship_Status": Relationship_Status,
            "Conflicts_Over_Social_Media": Conflicts_Over_Social_Media
        }])

        # Realizar la predicción
        prediction = model.predict(input_data)[0]

        return templates.TemplateResponse("form.html", {
            "request": request,
            "result": f"Predicted Addiction Score: {prediction}",
            "range_info": "The score ranges from 1 (low) to 10 (high) for social media addiction."
        })

    except Exception as e:

        return templates.TemplateResponse("form.html", {
            "request": request,
            "error": "An error occurred while processing the prediction. Please verify the data entered."
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
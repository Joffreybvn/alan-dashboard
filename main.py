
import uvicorn
from config import config
from src import Dashboard

# Create the Dashboard backend object
app = Dashboard().get_app()


if __name__ == "__main__":
    uvicorn.run("main:app", port=config.PORT, host="0.0.0.0", reload=True, access_log=False)

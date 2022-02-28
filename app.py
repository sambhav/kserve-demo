import kserve
from typing import Dict

class CustomModel(kserve.Model):
    def __init__(self, name: str):
       super().__init__(name)
       self.name = name

    def predict(self, request: Dict) -> Dict:
        return {"predictions": request.get("instances", [])}

if __name__ == "__main__":
    model = CustomModel("custom-model")
    kserve.ModelServer().start([model])

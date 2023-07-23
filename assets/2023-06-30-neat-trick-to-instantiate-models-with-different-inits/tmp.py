from abc import ABC, abstractmethod
from enum import Enum


class ModelInterface(ABC):
    @abstractmethod
    def forward(self):
        raise NotImplementedError


class ModelA(ModelInterface):
    def __init__(self, latent_dim):
        self.latent_dim = latent_dim

    def forward(self):
        print(f"fwd pass with latent_dim={self.latent_dim}")


class ModelIdentifier(Enum):
    ModelA = "ModelA"
    ModelB = "ModelB"


class ModelB(ModelInterface):
    def __init__(self, num_embeddings):
        self.num_embeddings = num_embeddings

    def forward(self):
        print(f"fwd pass with num_embeddings={self.num_embeddings}")


if __name__ == "__main__":
    print("hi")

    model_name_to_model = {
        ModelIdentifier.ModelA: ModelA,
        ModelIdentifier.ModelB: ModelB,
    }

    config = {
        "latent_dim": 10,
    }
    model = model_name_to_model[ModelIdentifier.ModelA](**config)
    model.forward()

    config2 = {
        "num_embeddings": 1,
    }
    model = model_name_to_model[ModelIdentifier.ModelB](**config2)
    model.forward()

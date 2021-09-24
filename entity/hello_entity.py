from dataclasses import dataclass


@dataclass(frozen=True)
class HelloEntity:
    environment: str
    py_version: str
    event: dict

    def __post_init__(self):
        if not self.environment:
            raise ValueError('environment is empty!!')

from pydantic import BaseModel


class Movie(BaseModel):
    """
    Represents the data structure of the Question.
    """

    name: str
    question: str
    answer: str
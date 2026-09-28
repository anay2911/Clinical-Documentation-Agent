from pydantic import BaseModel, Field
from typing import List

class Medication(BaseModel):
    name: str = Field(description = "Name of the medication")
    dosage: str = Field(default = "", description = "Dosage if mentioned")

class extractedData(BaseModel):
    symptoms: List[str] = Field(description = "Symptoms and complains reported by patients")
    diagnosis: str = Field(default = "", description = "Doctor's implied or stated diagnosis")
    lab_results: str = Field(default = "", description = "Implications of the lab reports")
    medications : List[Medication] = Field(description = "List of all the medications prescribed with dosage if available")
    medical_history: str = Field(default = "", description = "Relevant prior conditions or allergies mentioned, if any")
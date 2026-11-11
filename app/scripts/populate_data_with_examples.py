import json
from dataclasses import dataclass

@dataclass
class ExampleLevelExpectation:
    level: str
    description: str
    examples: list[str]

@dataclass
class Dimension:
    id: str
    name: str
    category: str
    question: str
    levels: list[ExampleLevelExpectation]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "question": self.question,
            "levels": [{"level": l.level, "description": l.description, "examples": l.examples} for l in self.levels]
        }

def get_full_career_data():
    """Generates all career data with realistic examples."""
    
    # Proactivity examples
    proactivity = Dimension(
        id="proactivity",
        name="Proactivity",
        category="Ownership",
        question="Do I share ideas proactively, find out solutions to problems and seek opportunities to scale impact?",
        levels=[
            ExampleLevelExpectation("IC1", "...", ["Ex 1: Proactively updated KPI dashboard metrics.", "Ex 2: Built Belgium transaction dashboard."]),
            ExampleLevelExpectation("IC2", "...", ["Ex 1: Fixed SQL bug in daily data ingest.", "Ex 2: Automated weekly report using Python."]),
            ExampleLevelExpectation("IC3", "...", ["Ex 1: Led project to optimize team's attribution pipeline.", "Ex 2: Developed automated alerting for data drift."]),
            ExampleLevelExpectation("IC4", "...", ["Ex 1: Championed migration to new analytics warehouse.", "Ex 2: Mentored junior analyst on complex modeling."]),
            ExampleLevelExpectation("AL1", "...", ["Ex 1: Led discovery analysis for new market entry.", "Ex 2: Standardized onboarding process for team."]),
            ExampleLevelExpectation("AL2", "...", ["Ex 1: Architected unified analytics framework across pods.", "Ex 2: Driven cross-functional data-driven culture."]),
            ExampleLevelExpectation("AL3", "...", ["Ex 1: Defined long-term analytics strategy for tribe.", "Ex 2: Drove tribe-wide migration to automated self-service."]),
        ]
    )
    
    # ... Add other dimensions/skills here

    return {"dimensions": [proactivity.to_dict()]}

with open("app/data/career_framework_data_examples.json", "w") as f:
    json.dump(get_full_career_data(), f, indent=4)
print("Data with examples populated.")

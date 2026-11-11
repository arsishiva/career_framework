"""Career map data structures for the Wise Analytics Career Framework."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SalaryBand:
    """Salary information for a specific location."""

    location: str
    min_salary: int
    max_salary: int
    currency: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "location": self.location,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary,
            "currency": self.currency,
        }


@dataclass
class LevelExpectation:
    """Expectations for a specific level within a dimension."""

    level: str
    description: str

    def to_dict(self) -> dict[str, str]:
        return {
            "level": self.level,
            "description": self.description,
        }


@dataclass
class Dimension:
    """A career dimension (e.g., Ownership, Problem Solving)."""

    id: str
    name: str
    category: str
    question: str
    levels: list[LevelExpectation] = field(default_factory=list)

    def get_level(self, level_id: str) -> LevelExpectation | None:
        for lvl in self.levels:
            if lvl.level == level_id:
                return lvl
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "question": self.question,
            "levels": [lvl.to_dict() for lvl in self.levels],
        }


@dataclass
class TechnicalSkill:
    """A technical skill area with level expectations."""

    area: str
    question: str
    levels: list[LevelExpectation] = field(default_factory=list)

    def get_level(self, level_id: str) -> LevelExpectation | None:
        for lvl in self.levels:
            if lvl.level == level_id:
                return lvl
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "area": self.area,
            "question": self.question,
            "levels": [lvl.to_dict() for lvl in self.levels],
        }


@dataclass
class CareerLevel:
    """A complete career level with all its details."""

    id: str
    name: str
    track: str  # "IC" (Individual Contributor) or "AL" (Analytics Lead)
    display_order: int
    salaries: list[SalaryBand] = field(default_factory=list)
    dimensions: list[Dimension] = field(default_factory=list)
    technical_skills: list[TechnicalSkill] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "track": self.track,
            "display_order": self.display_order,
            "salaries": [s.to_dict() for s in self.salaries],
            "dimensions": [d.to_dict() for d in self.dimensions],
            "technical_skills": [t.to_dict() for t in self.technical_skills],
        }


@dataclass
class CareerMap:
    """Complete career map containing all levels and dimensions."""

    levels: list[CareerLevel] = field(default_factory=list)
    dimensions: list[Dimension] = field(default_factory=list)
    technical_skills: list[TechnicalSkill] = field(default_factory=list)

    def get_level(self, level_id: str) -> CareerLevel | None:
        for lvl in self.levels:
            if lvl.id == level_id:
                return lvl
        return None

    def get_levels_by_track(self, track: str) -> list[CareerLevel]:
        return [lvl for lvl in self.levels if lvl.track == track]

    def get_dimension(self, dim_id: str) -> Dimension | None:
        for dim in self.dimensions:
            if dim.id == dim_id:
                return dim
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "levels": [lvl.to_dict() for lvl in self.levels],
            "dimensions": [d.to_dict() for d in self.dimensions],
            "technical_skills": [t.to_dict() for t in self.technical_skills],
        }


# Initial mock data for the career map
def get_career_map() -> CareerMap:
    """Returns a CareerMap object populated with initial data."""
    
    # Create dimensions
    dimensions = [
        Dimension(
            id="ownership",
            name="Ownership",
            category="Core",
            question="How do you take responsibility for your work?",
            levels=[
                LevelExpectation(level="1", description="Takes ownership of tasks."),
                LevelExpectation(level="2", description="Takes ownership of projects."),
            ]
        ),
        Dimension(
            id="problem_solving",
            name="Problem Solving",
            category="Core",
            question="How do you approach complex problems?",
            levels=[
                LevelExpectation(level="1", description="Solves well-defined problems."),
                LevelExpectation(level="2", description="Solves ambiguous problems."),
            ]
        )
    ]
    
    # Create levels
    levels = [
        CareerLevel(
            id="l1",
            name="Associate Analyst",
            track="IC",
            display_order=1,
            dimensions=dimensions
        ),
        CareerLevel(
            id="l2",
            name="Analyst",
            track="IC",
            display_order=2,
            dimensions=dimensions
        )
    ]
    
    return CareerMap(levels=levels, dimensions=dimensions)

from agents import ModelSettings
from openai.types.shared import Reasoning
from agency_swarm import Agent


app_builder = Agent(
    name="AppBuilder",
    description="Turns plain-English product ideas into production-ready applications with end-to-end implementation.",
    instructions="./instructions.md",
    tools_folder="./tools",
    files_folder="./files",
    model="gpt-5.2",
    model_settings=ModelSettings(
        max_tokens=25000,
        reasoning=Reasoning(
            effort="medium",
            summary="auto",
        ),
    ),
)

from dotenv import load_dotenv
from agency_swarm import Agency

from app_builder import app_builder

load_dotenv()

# do not remove this method, it is used in the main.py file to deploy the agency (it has to be a method)
def create_agency(load_threads_callback=None):
    agency = Agency(
        app_builder,
        communication_flows=[],
        name="AppBuilderAgency",
        shared_instructions="shared_instructions.md",
        load_threads_callback=load_threads_callback,
    )

    return agency

if __name__ == "__main__":
    agency = create_agency()

    # run in terminal
    agency.terminal_demo()

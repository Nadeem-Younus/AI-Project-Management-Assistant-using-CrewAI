from crewai import Crew, Process

from agents import (
    requirements_agent,
    planning_agent,
    risk_agent,
    resource_agent,
    report_agent
)

from tasks import (
    requirements_task,
    planning_task,
    risk_task,
    resource_task,
    report_task
)

project_crew = Crew(
    agents=[
        requirements_agent,
        planning_agent,
        risk_agent,
        resource_agent,
        report_agent
    ],
    tasks=[
        requirements_task,
        planning_task,
        risk_task,
        resource_task,
        report_task
    ],
    process=Process.sequential,
    verbose=True
)

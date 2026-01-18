from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FirstTest():
    """FirstTest crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def concert_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['concert_researcher'],
            verbose=True
        )
    @agent
    def concert_info_organizer(self) -> Agent:
        return Agent(
            config=self.agents_config['concert_info_organizer'],
            verbose=True
        )

    @task
    def concert_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['concert_research_task'],
        )

    @task
    def concert_organizing_task(self) -> Task:
        return Task(
            config=self.tasks_config['concert_organizing_task'],
            output_file='report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the FirstTest crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

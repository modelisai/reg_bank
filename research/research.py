import streamlit as st
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

def create_research_agent():
    return Agent(
        role='Researcher',
        goal='Find and summarize the latest news on a given topic',
        backstory="""You're a researcher at a large company.
        You're responsible for analyzing data and providing insights
        to the business.""",
        verbose=True
    )

def create_research_task(agent, topic):
    search_tool = SerperDevTool()
    return Task(
        description=f'Find and summarize the latest news about {topic}',
        expected_output=f'A bullet list summary of the top 10 most important news articles about {topic}',
        agent=agent,
        verbose=True,
        tools=[search_tool]
    )

def run_research(topic):
    research_agent = create_research_agent()
    task = create_research_task(research_agent, topic)
    crew = Crew(
        agents=[research_agent],
        tasks=[task],
        verbose=True,
    )
    return crew.kickoff()

# Streamlit UI
st.title('AI News Research Tool')

topic = st.text_input('Enter a topic to research:', 'Olympics')

if st.button('Run Research'):
    with st.spinner('Researching... This may take a few minutes.'):
        result = run_research(topic)
    st.subheader('Research Results:')
    st.markdown(result)


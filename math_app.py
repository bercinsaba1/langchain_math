
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.llms import OpenAI
from math import pi 

import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
 
openai.api_key  = os.environ['OPENAI_API_KEY']   
#### LLM TTOOL allows mathematical operations #####
llm = OpenAI(
        openai_api_key= os.environ['OPENAI_API_KEY'],
        temperature=0,
        model_name='gpt-4'
) 
tool_names = ["llm-math"] 
tools = load_tools(tool_names, llm=llm)

agent = initialize_agent(
    tools=tools, llm=llm, verbose=True, agent="zero-shot-react-description")
 

agent("In triangle ABC, the measure of <B is 90 degree, BC = 16 and AC = 20. Triangle DEF is similar to triangle ABC, where vertices
 D,E and F correspond to vertices A,B and C, resectively, and each side of triangle DEF is 1/3 the length of the corresponding side of triangle ABC. What is the value of sinF?" ) 


"""
with get_openai_callback() as cb:
    agent("can you calculate the circumference of a circle that has a radius of 7.81mm")
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")""" 
    
#agent.run("what is 10 added by 255?")
#agent("can you calculate the square of a number that has a value of 7.0")  
#agent("can you calculate the circumference of a circle that has a radius of 7.81mm")

#print( 2 * pi* 7.81) 

#agent("Jack has 8 cats and 2 dogs. Jill has 7 cats and 4 dogs. How many dogs are there in all?")
#agent("Rhonda has 12 marbles more than Douglas. Douglas has 6 marbles more than Bertha. Rhonda has twice as many marbles as Bertha has.How many marbles does Douglas have?")
#agent("If I have a triangle with two sides of length 51cm and 34cm, what is the length of the hypotenuse?")  
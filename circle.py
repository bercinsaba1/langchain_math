
from langchain.tools import BaseTool
from math import pi
from typing import Union

from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']  

    
llm = ChatOpenAI(
        openai_api_key= os.environ['OPENAI_API_KEY'] ,
        temperature=0,
        model_name='gpt-4'
)

# initialize conversational memory
conversational_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
) 
from langchain.agents import initialize_agent



class CircumferenceTool(BaseTool):
    name = "Circumference calculator"
    description = "use this tool when you need to calculate a circumference using the radius of a circle"

    def _run(self, radius: Union[int, float]):
        return float(radius)*2.0*pi

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")  
 
tools = [CircumferenceTool()]

# initialize agent with tools
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory
) 
#agent("can you calculate the circumference of a circle that has a radius of 7.81mm")
# 

sys_msg = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Unfortunately, Assistant is terrible at maths. When provided with math questions, no matter how simple, assistant always refers to it's trusty tools and absolutely does NOT try to answer math questions by itself

Overall, Assistant is a powerful system that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
"""   
new_prompt = agent.agent.create_prompt(system_message=sys_msg,tools=tools) 

agent.agent.llm_chain.prompt = new_prompt
#agent("can you calculate the circumference of a circle that has a radius of 7.81mm") 
from langchain.callbacks import get_openai_callback 
with get_openai_callback() as cb:
    agent("can you calculate the circumference of a circle that has a radius of 7.81mm")
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}") 

##square calculator##
""" 
class mathTool(BaseTool):
    name = "square calculator"
    description = "use this tool when you need to find the square of a number"

    def _run(self,number: Union[int, float] ):
        return (float(number)*float(number))

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async") 
    
tools = [mathTool()]
new_prompt = agent.agent.create_prompt(system_message=sys_msg,tools=tools)
agent.agent.llm_chain.prompt = new_prompt
agent.tools = tools 
#agent("can you calculate the square of a number that has a value of 7.0")  




#--------------------------#

##### multiple parameter tool#####
####### hypotenuse calculator############## 
from typing import Optional
from math import sqrt, cos, sin

desc = (
    "use this tool when you need to calculate the length of a hypotenuse"
    "given one or two sides of a triangle and/or an angle (in degrees). "
    "To use the tool, you must provide at least two of the following parameters "
    "['adjacent_side', 'opposite_side', 'angle']."
)

class PythagorasTool(BaseTool):
    name = "Hypotenuse calculator"
    description = desc
    
    def _run(
        self,
        adjacent_side: Optional[Union[int, float]] = None,
        opposite_side: Optional[Union[int, float]] = None,
        angle: Optional[Union[int, float]] = None
    ):
        # check for the values we have been given
        if adjacent_side and opposite_side:
            return sqrt(float(adjacent_side)**2 + float(opposite_side)**2)
        elif adjacent_side and angle:
            return adjacent_side / cos(float(angle))
        elif opposite_side and angle:
            return opposite_side / sin(float(angle))
        else:
            return "Could not calculate the hypotenuse of the triangle. Need two or more of `adjacent_side`, `opposite_side`, or `angle`."
    
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

tools = [PythagorasTool()] 

new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
)

agent.agent.llm_chain.prompt = new_prompt 
agent.tools = tools 
from langchain.callbacks import get_openai_callback 
with get_openai_callback() as cb:
    agent("If I have a triangle with two sides of length 51cm and 34cm, what is the length of the hypotenuse?") 
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")
     

#agent("If I have a triangle with opposite side of length 51cm and angle of 20 degrees, what is the length of the hypotenuse?")


""" 
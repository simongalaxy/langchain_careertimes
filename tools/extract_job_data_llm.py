from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_classic.chains.llm import LLMChain

class job_data_extractor:
    def __init__(self, model_name: str):
        self.llm = OllamaLLM(model=model_name)
        self.prompt = PromptTemplate(
            input_variables=["job_content"],
            template="""
            Extract job-related information from the following webpage text.
            Return JSON with keys: job_title, job_description, job_duties, qualifications, skills, experiences.

            Webpage text:
            {job_content}
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)


def extract_job_data(job_content: str) -> dict:

    return chain.run(job_content=job_content)
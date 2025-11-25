import asyncio
from crawl4ai import AsyncWebCrawler
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.chains import LLMChain

class JobExtractor:
    def __init__(self, model_name: str):
        # Initialize LLM + prompt chain
        self.prompt_template = PromptTemplate(
            input_variables=["webpage_text"],
            template="""
                Extract job-related information from the following webpage text.
                Return JSON with keys: job_title, job_description, duties, qualifications, skills, experiences.

                Webpage text:
                {webpage_text}
                """
            )
        self.llm = Ollama(model=model_name)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    async def fetch_page(self, url: str) -> str:
        """Render JS-heavy webpage and return text"""
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url, render_js=True)
            return result["content"]

    async def extract_job_info(self, url: str) -> str:
        """Main pipeline: crawl + extract structured info"""
        text = await self.fetch_page(url)
        result = self.chain.run(webpage_text=text)
        return result


# --------------------------
# Example usage in main program
# --------------------------
# if __name__ == "__main__":
#     async def run():
#         extractor = JobExtractor(model_name="mistral")  # or llama2, etc.
#         url = "https://example.com/job-posting"
#         job_info = await extractor.extract_job_info(url)
#         print(job_info)

#     asyncio.run(run())

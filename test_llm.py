from llm.llm_client import call_llm

print(
    call_llm(
        "You are a helpful assistant.",
        "Say hello in one short sentence."
    )
)

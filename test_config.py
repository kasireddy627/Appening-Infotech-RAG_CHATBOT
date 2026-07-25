from graph import graph

question = input("Ask a question: ")

result = graph.invoke(
    {
        "question": question
    }
)

print("\nAnswer:\n")
print(result["answer"])
import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = 'Enter your openai secret key'


def chatbot(query):
    # Constructing a message list for the conversation
    messages = [
        {"role": "system", "content": "You are a helpful healthcare assistant."},
        {"role": "user", "content": query}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model, e.g., "gpt-4"
            messages=messages,
            max_tokens=150
        )
        # Extracting the assistant's response
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)


# Create Gradio interface
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=7, label="Ask me anything about healthcare."),
    outputs=gr.Textbox(label="Response"),
    title="Healthcare Chatbot",
    description="Ask me anything about healthcare."
)

# Launch the interface
iface.launch()


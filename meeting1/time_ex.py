import gradio

def format_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{sec:02d}"


# formatted_time = format_seconds(3665)
# print(formatted_time)

my_interface = gradio.Interface(
    format_seconds,
    inputs=["number"],
    outputs=["text"],
    title="My best app"
)
my_interface.launch(share=False)
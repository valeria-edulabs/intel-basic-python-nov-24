# Exercise: Sum of Even Numbers
# Write a function sum_even_numbers that takes a range of integers (using range)
# and returns the sum of all even numbers in that range.

# Input:
# Two integers, start and end, where start is the starting number and end is the ending number (inclusive).
# Task:
# Use a for loop with range to iterate through the numbers from start to end (inclusive).
# Check if a number is even (i.e., divisible by 2).
# Add all even numbers to a running total.
# Return the total sum of even numbers in the given range.

# Example input:
# sum_even_numbers(1, 10)  # output: 30

# Hints:
# Use the range function to generate numbers from start to end (inclusive).
# Use the modulo operator (%) to check if a number is even.
# The range(start, end+1) will generate a range from start to end, inclusive of end.
#

import gradio as gr

def sum_even_numbers(start_num, end_num):
    if start_num % 2 == 0:
        pass
    else:
        # start_num = start_num + 1
        start_num += 1
    even_sum = 0
    for i in range(start_num, end_num+1, 2):
        even_sum += i
    return even_sum


demo = gr.Interface(
    fn=sum_even_numbers,
    # inputs=["slider", "number"],
    inputs=[gr.Slider(minimum=10, maximum=1000, label="First:"), gr.Number(label="Last:")],
    outputs=["number"],
    title="Even Sum",
    description="This calculates sum of even numbers",
    theme="soft",
    flagging_mode="never",
    submit_btn="GO"
)
demo.launch(share=False)


# print(sum_even_numbers(5, 10)) #24
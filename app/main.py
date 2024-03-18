from transformers import AutoModelForCausalLM, AutoTokenizer
import textwrap

# Initialization
model_name = "AI-Sweden-Models/gpt-sw3-126m"  # Replace with the actual model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set the width of the terminal or desired text width
terminal_width = 80

try:
    while True:  # Keep running until the user interrupts
        # Prompt the user for input
        input_text = input("Please enter your input: ").strip()

        if not input_text:
            print("Input text is empty, please provide valid input.")
            continue

        # Encode the input text and convert to the format expected by the model
        inputs = tokenizer.encode(input_text, return_tensors="pt")

        if inputs.size(1) == 0:  # Check if the input tensor is empty
            print("The input text did not return any tokens. Please try again with different text.")
            continue
        
        # Generate output from the model
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
        
        # Decode the generated text, skipping any special tokens
        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Format the input and output text with prefixes and wrapping
        formatted_input_text = textwrap.fill("Input: " + input_text, width=terminal_width)
        formatted_output_text = textwrap.fill("Output: " + output_text, width=terminal_width)
        
        # Print the formatted input and output text
        print(formatted_input_text)
        print()  # Add an empty line between input and output for better readability
        print(formatted_output_text)
        print()  # Add another empty line before the next prompt for clarity

except KeyboardInterrupt:
    print("\nProgram terminated by the user.")

from gradio_client import Client
import shutil

# Initialize client
client = Client("Heartsync/NSFW-Uncensored")

# Run prediction
result = client.predict(
    prompt="a girl massaging his own boobs and feeling horny",
    negative_prompt="text, talk bubble, low quality, watermark, signature",
    seed=0,
    randomize_seed=True,
    width=1024,
    height=1024,
    guidance_scale=7,
    num_inference_steps=28,
    api_name="/infer"
)

print("Result (file path):", result)

# Copy the generated image to current folder with a new name
output_path = "generated_image.webp"
shutil.copy(result, output_path)
print(f"Image copied to {output_path}")

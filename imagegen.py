import torch
from diffusers import StableDiffusionPipeline
from datetime import datetime
import os
def generate_image(prompt, model_id="runwayml/stable-diffusion-v1-5", output_dir="generated_images", seed=None):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to(device)
    if seed is not None:
        generator = torch.Generator(device).manual_seed(seed)
    else:
        generator = Non
    result = pipe(prompt, generator=generator)
    image = result.images[0]
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/image_{timestamp}.png"
    image.save(filename)
    print(f"Image saved as {filename}")
    return filename
if __name__ == "__main__":
    prompt = (
        "A peaceful sunrise over a calm lake surrounded by mountains. With soft, fluffy clouds scattered above."
    )
    generate_image(prompt, seed=42)

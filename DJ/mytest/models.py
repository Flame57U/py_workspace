import replicate

output = replicate.run(
  "black-forest-labs/flux-dev",
  input={
    "aspect_ratio": "1:1",
    "num_outputs": 1,
    "output_format": "jpg",
    "output_quality": 80,
    "prompt": "An astronaut riding a rainbow unicorn, cinematic, dramatic",
  }
)

print(output)
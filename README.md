# Flash MLLM

*Flash MLLM* is a quantization package and inference interface of multi-modal LLMs. It not only consist of VLM, but also some TTS, Speech2Speech (Omni) models based on LLM arch. 

Flash MLLM mainly focusing on CPU and consumer grade GPU inference, it's useful for users who want run small VLMs or TTS models faster on consumer GPU or CPU (M4 mac etc) with quantization.

Flash MLLM can be taken into 3 parts:

- `python`: quantization make popular models into GGUF format with ease;
- `rust`: using candle to inference quantized model, GGUF mainly, not just LLMs;
- `cpp`: using llama.cpp for inference;



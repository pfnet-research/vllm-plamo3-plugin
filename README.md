# vLLM Plugin for PLaMo3

A vLLM plugin for running PLaMo3 models.
This plugin enables running inference for PLaMo3 using vLLM using vLLM's [Plugin System](https://docs.vllm.ai/en/stable/design/plugin_system.html).

## Quick Start

To get started with the vLLM PLaMo3 plugin, just build and install the plugin, then run vLLM with the desired PLaMo3 model.

```bash
git clone https://github.com/pfnet-research/vllm-plamo3-plugin.git
cd vllm-plamo3-plugin
pip install -e .
vllm serve pfnet/plamo-3-nict-2b-base --trust-remote-code
```

## License

This project is distributed under the Apache License 2.0.

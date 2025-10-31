def register():
    """ Registers the PLaMo 3 implementation in vLLM. """

    from vllm import ModelRegistry
    model_cls = "vllm_plamo3.plamo3:Plamo3ForCausalLM"

    ModelRegistry.register_model("Plamo3ForCausalLM", model_cls)

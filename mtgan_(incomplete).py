class TrafficGENm:
    def __init__(self, use_individual_gan=False):
        self.generator_collection = {}
        self.discriminator_collection = {}
        self.gan_collection = {}
        
    def add_generator(self, generator):
        self.generator_collection{generator.data_name} = generator.generator
        
class Generator:
    def __init__(self, is_sequential=False, use_conv=False, use_wasserstein=True, n_layers=3, nodes_per_layer=64):
        self.generator = None
        self.data_name = None
        self.parameters = {}
    
class Discriminator:
    def __init__(self, is_sequential=False, use_conv=False, use_wasserstein=True, n_layers=3, nodes_per_layer=64):
        self.discriminator = None
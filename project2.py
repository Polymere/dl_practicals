from torch import tensor,set_grad_enabled,empty
set_grad_enabled(False);

class myNetwork:
	def __init__(self):
		self.layers=[]
		self.weights=[]
	def add_layer(self,activation,input_shape,bias_val):
		"""if len(sinput_shape!=self.layers[:-1][2]:
			print("Input shape of layer #",len(self.layers)+1,"=",input_shape,\
				 "\nOutput shape of layer #",len(self.layers),"=",self.layers[:-1][2])
			raise ValueError"""
		self.layers.append((activation,
							self._init_weights(input_shape),
						   self._init_bias(bias_val)))
	
	def _init_weights(self,sz):
		return empty(sz)
	def _init_bias(self,bias_val):
		return bias_val
	def output(self,x):
		print(x)
		prev_input=x
		for lay in self.layers:
			prev_input=self._lay_output(prev_input,lay[1],lay[2],lay[0])
		return prev_input
	def _lay_output(self,prev_input,weights,bias,act):
		if act=="relu":
			print(prev_input)
			return min((prev_input*weights.sum()+bias).max(),1)
		elif act=="tanh":
			return (prev_input*weights.sum()+bias).tanh()

if __name__ == '__main__':
	nw=myNetwork()
	nw.add_layer('relu',2,2)
	nw.output(tensor[1,2,3])
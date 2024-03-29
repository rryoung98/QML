import sympy

class CircuitLayerBuilder():
    def __init__(self, data_qubits, readout):
        self.data_qubits = data_qubits
        self.readout = readout
    
    def add_layer(self, circuit, single_qubit_gate,two_qubit_gate, prefix):
        for i, qubit in enumerate(self.data_qubits):
            if i < len(self.data_qubits)-1:
                symbol = sympy.Symbol(prefix + '-' + str(i))
                circuit.append(two_qubit_gate(qubit, self.data_qubits[i+1]))
                circuit.append(single_qubit_gate(self.data_qubits[i+1])**(2*symbol))
                circuit.append(two_qubit_gate(qubit, self.data_qubits[i+1]))



# def ccwyy_qconv_layer( wires,weights,):  # pylint: disable=arguments-differ
#     r"""Quantum Convolutional Neural Networks for High Energy Physics Data Analysis
#     `arXiv:2012.12  <https://arxiv.org/abs/2012.12177>`_.

#     Representation of the operator as a product of other operators.

#     .. math:: O = O_1 O_2 \dots O_n.



#     .. seealso:: :meth:`~.StronglyEntanglingLayers.decomposition`.

#     Args:
#         weights (tensor_like): weight tensor
#         wires (Any or Iterable[Any]): wires that the operator acts on
#         ranges (Sequence[int]): sequence determining the range hyperparameter for each subsequent layer
#         imprimitive (pennylane.ops.Operation): two-qubit gate to use

#     Returns:
#         list[.Operator]: decomposition of the operator

#     **Example**

#     >>> weights = torch.tensor([[-0.2, 0.1, -0.4], [1.2, -2., -0.4]])
#     >>> qml.StronglyEntanglingLayers.compute_decomposition(weights, wires=["a", "b"], ranges=[2], imprimitive=qml.CNOT)
#     [Rot(tensor(-0.2000), tensor(0.1000), tensor(-0.4000), wires=['a']),
#     Rot(tensor(1.2000), tensor(-2.), tensor(-0.4000), wires=['b']),
#     CNOT(wires=['a', 'a']),
#     CNOT(wires=['b', 'b'])]
#     """
#     if len(wires) > 1:
#         for i in range(len(wires)):
#             if i < len(wires) - 1:
#                 qml.CNOT(wires=[wires[i], wires[i + 1]])
#             else:
#                 qml.CNOT(wires=[wires[i], wires[0]])
#     for i in range(len(wires)):  # pylint: disable=consider-using-enumerate
#             qml.Rot(
#                 weights[i][0],
#                 weights[i][1],
#                 weights[i][2],
#                 wires=wires[i],
#             )
#     print(weights, 'weights')
#     print(weights.shape, 'weights.shape')

# def block(weights, wires):
#     qml.RX(weights[0], wires=wires[0])
#     qml.RX(weights[1], wires=wires[1])
#     qml.CNOT(wires=[wires[0],wires[1]])

# def ttn_layer(n_wires,weights, n_params_block=4):  # pylint: disable=arguments-differ
#     '''
#     This is the template for a single layer of the TTN network.
#     '''
#     # print(weights)
#     # ttn_weights = weights*n_params_bloc
#     # print(ttn_weights)
#     # weights should be [qubit length, block length]
#     qml.TTN(
#         wires=range(n_wires),
#         n_block_wires=4,
#         block=block,
#         n_params_block=n_params_block,
#         template_weights=weights,
#     )




# # n_wires = 4
# # n_block_wires = 2
# # n_params_block = 2
# # n_blocks = qml.MERA.get_n_blocks(range(n_wires),n_block_wires)
# # template_weights = [[0.1,-0.3]]*n_blocks

# # dev= qml.device('default.qubit',wires=range(n_wires))
# def MERAblock(weights, wires):
#         qml.CNOT(wires=[wires[0],wires[1]])
#         qml.RY(weights[0][0], wires=wires[0])
#         qml.RY(weights[0][1], wires=wires[1])
# def mera_circuit(template_weights,n_wires,n_block_wires,n_params_block):
#     qml.MERA(range(n_wires),n_block_wires, block, n_params_block, [template_weights[0]])
#     print(qml.MERA.get_n_blocks(range(n_wires),n_block_wires))


# Swing simulations

This repository contains simulations of the collective operation **Allreduce**, discussed in my Bachelor's thesis work [Distributed training: an analysis of Swing algorithm
and application to Honeycomb networks.](https://drive.google.com/file/d/1R2Y-eNn487G8_1zKZ8nunKskbN2GOeqx/view?usp=sharing). The simulations implement Allreduce with the **Swing algorithm** [2] on collectives with different topologies.

## Collectives

The collective is here represented as a directed graph, with each direct edge representing a link between two compute units. The model assumes that a link can be traversed by one item per direction at each clock cycle. The topologies definied in `utils.py` are:

- **1D tori**, built via `torus(n)`<br>creates a ring of $n$ units;
- **supertori**, with `supertorus(n,k)`<br>a ring of $n$ units, with reserved links for communications up to step $k$ of the Swing algorithm, inspired by [1];
- **2D tori** based on a square tessellation of the plane [3], created with `recTorus(b,h)`<br>builds a 2D torus with dimensions $b \times h$;
- **2D Honeycomb tori** based on a hexagonal tessellation of the plane, created with `honeycomb(b,h)`<br>like the  square-based tori, builds a $b \times h$ torus.

## Outputs

The simulations return the congestion deficiency $\Xi$ evaluated on the Swing algorithm run on the specific topology. They also return the number of clock cycles required for a complete execution.

## Code information

- `notebook.ipynb` contains contains all the simulations, for all the different topologies stated before.

- `utils.py` contains class definitions (Graph and Queue) and functions, that will be imported in the notebook.

## Bibliography

[1] Ke Cui and Michihiro Koibuchi. “A High-Radix Circulant Network Topology for Eﬃcient Collective
Communication”. In: Parallel and Distributed Computing, Applications and Technologies. Ed. by
Hiroyuki Takizawa et al. Cham: Springer Nature Switzerland, 2023, pp. 401–412. ISBN:
978-3-031-29927-8.

[2] Daniele De Sensi et al. “Swing: Short-cutting Rings for Higher Bandwidth Allreduce”. In: 21st USENIX
Symposium on Networked Systems Design and Implementation (NSDI 24). Santa Clara, CA: USENIX
Association, Apr. 2024, pp. 1445–1462. ISBN: 978-1-939133-39-7. URL:
https://www.usenix.org/conference/nsdi24/presentation/de-sensi.

[3] Ivan Stojmenovi´
c. “Honeycomb networks: Topological properties and communication algorithms”. In:
IEEE Transactions on Parallel and Distributed Systems 8.10 (1997), pp. 1036–1042. DOI:
10.1109/71.629486